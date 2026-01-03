SELECT strftime('%m', fecha) mes, sum(cantidad)
FROM movimientos
WHERE
    strftime('%Y', fecha) = '{}'
    AND concepto = '{}'
GROUP BY
    strftime('%m', fecha)
ORDER BY strftime('%m', fecha);