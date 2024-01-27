const express = require("express");
const app = express();
const portNum = 8088;

app.get("/",(req,res)=>{
    res.send("==");
});

app.listen(portNum,()=>{
    console.log(`server:${portNum}`);
});