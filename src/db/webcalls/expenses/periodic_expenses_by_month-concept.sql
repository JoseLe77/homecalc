SELECT gp.id, gp.concepto, p.periodicidad, gp.cantidad FROM (
SELECT id, concepto, periodicidad, cantidad FROM gastosPeriodicos WHERE periodicidad = 'M' AND concepto = '{}' and active = 1
UNION ALL 
SELECT id, concepto, periodicidad, cantidad FROM gastosPeriodicos WHERE mes = {} AND concepto = '{}' and active = 1) gp
JOIN 
(SELECT codigo, periodicidad FROM periodicidad)p 
ON gp.periodicidad = p.codigo