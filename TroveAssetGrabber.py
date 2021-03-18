from bs4 import BeautifulSoup
import urllib.request
import urllib
from zipfile import ZipFile
import os

##Inputs
UserURL=input("Enter URL: ")
UserName=input("Enter zip name: ")
zipObj = ZipFile(UserName+".zip", 'w')
##Headers for HOST
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
##Getting links
parser = 'html.parser'  
resp = urllib.request.urlopen(UserURL)
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
##Downloading
for link in soup.select("[href$='.png'], [href$='.jpeg'], [href$='.jpg']"):
    print(link['href'])
    for i in link:
        try:
            urllib.request.urlretrieve(UserURL+"/"+i, i)
            zipObj.write(i)
            os.remove(i)
        except:
            pass
        try:
            urllib.request.urlretrieve(UserURL+"/"+link['href'], i)
            zipObj.write(i)
            os.remove(i)
        except:
            pass

zipObj.close()





