SELECT gp.id, gp.concepto, p.periodicidad, gp.cantidad 
FROM (SELECT id, concepto, periodicidad, cantidad FROM gastosPeriodicos WHERE active = 1) gp
JOIN 
(SELECT codigo, periodicidad FROM periodicidad)p 
ON gp.periodicidad = p.codigo
WHERE gp.periodicidad = '{}'