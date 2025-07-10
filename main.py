import hashlib
import base64

def x_browser_validation(useragent):
    key = 'AIzaSyA2KlwBX3mkFo30om9LUFYQhpqLoa_BNhE'
    return base64.b64encode(hashlib.sha1(f'{key}{useragent}'.encode()).digest()).decode()

print(x_browser_validation('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'))
