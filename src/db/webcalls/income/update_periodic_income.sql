UPDATE ingresosFijos
SET empresa='{}', año={}, mes_fin={}, mes_inicio={}, bruto_anual={},mensualidades=(CASE WHEN '{}' = 'S' THEN (CASE WHEN ({}-{}+1)<12 THEN {}-{}+2 ELSE {}-{}+3 END) ELSE ({}-{})+1 END)
WHERE id={};