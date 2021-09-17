const { table } = require('console');
const os = require('os');

console.log(os.arch());
console.log(os.platform());
console.log(os.cpus().length);
console.log(os.freemem());
console.log(os.totalmem());
console.log(os.hostname());

const SIZE = 1024

function kb(bytes) { return bytes / SIZE}
console.warn('Memoria Ram: ' + os.totalmem);
console.log('En KB: ' + kb(os.totalmem()));
console.table([{capacidad:'KB',tamaño:kb(os.totalmem())}])
