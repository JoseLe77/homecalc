SELECT
    'P' as income_type,
	t.id as id_income,
	t.empresa,
	t.año,
	t.mes_inicio,
	t.mes_fin,
	t.bruto_anual,
	t.mensualidades,
	dn.id as id_discounts,
	dn.irpf,
	dn.resto,
	dn.bonus
FROM
	ingresosFijos t
LEFT JOIN descuentosNomina dn ON
	t.año = dn.año
	and t.empresa = dn.empresa
WHERE
	t.id = {};
