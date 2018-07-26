#!/usr/bin/env python
from tornado import web, ioloop
from pprint import pprint


class PrinterHandler(web.RequestHandler):

    def get(self):
        pprint({
            "method": self.request.method,
            "host": self.request.host,
            "host_name": self.request.host,
            "uri": self.request.uri,
            "path": self.request.path,
            "version": self.request.version,
            "protocol": self.request.protocol,
            "full_url": self.request.uri,

            "cookies": self.request.cookies,
            "headers": list(self.request.headers.get_all()),
            "remote_ip": self.request.remote_ip,

            "query": self.request.query,
            "arguments": self.request.arguments,
            "query_arguments": self.request.query_arguments,

            "body": self.request.body,
            "body_arguments": self.request.body_arguments,
            "body_arguments dict comprehension":
                {k: [v.decode("utf-8") for v in vs]
                 for k, vs in self.request.body_arguments.items()},
        })


application = web.Application([(r"/scielo.php", PrinterHandler)], debug=True)
application.listen(8000)
ioloop.IOLoop.current().start()
