# Tugas 1
### Server dijalankan di 3 server yang berbeda, masing-masing client connect ke server tersebut
Kondisi awal server dengan port 3100,3101,3102 menyala
![Kondisi Awal](Foto/kondisi_awal.png)

Client mengirimkan pesan ke server port 3100
![3100](Foto/3100.png)

Client mengirimkan pesan ke server port 3101
![3101](Foto/3101.png)

Client mengirimkan pesan ke server port 3102
![3101](Foto/3102.png)

### Server dijalankan di komputer yang berbeda, client mencoba untuk mengirimkan file
Kondisi awal server di komputer yang berbeda(ip=192.168.1.7)

![server_awal_1a](Foto/1a_server_awal.jpg)

Client(pc saya dengan ip=192.168.1.19) mengirimkan file ke server

![client_1a](Foto/1a_client.png)

Server setelah mendapatkan kiriman file

![server_akhir_1a](Foto/1a_server_sent.jpg)

![file_1a](Foto/1a_file_hasil.jpg)

### Server dijalankan di komputer saya, client(komputer lain) request file untuk dikirimkan dari server
Kondisi awal server di pc saya(ip=192.168.1.19)
![server_awal_1b](Foto/1b_server_awal.png) 

Client(ip=192.168.1.7) meminta dan mendapatkan file dengan nama *22958.jpg*

![client_1b](Foto/1b_client.jpg)

Server menerima request dan mengirimkan file yang ada

![server_akhir_1b](Foto/1b_server_hasil.png)

Client berhasil mendapatkan file dengan nama *hasil22958.jpg*

![file_hasil_1b](Foto/1b_file_hasil.jpg)