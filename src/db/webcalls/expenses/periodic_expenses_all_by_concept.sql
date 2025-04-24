SELECT gp.id, gp.concepto, CASE WHEN gp.mes IS NOT NULL THEN p.periodicidad||' ('||gp.mes||')' ELSE p.periodicidad END periodicidad, gp.cantidad 
FROM (SELECT id, concepto, periodicidad, mes, cantidad FROM gastosPeriodicos WHERE active = 1) gp
JOIN 
(SELECT codigo, periodicidad FROM periodicidad)p 
ON gp.periodicidad = p.codigo
WHERE gp.concepto = '{}'