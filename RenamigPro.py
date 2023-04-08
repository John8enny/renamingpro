import os
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
d=input("Enter file name:")
s=input("Enter source directory:")
#For Mp3 files
if ".mp3"in d:
	audio = EasyID3(d)
	u=str(audio["title"])
#For FLAC Files
elif ".flac" in d:
	audio = FLAC(d)
	u=str(audio["title"])
#Filtering out unwanted Characters
bad=['[',']',"'"]
for i in bad:
    u = u.replace(i,'')
print(u)

#The os.rename() method allows you to rename files in Python. When used with the os.listdir() method, you can use os.rename() to rename all the files in a folder.

# Setting the extention

if ".mp3" in d:
	old_file_name = d
	new_file_name = s+u+".mp3"
elif ".flac" in d:
	old_file_name = d
	new_file_name = s+u+".flac"
#Renaming
os.rename(old_file_name, new_file_name)
#Confirmation Message().
print("File renamed!")
