SELECT
	'P'||t.id id,
	t.empresa,
	t.año,
	m1.mes_texto ||' a '|| m2.mes_texto meses,
	t.bruto_anual,
	ROUND((t.bruto_anual * dn.neto)/ 100, 2) neto_anual,
	t.mensualidades, 
	ROUND((((t.bruto_anual * dn.neto)/ 100)/mm.mensualidades ), 2) mensualidad_neta, 
	CASE WHEN dn.bonus = 0 THEN 0 ELSE ROUND(((t.bruto_anual * dn.neto)/ 100)/dn.bonus, 2) END bonus
FROM
	(
	SELECT
		*
	FROM
		ingresosFijos
	WHERE activo=1
	and empresa = '{}'
	and año='{}') t
LEFT JOIN (
	SELECT
		empresa,
		año,
		sum(mensualidades) mensualidades
	FROM
		ingresosFijos
	group by
		empresa,
		año) mm 
	ON
	t.empresa = mm.empresa
	and t.año = mm.año
LEFT JOIN (
	SELECT
		*
	FROM
		descuentosNomina)dn 
ON
	t.año = dn.año
LEFT JOIN (
	SELECT
		*
	FROM
		Meses)m1
ON
	t.mes_inicio = m1.mes
LEFT JOIN (
	SELECT
		*
	FROM
		Meses)m2
ON
	t.mes_fin = m2.mes
; 