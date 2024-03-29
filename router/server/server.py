from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import json
import struct
import ast
import sys

sock = socket.socket()
sock.connect(('127.0.0.1', 7070))


def bytes_to_json(data):
    out = []
    while data:
        out.append(data[:4])
        data = data[4:]
    gg = []
    for aa in out:
        gg.append(struct.unpack('i', aa)[0])
    data = []
    while gg:
        data.append(gg[:3])
        gg = gg[3:]

    gg = {"Product_path":[]}

    for hub_it in data:
        d = {"HubID": hub_it[0], "Dst_time": hub_it[1], "Dep_time": hub_it[2]}
        gg["Product_path"].append(d)
    return gg


class S(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print("Body:\n%s\n", post_data.decode('ascii'))
        try:
            d = dict(ast.literal_eval(json.loads(post_data)))
            id1 = int(d["first_hub"])
            id2 = int(d["last_hub"])
            weight = float(d["weight"])
            print(weight, "  ", id1, "  ", id2, '\n')
            res = struct.pack("dii", weight, id1, id2)
        except KeyError:
            return
        self._set_response()

        sock.send(res)
        data = sock.recv(1024)
        data = bytes_to_json(data)
        self.wfile.write(json.dumps(data).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, ip='188.134.78.182'):
    print(ip)
    server_address = (ip, 10000)
    httpd = server_class(server_address, handler_class)
    print(' Starting httpd...\n')
    try:
        print(" Started!\n")
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping httpd...\n')


if __name__ == '__main__':
    print('Start logging\n')
    run()
