import re

url= 'https://csf101-server-cap1.onrender.com/get/input/352'
txt_file=re.get(url)

with open('352.txt','wb')as file:
    data = file.write(txt_file.content)

print('Download 352.txt')



