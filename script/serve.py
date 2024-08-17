import http.server
import socketserver
import os

DIRECTORY = "C:/atari-monk/code/apollo"
os.chdir(DIRECTORY)

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving directory {DIRECTORY} at port {PORT}")
    httpd.serve_forever()
