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

        elif self.path =="/create":
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(bytes(f"creating file","utf-8"))
                
        else:
            self.send_response(404)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(bytes(f"<body>Page Not Found</body>","utf-8"))   


   

def build_webserver(host, port) -> HTTPServer:
    return HTTPServer((host,port),RequestHandler)


my_server = build_webserver("localhost",8000)
my_server.serve_forever()

