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
# ----------------------------------------------------------------------
def validarTipoUsuario(user, contrasena):
    cr.execute('''
        SELECT * FROM usuarios ''')
    usuarios = cr.fetchall()
    for usuario in usuarios:
        if usuario[1]==user and usuario[2]==contrasena and usuario[3]==2:
                return 'Usuario Cliente'
        if usuario[1]==user and usuario[2]==contrasena and usuario[3]==1:
                return  'Usuario Administrator'
    return 'User no valido'
# ----------------------------------------------------------------------
#UPDATE
def actualizarUsuarios():
    idUsuario = int(input("Ingrese ID para modificar: "))
    print("Seleccione que desea modificar: ")
    print("1. Nombre")
    print("2. Contraseña")
    print("3. Rol")
    opcion = int(input())
    match opcion:
        case 1:
            nuevoNombre = str(input("Ingrese el nuevo nombre: "))
            cr.execute('''UPDATE usuarios
                            SET nombre = ?
                            WHERE idUsuario = ?''', (nuevoNombre, idUsuario))
        case 2:
            nuevaContraseña = str(input("Ingrese el nuevo nombre: "))
            cr.execute('''UPDATE usuarios
                                SET contraseña = ?
                                WHERE idUsuario = ?''', (nuevaContraseña, idUsuario))

        case 3:
            nuevoRol = str(input("Ingrese el nuevo nombre: "))
            cr.execute('''UPDATE roles
                                SET nombreRol = ?
                                WHERE idRol = ?''', (nuevoRol, idUsuario))
    baseDeDatos.commit()

    print("Usuario modificado exitosamente")
# ----------------------------------------------------------------------
# DELETE
def eliminarUsuarios():
    idUsuario = int(input("Ingrese ID para eliminar: "))
    cr.execute('''DELETE FROM usuarios
                  WHERE idUsuario = ?''', (idUsuario,))
    baseDeDatos.commit()
    print('Usuario eliminado exitosamente')
#----------------------------------------------------------------------
#funcion para opciones de usuario cliente
def UsuarioCliente():
    while True:
        print('1.Ver usuarios \n2.Regresar al login \n3.Salir')
        opc =int(input('Seleccione su opcion: '))
        match opc:
            case 1:
                verUsuario()
            case 2:
                print('Regresando al login...')
                break
            case 3:#detiene elbucle del usuari cliente
                return 1#retorna un valor para detener el bucle principal
                break
def UsuarioAdministrator():
    while True:
        print('1.Agregar nuevo usuario \n2.Eliminar usuario \n3.Modificar usuario \n4.Ver usuarios \n5.Regresar al login \n6.Salir')
        opc =int(input('Seleccione su opcion: '))
        match opc:
            case 1:
                nombreUs = input('Ingrese nombre: ')
                apellidoUs = input('Ingrese apellido: ')
                rol=int(input('Elija un rol para el nuevo usuario (1=Adminstrador, 2=Cliente)'))
                crearUsuario(nombreUs, apellidoUs, rol)
            case 2:
                pass
            case 3:
                pass
            case 4:
                verUsuario()
            case 5:
                print('Regresando al login...')
                break
            case 6:
                return 1
                break
            case 7:
                print('Opcion no valida')
#----------------------------------------------------------------------
#menu de acciones parq cada tipo de usario
while True:
    Ingresar_usuario=str(input('Ingrese su usuario: '))
    Ingresar_contraseña=str(input('Ingrese su contraseña: '))

    #condicional para verificar el tipo de usuario
    if validarTipoUsuario(Ingresar_usuario, Ingresar_contraseña)=='Usuario Cliente':
        print('USUARIO ES DE TIPO CLIENTE')
        #UsuarioCliente()
        salida=UsuarioCliente()
        if salida==1:
            break
    elif validarTipoUsuario(Ingresar_usuario, Ingresar_contraseña)=='Usuario Administrator':
        print ('USUARIO ES DE TIPO ADMINISTRATOR')
        #UsuarioAdministrator()
        salida=UsuarioAdministrator()
        if salida==1:
            break
    else:
        print('Usuario no encontrado')