SELECT strftime('%m', fecha) mes, sum(cantidad)
FROM movimientos
WHERE
    strftime('%Y', fecha) = '{}'
    AND concepto = '{}'
    AND tipo_abono = '{}'
GROUP BY
    strftime('%m', fecha)
ORDER BY strftime('%m', fecha);