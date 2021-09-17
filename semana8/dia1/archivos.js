const fs = require('fs');

function leer(ruta,cb){
    fs.readFile(ruta,(err,data)=>{
        cb(data.toString());
    });
}

function escribir(ruta,contenido,cb){
    fs.writeFile(ruta,contenido,function(err){
        if(err){
            console.error('No pude escribir el texto',err);;
        } else {
            console.log('Se ha esccrito el texto');
        }
    })
}

function borrar(ruta,cb){
    fs.unlink(ruta,cb);
}
    
leer(__dirname + '/archivo1.txt',console.log);
escribir(__dirname + '/archivo2.txt','ESTE ES MI SEGUNDO ARCHIVO CREADO EN NODE JS',console.log)
// borrar(__dirname + '/archivo2.txt',console.log)