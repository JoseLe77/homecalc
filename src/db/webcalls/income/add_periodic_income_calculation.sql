SELECT
	ROUND((1-(p2.bruto_anual / p1.bruto_anual))* 100, 2) subida_anual
FROM
	(
	SELECT
		t.bruto_anual
	FROM
		ingresosFijos t
	WHERE
		id = (
		SELECT
			MAX(id)
		FROM
			ingresosFijos
		WHERE
			año = ((
			SELECT
				MAX(año)
			FROM
				ingresosFijos t2)))) p1
LEFT JOIN (
	SELECT
		t.bruto_anual
	FROM
		ingresosFijos t
	WHERE
		id = (
		SELECT
			MAX(id)
		FROM
			ingresosFijos
		WHERE
			año = ((
			SELECT
				MAX(año)
			FROM
				ingresosFijos t2)-1))) p2 
ON
	1 = 1;