const express = require('express')
// instanciando a express
const app = express()
const port = 3000

app.get('/',(req,res)=>{
    res.send('<h1>Hola mundo express</h1>')
})

// para pasar un json
app.get('/json',function(req,res){
    res.json({nombre:'Fabio'});
})

// para pasar una variable
app.get('/usuario/:id',function(req,res){
    res.send("usuario id: " + req.params.id);
})

app.listen(port,()=>{
    console.log('Servidor en http://localhost:',port)
})

