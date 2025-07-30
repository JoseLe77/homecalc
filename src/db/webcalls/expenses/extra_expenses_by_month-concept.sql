SELECT gt.id, gt.año, m.mes_texto, gt.concepto, gt.cantidad 
FROM 
gastosTemporales gt 
LEFT JOIN  
Meses m USING(mes) 
WHERE active =1
AND gt.mes = {} 
AND gt.concepto= '{}'
UNION ALL 
SELECT NULL id, '' año, '' mes_texto, 'TOTAL' concepto, SUM(gt.cantidad) cantidad
FROM 
gastosTemporales gt 
LEFT JOIN  
Meses m USING(mes) 
WHERE active =1
AND gt.mes = {} 
AND gt.concepto= '{}';