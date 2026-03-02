create table paginas
(
    id     INTEGER   not null
        primary key autoincrement,
    nombre TEXT(125) not null,
    enlace TEXT(250) default '#',
    activo boolean   default 1
);

create table Meses
(
    mes       INTEGER   not null
        primary key autoincrement,
    mes_texto TEXT(125) not null
);

create table empresas
(
    id            INTEGER not null,
    tipo          TEXT    not null,
    empresa       TEXT    not null,
    nombreEmpresa TEXT    not null,
    activo        BOOLEAN not null
);


create table ingresosFijos
(
    id            INTEGER
        primary key autoincrement,
    empresa       TEXT    not null,
    año           NUMERIC not null,
    mes_inicio    NUMERIC not null,
    mes_fin       NUMERIC not null,
    bruto_anual   NUMERIC not null,
    mensualidades NUMERIC not null,
    activo        BOOLEAN default 1
);


create table descuentosNomina
(
    id           INTEGER    not null
        primary key autoincrement,
    empresa      TEXT(50)   not null,
    año          NUMERIC(4) not null,
    subida_anual NUMERIC(5) not null,
    neto         NUMERIC(5) not null,
    irpf         NUMERIC(5) not null,
    resto        NUMERIC(5) not null,
    bonus        NUMERIC(5)
);

create table mesesExtraFijos
(
    id      INTEGER not null
        primary key autoincrement,
    empresa TEXT(50),
    tipo    TEXT(50),
    mes     INTEGER,
    active  BOOLEAN default 1
);

create table IngresosExtra
(
    id       INTEGER not null
        primary key autoincrement,
    empresa  TEXT    not null,
    año      NUMERIC not null,
    mes      NUMERIC not null,
    cantidad NUMERIC not null,
    concepto TEXT,
    activo   BOOLEAN default 1
);

create table gastosPeriodicos
(
    id           INTEGER           not null
        primary key autoincrement,
    concepto     TEXT              not null,
    periodicidad TEXT              not null,
    cantidad     NUMERIC default 0 not null,
    mes          NUMERIC,
    active       BOOLEAN default 1
);

create table periodicidad
(
    id           INTEGER           not null
        primary key autoincrement,
    codigo       TEXT(3)           not null,
    periodicidad TEXT(150)         not null,
    active       BOOLEAN default 1 not null
);

create table gastosTemporales
(
    id       INTEGER   not null
        primary key autoincrement,
    concepto TEXT(125) not null,
    cantidad NUMERIC   not null,
    año      INTEGER   not null,
    mes      INTEGER   not null,
    active   BOOLEAN default 1
);

create table movimientos
(
    id         INTEGER
        primary key autoincrement,
    fecha      DATE           not null,
    tipo_abono varchar(50)    not null,
    concepto   varchar(100)   not null,
    cantidad   numeric(10, 2) not null
);

create table registroGastos
(
    id            INTEGER not null
        primary key autoincrement,
    fecha         DATE    not null,
    concepto      TEXT    not null,
    cantidad      INTEGER not null,
    fechaRegistro DATE default (NOW())
);

create table usuarios
(
    usr_id  INTEGER
        primary key autoincrement,
    usrnam  TEXT not null
        unique,
    usrmail TEXT not null
        unique,
    usrpass TEXT not null,
    usrrole TEXT     default 'user',
    insdte  DATETIME default (datetime('now', 'localtime')),
    moddte  DATETIME,
    active  INTEGER  default 1
);

create table usr_temp
(
    temp_id    INTEGER
        primary key autoincrement,
    usrmail    TEXT not null
        unique,
    usrpass    TEXT not null,
    created_at TIMESTAMP default CURRENT_TIMESTAMP,
    active     INTEGER   default 1
);

create table policies
(
    policy_id          INTEGER
        primary key autoincrement,
    policy_name        TEXT not null,
    policy_description TEXT,
    policy_action      TEXT not null,
    created_at         TIMESTAMP default CURRENT_TIMESTAMP,
    active             INTEGER   default 1,
    modified_at        datetime
);