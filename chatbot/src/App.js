import React from "react";
import {Routes, Route} from 'react-router-dom';
import Playground from "./Playground";
import Home from "./Home";
import Documentation from "./Documentation";

export default function App(){
  return(
    <div>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/playground" element={<Playground/>}/>
        <Route path="/documentation" element={<Documentation/>}/>
      </Routes>
    </div>
  )
}