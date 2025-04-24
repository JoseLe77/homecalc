SELECT año, mes, ROUND(mensualidad_neta, 2) mensualidad_neta , mensualidad_extra, gastos_fijos, gastos_temporales, ROUND(mensualidad_neta + mensualidad_extra, 2) total_ingresos,total_gastos  
FROM ingresos_gastos_view
WHERE año = {}