
import base64

def safe_base64_decode(s):

    if len(s) % 4 != 0:
        for i in range(len(s) % 4):
            s = s + '='

    return base64.b64decode(s)


print(safe_base64_decode('YmluYXJ5AHN0cmluZw=='))