SELECT 'E'||gt.id, gt.concepto, gt.año ||' - '|| m.mes_texto añomes, gt.cantidad
FROM 
gastosTemporales gt 
LEFT JOIN  
Meses m USING(mes) 
WHERE active =1
AND gt.año = {}
AND gt.mes = {}
ORDER BY año, mes