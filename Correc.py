import mysql.connector
from tabulate import tabulate

# ==========================================
# Clase base de conexión
# ==========================================
class ConexionBD:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='viverodef'
            )
            self.cursor = self.conn.cursor(dictionary=False)
            print("Conexion Realizada")
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            self.conn = None
            self.cursor = None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

# ==========================================
# Clase Tipo_Usuarios
# ==========================================
class Tipo_Usuarios(ConexionBD):
    def crearTipoUsuario(self, idTipoUsuario, descripcion):
        sqlString = '''INSERT INTO tipo_usuario(idTipoUsuario, descripcion) VALUES (%s, %s)'''
        valores = (idTipoUsuario, descripcion)
        self.cursor.execute(sqlString, valores)
        self.conn.commit()
        print("Tipo de usuario agregado")

    def VerificarTiposUsuarios(self):
        sqlString = '''SELECT * FROM tipo_usuario'''
        self.cursor.execute(sqlString)
        return self.cursor.fetchall()

    def MostrarTablaTipoUsuarios(self):
        datos = self.VerificarTiposUsuarios()
        if not datos:
            print("No hay registros en la tabla tipo_usuario")
            return
        NombreColumnas = ["ID TIPO DE USUARIO", "DESCRIPCION"]
        print("\n=== LISTA DE TIPOS DE USUARIOS ===")
        print(tabulate(datos, headers=NombreColumnas, tablefmt="fancy_grid"))

# ==========================================
# Clase Tipo_Actividades
# ==========================================
class Tipo_Actividades(ConexionBD):
    def crearTipoActividad(self, idTipoActividad, descripcion):
        sqlString = '''INSERT INTO tipo_de_actividad(idTipoActividad, descripcion) VALUES (%s, %s)'''
        valores = (idTipoActividad, descripcion)
        self.cursor.execute(sqlString, valores)
        self.conn.commit()
        print("Nueva Actividad agregada")

    def VerificarTipoActividades(self):
        sqlString = '''SELECT * FROM tipo_de_actividad'''
        self.cursor.execute(sqlString)
        return self.cursor.fetchall()

    def MostrarTablaActividades(self):
        datos = self.VerificarTipoActividades()
        if not datos:
            print("No hay registros en la tabla tipo_de_ACTIVIDADES")
            return
        NombreColumnas = ["ID TIPO DE ACTIVIDADES", "ACTIVIDADES"]
        print("\n=== LISTA DE TIPOS DE ACTIVIDADES ===")
        print(tabulate(datos, headers=NombreColumnas, tablefmt="fancy_grid"))

# ==========================================
# Clase Tipos_Insumos
# ==========================================
class Tipos_Insumos(ConexionBD):
    def crearTipoInsumo(self, idTipoInsumo, descripcion):
        sqlString = '''INSERT INTO tipo_de_insumo(idTipoInsumo, nombreDelInsumo) VALUES (%s, %s)'''
        valores = (idTipoInsumo, descripcion)
        self.cursor.execute(sqlString, valores)
        self.conn.commit()
        print("Nuevo Insumo agregado")

    def VerificarTipoInsumo(self):
        sqlString = '''SELECT * FROM tipo_de_insumo'''
        self.cursor.execute(sqlString)
        return self.cursor.fetchall()

    def MostrarTablaInsumos(self):
        datos = self.VerificarTipoInsumo()
        if not datos:
            print("No hay registros en la tabla tipo_de_INSUMOS")
            return
        NombreColumnas = ["ID TIPO DE INSUMOS", "INSUMOS"]
        print("\n=== LISTA DE TIPOS DE INSUMOS ===")
        print(tabulate(datos, headers=NombreColumnas, tablefmt="fancy_grid"))

# ==========================================
# Clase Tipo_Pago
# ==========================================
class Tipo_Pago(ConexionBD):
    def crearTipoPago(self, idTipoPago, descripcion):
        sqlString = '''INSERT INTO tipo_pago(idTipoPago, descripcion) VALUES (%s, %s)'''
        valores = (idTipoPago, descripcion)
        self.cursor.execute(sqlString, valores)
        self.conn.commit()
        print("Nuevo metodo de pago agregado")

    def VerificarTiposPagos(self):
        sqlString = '''SELECT * FROM tipo_pago'''
        self.cursor.execute(sqlString)
        return self.cursor.fetchall()

    def MostrarTablaPagos(self):
        datos = self.VerificarTiposPagos()
        if not datos:
            print("No hay registros en la tabla tipo_pago")
            return
        NombreColumnas = ["ID TIPO DE PAGOS", "TIPOS DE PAGOS"]
        print("\n=== LISTA DE TIPOS DE PAGOS ===")
        print(tabulate(datos, headers=NombreColumnas, tablefmt="fancy_grid"))

# ==========================================
# Clase Estado_Produ
# ==========================================
class Estado_Produ(ConexionBD):
    def crearEstadoProdu(self, idEstadoProdu, descripcion):
        sqlString = '''INSERT INTO estado_produ(idEstadoProdu, descripcion) VALUES (%s, %s)'''
        valores = (idEstadoProdu, descripcion)
        self.cursor.execute(sqlString, valores)
        self.conn.commit()
        print("Nuevo estado de produccion agregado")

    def VerificarEstadosProdu(self):
        sqlString = '''SELECT * FROM estado_produ'''
        self.cursor.execute(sqlString)
        return self.cursor.fetchall()

    def MostrarEstadosProdu(self):
        datos = self.VerificarEstadosProdu()
        if not datos:
            print("No hay registros en la tabla estado_produ")
            return
        NombreColumnas = ["ID DE TIPO DE ESTADOS DE PRODUCCION", "TIPOS DE ESTADOS DE PRODUCCION"]
        print("\n=== LISTA DE ESTADOS DE PRODUCCION ===")
        print(tabulate(datos, headers=NombreColumnas, tablefmt="fancy_grid"))

# ==========================================
# Clase Tipo_cuidado
# ==========================================
class Tipo_cuidado(ConexionBD):
    def crearTipoCuidado(self, idTipoCuidado, descripcion):
        sqlString = '''INSERT INTO tipo_cuidado(idTipoCuidado, descripcion) VALUES (%s, %s)'''
        valores = (idTipoCuidado, descripcion)
        self.cursor.execute(sqlString, valores)
        self.conn.commit()
        print("Nuevo tipo de cuidado agregado")

    def VerificarTiposCuidado(self):
        sqlString = '''SELECT * FROM tipo_cuidado'''
        self.cursor.execute(sqlString)
        return self.cursor.fetchall()

    def MostrarTiposCuidados(self):
        datos = self.VerificarTiposCuidado()
        if not datos:
            print("No hay registros en la tabla tipo_cuidado")
            return
        NombreColumnas = ["ID DE TIPO DE CUIDADO", "TIPOS DE CUIDADO"]
        print("\n=== LISTA DE TIPOS DE CUIDADOS ===")
        print(tabulate(datos, headers=NombreColumnas, tablefmt="fancy_grid"))

# ==========================================
# Clase Usuario
# ==========================================
class Usuario(ConexionBD):
    def crearUsuario(self, nombre, primerApell, segApell, constraseña, tipoUsuario):
        sqlString = '''INSERT INTO usuarios(nombre, primerApell, segApell, contraseña, tipoUsuario) VALUES (%s, %s, %s, %s, %s)'''
        valores = (nombre, primerApell, segApell, constraseña, tipoUsuario)
        self.cursor.execute(sqlString, valores)
        self.conn.commit()
        print("Usuario agregado Exitosamente")

    def VerificarUsuarios(self):
        sqlString = '''
        SELECT
            u.idUsuario,
            u.nombre,
            u.primerApell,
            u.segApell,
            u.contraseña,
            u.tipoUsuario,
            t_u.descripcion
        FROM usuarios u
        INNER JOIN tipo_usuario t_u ON u.tipoUsuario = t_u.idTipoUsuario
        '''
        self.cursor.execute(sqlString)
        return self.cursor.fetchall()

    def MostrarUsuarios(self):
        datos = self.VerificarUsuarios()
        if not datos:
            print("No hay registros en la tabla usuarios")
            return
        NombreColumnas = ["ID DE USUARIO", "NOMBRE", "PRIMER_APELL", "SEG_APELL", "CONTRASEÑAS", "ID DE TIPO DE USUARIO", "TIPO DE USUARIO"]
        print("\n=== LISTA DE USUARIOS ===")
        print(tabulate(datos, headers=NombreColumnas, tablefmt="fancy_grid"))

# ==========================================
# Clase Insumos (corregido JOIN)
# ==========================================
class Insumos(ConexionBD):
    def crearInsumo(self, nombreDelInsumo, precioCompra, stockMinimo, stockActual, tipoDeInsumo):
        sqlString = '''INSERT INTO insumos(nombreDelInsumo, precioDeCompra, stockMinimo, stockActual, tipoDeInsumo) VALUES (%s, %s, %s, %s, %s)'''
        valores = (nombreDelInsumo, precioCompra, stockMinimo, stockActual, tipoDeInsumo)
        self.cursor.execute(sqlString, valores)
        self.conn.commit()
        print("Insumo agregado Exitosamente")

    def VerificarInsumos(self):
        sqlString = '''
        SELECT i.idInsumo, i.nombreDelInsumo, i.precioDeCompra, i.stockMinimo, i.stockActual, i.tipoDeInsumo, t_i.nombreDelInsumo
        FROM insumos i
        INNER JOIN tipo_de_insumo t_i ON i.tipoDeInsumo = t_i.idTipoInsumo
        '''
        self.cursor.execute(sqlString)
        return self.cursor.fetchall()

    def MostrarInsumos(self):
        datos = self.VerificarInsumos()
        if not datos:
            print("No hay registros en la tabla insumos")
            return
        NombreColumnas = ["ID DEL INSUMO", "NOMBRE", "PRECIO DE COMPRA", "STOCK MINIMO", "STOCK ACTUAL", "ID DE TIPO INSUMO", "TIPO DE INSUMO"]
        print("\n=== LISTA DE INSUMOS ===")
        print(tabulate(datos, headers=NombreColumnas, tablefmt="fancy_grid"))

class Pago(ConexionBD):

    def CrearPago(self, fecha, numeroPago, montoPago, saldo, tipoDePago, pedido, usuarios):
        sqlString = '''INSERT INTO pago(fecha, numeroPago, montoPago, saldo, tipoDePago, pedido, usuarios)
                       VALUES(%s,%s,%s,%s,%s,%s,%s)'''
        valores = (fecha, numeroPago, montoPago, saldo, tipoDePago, pedido, usuarios)
        self.cursor.execute(sqlString, valores)
        self.conn.commit()
        print("Pago registrado correctamente")

    def VerificarPagos(self):
        sqlString = '''
                    SELECT 
                        p.numero,
                        p.fecha,
                        p.numeroPago,
                        p.montoPago,
                        p.saldo,
                        tp.descripcion AS tipoDePago,
                        ped.idPedido AS pedido,
                        u.nombre AS usuario
                    FROM pago p
                    INNER JOIN tipo_pago tp ON p.tipoDePago = tp.idTipoPago
                    INNER JOIN pedido ped ON p.pedido = ped.idPedido
                    INNER JOIN usuarios u ON p.usuarios = u.idUsuario
                    '''
        self.cursor.execute(sqlString)
        return self.cursor.fetchall()

    def MostrarPagos(self):
        datos = self.VerificarPagos()

        if not datos:
            print("No hay registros en la tabla pago")
            return

        NombreColumnas = [
            "NUMERO",
            "FECHA",
            "NUMERO DE PAGO",
            "MONTO",
            "SALDO",
            "TIPO DE PAGO",
            "PEDIDO",
            "USUARIO"
        ]

        print("\n=== LISTA DE PAGOS ===")
        print(tabulate(datos, headers=NombreColumnas, tablefmt="fancy_grid"))


#Metodo para realizar acciones en la tabla Pedido
class Pedido(ConexionBD):

    def CrearPedido(self, fecha, subtotal, IVA, total, proveedores, usuarios):
        sqlString = '''INSERT INTO pedido(fecha, subtotal, IVA, total, proveedores, usuarios)
                       VALUES(%s, %s, %s, %s, %s, %s)'''
        valores = (fecha, subtotal, IVA, total, proveedores, usuarios)
        self.cursor.execute(sqlString, valores)
        self.conn.commit()
        print("Pedido registrado correctamente")

    def VerificarPedido(self):
        sqlString = '''
                    SELECT 
                        p.idPedido,
                        p.fecha,
                        p.subtotal,
                        p.IVA,
                        p.total,
                        pr.nombreEmpresa AS proveedor,
                        u.nombre AS usuario
                    FROM pedido p
                    LEFT JOIN proveedores pr ON p.proveedores = pr.idProveedores
                    INNER JOIN usuarios u ON p.usuarios = u.idUsuario
                    '''
        self.cursor.execute(sqlString)
        return self.cursor.fetchall()

    def MostrarPedido(self):
        datos = self.VerificarPedido()

        if not datos:
            print("No hay registros en la tabla pedido")
            return

        NombreColumnas = [
            "ID PEDIDO",
            "FECHA",
            "SUBTOTAL",
            "IVA",
            "TOTAL",
            "PROVEEDOR",
            "USUARIO"
        ]

        print("\n=== LISTA DE PEDIDOS ===")
        print(tabulate(datos, headers=NombreColumnas, tablefmt="fancy_grid"))

#Metodo para realizar acciones en la tabla Produccion
class Produccion(ConexionBD):

    def CrearProduccion(self, fechaInicio, fechaFin, estadoProduccion, usuarios):
        sqlString = '''INSERT INTO produccion(fechaInicio, fechaFin, estadoProduccion, usuarios)
                       VALUES(%s, %s, %s, %s)'''
        valores = (fechaInicio, fechaFin, estadoProduccion, usuarios)
        self.cursor.execute(sqlString, valores)
        self.conn.commit()
        print("Registro de producción agregado correctamente")

    def VerificarProduccion(self):
        sqlString = '''
                    SELECT 
                        p.idProduccion,
                        p.fechaInicio,
                        p.fechaFin,
                        e.descripcion AS estadoProduccion,
                        u.nombre AS usuario
                    FROM produccion p
                    INNER JOIN estado_produ e ON p.estadoProduccion = e.idEstadoProdu
                    INNER JOIN usuarios u ON p.usuarios = u.idUsuario
                    '''
        self.cursor.execute(sqlString)
        return self.cursor.fetchall()

    def MostrarProduccion(self):
        datos = self.VerificarProduccion()

        if not datos:
            print("No hay registros en la tabla produccion")
            return

        NombreColumnas = [
            "ID PRODUCCION",
            "FECHA INICIO",
            "FECHA FIN",
            "ESTADO",
            "USUARIO"
        ]

        print("\n=== LISTA DE PRODUCCIÓN ===")
        print(tabulate(datos, headers=NombreColumnas, tablefmt="fancy_grid"))

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestión de Tipos de Usuario")
        print("2. Gestión de Tipos de Actividad")
        print("3. Gestión de Tipos de Insumo")
        print("4. Gestión de Tipos de Pago")
        print("5. Gestión de Estados de Producción")
        print("6. Gestión de Tipos de Cuidado")
        print("7. Gestión de Usuarios")
        print("8. Gestión de Insumos")
        print("9. Gestión de Pagos")
        print("10. Gestión de Pedidos")
        print("11. Gestión de Producción")
        print("0. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            menu_tipos_usuario()
        elif opcion == '2':
            menu_tipos_actividad()
        elif opcion == '3':
            menu_tipos_insumo()
        elif opcion == '4':
            menu_tipos_pago()
        elif opcion == '5':
            menu_estados_produccion()
        elif opcion == '6':
            menu_tipos_cuidado()
        elif opcion == '7':
            menu_usuarios()
        elif opcion == '8':
            menu_insumos()
        elif opcion == '9':
            menu_pagos()
        elif opcion == '10':
            menu_pedidos()
        elif opcion == '11':
            menu_produccion()
        elif opcion == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


# Submenú Gestión de Tipos de Usuario
def menu_tipos_usuario():
    while True:
        print("\n=== GESTIÓN DE TIPOS DE USUARIO ===")
        print("1. Crear Tipo de Usuario")
        print("2. Mostrar Tipos de Usuario")
        print("0. Regresar al Menú Principal")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            descripcion = input("Introduce la descripción del tipo de usuario: ")
            tipo_usuario = Tipo_Usuarios()
            tipo_usuario.crearTipoUsuario(None, descripcion)
        elif opcion == '2':
            tipo_usuario = Tipo_Usuarios()
            tipo_usuario.MostrarTablaTipoUsuarios()
        elif opcion == '0':
            break
        else:
            print("Opción no válida, intenta de nuevo.")


# Submenú Gestión de Tipos de Actividad
def menu_tipos_actividad():
    while True:
        print("\n=== GESTIÓN DE TIPOS DE ACTIVIDAD ===")
        print("1. Crear Tipo de Actividad")
        print("2. Mostrar Tipos de Actividad")
        print("0. Regresar al Menú Principal")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            descripcion = input("Introduce la descripción del tipo de actividad: ")
            tipo_actividad = Tipo_Actividades()
            tipo_actividad.crearTipoActividad(None, descripcion)
        elif opcion == '2':
            tipo_actividad = Tipo_Actividades()
            tipo_actividad.MostrarTablaActividades()
        elif opcion == '0':
            break
        else:
            print("Opción no válida, intenta de nuevo.")


# Submenú Gestión de Tipos de Insumo
def menu_tipos_insumo():
    while True:
        print("\n=== GESTIÓN DE TIPOS DE INSUMO ===")
        print("1. Crear Tipo de Insumo")
        print("2. Mostrar Tipos de Insumo")
        print("0. Regresar al Menú Principal")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            descripcion = input("Introduce el nombre del insumo: ")
            tipo_insumo = Tipos_Insumos()
            tipo_insumo.crearTipoInsumo(None, descripcion)
        elif opcion == '2':
            tipo_insumo = Tipos_Insumos()
            tipo_insumo.MostrarTablaInsumos()
        elif opcion == '0':
            break
        else:
            print("Opción no válida, intenta de nuevo.")


# Submenú Gestión de Tipos de Pago
def menu_tipos_pago():
    while True:
        print("\n=== GESTIÓN DE TIPOS DE PAGO ===")
        print("1. Crear Tipo de Pago")
        print("2. Mostrar Tipos de Pago")
        print("0. Regresar al Menú Principal")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            descripcion = input("Introduce la descripción del tipo de pago: ")
            tipo_pago = Tipo_Pago()
            tipo_pago.crearTipoPago(None, descripcion)
        elif opcion == '2':
            tipo_pago = Tipo_Pago()
            tipo_pago.MostrarTablaPagos()
        elif opcion == '0':
            break
        else:
            print("Opción no válida, intenta de nuevo.")


# Submenú Gestión de Estados de Producción
def menu_estados_produccion():
    while True:
        print("\n=== GESTIÓN DE ESTADOS DE PRODUCCIÓN ===")
        print("1. Crear Estado de Producción")
        print("2. Mostrar Estados de Producción")
        print("0. Regresar al Menú Principal")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            descripcion = input("Introduce la descripción del estado de producción: ")
            estado_produ = Estado_Produ()
            estado_produ.crearEstadoProdu(None, descripcion)
        elif opcion == '2':
            estado_produ = Estado_Produ()
            estado_produ.MostrarEstadosProdu()
        elif opcion == '0':
            break
        else:
            print("Opción no válida, intenta de nuevo.")


# Submenú Gestión de Tipos de Cuidado
def menu_tipos_cuidado():
    while True:
        print("\n=== GESTIÓN DE TIPOS DE CUIDADO ===")
        print("1. Crear Tipo de Cuidado")
        print("2. Mostrar Tipos de Cuidado")
        print("0. Regresar al Menú Principal")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            descripcion = input("Introduce la descripción del tipo de cuidado: ")
            tipo_cuidado = Tipo_cuidado()
            tipo_cuidado.crearTipoCuidado(None, descripcion)
        elif opcion == '2':
            tipo_cuidado = Tipo_cuidado()
            tipo_cuidado.MostrarTiposCuidados()
        elif opcion == '0':
            break
        else:
            print("Opción no válida, intenta de nuevo.")


# Submenú Gestión de Usuarios
def menu_usuarios():
    while True:
        print("\n=== GESTIÓN DE USUARIOS ===")
        print("1. Crear Usuario")
        print("2. Mostrar Usuarios")
        print("0. Regresar al Menú Principal")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            nombre = input("Introduce el nombre del usuario: ")
            primer_apell = input("Introduce el primer apellido: ")
            seg_apell = input("Introduce el segundo apellido: ")
            contraseña = input("Introduce la contraseña: ")
            tipo_usuario = input("Introduce el tipo de usuario (ID): ")
            usuario = Usuario()
            usuario.crearUsuario(nombre, primer_apell, seg_apell, contraseña, tipo_usuario)
        elif opcion == '2':
            usuario = Usuario()
            usuario.MostrarUsuarios()
        elif opcion == '0':
            break
        else:
            print("Opción no válida, intenta de nuevo.")


# Submenú Gestión de Insumos
def menu_insumos():
    while True:
        print("\n=== GESTIÓN DE INSUMOS ===")
        print("1. Crear Insumo")
        print("2. Mostrar Insumos")
        print("0. Regresar al Menú Principal")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            nombre_insumo = input("Introduce el nombre del insumo: ")
            precio_compra = float(input("Introduce el precio de compra: "))
            stock_minimo = int(input("Introduce el stock mínimo: "))
            stock_actual = int(input("Introduce el stock actual: "))
            tipo_insumo = input("Introduce el tipo de insumo (ID): ")
            insumo = Insumos()
            insumo.crearInsumo(nombre_insumo, precio_compra, stock_minimo, stock_actual, tipo_insumo)
        elif opcion == '2':
            insumo = Insumos()
            insumo.MostrarInsumos()
        elif opcion == '0':
            break
        else:
            print("Opción no válida, intenta de nuevo.")


# Submenú Gestión de Pagos
def menu_pagos():
    while True:
        print("\n=== GESTIÓN DE PAGOS ===")
        print("1. Crear Pago")
        print("2. Mostrar Pagos")
        print("0. Regresar al Menú Principal")
        
        opcion = input("\nSelecciona una")
 

menu_principal()