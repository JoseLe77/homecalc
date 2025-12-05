SELECT codigo, periodicidad FROM periodicidad WHERE codigo = '{}'
UNION ALL
SELECT codigo, periodicidad FROM periodicidad WHERE codigo != '{}'