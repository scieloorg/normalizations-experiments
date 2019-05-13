#!/usr/bin/env python3
"""
Country classifier based on a pre-trained Word2Vec model.

The input is a bunch of files,
the output is a CSV file without a header schema line.
"""
import csv
from functools import partial, reduce
from itertools import starmap
from operator import concat
import re

import click
from gensim.matutils import corpus2csc
import joblib
import pandas as pd
from unidecode import unidecode

from clea.core import Article
from clea.join import aff_contrib_full


TEXT_ONLY_REGEX = re.compile("[^a-zA-Z ]")
DEFAULT_DICTIONARY_DUMP = "dictionary_w2v_both.dump"
DEFAULT_MODEL_DUMP = "rf_w2v_200.dump"
COMMON_FIELDS = [
    ("article_meta", 0, "article_title"),
    ("journal_meta", 0, "journal_title"),
    ("journal_meta", 0, "publisher_name"),
]
ROWS_FIELDS = [
    "addr_city",
    "addr_state",
    "aff_text",
    "contrib_bio",
    "contrib_prefix",
    "contrib_name",
    "contrib_surname",
    "institution_orgdiv1",
    "institution_orgdiv2",
    "institution_orgname",
    "institution_orgname_rewritten",
    "institution_original",
    "institution_orgname_rewritten",
]


def nestget(data, *path, default):
    """Getter for data in nested dicts/lists/"itemgettables"."""
    for key_or_index in path:
        try:
            data = data[key_or_index]
        except (KeyError, IndexError, TypeError):
            return default
    return data


nestget_list = partial(nestget, default=[])
nestget_str = partial(nestget, default="")


def pre_normalize(name):
    return TEXT_ONLY_REGEX.sub("", unidecode(name).lower())


class Classifier:

    def __init__(self, dictionary_file=DEFAULT_DICTIONARY_DUMP,
                       model_file=DEFAULT_MODEL_DUMP):
        self.dictionary = joblib.load(dictionary_file)
        self.rf_model = joblib.load(model_file)
        self.u = self.rf_model.u
        self.num_terms = len(self.dictionary)

    def msg2bow(self, msg):
        return self.dictionary.doc2bow(pre_normalize(msg).split())

    def msg2csc(self, msg):
        return corpus2csc([self.msg2bow(msg)], num_terms=self.num_terms)

    def predict(self, msg):
        return self.rf_model.predict(self.msg2csc(msg).T @ self.u)[0]

    def predict_proba(self, msg):
        result = self.rf_model.predict_proba(self.msg2csc(msg).T @ self.u)
        result_series = pd.Series(result.ravel(), index=self.rf_model.classes_)
        return result_series[result_series > 0].sort_values(ascending=False)


def process_file(classifier, xml_file, csv_writer):
    art = Article(xml_file)
    common_lists = starmap(partial(nestget_list, art), COMMON_FIELDS)
    common_values = reduce(concat, common_lists)
    for idx, row_dict in enumerate(aff_contrib_full(art)):
        row = [row_dict[field] for field in ROWS_FIELDS]
        msg = " ".join(reduce(concat, row) + common_values)
        result = classifier.predict(msg)
        expected = "|".join(set(row_dict["addr_country_code"]))
        csv_writer.writerow([result, expected, idx, xml_file.name])


@click.command(help=__doc__)
@click.option("output_file", "-o", "--output", type=click.File("w"),
              default="-",
              help="Headerless CSV output, "
                   "defaults to the standard output stream.")
@click.argument("xml_files", type=click.File("r"), nargs=-1, required=True)
def main(xml_files, output_file):
    classifier = Classifier()
    csv_writer = csv.writer(output_file)
    for xml_file in xml_files:
        process_file(classifier, xml_file, csv_writer)


if __name__ == "__main__":
    main()
