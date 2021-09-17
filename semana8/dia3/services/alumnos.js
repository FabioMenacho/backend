const SqlServerLib = require('../lib/sqlserver');

class AlumnosService{
    constructor(){
        this.sql = new SqlServerLib();
    }

    async getAll(){
        const sqlAll = "select top 10 * from alumnos";
        const result = await this.sql.querySql(sqlAll);
        return result.recordsets;
    }

    async getById(alumnoId){
        const SqlOne = "select * from alumnos where id='"+ alumnoId +"'";
        const result = await this.sql.querySql(SqlOne);
        return result.recordsets;
    }
}

module.exports = AlumnosService