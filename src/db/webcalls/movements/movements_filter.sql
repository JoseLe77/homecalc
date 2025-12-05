SELECT id,
        fecha, 
        concepto, 
        CASE WHEN tipo_abono='T' THEN 'Tarjeta' WHEN tipo_abono='E' THEN 'Efectivo' END, 
        cantidad  
FROM movimientos 
WHERE CASE WHEN '{}'='TODOS' THEN 1=1 ELSE  concepto='{}' END
AND CASE WHEN '{}'='TODOS' THEN 1=1 ELSE  tipo_abono='{}' END 
AND SUBSTR(fecha,1,4)='{}' 
AND CASE WHEN '{}' = '0' THEN 1=1 ELSE SUBSTR(fecha,6,2)='{}' END
ORDER BY fecha DESC;