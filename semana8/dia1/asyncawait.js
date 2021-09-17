async function hola(nombre){
    return new Promise(function(resolve,reject){
        setTimeout(function(){
            console.log('Hola ' + nombre);
            resolve(nombre);
        },1000);
    });
}

async function hablar(nombre){
    return new Promise((resolve,reject)=>{
        setTimeout(function(){
            console.log('hablar');
            resolve(nombre)
            reject('Hay un error')
        },1000);
    })
}

async function adios(nombre){
    return new Promise((resolve,reject)=>{
        setTimeout(function(){
            console.log('adios',nombre);
            resolve()
        },1000);
    })
}

async function main(){
    let nombre = await hola('Fabio');
    await hablar();
    await adios(nombre);
    console.log('Terminando proceso');
}

console.log('Iniciando el proceso');
main();
console.log('Va a ser la segunda instrucción');