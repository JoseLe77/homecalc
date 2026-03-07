# HOMECALC - Database basic data



## Paginas

``` SQL
INSERT INTO paginas (id, nombre, enlace, activo)
VALUES
(1, 'Inicio', 'home', 1),
(2, 'Movimientos', 'form', 1),
(3, 'Ingresos', 'income', 1),
(4, 'Gastos', 'expenses', 1),
(5, 'Acerca de', 'about', 1),
(6, '⏻', '/', 1);
```



## Meses

```SQL
INSERT INTO Meses (mes, mes_texto)
VALUES
(0, 'TODOS'),
(1, 'ENERO'),
(2, 'FEBRERO'),
(3, 'MARZO'),
(4, 'ABRIL'),
(5, 'MAYO'),
(6, 'JUNIO'),
(7, 'JULIO'),
(8, 'AGOSTO'),
(9, 'SEPTIEMBRE'),
(10, 'OCTUBRE'),
(11, 'NOVIEMBRE'),
(12, 'DICIEMBRE');
```



## Politicas
```SQL
INSERT INTO policies
(policy_id, policy_name, policy_description, policy_action, created_at, active, modified_at)
VALUES(1, 'REGISTRY_ACTIVATION', 'Enable & Disable registry form', 'disabled', '2026-01-29 20:16:53', 1, '2026-02-03 16:40:03');
```



## Usuarios
```SQL
INSERT INTO usuarios
(usr_id, usrnam, usrmail, usrpass, usrrole, insdte, moddte, active)
VALUES(1, 'Jose Luis Perez Ariza', 'joseluisperezariza@gmail.com', 'd1fef2428abe413a56d38b6d737c8fc627f3c2f0', 'admin', '2026-01-12 06:23:22', '2026-01-28 03:54:18', 1);
```