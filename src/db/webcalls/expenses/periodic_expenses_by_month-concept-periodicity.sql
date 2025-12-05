SELECT DISTINCT gp.id, gp.concepto, p.periodicidad, gp.cantidad
FROM 
(SELECT id, concepto, periodicidad, {} mes, cantidad FROM gastosPeriodicos WHERE periodicidad = 'M' AND active = 1
UNION ALL 
SELECT id, concepto, periodicidad, mes, cantidad FROM gastosPeriodicos WHERE periodicidad != 'M' AND active = 1) gp
JOIN 
(SELECT codigo, periodicidad FROM periodicidad) p 
ON gp.periodicidad = p.codigo 
WHERE gp.concepto = '{}' AND p.codigo = '{}' AND gp.mes={}