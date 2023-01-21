import http.server
import socketserver

port = 8002

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", port), handler) as httpd:
    print("server started...")
    httpd.serve_forever()