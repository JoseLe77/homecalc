SELECT 'TODOS' año 
UNION ALL
SELECT DISTINCT if2.año FROM IngresosFijos if2 /* WHERE if2.año <= strftime('%Y', 'now')*/ ORDER BY if2.año DESC