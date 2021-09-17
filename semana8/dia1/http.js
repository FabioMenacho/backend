const http = require('http');

// req=requeriment, res=response
http.createServer(function(req,res){
    console.log('nueva petición http');
    // me da la ruta
    console.log('ruta: ' + req.url);
    res.write('<h1>Hola mundo node</h1>');
    res.end();
}).listen(3000);