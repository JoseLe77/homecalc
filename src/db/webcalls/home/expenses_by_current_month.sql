SELECT concepto, cantidad FROM "gastosPeriodicos" WHERE mes = strftime('%m', CURRENT_DATE)
UNION ALL
SELECT concepto, cantidad FROM "gastosPeriodicos" WHERE mes IS NULL
UNION ALL
SELECT concepto, cantidad FROM "gastosTemporales" WHERE mes= strftime('%m', CURRENT_DATE) AND año= strftime('%Y', CURRENT_DATE);