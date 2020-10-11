from zlib import compress
from base64 import b64encode

with open("wx.png", "rb") as fileobj:
    #data = b64encode(compress(fileobj.read()))
    data = b64encode(fileobj.read())

print(data)