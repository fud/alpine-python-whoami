#!/usr/bin/env python

import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080

class HelloWorldRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        self.send_header("Content-type", "text/html")
        self.end_headers()

        message = socket.gethostname()
        self.wfile.write(bytes(message, "utf8"))
        return


def run():

    server_address = ("0.0.0.0", PORT)
    httpd = HTTPServer(server_address, HelloWorldRequestHandler)

    print("✓ Server running on port {}...".format(PORT))
    httpd.serve_forever()


if __name__ == "__main__":
    run()
