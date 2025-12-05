SELECT DISTINCT gp.id, gp.concepto, p.periodicidad, gp.cantidad
FROM 
(SELECT id, concepto, periodicidad, cantidad FROM gastosPeriodicos WHERE periodicidad = (CASE WHEN '{}' = 'M' THEN 'M' ELSE NULL END) and active = 1
UNION ALL 
SELECT id, concepto, periodicidad, cantidad FROM gastosPeriodicos WHERE mes = {} AND periodicidad = '{}' AND  active = 1) gp
JOIN 
(SELECT codigo, periodicidad FROM periodicidad) p 
ON gp.periodicidad = p.codigo 