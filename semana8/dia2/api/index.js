const express = require('express');
const app = express();

const {config} = require('./config/index');
const alumnosApi = require('./routes/alumnos.js')

// instancio
alumnosApi(app);

app.listen(config.port,function(){
    console.log('Servidor corriendo en puerto: ',config.port);
})