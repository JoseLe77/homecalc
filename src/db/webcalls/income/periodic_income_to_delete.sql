DELETE FROM "ingresosFijos" WHERE id={};

DELETE FROM "descuentosNomina" WHERE año NOT IN (SELECT año FROM "ingresosFijos");
