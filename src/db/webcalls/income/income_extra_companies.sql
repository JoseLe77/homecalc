SELECT 'TODAS' empresa
UNION ALL
SELECT DISTINCT empresa FROM IngresosExtra WHERE activo =1;