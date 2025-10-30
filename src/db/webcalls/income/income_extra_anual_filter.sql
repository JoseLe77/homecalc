SELECT
	'E'||ie.id as id,
	ie.empresa,
	ie.año,
	m.mes_texto mes,
	ie.concepto,
	ie.cantidad
FROM
	IngresosExtra ie,
	Meses m
WHERE
	ie.mes = m.mes
	AND ie.activo = 1
	AND ie.año = '{}';