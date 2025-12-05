import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

print(f"Starting local server at http://localhost:{PORT}")
print(f"Serving files from: {DIRECTORY}")

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Server started. Opening browser...")
        webbrowser.open(f"http://localhost:{PORT}/index.html")
        print("Press Ctrl+C to stop the server.")
        httpd.serve_forever()
except OSError as e:
    if e.errno == 10048:
        print(f"Port {PORT} is already in use. Please try a different port.")
    else:
        raise
except KeyboardInterrupt:
    print("\nServer stopped.")
