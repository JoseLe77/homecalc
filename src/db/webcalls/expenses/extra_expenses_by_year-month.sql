SELECT gt.id, gt.año, m.mes_texto, gt.concepto, gt.cantidad 
FROM 
gastosTemporales gt 
LEFT JOIN  
Meses m 
USING(mes) 
WHERE gt.active = 1
AND gt.año = {} 
AND gt.mes = {};