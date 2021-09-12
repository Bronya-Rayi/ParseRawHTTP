from http.server import BaseHTTPRequestHandler
from io import BytesIO
import base64

class HTTPRequestHeader(BaseHTTPRequestHandler):
    # print(request.error_code)       # None  (check this first)
    # print(request.command)          # "GET"
    # print(request.path)             # "/who/ken/trust.html"
    # print(request.request_version)  # "HTTP/1.1"
    # print(len(request.headers))     # 3
    # print(request.headers.keys())   # ['Host', 'Accept-Charset', 'Accept']
    # print(request.headers._headers) # [('Host', 'cm.bell-labs.com'), ('Accept', 'application/xml') ...
    # print(request.headers['host'])  # "cm.bell-labs.com"
    # https://stackoverflow.com/questions/4685217/parse-raw-http-headers?noredirect=1&lq=1
    def __init__(self, request_text):
        self.rfile = BytesIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message


def ParseRawHTTP(http_raw,is_base64=False):
    if is_base64:
        http_raw = base64.b64decode(http_raw.strip())
    else:
        http_raw = http_raw.lstrip().encode('utf-8')

    # 解析http请求头
    http_headers_class = HTTPRequestHeader(http_raw)
    if http_headers_class.error_code != None:
        raise Exception("HTTP header parse error !", http_headers_class.error_code)
    http_headers_dict = dict(http_headers_class.headers._headers)

    # 构造请求
    http_url = http_headers_dict['Host'] +  http_headers_class.path
    # print(http_headers_dict['Content-Length'])
    # 筛选出http body
    http_method = http_headers_class.command
    if http_method == 'POST':
        last_header = http_headers_dict[http_headers_class.headers.keys()[-1]].encode('utf-8')
        http_body = http_raw[http_raw.index(last_header):].replace(last_header,b'').lstrip()
        content_length = len(http_body)
        http_headers_dict['Content-Length'] = str(content_length).encode('utf-8')
    else:
        http_body = ''
    return http_url.strip(),http_method.strip(),http_headers_dict,http_body

# http_url,http_method,http_headers_dict,http_body = ParseRawHTTP(Raw_HTTP_Strings,True)
# print("URL : " + http_url)
# print("+--------------------------------------------------------------------+")
# print("Headers : " , http_headers_dict)
# print("+--------------------------------------------------------------------+")
# print("Body : ", http_body.decode('utf8'))
# req = requests.request(method=http_method,url = "http://127.0.0.1:8000",headers=http_headers_dict,data=http_body).text
# print(req)