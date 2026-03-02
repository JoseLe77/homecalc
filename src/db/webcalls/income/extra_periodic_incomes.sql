SELECT
	mef.id,
	e.nombreEmpresa, 
	mef.tipo,
	case
		mef.tipo when 'EXTRA' THEN 'Extraordinaria'
		when 'BONUS' then 'Bonus'
	end tipo_texto,
	m.mes_texto
FROM mesesExtraFijos mef 
LEFT JOIN empresas e 
ON mef.empresa =e.empresa 
LEFT JOIN Meses m
ON mef.mes = m.mes 
ORDER BY
	mef.empresa,
	mef.mes,
	mef.tipo