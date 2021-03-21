from zlib import compress
from base64 import b64encode

#filename = 'wx.png'
filename = 'qt.png'
with open(filename, 'rb') as fileobj:
    #data = b64encode(compress(fileobj.read()))
    data = b64encode(fileobj.read())

print(data)