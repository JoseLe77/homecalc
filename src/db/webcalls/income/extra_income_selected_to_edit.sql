SELECT 'E' as income_type,
	ie.id as id_income,
	ie.año,
	ie.mes, 
	ie.empresa,
	ie.concepto, 
	ie.cantidad 
FROM IngresosExtra ie  
WHERE id={};