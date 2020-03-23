from handler import Handle
import json
import logging

'''
        PROTOCOL FORMAT

string terbagi menjadi 2 bagian yang dipisahkan oleh spasi
Format : command *spasi* parameter *spasi* parameter

        FITUR

a. Meletakkan File
   Untuk meletakkan file ke dalam folder "storage"
   Request : add_file
   Parameter : namafile *spasi* isi dari file
   Response : berhasil -> "File Added"
              gagal -> "ERROR"

b. List File
   Untuk melihat list file di dalam folder 'storage'
   Request : list_file
   Parameter: -
   Response: list file yang ada dalam folder 'storage'

c. Mengambil File
   Untuk mengambil file berdasarkan nama file dari folder 'storage'
   Request : get_file
   Parameter : namafile yang ingin diambil
   Response: file ter download pada folder tempat script berada

d. Jika command tidak dikenali akan merespon dengan ERRCMD

'''
p = Handle()

class Machine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='add_file'):
                print("add_file")
                filename = cstring[1].strip()
                file = cstring[2].strip()
                # print(file)
                print("Adding",filename)
                # print()
                p.add(filename,file.encode())
                return "File Added"

            elif (command=='get_file'):
                print("get_file")
                filename = cstring[1].strip()
                print("Retrieving", filename)
                hasil = p.get(filename)
                return hasil

            elif (command=='list_file'):
                logging.info("list_file")
                data = {}
                data['files'] = []
                hasil = p.list()
                for filename in hasil:
                    data['files'].append({"filename":filename})
                return json.dumps(data, indent=4)
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    machine = Machine()