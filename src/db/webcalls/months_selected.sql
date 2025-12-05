SELECT
	*
FROM
	(
	SELECT
		*
	FROM
		Meses m
	WHERE
		mes >= {}
UNION ALL
	SELECT
		*
	FROM
		Meses m
	WHERE
		mes < {})
WHERE
	mes > 0