let nombre = process.env.NOMBRE || 'sin nombre'
let email = process.env.EMAIL || 'no tiene correo'

console.log('Nombre: ' + nombre);
console.log('Email: ' + email);