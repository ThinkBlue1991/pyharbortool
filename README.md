# pyharbortool
SDK about harbor
## Install
```
pip3 install pyharbortool==0.1
```
## Usage
```
from pyharbor import HarborClient
hc=HarborClient(host="127.0.0.1:443",user="admin",password="Harbor12345",protocol="https")
print(hc)
```
