// servidor de web socket

// console.log("Servidor corriendo...")
const express = require('express');
const path = require('path')
const app =express();

// levantar servidor por el puerto 3000
app.set('port',process.env.PORT || 3000);

// archivos estáticos
app.use(express.static(path.join(__dirname,'public')));

const server = app.listen(app.get('port'),() =>{
    console.log(`servidor: http://localhost:${app.get('port')}`);
})

// creación de socket
const SocketIo = require('socket.io');

const io = SocketIo(server);

// esta escuchando
io.on('connection',(socket) =>{
    console.log("nueva conexión", socket.id);

    socket.on('mensajecliente',(data)=>{
        console.log(data);
        io.sockets.emit('mensajeservidor',data);
    })
});