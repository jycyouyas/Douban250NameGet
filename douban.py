# coding: utf-8
import os
os.system("touch douban250.txt")
for i in range(10):
    number=i*25
    url=f"\'https://movie.douban.com/top250?start={number}&filter=\'"
    cmd = f"curl {url} >> douban250.txt"
    os.system(cmd)
    
with open("douban250.txt","r") as file:
  name=[]
  for i in file:
      if "<span class=\"title\">" in i and "&nbsp" not in i and "main-title" not in i and "sub-title" not in i :
          name.append(i)
          
os.system("rm douban250.txt")

sort=1
for i in name:
    l=i.find(">")
    r=i.rfind("<")
    movie_name=i[l+1:r]
    with open("douban250.txt","a") as file_to_write:
        file_to_write.write(f"{sort}.{movie_name}\n")
    sort=sort+1
    
    
