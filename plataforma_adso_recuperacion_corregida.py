import random
import string
import sys
usuarios = {}
solicitudes_credenciales = []
solicitudes_compra = []
codigos_pago = {}
#diciionario de peliculas
categorias = {
    "Accion": {
        "Pelicula": {
            "John Wick": {
                "anio": 2014,
                "descripcion": "Asesino retirado busca venganza",
                "calificaciones": []
            },
            "Mad Max Fury Road": {
                "anio": 2015,
                "descripcion": "Persecucion en el desierto",
                "calificaciones": []
            },
            "Gladiador": {
                "anio": 2000,
                "descripcion": "Un general busca justicia en Roma",
                "calificaciones": []
            },
            "Duro de Matar": {
                "anio": 1988,
                "descripcion": "Un policia enfrenta terroristas",
                "calificaciones": []
            },
            "Mision Imposible": {
                "anio": 1996,
                "descripcion": "Un agente debe limpiar su nombre",
                "calificaciones": []
            }
        },
        "Serie": {
            "The Boys": {
                "anio": 2019,
                "descripcion": "Superheroes corruptos y sus rivales",
                "calificaciones": []
            },
            "Daredevil": {
                "anio": 2015,
                "descripcion": "Un abogado ciego combate el crimen",
                "calificaciones": []
            },
            "Vikingos": {
                "anio": 2013,
                "descripcion": "Las conquistas de Ragnar Lothbrok",
                "calificaciones": []
            },
            "24": {
                "anio": 2001,
                "descripcion": "Un agente contra el reloj",
                "calificaciones": []
            },
            "Reacher": {
                "anio": 2022,
                "descripcion": "Un ex militar resuelve crimenes",
                "calificaciones": []
            }
        }
    },
    "Comedia": {
        "Pelicula": {
            "Superbad": {
                "anio": 2007,
                "descripcion": "Dos amigos y una fiesta de graduacion",
                "calificaciones": []
            },
            "Que paso ayer": {
                "anio": 2009,
                "descripcion": "Una despedida de soltero sin control",
                "calificaciones": []
            },
            "Chicas pesadas": {
                "anio": 2004,
                "descripcion": "Una chica nueva en un colegio cruel",
                "calificaciones": []
            },
            "Dos tontos muy tontos": {
                "anio": 1994,
                "descripcion": "Dos amigos y un viaje absurdo",
                "calificaciones": []
            },
            "Elf": {
                "anio": 2003,
                "descripcion": "Un humano criado por elfos",
                "calificaciones": []
            }
        },
        "Serie": {
            "Brooklyn Nine-Nine": {
                "anio": 2013,
                "descripcion": "Policias divertidos en Nueva York",
                "calificaciones": []
            },
            "Friends": {
                "anio": 1994,
                "descripcion": "Seis amigos viviendo en Nueva York",
                "calificaciones": []
            },
            "The Office": {
                "anio": 2005,
                "descripcion": "La vida diaria en una oficina",
                "calificaciones": []
            },
            "Parks and Recreation": {
                "anio": 2009,
                "descripcion": "Una funcionaria y su pueblo",
                "calificaciones": []
            },
            "Modern Family": {
                "anio": 2009,
                "descripcion": "Tres familias muy diferentes",
                "calificaciones": []
            }
        }
    },
    "Terror": {
        "Pelicula": {
            "El Conjuro": {
                "anio": 2013,
                "descripcion": "Una familia acosada por una presencia",
                "calificaciones": []
            },
            "Hereditary": {
                "anio": 2018,
                "descripcion": "Una familia y un oscuro secreto",
                "calificaciones": []
            },
            "It": {
                "anio": 2017,
                "descripcion": "Amigos enfrentan a un payaso siniestro",
                "calificaciones": []
            },
            "Sinister": {
                "anio": 2012,
                "descripcion": "Un escritor encuentra videos macabros",
                "calificaciones": []
            },
            "Scream": {
                "anio": 1996,
                "descripcion": "Un asesino enmascarado acecha un pueblo",
                "calificaciones": []
            }
        },
        "Serie": {
            "La maldicion de Hill House": {
                "anio": 2018,
                "descripcion": "Una casa embrujada y su pasado",
                "calificaciones": []
            },
            "American Horror Story": {
                "anio": 2011,
                "descripcion": "Una historia de terror por temporada",
                "calificaciones": []
            },
            "Stranger Things": {
                "anio": 2016,
                "descripcion": "Misterios sobrenaturales en un pueblo",
                "calificaciones": []
            },
            "The Walking Dead": {
                "anio": 2010,
                "descripcion": "Sobrevivientes de un apocalipsis zombi",
                "calificaciones": []
            },
            "Penny Dreadful": {
                "anio": 2014,
                "descripcion": "Monstruos clasicos en Londres",
                "calificaciones": []
            }
        }
    },
    "Ciencia ficcion": {
        "Pelicula": {
            "Interestelar": {
                "anio": 2014,
                "descripcion": "Un viaje espacial para salvar la Tierra",
                "calificaciones": []
            },
            "Matrix": {
                "anio": 1999,
                "descripcion": "Un hacker descubre la realidad",
                "calificaciones": []
            },
            "Blade Runner 2049": {
                "anio": 2017,
                "descripcion": "Un cazador de replicantes busca respuestas",
                "calificaciones": []
            },
            "Avatar": {
                "anio": 2009,
                "descripcion": "Un marine en el planeta Pandora",
                "calificaciones": []
            },
            "Ex Machina": {
                "anio": 2014,
                "descripcion": "Un programador evalua una inteligencia artificial",
                "calificaciones": []
            }
        },
        "Serie": {
            "Black Mirror": {
                "anio": 2011,
                "descripcion": "El lado oscuro de la tecnologia",
                "calificaciones": []
            },
            "Dark": {
                "anio": 2017,
                "descripcion": "Viajes en el tiempo en un pueblo aleman",
                "calificaciones": []
            },
            "Westworld": {
                "anio": 2016,
                "descripcion": "Androides en un parque tematico",
                "calificaciones": []
            },
            "The Mandalorian": {
                "anio": 2019,
                "descripcion": "Un cazarrecompensas en la galaxia",
                "calificaciones": []
            },
            "Fringe": {
                "anio": 2008,
                "descripcion": "Casos de ciencia extrema en el FBI",
                "calificaciones": []
            }
        }
    }
}

# Administrador
admin = {
    "usuario": "admin",
    "clave": None
}
# Cantidad de contenidos que puede ver una cuenta durante la prueba.
LIMITE_PRUEBA = 5
# La plataforma siempre debe conservar por lo menos diez peliculas.
MINIMO_PELICULAS = 10
# Precio del acceso completo a la plataforma.
PRECIO = 12000

# Validar la clave

def validar_clave(clave):
    """Comprueba que la contraseña cumpla las reglas y que no esté repetida."""
    if len(clave) < 8:
        return False
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False
    for caracter in clave:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        elif caracter in string.punctuation:
            tiene_especial = True
    if not tiene_mayuscula or not tiene_minuscula or not tiene_numero or not tiene_especial:
        return False
    for datos_usuario in usuarios.values():
        if datos_usuario["clave"] == clave:
            return False
    if admin["clave"] == clave:
        return False
    return True

# Generar clave

def generar_clave():
    """Crea una contraseña aleatoria que cumple las reglas de seguridad del programa."""
    caracteres_posibles = string.ascii_letters + string.digits + string.punctuation
    while True:
        caracteres_elegidos = random.choices(caracteres_posibles, k=10)
        clave = "".join(caracteres_elegidos)
        if validar_clave(clave):
            return clave

# Generar token

def generar_token():
    """Genera un token con dos letras mayúsculas y un número."""
    letras = random.choices(string.ascii_uppercase, k=2)
    numero = random.randint(0, 9)
    token = "".join(letras) + str(numero)
    return token

# Generar codigo de pago

def generar_codigo_pago():
    """Genera un código numérico de cuatro dígitos para las compras."""
    codigo = random.randint(1000, 9999)
    return str(codigo)
#pedir numero

def pedir_numero(mensaje, minimo, maximo):
    """Solicita un número y repite la pregunta hasta que esté dentro del rango permitido."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Error: debe ingresar un numero.")
            continue
        if not texto.isdigit():
            print("Error: solo se permiten numeros.")
            continue
        numero = int(texto)
        if numero >= minimo and numero <= maximo:
            return numero
        print(f"Error: el numero debe estar entre {minimo} y {maximo}.")
# pedir texto

def pedir_texto(mensaje, minimo=1, maximo=100):
    """Solicita texto y valida que no esté vacío y que tenga la longitud permitida."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Error: este campo no puede quedar vacio.")
            continue
        if len(texto) < minimo:
            print(f"Error: debe tener minimo {minimo} caracteres.")
            continue
        if len(texto) > maximo:
            print(f"Error: no puede superar los {maximo} caracteres.")
            continue
        return texto
# s y n

def pedir_si_no(mensaje):
    """Solicita una respuesta de sí o no usando S o N."""
    while True:
        respuesta = input(mensaje).strip().upper()
        if respuesta == "S":
            return True
        if respuesta == "N":
            return False
        print("Error: solo puede responder S o N.")

def pedir_cedula():
    """Solicita una cédula numérica de entre seis y diez dígitos."""
    while True:
        cedula = pedir_texto("Cedula: ", 6, 10)
        if cedula.isdigit():
            return cedula
        print("Error: la cedula solo debe tener numeros.")

def pedir_telefono():
    """Solicita un teléfono que contenga solamente números."""
    while True:
        telefono = pedir_texto("Telefono: ", 7, 10)
        if telefono.isdigit():
            return telefono
        print("Error: el telefono solo debe tener numeros.")

def pedir_correo():
    """Solicita un correo electrónico y revisa su formato básico."""
    while True:
        correo = pedir_texto("Correo electronico: ", 5, 50)
        if " " in correo:
            print("Error: el correo no puede tener espacios.")
            continue
        if correo.count("@") != 1:
            print("Error: el correo debe tener una sola @.")
            continue
        partes = correo.split("@")
        nombre = partes[0]
        dominio = partes[1]
        if nombre == "" or dominio == "":
            print("Error: escriba texto antes y despues de la @.")
            continue
        if "." not in dominio:
            print("Error: el dominio debe tener un punto, como gmail.com.")
            continue
        if dominio.startswith(".") or dominio.endswith("."):
            print("Error: el punto no puede estar al principio ni al final del dominio.")
            continue
        return correo

def pedir_codigo_pago():
    """Solicita un código de pago compuesto por cuatro números."""
    while True:
        codigo = pedir_texto("Ingrese el codigo de pago (4 digitos): ", 4, 4)
        if codigo.isdigit():
            return codigo
        print("Error: el codigo de pago solo puede tener numeros.")
# Elegir una categoria

def elegir_categoria():
    """Muestra las categorías disponibles y devuelve la que el usuario elige."""
    print("Categorias disponibles:")
    lista_categorias = list(categorias.keys())
    numero = 1
    for categoria in lista_categorias:
        print(f"{numero}. {categoria}")
        numero = numero + 1
    opcion = pedir_numero( "Seleccione una categoria: ", 1, len(lista_categorias))
    posicion = opcion - 1
    categoria_seleccionada = lista_categorias[posicion]
    return categoria_seleccionada
# Elegir el tipo de contenido

def elegir_tipo(categoria):
    """Muestra los tipos de contenido disponibles en la categoría elegida."""
    lista_tipos = list(categorias[categoria].keys())
    print(f"Tipos disponibles en la categoria '{categoria}':")
    numero = 1
    for tipo in lista_tipos:
        print(f"{numero}. {tipo}")
        numero = numero + 1
    opcion = pedir_numero("Seleccione un tipo: ", 1, len(lista_tipos))
    posicion = opcion - 1
    tipo_seleccionado = lista_tipos[posicion]
    return tipo_seleccionado

def promedio(datos):
    """Calcula la calificación promedio de una película o serie."""
    calificaciones = datos["calificaciones"]
    if len(calificaciones) == 0:
        return 0
    suma_calificaciones = sum(calificaciones)
    resultado = suma_calificaciones / len(calificaciones)
    return resultado
#  """Muestra una lista de resultados con su tipo, año y calificacion."""

def mostrar_lista(lista):
    """Muestra los contenidos con su tipo, nombre, año, categoría y calificación."""
    if len(lista) == 0:
        print("No hay resultados.")
        return
    numero = 1
    for elemento in lista:
        # Obtener la categoria, el tipo y el nombre
        categoria = elemento[0]
        tipo = elemento[1]
        nombre = elemento[2]
        datos = categorias[categoria][tipo][nombre]
        # Calcular la calificacion promedio del contenido
        calificacion = promedio(datos)
        # Mostrar la informacion del contenido
        print(
            f"{numero}. [{tipo}] {nombre} ({datos['anio']}) - "
            f"{categoria} - Calificacion: {calificacion:.1f}"
        )
        numero +=  1
#    """Permite buscar por categoria y tipo o por nombre."""

def buscar():
    """Permite buscar contenidos por categoría y tipo, o por una parte del nombre."""
    resultados = []
    print("Como desea buscar?")
    print("1. Por categoria y tipo")
    print("2. Por nombre")
    opcion = pedir_numero("Opcion: ", 1, 2)
    if opcion == 1:
        # La persona elige una categoria y despues Pelicula o Serie.
        categoria = elegir_categoria()
        tipo = elegir_tipo(categoria)
        for nombre in categorias[categoria][tipo]:
            resultados.append((categoria, tipo, nombre))
    else:
        texto_buscado = pedir_texto("Nombre a buscar: ", 1, 80).lower()
        for categoria in categorias:
            for tipo in categorias[categoria]:
                for nombre in categorias[categoria][tipo]:
                    if texto_buscado in nombre.lower():
                        resultados.append((categoria, tipo, nombre))
    if len(resultados) == 0:
        print("No se encontraron coincidencias.")
    return resultados
#    """Permite elegir un resultado. El numero cero sirve para volver."""

def seleccionar(lista):
    """Muestra una lista y devuelve el contenido seleccionado; cero permite volver."""
    if len(lista) == 0:
        print("No hay resultados para seleccionar.")
        return None
    mostrar_lista(lista)
    opcion = pedir_numero("Elija un numero (0 para volver): ", 0, len(lista))
    if opcion == 0:
        return None
    elemento_seleccionado = lista[opcion - 1]
    return elemento_seleccionado
#"""Actualiza o elimina una pelicula de los espacios personales de usuarios."""

def reemplazar_en_espacios(viejo, nuevo):
    """Actualiza o elimina un contenido guardado en los espacios personales de los usuarios."""
    for cedula in usuarios:
        espacio_personal = usuarios[cedula]["espacio_personal"]
        if viejo in espacio_personal:
            posicion = espacio_personal.index(viejo)
            if nuevo is None:
                # Si se elimina el contenido, tambien se quita de las listas.
                espacio_personal.pop(posicion)
            else:
                # Si se cambia el nombre, se actualiza la referencia guardada.
                espacio_personal[posicion] = nuevo
# """Permite solicitar la compra, ingresar un codigo o regresar."""

def pantalla_bloqueo(usuario_actual):
    """Permite solicitar la compra, ingresar el código de pago o volver."""
    while True:
        print("sus credenciales estan bloqueadas: termino la version de prueba.")
        print("1. Comprar la plataforma digital ADSO")
        print("2. Ingresar codigo de pago")
        print("3. Volver")
        opcion = pedir_numero("Opcion: ", 1, 3)
        if opcion == 1:
            # Evitamos que el mismo usuario envie varias solicitudes pendientes.
            if usuario_actual in solicitudes_compra:
                print("Ya tiene una solicitud de compra pendiente.")
            else:
                solicitudes_compra.append(usuario_actual)
                print(f"Solicitud enviada al administrador. Valor: ${PRECIO:,}")
                print("El administrador le entregara un codigo de cuatro digitos.")
        elif opcion == 2:
            codigo_escrito = pedir_codigo_pago()
            # Revisamos si el codigo guardado para el usuario coincide.
            if codigos_pago.get(usuario_actual) == codigo_escrito:
                usuarios[usuario_actual]["bloqueado"] = False
                usuarios[usuario_actual]["comprado"] = True
                # El codigo se elimina para que no se vuelva a utilizar.
                del codigos_pago[usuario_actual]
                print("Acceso total restablecido. Disfrute la plataforma.")
                return True
            print("Error: codigo incorrecto.")
        else:
            return False

def ver_recurso(usuario_actual, seleccion, desde_espacio=False):
    """Muestra un contenido, registra su calificación y controla el acceso de prueba."""
    categoria, tipo, nombre = seleccion
    datos = categorias[categoria][tipo][nombre]
    usuario = usuarios[usuario_actual]
    # Mostramos la informacion principal del contenido seleccionado.
    print(f"--- Reproduciendo: {nombre} ---")
    print(f"Categoria: {categoria}")
    print(f"Tipo: {tipo}")
    print(f"Año: {datos['anio']}")
    print(f"Descripcion: {datos['descripcion']}")
    print(f"Calificacion promedio: {promedio(datos):.1f}")
    # Solo contamos los contenidos si la persona aun esta en version de prueba.
    if not usuario["comprado"]:
        usuario["vistos"] += 1
        print(f"Version de prueba: {usuario['vistos']} de {LIMITE_PRUEBA} recursos.")
    # Pedimos una calificacion del uno al cinco y la guardamos.
    calificacion = pedir_numero("Califique de 1 (mala) a 5 (excelente): ", 1, 5)
    datos["calificaciones"].append(calificacion)
    print(f"Gracias por calificar '{nombre}' con {calificacion}.")
    # Si no se abrio desde el espacio personal, se puede guardar alli.
    if not desde_espacio and seleccion not in usuario["espacio_personal"]:
        desea_guardar = pedir_si_no("¿Agregar a su espacio personal? (S/N): ")
        if desea_guardar:
            usuario["espacio_personal"].append(seleccion)
            print("Agregada a su espacio personal.")
    # Al llegar al limite, pedimos comprar o ingresar el codigo.
    if not usuario["comprado"] and usuario["vistos"] >= LIMITE_PRUEBA:
        usuario["bloqueado"] = True
        print(f"Llego al limite de {LIMITE_PRUEBA} recursos de la version de prueba.")
        if not pantalla_bloqueo(usuario_actual):
            return "inicio"
    # Opciones disponibles despues de ver un contenido.
    print("1. Seguir en la plataforma")
    print("2. Ir al inicio del aplicativo")
    print("3. Salir de la plataforma")
    opcion = pedir_numero("Opcion: ", 1, 3)
    if opcion == 3:
        print("Gracias por usar el sistema. Hasta luego.")
        sys.exit()
    if opcion == 2:
        return "inicio"
    return "seguir"

def menu_admin():
    """Administra el catálogo, las solicitudes, las compras y los informes de la plataforma.

    El administrador puede agregar, consultar, actualizar y eliminar contenidos.
    También revisa recuperaciones de credenciales, solicitudes de compra e informes.
    """
    while True:
        print("--- MENU ADMIN ---")
        print("1. Agregar pelicula o serie")
        print("2. Consultar por categoria o nombre")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Categoria con mayor y menor cantidad")
        print("6. Solicitudes de credenciales")
        print("7. Solicitudes de compra")
        print("8. Informes")
        print("9. Cerrar sesion")
        opcion = pedir_numero("Opcion: ", 1, 9)
        if opcion == 1:
            #agregar pelicula o serie
            categoria = elegir_categoria()
            tipo = elegir_tipo(categoria)
            # El nombre es obligatorio y no se puede repetir en la misma categoria y tipo.
            while True:
                nombre = pedir_texto("Ingrese el nombre: ", 1, 80)
                if nombre in categorias[categoria][tipo]:
                    print("Error: ya existe un contenido con ese nombre en esta categoria y tipo.")
                else:
                    break
            anio = pedir_numero("Ingrese el año (1900-2026): ", 1900, 2026)
            descripcion = pedir_texto("Ingrese la descripcion: ", 5, 300)
            # Guardamos los datos con una lista vacia de calificaciones.
            categorias[categoria][tipo][nombre] = {
                "anio": anio,
                "descripcion": descripcion,
                "calificaciones": []
            }
            print(f"{tipo} '{nombre}' agregada a '{categoria}' con calificacion 0.")
        elif opcion == 2:
            #"""Busca un contenido y muestra todos sus datos."""
            resultados = buscar()
            seleccion = seleccionar(resultados)
            if seleccion is not None:
                categoria = seleccion[0]
                tipo = seleccion[1]
                nombre = seleccion[2]
                datos = categorias[categoria][tipo][nombre]
                print(f"Nombre: {nombre}")
                print(f"Categoria: {categoria}")
                print(f"Tipo: {tipo}")
                print(f"Año: {datos['anio']}")
                print(f"Descripcion: {datos['descripcion']}")
                print(f"Calificacion promedio: {promedio(datos):.1f}")
        elif opcion == 3:
            resultados = buscar()
            seleccion = seleccionar(resultados)
            if seleccion is not None:
                categoria = seleccion[0]
                tipo = seleccion[1]
                nombre_anterior = seleccion[2]
                datos = categorias[categoria][tipo][nombre_anterior]
                print("Ingrese los nuevos datos. Todos los campos son obligatorios.")
                # Pedimos el nombre y que no se duplique.
                while True:
                    nombre_nuevo = pedir_texto("Nuevo nombre: ", 2, 90)
                    if nombre_nuevo != nombre_anterior and nombre_nuevo in categorias[categoria][tipo]:
                        print("Error: ya existe otra pelicula o serie con ese nombre.")
                    else:
                        break
                anio_nuevo = pedir_numero("Nuevo año (1900-2026): ", 1900, 2026)
                descripcion_nueva = pedir_texto("Nueva descripcion: ", 5, 300)
                # Si el nombre cambió, movemos el contenido al nombre nuevo.
                if nombre_nuevo != nombre_anterior:
                    categorias[categoria][tipo][nombre_nuevo] = categorias[categoria][tipo].pop(nombre_anterior)
                    seleccion_nueva = (categoria, tipo, nombre_nuevo)
                    # Actualizamos el contenido guardado en espacios personales.
                    reemplazar_en_espacios(seleccion, seleccion_nueva)
                    nombre_final = nombre_nuevo
                else:
                    nombre_final = nombre_anterior
                categorias[categoria][tipo][nombre_final]["anio"] = anio_nuevo
                categorias[categoria][tipo][nombre_final]["descripcion"] = descripcion_nueva
                # Al actualizar el contenido, su calificacion vuelve a cero, igual que antes.
                categorias[categoria][tipo][nombre_final]["calificaciones"] = []
                print(f"{tipo} '{nombre_final}' actualizada. Su calificacion volvio a 0.")
        elif opcion == 4:
            resultados = buscar()
            seleccion = seleccionar(resultados)
            if seleccion is not None:
                categoria = seleccion[0]
                tipo = seleccion[1]
                nombre = seleccion[2]

                # Antes de borrar una pelicula, contamos cuantas hay en todo el catalogo.
                # Las series no cuentan para este limite porque son otro tipo de contenido.
                cantidad_peliculas = 0
                for categoria_actual in categorias:
                    cantidad_peliculas = cantidad_peliculas + len(categorias[categoria_actual]["Pelicula"])

                # No permitimos eliminar peliculas cuando el catalogo tiene diez o menos.
                if tipo == "Pelicula" and cantidad_peliculas <= MINIMO_PELICULAS:
                    print(f"No se puede eliminar '{nombre}'. La plataforma debe conservar al menos {MINIMO_PELICULAS} peliculas.")
                    continue

                primera_confirmacion = pedir_si_no(f"¿Esta seguro de eliminar '{nombre}'? (S/N): ")
                if primera_confirmacion:
                    segunda_confirmacion = pedir_si_no(f"¿Realmente desea eliminar '{nombre}'? (S/N): ")
                else:
                    segunda_confirmacion = False

                if segunda_confirmacion:
                    tercera_confirmacion = pedir_si_no(
                        f"ULTIMA CONFIRMACION: ¿Eliminar '{nombre}' definitivamente? (S/N): "
                    )
                else:
                    tercera_confirmacion = False

                if primera_confirmacion and segunda_confirmacion and tercera_confirmacion:
                    del categorias[categoria][tipo][nombre]
                    reemplazar_en_espacios(seleccion, None)
                    print(f"{tipo} '{nombre}' eliminada exitosamente.")
                else:
                    print("Eliminacion cancelada.")
        elif opcion == 5:
            categoria_mayor = None
            categoria_menor = None
            for categoria in categorias:
                cantidad_peliculas = len(categorias[categoria]["Pelicula"])
                cantidad_series = len(categorias[categoria]["Serie"])
                cantidad_total = cantidad_peliculas + cantidad_series
                if categoria_mayor is None or cantidad_total > categoria_mayor[1]:
                    categoria_mayor = (categoria, cantidad_total)
                if categoria_menor is None or cantidad_total < categoria_menor[1]:
                    categoria_menor = (categoria, cantidad_total)
            print(
                f"Categoria con mayor cantidad: {categoria_mayor[0]} "
                f"({categoria_mayor[1]} contenidos)"
            )
            print(
                f"Categoria con menor cantidad: {categoria_menor[0]} "
                f"({categoria_menor[1]} contenidos)"
            )
        elif opcion == 6:
            # El administrador selecciona una solicitud y verifica el token que le entrega el usuario.
            # Si coincide, autoriza la recuperacion; la contraseña todavia no se cambia aqui.
            print("Solicitudes de credenciales (orden de llegada):")
            # Comprobar si hay solicitudes pendientes
            if len(solicitudes_credenciales) == 0:
                print("No hay solicitudes pendientes.")
            else:
                posicion = 1
                for cedula in solicitudes_credenciales:
                    nombre = usuarios[cedula]["nombre"]
                    if usuarios[cedula]["recuperacion_aprobada"]:
                        estado = "APROBADA"
                    else:
                        estado = "PENDIENTE"
                    print(f"{posicion}. {nombre} - cedula {cedula} - {estado}")
                    posicion = posicion + 1

                eleccion = pedir_numero(
                    "Seleccione una solicitud (0 para volver): ",
                    0,
                    len(solicitudes_credenciales)
                )

                if eleccion != 0:
                    posicion = eleccion - 1
                    cedula_seleccionada = solicitudes_credenciales[posicion]

                    if usuarios[cedula_seleccionada]["recuperacion_aprobada"]:
                        print("Esta solicitud ya fue aprobada. El usuario debe ingresar su token en la opcion de recuperacion.")
                    else:
                        token_escrito = pedir_texto("Token que entrega el usuario: ", 3, 3).upper()

                        if token_escrito == usuarios[cedula_seleccionada]["token"]:
                            usuarios[cedula_seleccionada]["recuperacion_aprobada"] = True
                            print("Token verificado. Solicitud aprobada.")
                            print("El usuario puede volver a recuperacion e ingresar su token para recibir la nueva clave.")
                        else:
                            print("Token incorrecto. La solicitud sigue pendiente.")
        elif opcion == 7:
            print("Solicitudes de compra (orden de llegada):")
            if len(solicitudes_compra) == 0:
                print("No hay solicitudes de compra pendientes.")
            else:
                posicion = 1
                for cedula in solicitudes_compra:
                    nombre = usuarios[cedula]["nombre"]
                    print(f"{posicion}. {nombre} - cedula {cedula}")
                    posicion = posicion + 1
                eleccion = pedir_numero(
                    "Seleccione una solicitud (0 para volver): ",
                    0,
                    len(solicitudes_compra)
                )
                if eleccion != 0:
                    posicion = eleccion - 1
                    cedula_seleccionada = solicitudes_compra.pop(posicion)
                    # Generar y guardar un codigo de pago para el usuario
                    codigo = generar_codigo_pago()
                    codigos_pago[cedula_seleccionada] = codigo
                    nombre = usuarios[cedula_seleccionada]["nombre"]
                    print(f"Codigo de pago para {nombre}: {codigo}")
                    print("Entregue este codigo al usuario.")
        elif opcion == 8:
            # Mostrar los informes de la plataforma
            compradores = 0
            usuarios_que_ingresaron = 0
            # Contar los usuarios que compraron o ingresaron
            for cedula in usuarios:
                datos_usuario = usuarios[cedula]
                if datos_usuario["comprado"]:
                    compradores = compradores + 1
                if datos_usuario["ingreso"]:
                    usuarios_que_ingresaron = usuarios_que_ingresaron + 1
            # Calcular el dinero recaudado
            dinero_recaudado = compradores * PRECIO
            print("--- INFORMES ---")
            print(f"Usuarios que compraron el acceso: {compradores}")
            print(f"Usuarios que ingresaron a la version de prueba: {usuarios_que_ingresaron}")
            print(f"Monto recaudado: ${dinero_recaudado:,}")
        else:
            print("Sesion cerrada con exito.")
            return

def menu_espacio_personal(usuario_actual):
    """Permite consultar, agregar, reproducir y quitar contenidos de la lista personal."""
    while True:
        mi_lista = usuarios[usuario_actual]["espacio_personal"]
        print("--- MI ESPACIO PERSONAL ---")
        print("1. Ver mi lista")
        print("2. Agregar pelicula o serie")
        print("3. Reproducir")
        print("4. Eliminar")
        print("5. Volver")
        opcion = pedir_numero("Opcion: ", 1, 5)
        if opcion == 1:
            mostrar_lista(mi_lista)
        elif opcion == 2:
            seleccion = seleccionar(buscar())
            if seleccion is not None:
                if seleccion in mi_lista:
                    print("Ya esta en su espacio personal.")
                else:
                    mi_lista.append(seleccion)
                    print("Agregada a su espacio personal.")
        elif opcion == 3:
            if len(mi_lista) == 0:
                print("Su espacio personal esta vacio.")
            else:
                seleccion = seleccionar(mi_lista)
                if seleccion is not None:
                    resultado = ver_recurso(usuario_actual, seleccion, True)
                    if resultado == "inicio":
                        # Avisamos al menu del usuario que debe volver al inicio general.
                        return "inicio"
        elif opcion == 4:
            if len(mi_lista) == 0:
                print("Su espacio personal esta vacio.")
            else:
                seleccion = seleccionar(mi_lista)
                if seleccion is not None:
                    desea_eliminar = pedir_si_no(
                        f"¿Eliminar '{seleccion[2]}' de su lista? (S/N): "
                    )
                    if desea_eliminar:
                        mi_lista.remove(seleccion)
                        print("Eliminada de su espacio personal.")
                    else:
                        print("Operacion cancelada.")
        else:
            return

def menu_usuario(usuario_actual):
    """Presenta las opciones principales disponibles para un usuario que inició sesión."""
    while True:
        print("--- MENU USUARIO ---")
        print("1. Buscar pelicula o serie")
        print("2. Recomendadas")
        print("3. Mi espacio personal")
        print("4. Cerrar sesion")
        opcion = pedir_numero("Opcion: ", 1, 4)
        if opcion == 1:
            resultados = buscar()
            seleccion = seleccionar(resultados)
            if seleccion is not None:
                resultado = ver_recurso(usuario_actual, seleccion)
                if resultado == "inicio":
                    return
        elif opcion == 2:
            todos_los_contenidos = []
            existen_calificaciones = False
            # Reunimos todos los contenidos disponibles y revisamos si ya hay notas.
            for categoria in categorias:
                for tipo in categorias[categoria]:
                    for nombre in categorias[categoria][tipo]:
                        contenido = (categoria, tipo, nombre)
                        todos_los_contenidos.append(contenido)
                        notas = categorias[categoria][tipo][nombre]["calificaciones"]
                        if len(notas) > 0:
                            existen_calificaciones = True
            # Si nadie ha calificado, mostramos hasta diez contenidos aleatorios.
            if not existen_calificaciones:
                cantidad = min(10, len(todos_los_contenidos))
                recomendadas = random.sample(todos_los_contenidos, cantidad)
            else:
                # Si ya hay notas, ordenamos los contenidos desde el promedio mas alto.
                contenidos_con_promedio = []
                for contenido in todos_los_contenidos:
                    categoria = contenido[0]
                    tipo = contenido[1]
                    nombre = contenido[2]
                    datos = categorias[categoria][tipo][nombre]
                    calificacion = promedio(datos)
                    contenidos_con_promedio.append((calificacion, contenido))
                contenidos_con_promedio.sort(reverse=True)
                recomendadas = []
                for calificacion, contenido in contenidos_con_promedio[:10]:
                    recomendadas.append(contenido)
            print("*** RECOMENDADAS ***")
            seleccion = seleccionar(recomendadas)
            if seleccion is not None:
                resultado = ver_recurso(usuario_actual, seleccion)
                if resultado == "inicio":
                    return
        elif opcion == 3:
            resultado_espacio = menu_espacio_personal(usuario_actual)
            if resultado_espacio == "inicio":
                return
        else:
            print("Sesion cerrada con exito.")
            return

def menu_principal():
    """Controla el inicio de sesión, el registro, la recuperación de credenciales y la salida.

    Es el menú general del programa. Desde aquí se registran cuentas, se inicia sesión
    y se tramita la recuperación de credenciales con aprobación previa del administrador.
    """
    while True:
        print("===== BIENVENIDO A LA PLATAFORMA ADSO =====")
        print("1. Iniciar sesion")
        print("2. Registrarse")
        print("3. Olvide mis credenciales")
        print("4. Salir")
        opcion = pedir_numero("Opcion: ", 1, 4)
        if opcion == 1:
            usuario_escrito = pedir_texto("Ingrese su usuario (cedula): ", 1, 30)
            # En el primer intento del administrador se genera su clave.
            if usuario_escrito == admin["usuario"] and admin["clave"] is None:
                admin["clave"] = generar_clave()
                print("Primer ingreso del administrador.")
                print(f"Su contraseña es: {admin['clave']}")
                print("Guardela, la necesitara para ingresar.")
            clave_escrita = pedir_texto("Ingrese su clave: ", 1, 100)
            if usuario_escrito == admin["usuario"] and clave_escrita == admin["clave"]:
                print("Sesion iniciada como administrador.")
                menu_admin()
            elif usuario_escrito in usuarios and clave_escrita == usuarios[usuario_escrito]["clave"]:
                print(f"Bienvenido {usuarios[usuario_escrito]['nombre']}.")
                usuarios[usuario_escrito]["ingreso"] = True
                acceso_permitido = True
                if usuarios[usuario_escrito]["bloqueado"]:
                    acceso_permitido = pantalla_bloqueo(usuario_escrito)
                if acceso_permitido:
                    menu_usuario(usuario_escrito)
            else:
                print("Error: usuario o clave incorrectos.")
        elif opcion == 2:
            print("--- REGISTRO ---")
            # El nombre debe tener al menos nombre y apellido, con letras y espacios.
            while True:
                nombre_completo = pedir_texto("Nombre completo: ", 1, 60)
                nombre_sin_espacios = nombre_completo.replace(" ", "")
                partes_nombre = nombre_completo.split()
                if nombre_sin_espacios.isalpha() and len(partes_nombre) >= 2:
                    break
                print("Error: escriba nombre y apellido, usando solo letras y espacios.")
            while True:
                cedula = pedir_cedula()
                if cedula not in usuarios:
                    break
                print("Error: esa cedula ya esta registrada. Intente con otra.")
            telefono = pedir_telefono()
            correo = pedir_correo()
            usuarios[cedula] = {
                "nombre": nombre_completo,
                "telefono": telefono,
                "correo": correo,
                "clave": generar_clave(),
                "token": generar_token(),
                "recuperacion_aprobada": False,
                "vistos": 0,
                "bloqueado": False,
                "comprado": False,
                "ingreso": False,
                "espacio_personal": []
            }
            print("Registro exitoso. GUARDE ESTOS DATOS:")
            print(f"Usuario: {cedula}")
            print(f"Contraseña: {usuarios[cedula]['clave']}")
            print(f"Token de recuperacion: {usuarios[cedula]['token']}")
        elif opcion == 3:
            # Primero se identifica la cuenta que necesita recuperar sus credenciales.
            cedula = pedir_cedula()

            if cedula not in usuarios:
                print("Error: esa cedula no esta registrada.")
            elif cedula not in solicitudes_credenciales:
                # La solicitud queda pendiente hasta que el administrador la revise.
                solicitudes_credenciales.append(cedula)
                print("Solicitud enviada al administrador.")
                print("Entregue su token de recuperacion al administrador para que revise y apruebe la solicitud.")
                print("Cuando el administrador la apruebe, vuelva a elegir la opcion 3 para terminar la recuperacion.")
            elif not usuarios[cedula]["recuperacion_aprobada"]:
                print("Su solicitud sigue pendiente. Espere a que el administrador la apruebe.")
                print("Cuando sea aprobada, entre otra vez a la opcion 3 e ingrese su token.")
            else:
                # Solo se solicita el token al usuario cuando el administrador ya aprobo la solicitud.
                print("Su solicitud fue aprobada por el administrador.")
                token_escrito = pedir_texto("Ingrese su token de recuperacion: ", 3, 3).upper()

                if token_escrito == usuarios[cedula]["token"]:
                    # Si el administrador aprobo la solicitud y el token coincide, se genera una clave nueva.
                    # La cedula se conserva como nombre de usuario.
                    usuarios[cedula]["clave"] = generar_clave()
                    usuarios[cedula]["token"] = generar_token()
                    usuarios[cedula]["recuperacion_aprobada"] = False
                    solicitudes_credenciales.remove(cedula)

                    print("Token verificado. Estas son sus nuevas credenciales:")
                    print(f"Usuario: {cedula}")
                    print(f"Nueva contraseña: {usuarios[cedula]['clave']}")
                    print(f"Nuevo token de recuperacion: {usuarios[cedula]['token']}")
                else:
                    print("Token incorrecto. No se cambiaron sus credenciales.")
        else:
            print("Gracias por usar el sistema. Hasta luego.")
            break
if __name__ == "__main__":
    menu_principal()
