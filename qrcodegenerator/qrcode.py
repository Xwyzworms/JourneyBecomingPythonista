import pyqrcode

s = "38123128"

url = pyqrcode.create(s)

url.png('QrPram.png',scale=6,module_color=[0,0,0,128])
url.show()
url.save()