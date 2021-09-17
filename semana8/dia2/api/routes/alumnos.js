const express = require('express');
const {dataAlumnos} = require('../data/alumnos');

function alumnosApi(app){
    // creo un router 
    const router = express.Router();
    // instancio el router a la ruta /alumnos es la ruta raiz
    app.use('/alumnos',router);
    // al colocar / es la ruta raiz (/alumnos)
    router.get('/',async function(req,res,next){
        try{
            const alumnos = await Promise.resolve(dataAlumnos)

            res.status(200).json({
            status: 'OK',
            data: alumnos
        });
        } catch(err){
            next(err);
        }   
     });
}

module.exports = alumnosApi;