SELECT 'TODAS' empresa, 'TODAS' nombreEmpresa
UNION ALL
SELECT empresa, nombreEmpresa FROM empresas WHERE activo = 1;
--SELECT DISTINCT empresa FROM IngresosExtra WHERE activo =1;