import os
from zipfile import ZipFile

os.mkdir('0')
filepath = "0"
ZipFile('flag.zip', 'r').extractall(filepath)
for i in range(1000,0,-1):
	directionpath = filepath + "/direction.txt"
	f = open(directionpath,'r')
	direction = str(f.read())
	f.close()
	zippath = filepath+"/"+str(i)+direction+".zip"
	filepath = filepath + "/"+str(i)
	os.mkdir(filepath)
	ZipFile(zippath, 'r').extractall(filepath)
f = open(filepath+"/flag.txt")
print(f.read())
