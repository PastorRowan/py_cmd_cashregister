PastorRowan
pastorrowan
🫡One step at a time.

Darkcustard — 30/03/2023 18:42
dooota 2
I thought you were a league boy
PastorRowan — Today at 20:54
ayo big man
sorry im a bit late
mind still helping me
Darkcustard — Today at 20:54
9:30
we begin
PastorRowan — Today at 20:55
oh my god i thought it was 9:55
sorry
Darkcustard — Today at 20:55
no bro dw
Darkcustard — Today at 21:32
ready?
PastorRowan — Today at 21:32
yeah
i just gotta get my mic
Darkcustard — Today at 21:32
in molo when u ready
# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer

data = 'Halo'
connected = False
time_since_last_poll = 0
Expand
server.py
2 KB
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

Handle Data
        if self.path == "/data":
            self.send_response(200)
            self.wfile.write(bytes("hi there","utf-8"))

        elif self.path =="/view":
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(bytes(f"Viewing data : <{data}> <br> length : {len(data)}","utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(bytes(f"<body>Page Not Found</body>","utf-8"))




def build_webserver(host, port) -> HTTPServer:
    return HTTPServer((host,port),RequestHandler)
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
Expand
script.py
1 KB
Darkcustard — Today at 21:46
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
Expand
script.py
1 KB
﻿
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
       
        # Handle Data
        if self.path == "/data":
            self.send_response(200)
            self.wfile.write(bytes("hi there","utf-8"))

        elif self.path =="/view":
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(bytes(f"Viewing data","utf-8"))
                
        else:
            self.send_response(404)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(bytes(f"<body>Page Not Found</body>","utf-8"))   


   

def build_webserver(host, port) -> HTTPServer:
    return HTTPServer((host,port),RequestHandler)


my_server = build_webserver("localhost",8000)
my_server.serve_forever()

script.py
1 KB