function hola(nombre,micallback){
    setTimeout(function(){
        console.log('Hola ' + nombre);
        micallback(nombre);
    },1000);
} 

function adios(nombre,otrocallback){
    setTimeout(function(){
        console.log('Adios ' + nombre);
        otrocallback(nombre);
    },1500);
} 

// hola('Fabio',function(){
//     console.log('Un gusto conocerte');
// });
// adios('Fabio',function(){
//     console.log('Nos vemos en otra oportunidad');
// });

console.log('Iniciando proceso');
hola('Fabio',function(nombre){
    adios(nombre,function(){
        console.log(('Proceso terminado'));
    })
})