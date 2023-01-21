import http.server
import socketserver

class CustomHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'main.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler = CustomHttpRequestHandler
PORT = 8005


with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Server startd at localhost:{str(PORT)}, serving html...")
    httpd.serve_forever()