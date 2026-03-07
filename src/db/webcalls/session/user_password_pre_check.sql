SELECT
	CASE WHEN usuarios.usrmail IS NULL THEN  usr_temp.usrmail ELSE usuarios.usrmail END usrmail,
	usuarios.usrpass
FROM
	usuarios
LEFT JOIN 
    usr_temp 
ON
	usuarios.usrmail = usr_temp.usrmail
WHERE
	usuarios.usrmail = '{}' 
	and usuarios.active =1 
	and (usuarios.usrpass = '{}'
		or usr_temp.usrpass ='{}');