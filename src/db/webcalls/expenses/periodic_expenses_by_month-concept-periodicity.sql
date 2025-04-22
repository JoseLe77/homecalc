SELECT DISTINCT gp.id, gp.concepto, p.periodicidad, gp.cantidad
FROM 
(SELECT id, concepto, periodicidad, cantidad FROM gastosPeriodicos WHERE concepto = '{}' AND periodicidad = (CASE WHEN '{}' = 'M' THEN 'M' ELSE NULL END) AND mes = {} and active = 1
UNION ALL 
SELECT id, concepto, periodicidad, cantidad FROM gastosPeriodicos WHERE concepto = '{}' AND periodicidad = '{}' AND mes={} AND  active = 1) gp
JOIN 
(SELECT codigo, periodicidad FROM periodicidad) p 
ON gp.periodicidad = p.codigo 
