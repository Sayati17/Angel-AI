import React from "react";
import HeaderComponent from "./Header";
import { Box, Typography } from "@mui/material";

export default function Home() {
  return (
    <>
      <HeaderComponent />
      <Box sx={{ 
        display: 'flex', 
        justifyContent: 'center',   // Centers horizontally
        alignItems: 'center',       // Centers vertically
        marginTop: '50px'            // Keeps the 50px margin if needed
      }}>
        <Box sx={{ 
          display: 'inline-block', 
          backgroundColor: 'lightblue', 
          padding: '20px', 
          borderRadius: '8px',
          maxWidth:'60%',
          justifyContent:'center',
          alignItems:'center'
        }}>
          <Typography sx={{ textIndent: '20px', fontSize: '16px' }}>
            Angel AI merupakan tools yang dirancang untuk meningkatkan aspek keamanan dari penggunaan LLM Chat Bot. 
            Angel AI bekerja sebagai filter untuk setiap input yang masuk ke dalam Chat Bot, sebelum input diproses oleh Chat Bot AI, 
            input tersebut akan melewati beberapa lapisan pertahanan yang terdapat pada Angel AI, pertama-tama input akan diperiksa 
            oleh Model AI Text Classifier yang sudah dilatih untuk dapat mendeteksi Prompt Injection atau Jailbreaking, Model 
            AI akan menghasilkan penilaian yang nantinya akan dibandingkan dengan batasan aman yang sudah ditentukan. Input 
            juga akan diperiksa dan dibandingkan dengan database yang sudah disiapkan yang berisikan dataset Prompt Injection atau 
            Jailbreaking sehingga dapat menghasilkan nilai maksimal berdasarkan dari data dengan tingkat kemiripan tertinggi. 
            <br/><br/>
            Setelah mendapatkan penilaian dari Model AI dan kemiripan input user dengan database, masing-masing dari penilaian 
            tersebut akan dibandingkan dengan batasan aman yang sudah ditentukan, jika salah satu dari penilaian lebih besar 
            dari batasan aman yang sudah ditentukan, maka input user dikategorikan sebagai prompt yang berbahaya dan tidak 
            akan dilanjutkan ke Chat Bot melainkan Chat Bot akan memberikan warning. Jika input dikategorikan sebagai
            input yang aman, maka input akan melewati proses sanitasi untuk memastikan bahwa input benar benar aman,
            proses sanitasi dilakukan dengan cara memeriksa apakah pada input user terdapat kata-kata yang biasanya 
            digunakan untuk teknik Prompt Injection atau Jailbreaking, jika pada input user terdapat kata-kata
          </Typography>
        </Box>
      </Box>
    </>
  );
}
