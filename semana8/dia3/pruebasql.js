console.log('Prueba de conexión a MSQLserver')

const sql = require('mssql')

const sqlConfig = {
    user: 'expressadmin',
    password: '123456',
    server: 'localhost',
    database: 'codigo',
    options: {
        // para azure
        encrypt: true, 
        // true en el desarrollo local
        trustServerCertificate: true
    }
}

async function getConnection() {
    try {
        // make sure that any items are correctly URL encoded in the connection string
        const pool = await sql.connect(sqlConfig)
        const result = await pool.request().query("select top 3 * from alumnos")
        // recordests es para que solo aparezcan los alumnos
        console.log(result.recordsets);
    } catch (err) {
        console.error(err);
    }
}

getConnection();