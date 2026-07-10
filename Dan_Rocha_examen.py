juegos = {'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True,
'NovaStudio'],
'G002': ['Puzzle Atlas', 'PC', 'puzzle', 'E', False,
'BrightWorks'],'G003': ['Auzfzle tlas', 'PC', 'pffuzzle', 'E', False,
'BrightWorkadss']}
inventario = {'G001': [9990, 7],'G002': [19990, 0],'G003': [9000, 1]}
def leer_opcion():
    try:
        opcion = int(input("Ingrese una opcion: "))
        if opcion < 0 or opcion > 6:
            print("Porfavor ingrese una opción valida")
        else:
            return opcion
    except:
        print("Porfavor ingrese una opción valida")
def buscar_plataforma(plataforma):
    cantidad_total = 0
    plataforma = plataforma.lower()
    for juego in juegos:
        plataformainv = juegos[juego][1]
        if plataformainv.lower() == plataforma:
                cantidad = inventario[juego][1]
                cantidad_total = cantidad_total + cantidad
    print(cantidad_total)
def busqueda_precio(minimo,maximo):
    lista_precios = []
    for juego in inventario:
        if inventario[juego][0] >= minimo and inventario[juego][0] <= maximo:
            lista_precios.append([juegos[juego][0]])
    lista_precios = sorted(lista_precios)
    print(lista_precios)
def buscar_codigo(codigo):
    codigo = codigo.upper()
    codigobool = False
    for codigos in inventario:
        if codigos != codigo:
           continue
        elif codigo == codigos:
           codigobool = True
    return codigobool
def actualizar_precio(codigo,nuevoprecio):
    if buscar_codigo(codigo) == True:
        codigo = codigo.upper()
        inventario[codigo][0] = nuevoprecio
        if inventario[codigo][0] == nuevoprecio:
           return True
    else:
       return False    
def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, juegos, inventario):
  upper_codigo = codigo.upper()
  if upper_codigo in juegos:
    return False
  if multiplayer.lower() == 's':
    multiplayer_bool = True  
  else:
    multiplayer_bool = False
  juegos[upper_codigo] = [titulo.strip(), plataforma.strip(), genero.strip(), clasificacion, multiplayer_bool, editor.strip()]
  juegos[upper_codigo] = [int(precio), int(stock)]

  return True
def eliminar_juego(codigo):
    if buscar_codigo(codigo) == True:
        codigo = codigo.upper()
        del inventario[codigo]
        del juegos[codigo] 
        return True
    else:
       return False    
while True:
    print('''========== MENÚ PRINCIPAL ==========
1. Stock por plataforma
2. Búsqueda de juegos por rango de precio
3. Actualizar precio de juego
4. Agregar juego
5. Eliminar juego
6. Salir 
=====================================''')
    opcion_elegida = leer_opcion()
    
    if opcion_elegida == 1:
        buscar_plataforma(input("ingrese la plataforma: "))
    elif opcion_elegida == 2:
        try:
            valor_minimo = int(input("Ingrese el Precio Minimo: "))      
        except:
            print("El valor ingresado no es valido")
        if valor_minimo >= 0:
                try:
                    valor_maximo = int(input("ingrese el precio maximo: "))
                except:
                    print("el valor ingresado no es valido")
        else:
            print("el valor ingresado no es valido")
        if valor_maximo >= valor_minimo:
            busqueda_precio(valor_minimo,valor_maximo)
        else:
            print("el valor ingresado no es valido")
    elif opcion_elegida == 3:
        Actualizar = True
        while Actualizar == True:
            codigo = input("Ingrese el codigo: ")
            try:
                precionuevo = int(input("Ingrese el precio nuevo: "))
            except:
                print("El valor ingresado no es valido")
                Actualizar = False
            if precionuevo >= 0:
                resultado = actualizar_precio(codigo,precionuevo)
                if resultado == True:
                    print("Precio actualizado")
                elif resultado == False:
                    print("El codigo no existe")
            seguir = input("Desea actualizar otro precio? (s/n): ")
            if seguir == "n":
                Actualizar = False
    elif opcion_elegida == 4:
        Actualizar = True
        while Actualizar == True:
            print("****Registrando un nuevo juego****")
            code = input("Codigo: ")
            titulo = input("Titulo: ")
            plataforma = input("Plataforma: ")
            classif = input("Clasificación (E, T o M): ")
            editor = input("Editor: ")
            genero = input("Género: ")
            multip = input("¿se puede jugar multiplayer? (s/n): ")
            try:
                precio = int(input("Precio: "))
            except:
                print("el valor ingresado no es valido")
                break
            
            stock = input("Stock: ")
    elif opcion_elegida == 5:
        resultado = eliminar_juego(input("Ingrese el codigo: "))
        if resultado == True:
            print("El juego ha sido eliminado")
        elif resultado == False:
            print("El codigo no existe")
    elif opcion_elegida == 6:
        print("Programa Finalizado")
        break