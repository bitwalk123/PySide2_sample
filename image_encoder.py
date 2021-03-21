from bz2 import compress
from base64 import b64encode

filename = 'qt.png'
with open(filename, 'rb') as fileobj:
    data = b64encode(compress(fileobj.read()))

print(data)