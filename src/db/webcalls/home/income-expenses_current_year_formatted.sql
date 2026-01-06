SELECT
    ingresos_gastos_view.mes,
    meses.mes_texto,
    ROUND(
        (
            ingresos_gastos_view.mensualidad_neta + ingresos_gastos_view.mensualidad_extra
        ),
        2
    ) ingresos,
    ROUND(ingresos_gastos_view.total_gastos, 2) total_gastos,
    ROUND(
        (
            (
                ingresos_gastos_view.mensualidad_neta + ingresos_gastos_view.mensualidad_extra
            ) - ingresos_gastos_view.total_gastos
        ),
        2
    ) resto
FROM ingresos_gastos_view
LEFT JOIN meses
ON meses.mes = ingresos_gastos_view.mes 
WHERE ingresos_gastos_view.año = strftime('%Y', CURRENT_DATE)
ORDER BY ingresos_gastos_view.mes;
