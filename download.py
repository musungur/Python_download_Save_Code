# download a file, save local
import requests
import os

url = "http://shelysafrica.com/images/shelys-logo/Shelys-AfricaLG.png"

logo = requests.get(url)

data = logo.content
# h = logo.headers
headers = logo.headers
headers_type = headers.get('content-type')

path = os.getcwd()
# print(f"{h.get('content-type')}")
print(f"\n{headers}")
print(f"\n{headers_type}")

# print(data)
# print(logo)

# opens file in write mode. If not available, file gets created
with open("beta-logo.png","wb") as fo:
    fo.write(data)

# prints currecnt working directory    
    print(path)

# after above file written, open in read mode and read the file    
with open("beta-logo.png","rb") as fi:
    read = fi.read()

# reads blob on console in txts
    print(read)
