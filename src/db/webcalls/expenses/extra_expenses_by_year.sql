SELECT gt.id, gt.año, m.mes_texto, gt.concepto, gt.cantidad 
FROM 
gastosTemporales gt 
LEFT JOIN  
Meses m USING(mes) 
WHERE active =1
AND gt.año = {};