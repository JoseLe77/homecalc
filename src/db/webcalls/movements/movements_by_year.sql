SELECT id,
    fecha, 
        concepto, 
        CASE WHEN tipo_abono='T' THEN 'Tarjeta' WHEN tipo_abono='E' THEN 'Efectivo' END TIPO, 
        cantidad
FROM movimientos 
WHERE SUBSTR(fecha,1,4) = SUBSTR(CURRENT_TIMESTAMP,1,4)
ORDER BY fecha DESC;