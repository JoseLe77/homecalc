import sqlite3

def dbconnection():
    # Connects to the specified SQLite database and returns a connection and cursor.
    connection = sqlite3.connect('src/db/database/homecalc.db')
    cursor = connection.cursor()
    return connection, cursor

# Configuración de Correo para HomeCalc


# Configuración SMTP (ejemplo para Gmail)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # 465 para SSL, 587 para TLS
SMTP_USE_SSL = True  # True para SSL, False para TLS

# Credenciales (reemplaza con tus datos)
REMITENTE_EMAIL = "homecalcapp@gmail.com"
REMITENTE_PASSWORD = ""  # Usa contraseña de aplicación si es Gmail


# ---- Database Connection ----
connection, cursor = dbconnection()

# ---- Database nav buttons SQL Query ----
webcall = open('src/db/webcalls/contact.sql', mode='r')
dest_users_query = webcall.read()
webcall.close()
try:
    cursor.execute(dest_users_query)
    dest_users_query_results = cursor.fetchall()
except Exception as e:
    print(f"Error al ejecutar la query: {e}")
finally:
    connection.close()

# Destinatarios (administradores que recibirán los mensajes)
DESTINATARIOS = [
    dest_users_query_results[i][0] for i in range(len(dest_users_query_results))
]

# Asunto del email
ASUNTO_PREFIX = "HomeCalc contact message: "

# Nota sobre contraseñas:
# Para Gmail: https://support.google.com/accounts/answer/185833
# Otros proveedores: Consulta la documentación de tu proveedor SMTP
