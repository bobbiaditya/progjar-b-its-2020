import shelve
import uuid
import socket
import os
import base64

class Handle:
    def __init__(self):
        if not os.path.exists("storage"):
            os.makedirs("storage")
    def add(self,filename=None,file=None):
        # file = file.encode()
        data_file = file
        f = open("storage/"+filename,"wb")
        f.write(data_file)
        return True

    def get(self,filename=None):
        temp = []
        f = open("storage/" +filename, "rb")
        hasil = f.read()
        f.close()
        hasil = str(hasil, "utf-8")
        return hasil

    def list(self):
        file_list = os.listdir("storage")
        return file_list

if __name__=='__main__':
    p = Handle()
    print(p.list())


