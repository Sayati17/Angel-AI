# Angel-AI

**#Documentation**

**#Database Setup**
**Langkah 1: Unduh dan install XAMPP**
- Unduh XAMPP dari situs resmi XAMPP.
- Setelah instalasi selesai, buka XAMPP Control Panel.

**Langkah 2: Jalankan MySQL dan phpMyAdmin**
- Pada XAMPP Control Panel, klik tombol Start di sebelah MySQL dan Apache.
- ![xampp](https://github.com/user-attachments/assets/b30f116a-a900-477b-9e7d-33a3922fb547)
- Klik Admin disebelah MySQL untuk membuka phpMyAdmin di browser Anda.

**Langkah 3: Buat Database**
- Pada phpMyAdmin, pilih tab SQL.
- Lalu masukan script berikut

CREATE DATABASE angelai;

CREATE TABLE tablePromptInjection (
InjectionId INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
InjectionName TEXT NULL,
InjectionDescription VARCHAR(255) NULL
);

CREATE TABLE tableSanitize (
sanitizeId INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
SanitizeName TEXT NULL
);

**Langkah 4: Impor Data CSV**
- File csv yang digunakan untuk import data terdapat pada repository Github Angel AI
- Untuk tabel tablePromptInjection:
1. Pilih tabel tablePromptInjection.
   ![Import_Prompt 88338de4d794cc8bb1ff](https://github.com/user-attachments/assets/58f845aa-0502-4606-b6b4-c3e2f4ee56ec)
2. Klik tab Import dan pilih file PromptInjeectionDataset.csv dari repository.
  ![Import_Prompt2 d16bea5966e30ee2209e](https://github.com/user-attachments/assets/3f0fbfc1-8b93-4019-a761-f3b72abead9e)
3. Pastikan format diatur ke CSV.
   ![Import_Prompt3 f5e370f2914c6ad2eb12](https://github.com/user-attachments/assets/6f49c88b-18fe-482e-8e29-3f009289d229)
4. Pilih Done pada bagian bawah page

- Untuk tabel **tableSanitize**:
1. Pilih tabel tableSanitize.
2. Ulangi langkah yang sama dengan file PromptInjectionDataset.csv

**Langkah 5: Verifikasi Data**
- Klik pada masing-masing tabel untuk memastikan data telah berhasil diimpor.
  ![SuccessImport bd758efe8f55f85e9146](https://github.com/user-attachments/assets/bb719d51-19d4-4466-bc13-52654854a0f2)

**#Pinecone Setup**
- Masuk ke dalam website Pinecone
- Masukan Akun Pinecone, jika belum ada, lakukan registrasi
- Saat membuat API KEY, pastikan untuk menyalin dan menyimpan API KEY di tempat yang aman karena hanya bisa dilihat sekali saja.
- Pada Tab di bagian kiri Pinecone, pilih Database, lalu Indexes
  ![Pinecone1 d407856cc4c5b4b8ca51](https://github.com/user-attachments/assets/b7706bc4-d32d-4808-a2b9-9d6607c1f1c8)
- Lalu pilih Create Index
- Lalu masukan spesifikasi berikut:
  ![Pinecone2 c8886fc766c47f278231](https://github.com/user-attachments/assets/bca19541-c1e2-4e99-95ad-4ef0ec8f2f56)
  ![Pinecone3 68608ed1f34183785adf](https://github.com/user-attachments/assets/c53331b8-f118-426b-9645-794f7d270433)
  ![Pinecone4 c2cc456480293982c7c4](https://github.com/user-attachments/assets/14fb7f65-f319-4c91-9b45-7de85917bcc0)

**#Configuration**
**Langkah 1: Cloning Repository**
- Untuk melakukan konfigurasi pada Angel AI, kita perlu melakukan cloning pada Repository Github Angel AI
- Cloning bisa dilakukan dengan memasukan command git clone https://github.com/Sayati17/Angel-AI.git pada Command Prompt / Command Line di folder yang diinginkan
- Pada folder angelai, tambahkan dan masukan file dengan nama config.py
- Lalu masukan template berikut:<br/>
"""<br/>
db_user = ""<br/>
mysql_db = ""<br/>
db_host = ""<br/>
db_password = ""<br/>
db_port = 3306<br/>
query = "SELECT * FROM tablePromptInjection"<br/>
query2 = "SELECT * FROM tableSanitize"<br/>
<br/>
pinecone_api_key = "" # Get from Pinecone API Keys tab<br/>
pinecone_region = ""<br/>
#Get from index's region pinecone_db = "angelai"<br/>
pinecone_dimension = 384<br/>
pinecone_index_name = "angelai"<br/>
pinecone_index_host = "" # Index host from Pinecone<br/>
<br/>
model_name = "protectai/deberta-v3-base-prompt-injection-v2"<br/>
"""<br/>
**Langkah 2: Install python requirements**
- Saat melakukan cloning pada repository github, terdapat file requirements.txt yang dapat digunakan untuk install library yang akan digunakan
- jalankan Command Prompt / Terminal pada folder yang sama, lalu masukan command pip install -r requirements.txt

**#Integration with Chatbot AI**

- Sebagai contoh, disini kami menggunakan Gemini AI API untuk integrasi
- Pada API yang akan digunakan untuk memproses prompt, kami mengimport dan memanggil class yang dipakai oleh Angel AI
  
from sim_db import simmilarity_check
from text_classifier import textClassifier
from conn import mysqlConnect
from sanitize import sanitizePrompt

- Untuk menggunakan fungsi Text Classifier dan Database Simmilarity Search, kami akan memanggil class dan functionnya
  ![download](https://github.com/user-attachments/assets/509d9214-01f9-4630-b28d-42830209b661)
- Function check_simmilarity dan get_classification_score akan mereturn output berupa score dan akan ditampung di dalam variable
- Untuk melakukan evaluase Score kami mengggunakan logic berikut:
  ![download (1)](https://github.com/user-attachments/assets/8b569c5c-a1be-4508-a7d6-0da43f69d6dd)
- Kami melakukan sanitasi prompt setelah prompt sudah melewati proses evaluasi (dinyatakan aman secara score) dan berikut adalah cara menggunakan sanitasi
  ![download (2)](https://github.com/user-attachments/assets/c3746263-eb0b-4a19-9cf2-82a3e089ddeb)
- yang akan diterima oleh Chabot AI adalah prompt yang sudah disanitasi dan akan diproses oleh Chatbot AI.

