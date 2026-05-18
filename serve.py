#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os

HTML_FILE = r"d:\xpeng.code\出免车主积分续电卡\站点详情页\站点详情.html"
PORT = 8080

# 切到 HTML 所在目录，保证 asset 相对路径正常解析
os.chdir(os.path.dirname(HTML_FILE))

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    url = f"http://localhost:{PORT}/{os.path.basename(HTML_FILE)}"
    print(f"预览地址: {url}")
    print(f"按 Ctrl+C 停止")
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
