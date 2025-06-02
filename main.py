from sqlite3 import *
baseDeDatos=connect("compendio.db")
baseDeDatos.execute("PRAGMA foreign_Keys =ON")
cr=baseDeDatos.cursor()

cr.execute('''
    CREATE TABLE IF NOT EXISTS roles(
    idRol INTEGER  PRIMARY KEY AUTOINCREMENT,
     nombreRol TEXT NOT NULL)''')
cr.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
    idUsuario INTEGER  PRIMARY KEY AUTOINCREMENT,
     nombre TEXT NOT NULL, 
     contraseña TEXT NOT NULL,
     idrol INTEGER NOT NULL,
     FOREIGN KEY(idRol) REFERENCES roles(idRol))''')

#----------------------------------------------------------------------
#CREATE
def crearUsuario(nombreUs, contraseñaUs, idROL):
    cr.execute('''
         INSERT INTO usuarios (nombre, contraseña, idrol)
         VALUES (?,?,?)''',(nombreUs, contraseñaUs, idROL))
    baseDeDatos.commit()
    print("Usuario creado exitosamente")
#----------------------------------------------------------------------
#READ
def verUsuario():
    cr.execute('''
        SELECT u.nombre, r.nombreRol  FROM usuarios u
        INNER JOIN roles r ON 
        r.idRol =u.idRol
       
        ''')
    usuarios = cr.fetchall()
    for usuario in usuarios:
        print(usuario)


def validarTipoUsuario(user, contrasena):
    cr.execute('''
        SELECT * FROM usuarios ''')
    usuarios = cr.fetchall()
    for usuario in usuarios:
        if usuario[1]==user and usuario[2]==contrasena and usuario[3]==2:
                return 'Usuario Cliente'.upper()
        if usuario[1]==user and usuario[2]==contrasena and usuario[3]==1:
                return  'Usuario Administrator'.upper()


    return 'User no valido'

