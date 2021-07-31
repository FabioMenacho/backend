/*Crea tablas para manejo de usuarios*/
/*drop table rol;*/
create table if not exists rol(
    /*entero, no puede recibir nulo, solo se va incrementar*/
    id int not null auto_increment,
    nombre varchar(50) not null,
    /*identificar la clave principal*/
    primary key (id)
/*myesan = no respetaban integridad referencial (más rapida)*/
/*innodb = tiene integridad referencial (más lenta) pero mejor para tablas relacionadas*/
)engine=innodb;
/*para ejecutarlo desde la terminal ubicado en esta direccion(dia2):*/
/*mysql -h localhost -u pos -p db_pos < 01-creartablas.sql*/


/*drop table usuario;*/
create table if not exists usuario(
    id int not null auto_increment,
    nombre varchar(50) not null,
    clave varchar(100) not null,
    rol_id int,
    primary key (id),
    /*on delete cascada restrict para restringir el borrado*/
    /*on update restrict para restringir la actualizada*/
    foreign key (rol_id) references rol(id) on delete restrict on update restrict
)engine=innodb;