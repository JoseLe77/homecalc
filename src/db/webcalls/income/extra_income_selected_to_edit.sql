SELECT 'E' as income_type,
	ie.id as id_income,
	ie.mes, 
	ie.año,
	ie.empresa,
	ie.concepto, 
	ie.cantidad 
FROM IngresosExtra ie  
WHERE id={};