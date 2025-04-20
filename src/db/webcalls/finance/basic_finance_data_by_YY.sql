SELECT año, mes, mensualidad_neta, mensualidad_extra, gastos_fijos, gastos_temporales, mensualidad_neta + mensualidad_extra total_ingresos,total_gastos  
FROM ingresos_gastos_view
WHERE año = {}