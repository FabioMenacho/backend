const http = require('http');

http.createServer(router).listen(3000);

function router(req,res){
    console.log('Nueva petición');
    console.log(req.url);

    switch(req.url){
        case '/hola':
            let saludo = hola();
            res.write(saludo);
            res.end();
            break;
        case '/api':
            res.writeHead(200, {'Content-Type':'application/json'})
            res.write('[{"nombre":"Fabio","email":"fmenacho@uni.pe"}]');
            res.end();
        default:
            res.write('<h1>Bienvenido a mi sitio web</h1>')
            res.end();
    }
}

function hola(){
    return '<b>Hola como estas</b>';
}

console.log("Escuchando http en el puerto 3000");