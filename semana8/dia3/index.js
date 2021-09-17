// const sqlServerLib = require('./lib/sqlserver');

// async function prueba(){
//     sqlsrv = new sqlServerLib();
//     const sqlAlumnos = "select top 2 * from alumnos";
//     const result = await sqlsrv.querySql(sqlAlumnos)
//     console.log(result.recordsets);
// }

// prueba();

const express = require('express')
const app = express();

const {config} = require('./config/index');
const alumnosApi = require('./routes/alumnos')

alumnosApi(app);

app.listen(config.port,function(){
    console.log('Servidor corriendo en puerto: ',config.port);
})