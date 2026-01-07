SELECT
    mes,
    ROUND(
        (
            mensualidad_neta + mensualidad_extra
        ),
        2
    ) ingresos,
    ROUND(total_gastos, 2) total_gastos,
    ROUND(
        (
            (
                mensualidad_neta + mensualidad_extra
            ) - total_gastos
        ),
        2
    ) resto
FROM ingresos_gastos_view
WHERE
    año = strftime('%Y', CURRENT_DATE)
ORDER BY mes;