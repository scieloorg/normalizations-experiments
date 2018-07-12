#!/usr/bin/env python3
"""
Politely download JSON data from the CrossRef API.
"""
import asyncio
from datetime import datetime, timedelta
import os

import aiohttp
import click
import pandas as pd


class RateLimitMemory:

    def __init__(self, interval, limit, update, interval_rate, limit_rate):
        self.tstamps = []
        self.interval = timedelta(seconds=interval)
        self.limit = limit
        self.update = update
        self.interval_rate = interval_rate
        self.limit_rate = limit_rate

    soft_limit = property(lambda self: self.limit * self.limit_rate)
    soft_interval = property(lambda self: self.interval * self.interval_rate)


async def download(rlm, session, url, fname):
    while len(rlm.tstamps) >= rlm.soft_limit:
        threshold = datetime.utcnow() - rlm.soft_interval
        rlm.tstamps = [dt for dt in rlm.tstamps if dt > threshold]
        await asyncio.sleep(0)

    print(f"Downloading {fname}!")
    rlm.tstamps.append(datetime.utcnow())
    async with session.get(url) as resp:
        if rlm.update:
            rlm.limit = int(resp.headers.get("X-Rate-Limit-Limit", rlm.limit))
            str_interval = resp.headers.get("X-Rate-Limit-Interval", None)
            if str_interval:
                rlm.interval = timedelta(seconds=int(str_interval.rstrip("s")))

        result = await resp.text()
        if resp.status != 200:
            print(f"Skipping {fname}:\n{result}")
        else:
            with open(fname, "w") as output_file:
                output_file.write(result)


async def perform_tasks(rlm, url_fmt, out_dir, dois):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for doi in dois:
            url = url_fmt.format(doi)
            fname = os.path.join(out_dir, doi.replace("/", "_") + ".json")
            if not os.path.exists(fname):
                download_coroutine = download(rlm, session, url, fname)
                tasks.append(asyncio.ensure_future(download_coroutine))
        if tasks:
            await asyncio.wait(tasks)
        else:
            print("No download was required!")


@click.command()
@click.option("--email", "-e", help="E-mail for using the polite pool.")
@click.option("--interval", "-i",
    default=1,
    help="Minimum duration in seconds between bursts.",
)
@click.option("--limit", "-l",
    default=50,
    help="Maximum number of requests allowed in an interval.",
)
@click.option("--update/--no-update",
    default=True,
    help="Update limit/interval following the X-Rate-Limit headers.",
)
@click.option("--interval-rate", "-I",
    default=1.1,
    help="Wait this rate times the interval between bursts.",
)
@click.option("--limit-rate", "-L",
    default=.9,
    help="Fetch this rate times the request limit in a burst.",
)
@click.option("--out-dir", "-d",
    default="crossref-by-doi",
    type=click.Path(file_okay=False, dir_okay=True, writable=True,
                    allow_dash=False, resolve_path=True),
    help="Directory to store the collected JSON files.",
)
@click.argument("csv_file", type=click.File("r"))
def main(email, interval, limit, update, interval_rate, limit_rate, out_dir,
         csv_file):
    dataset = pd.read_csv(csv_file, dtype=str, keep_default_na=False)
    dois = (doi for doi in dataset["article_doi"].str.strip().unique() if doi)
    os.makedirs(out_dir, exist_ok=True)
    url_fmt = "https://api.crossref.org/works/{}"
    if email:
        url_fmt += "?mailto=" + email
    rlm = RateLimitMemory(interval, limit, update, interval_rate, limit_rate)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(perform_tasks(rlm, url_fmt, out_dir, dois))


if __name__ == "__main__":
    main()
