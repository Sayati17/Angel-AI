import React from "react";
import { Box, Stack, Link, Typography } from "@mui/material";
import image from "./component/Logo/image.png"

export default function HeaderComponent(){
    return (
        <>
          <Box sx={{backgroundColor:"black"}}>
            <Stack direction="row" spacing="50px" sx={{display:'flex', alignContent:'center', alignItems:'center', justifyContent:'center'}}>
              <Link 
                href="/playground" 
                sx=
                    {{
                        alignContent:'center', 
                        display:'flex', 
                        alignItems:'center', 
                        textDecoration:'none', 
                        '&:hover':{
                            color:'white',
                        }
                    }} 
                underline="hover"
                >
                <Typography sx={{color:"white", fontSize:'18px'}}>Playground</Typography>
              </Link>
              <Box sx={{alignContent:'center', display:'flex', alignItems:'center'}}>
                <Link href="/">
                  <img src={image} alt="test"/>
                </Link>
              </Box>
              <Link 
                href="/documentation" 
                sx=
                    {{
                        alignContent:'center', 
                        display:'flex', 
                        alignItems:'center', 
                        textDecoration:'none',
                        '&:hover':{
                            color:'white'
                        }
                    }}
                underline="hover"
                >
                <Typography sx={{color:"white", fontSize:"18px"}}>Documentation</Typography>
              </Link>
            </Stack>
          </Box>
        </>
    );
}