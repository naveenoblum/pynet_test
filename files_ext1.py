#!/usr/bin/env python
fin=open("file1.txt")
print(fin.read())
fout=open("file2.txt","w")
fout.close()
fout=open("file2.txt","a")
fout.write("test+file")
fout.close()
