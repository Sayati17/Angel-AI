import React from "react";
import HeaderComponent from "./Header";
import { Box, Typography, Link } from "@mui/material";
import XAMPP from "./component/Assets/XAMPP.png"
import Import_Prompt from "./component/Assets/Import_Prompt.png"
import Import_Prompt2 from "./component/Assets/Import_Prompt2.png"
import Import_Prompt3 from "./component/Assets/Import_Prompt3.png"
import Success_Import from "./component/Assets/SuccessImport.png"
import Pinecone1 from "./component/Assets/Pinecone1.png"
import Pinecone2 from "./component/Assets/Pinecone2.png"
import Pinecone3 from "./component/Assets/Pinecone3.png"
import Pinecone4 from "./component/Assets/Pinecone4.png"

export default function Home() {
  return (
    <>
      <HeaderComponent />
      <Box sx={{ 
        display: 'flex', 
        justifyContent: 'center',
        alignItems: 'center',
        marginTop: '50px' 
      }}>
        <Box sx={{ 
          display: 'inline-block', 
          padding: '20px', 
          maxWidth:'60%',
          justifyContent:'center',
          alignItems:'center'
        }}>
          <Typography sx={{fontSize: '16px', lineHeight: '1.6' }}>
            <Typography variant="h3">Database Setup</Typography>
            <br/> 
            <b>Langkah 1: Unduh dan Instal XAMPP</b><br/>
            - Unduh XAMPP dari situs resmi <Link href="https://www.apachefriends.org/index.html" sx={{color:'blue'}}>XAMPP</Link>. <br/>
            - Setelah instalasi selesai, buka XAMPP Control Panel.<br/><br/>

            <b>Langkah 2: Jalankan MySQL dan phpMyAdmin</b><br/>
            - Pada XAMPP Control Panel, klik tombol <b>Start</b> di sebelah MySQL dan Apache.<br/>
            <img src={XAMPP} alt="XAMPP"/>
            - Klik <b>Admin</b> disebelah MySQL untuk membuka phpMyAdmin di browser Anda.<br/><br/>

            <b>Langkah 3: Buat Database</b><br/>
            - Pada phpMyAdmin, pilih tab <b>SQL</b>.<br/>
            - Lalu masukan script berikut<br/><br/>
            <code>
              CREATE DATABASE angelai; <br/><br/>

              CREATE TABLE tablePromptInjection ( <br/>
              InjectionId INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, <br/>
              InjectionName TEXT NULL, <br/>
              InjectionDescription VARCHAR(255) NULL <br/>
              );<br/><br/>

              CREATE TABLE tableSanitize ( <br/>
              sanitizeId INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, <br/>
              SanitizeName TEXT NULL <br/>
              );
            </code><br/><br/>

            <b>Langkah 4: Impor Data CSV</b><br/>
            - File csv yang digunakan untuk import data terdapat pada repository <Link href="https://github.com/Sayati17/Angel-AI" sx={{color:'blue'}}>Github Angel AI</Link> <br/>
            - Untuk tabel <b>tablePromptInjection</b>:<br/>
              1. Pilih tabel <b>tablePromptInjection</b>.<br/>
              <img src={Import_Prompt} alt="Import Prompt"/> <br/>
              2. Klik tab <b>Import</b> dan pilih file <b>PromptInjeectionDataset.csv</b> dari repository.<br/>
              <img src={Import_Prompt2} alt="Import Prompt2"/> <br/>
              3. Pastikan format diatur ke <b>CSV</b>.<br/><br/>
              <img src={Import_Prompt3} alt="Import Prompt3"/> <br/>
              4. Pilih Done pada bagian bawah page <br/><br/>
            - Untuk tabel <b>tableSanitize</b>:<br/>
              1. Pilih tabel <b>tableSanitize</b>.<br/>
              2. Ulangi langkah yang sama dengan file <b>PromptInjectionDataset.csv</b>.<br/><br/>

            <b>Langkah 5: Verifikasi Data</b><br/>
            - Klik pada masing-masing tabel untuk memastikan data telah berhasil diimpor.<br/>
            <img src={Success_Import} alt="success"/><br/>


            <Typography variant="h3">Pinecone Setup</Typography><br/>
            - Masuk ke dalam website <Link href="https://app.pinecone.io/"sx={{color:'blue'}}>Pinecone</Link> <br/>
            - Masukan Akun Pinecone, jika belum ada, lakukan registrasi <br/>
            - Saat membuat API KEY, pastikan untuk menyalin dan menyimpan API KEY di tempat yang aman karena hanya bisa dilihat sekali saja.<br/>
            - Pada Tab di bagian kiri Pinecone, pilih Database, lalu Indexes<br/>
            <img src={Pinecone1} alt="pinecone1"/> <br/>
            - Lalu pilih Create Index <br/>
            - Lalu masukan spesifikasi berikut: <br/>
            <img src={Pinecone2} alt="pinecone2"/> <br/>
            <img src={Pinecone3} alt="pinecone3"/> <br/>
            <img src={Pinecone4} alt="pinecone4"/> <br/>

            <Typography variant="h3">Configuration</Typography><br/>
            <b>Langkah 1: Cloning Repository</b><br/>
            - Untuk melakukan konfigurasi pada Angel AI, kita perlu melakukan cloning pada <Link href="https://github.com/Sayati17/Angel-AI" sx={{color:'blue'}}>Repository Github Angel AI</Link><br/>
            - Cloning bisa dilakukan dengan memasukan command <code>git clone https://github.com/Sayati17/Angel-AI.git </code> pada Command Prompt / Command Line di folder yang diinginkan <br/>
            - Pada folder angelai, tambahkan dan masukan file dengan nama config.py
          </Typography>
        </Box>
      </Box>
    </>
  );
}
