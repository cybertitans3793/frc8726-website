"""
Preview the website on your own computer.

    python preview.py          (on some computers: python3 preview.py)

Then open  http://localhost:8000  in your browser.
Press Ctrl+C in this window to stop it.

Why not just double-click the .html file?  The header and footer live in
html/partials/ and the real web server pastes them into each page. A plain
browser can't do that, so pages opened directly show no header or footer.
This script does the same pasting the real server does.

Needs Python 3 (free: python.org, or the Microsoft Store on Windows).
Nothing else to install.
"""
import http.server
import os
import re
import webbrowser

PORT = 8000
SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html")

# Matches the include lines in each page, e.g. the one for partials/header.html
INCLUDE = re.compile(r'<!--#include virtual="([^"]+)"\s*-->')


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SITE, **kwargs)

    def do_GET(self):
        path = self.path.split("?")[0].split("#")[0]
        if path.endswith("/"):
            path += "index.html"
        file = os.path.join(SITE, path.lstrip("/"))
        # The live site lets you leave off ".html" (frc8726.org/team), so do the same here.
        if not os.path.exists(file) and os.path.exists(file + ".html"):
            file += ".html"
        if file.endswith(".html") and os.path.isfile(file):
            return self.send_page(file)
        return super().do_GET()  # images, CSS, etc.

    def send_page(self, file):
        with open(file, encoding="utf-8") as f:
            html = f.read()

        def paste(match):
            part = os.path.join(SITE, match.group(1).lstrip("/"))
            with open(part, encoding="utf-8") as f:
                return f.read()

        body = INCLUDE.sub(paste, html).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print(f"Previewing the site at http://localhost:{PORT}  (Ctrl+C to stop)")
    webbrowser.open(f"http://localhost:{PORT}")
    http.server.ThreadingHTTPServer(("localhost", PORT), Handler).serve_forever()
