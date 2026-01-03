SELECT strftime('%m', fecha) mes, sum(cantidad)
FROM movimientos
WHERE
    strftime('%Y', fecha) = '{}'
    and tipo_abono = '{}'
GROUP BY
    strftime('%m', fecha)
ORDER BY strftime('%m', fecha);