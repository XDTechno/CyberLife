import cgi,os,re,json,threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from ..base_view import View
view:View=...
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        #solve strict MIME check
        if(self.path.endswith(".js")):
            self.send_header("Content-type",'application/javascript')
        self.end_headers()
        
        if(self.path.startswith("/map")):
            if not hasattr(view,'mapdata'):
                return None
            if view is not Ellipsis:
                content=json.dumps(view.mapdata,default=lambda o:o.__dict__)
                self.wfile.write(bytes(content,'utf-8'))
        if(self.path.startswith("/fps")):
            self.wfile.write(bytes(json.dumps([1]),'utf-8'))
        if(self.path.startswith("/message")):
            content=json.dumps(view.message_cache)
            
            self.wfile.write(bytes(content,"utf-8"))
            view.message_cache=[]
        if re.match(r'.*\.[a-zA-Z]+$', self.path):
            current_dir = os.path.abspath(os.getcwd())
            file_path = os.path.join(current_dir,"view\\webview\\dist", self.path.lstrip('/'))
            content="Nope"
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                self.wfile.write( bytes(content, 'utf-8'))
            except:
                pass
        #super().do_GET()  # 其他请求就用默认的处理方式
 
    def do_POST(self):
        if self.path == '/submit':
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )
            message = form.getvalue('message')
            self.send_response(200)
            self.end_headers()
            response = f"Message received: {message}"
            self.wfile.write(response.encode())
        else:
            self.send_error(404, "File not found")
    def log_message(self, format, *args):
        # 重写 log_message 方法,禁止打印任何消息
        pass

def launch(view_instance):
    server_address = ('', 8008)
    print(f"server start at http://127.0.0.1:{server_address[1]}")
    
    global view
    view =view_instance
    view.recv("loaded")

    try:
        thr=threading.Thread(target=lambda :HTTPServer(server_address, MyHandler).serve_forever())
        thr.start()
    except :
        print("something went wrong.")
    
if __name__ == '__main__':
    launch()


