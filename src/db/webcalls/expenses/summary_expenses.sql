SELECT meses.mes_texto AS "MES", gastos_detalle_view.mensual, gastos_detalle_view.bimensual, gastos_detalle_view.trimestral, gastos_detalle_view.cuatrimestral, gastos_detalle_view.semestral, gastos_detalle_view.anual, gastos_detalle_view.extra, ROUND(gastos_detalle_view.total, 2) AS "TOTAL"
FROM gastos_detalle_view
    LEFT JOIN meses ON gastos_detalle_view.mes = meses.mes
ORDER BY gastos_detalle_view.mes;