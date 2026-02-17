-- SELECT DISTINCT t.empresa  FROM ingresosFijos t WHERE t.activo =1;
SELECT empresa, nombreEmpresa FROM empresas WHERE tipo='P' AND activo = 1;