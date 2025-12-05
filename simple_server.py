import http.server
import socketserver
import os

# 设置端口号
PORT = 8080

# 获取当前目录
handler = http.server.SimpleHTTPRequestHandler

try:
    # 创建服务器
    with socketserver.TCPServer("", PORT) as httpd:
        print(f"服务器启动在 http://localhost:{PORT}")
        print("按 Ctrl+C 停止服务器")
        # 启动服务器
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n服务器已停止")