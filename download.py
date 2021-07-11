# download a file, save local
import requests
import os
url = "http://shelysafrica.com/images/shelys-logo/Shelys-AfricaLG.png"

logo = requests.get(url)

data = logo.content
h = logo.headers
print(f"{h.get('content-type')}")
# print(data)
# print(logo)
with open("beta-logo.png","wb") as fo:
    fo.write(data)
with open("beta-logo.png","rb") as fi:
    fi.read()
    print(fi.read())

#    with open("beta-logo.svg","wb") as s:

#        s.write(stor)
