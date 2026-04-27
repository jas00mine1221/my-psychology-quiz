import http.server
import socketserver
import webbrowser
import os

# 設定伺服器埠號
PORT = 8000

# 確保程式抓取到正確的 HTML 檔案名稱
# 如果你的檔案名稱不是 vango_quiz.html，請修改此處
HTML_FILE = "vango_quiz.html"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 如果存取根目錄，自動導向到你的心理測驗檔案
        if self.path == '/':
            self.path = '/' + HTML_FILE
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def run_server():
    # 檢查檔案是否存在
    if not os.path.exists(HTML_FILE):
        print(f"錯誤: 找不到檔案 '{HTML_FILE}'。")
        print("請確保此 Python 腳本與你的 HTML 檔案放在同一個資料夾中。")
        return

    handler = MyHandler
    
    # 允許地址重用，避免頻繁啟動時出現 Port 佔用錯誤
    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"伺服器已啟動於: {url}")
        print("按下 Ctrl+C 可停止伺服器。")
        
        # 自動打開預設瀏覽器
        webbrowser.open(url)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n伺服器已停止。")

if __name__ == "__main__":
    run_server()