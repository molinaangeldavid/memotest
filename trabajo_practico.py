import random

LISTA = ['⌚','⌛','⏩','⏪','⏫','⏬','⏭','⏮','⏯','⏰','⏸','⏹','⏺','◧','◨','◩','◪','☔','☕','♈','♉','♊','♋','♌','♍','♎','♏','♐','♑','♒','♓','⚽','⚾','⚿','⛄','⛅','⛉','⛊','⛋','⛌','⛍','⛔','⛝','⛞','⛟','⛡','⛢','⛣','⛨','⛩','⛪','⛫','⛰','⛱','⛲','⛳','⛴','⛵','⛶','⛷','⛸','⛹','⛺','✅','✆','✇','✈','✉','✊','✋','✌','✍','⨀','⨁','⨂','⨃','⨅','⨆','⨇','⨈','⨉','⨊','⨍','⨎','⨏','✐','✑','✒','✓','✔','✘','✜','✞','✟','❶','❷','❸','❹','❺','❻','❼','❽','❾','❿','➔','➕','➖','➗','➘','⚋','⚌','⚍','⚎','⚏','⚐','⚑','⚒','⚓','⚔','⚕','⚖','⚗','⚘','⚙','⚚','⚛','⚜','⚝','⚞','⚟''℁','ℂ','℃','℄','℆','ℇ','℈','℉','ℊ','ℋ','ℌ','ℍ','ℏ','ℐ','ℑ','ℒ','ℓ','℔','ℕ','№','℗','℘','℞']

def nombre_jugador()->str:
    '''
    PRE:---
    POST: Retorna una cadena de texto, la cual es el nombre del jugador
    '''
    nombre = input('\tIngrese nombre de jugador: ')
    while not nombre.isalpha():
        nombre = input('\tError. Ingrese de nuevo nombre de jugador: ')
    nombre = nombre.upper()
    return nombre

def validar_tablero()->int:
    '''
    PRE:---
    POST: Retorna un valor numérico positivo, la cual es la dimensión elegida por el usuario para la creación de la matriz cuadrada
    '''
    print('Tamaño de tablero || 4x4 ||  || 8x8 ||  || 12x12 ||')
    dimension = input('Ingrese el tamaño del tablero con el que desea jugar (4 - 8 - 12): ')
    while not dimension.isnumeric() or int(dimension) not in [4,8,12]:
        dimension = input('ERROR!!! Ingrese nuevamente el tamaño del tablero con el que desea jugar (4 - 8 - 12): ')
    dimension = int(dimension)
    return dimension

def validar_opcion()->int:
    '''
    PRE:---
    POST: Retorna un valor numérico positivo, la cual es la opcion elegida por el usuario validada
    '''
    numero = input('Ingrese su opción: ')
    while not(numero.isnumeric() and int(numero)>=1 and int(numero)<=5):
        numero = input('Ingreso invalido. Vuelva a ingresar una opción: (1-5): ')
    numero = int(numero)
    return numero

def validar_opcion_cartas()->int:
    '''
    PRE:---
    POST: Retorna un valor numérico positivo, la cual es la carta especial elegida por el usuario validada 
    '''
    numero = input('Ingrese su opción: ')
    while not(numero.isnumeric() and int(numero)>=1 and int(numero)<=3):
        numero = input('Ingreso invalido. Vuelva a ingresar una opción: (1-3): ')
    numero = int(numero)
    return numero

def validar_coordenadas(dimension:int,tablero_incognito:list)->int: #Modificar a fila y columna
    '''
    PRE: Ingresa un valor numerico positivo, la cual es la dimension de la matriz a jugar. Tambien ingresa el tablero incognito del jugador
    POST: Retorna la coordenada de la matriz a adivinar
    '''
    coord = input('\t1.Ingrese las coordenadas de la ficha: ')
    while not(coord.isnumeric() and int(coord)<=dimension and int(coord)>=1):
        coord = input('\t1.Coordenada incorrecta. Ingrese otra vez: ')
    coord = int(coord)
    coord -= 1
    return coord

def validar_filas_columnas(dimension:int,mi_tablero_incognito:list)->tuple:
    '''
    PRE: Ingresa un valor numerico, la cual es la dimension la cual se jugará. Luego se un tablero incognito, la cual pertenece al jugador
    POST: Retorna una tupla con las coordenadas validadas, la cual son coordenadas no repetidas ni fichas adivinadas
    '''
    fila1 = validar_coordenadas(dimension,mi_tablero_incognito)
    columna1 = validar_coordenadas(dimension,mi_tablero_incognito)
    fila2 = validar_coordenadas(dimension,mi_tablero_incognito)
    columna2 = validar_coordenadas(dimension,mi_tablero_incognito)
    while not (mi_tablero_incognito[fila1][columna1]=='·' and mi_tablero_incognito[fila2][columna2]=='·' and (fila1,columna1)!=(fila2,columna2)):
        print('Ingresaste coordenadas invalidas. Vuelva a ingresar')
        fila1 = validar_coordenadas(dimension,mi_tablero_incognito)
        columna1 = validar_coordenadas(dimension,mi_tablero_incognito)
        fila2 = validar_coordenadas(dimension,mi_tablero_incognito)
        columna2 = validar_coordenadas(dimension,mi_tablero_incognito)
    return fila1,columna1,fila2,columna2    

def validar_cartas(bolsillo_cartas:list)->int:
    '''
    PRE: Ingresa la lista del jugador, cuya lista pertenece al bolsillo del jugador 
    POST: Retorna la opcion del jugador si desea utilizar una carta especial
    '''
    preguntar_carta1 = input('Desea utilizar una carta especial de su bolsillo? (si/no): ')
    while not (preguntar_carta1.isalpha() and preguntar_carta1=='si' or preguntar_carta1=='no'):
        if(len(bolsillo_cartas)==0):
            print('No tiene cartas disponibles')
        preguntar_carta1 = input('Vuelva a ingresar su respuesta (si/no): ')
    return preguntar_carta1    

def crear_matriz_incognito(dimension:int)->list: 
    '''
    PRE: Ingresa un valor numérico positivo, la cual es la dimensión de una matriz
    POST: Crea una matriz cuadrada con valores de coordenadas de fila y columna
    '''
    matriz_final_inc = []
    lista_incognito = []
    for i in range(dimension):
        lista_incognito = []
        for j in range(dimension):
            lista_incognito.append('·')
        matriz_final_inc.append(lista_incognito)     
    return matriz_final_inc
    
def crear_matriz(dimension:int)->list:
    '''
    PRE: Ingreso un valor numerico positivo, la cual sera la dimensión de la matriz cuadrada
    POST: Retorna una matriz de dimensión (ingresado por el usuario)
    '''
    lista_anidada= [] # Aqui esta la lista anidada, la cual servira como la matriz funcional
    matriz = [] # Aqui estaran los caracteres y su respecto par
    paco = []
    random.shuffle(LISTA)
    for i in range((dimension**2)//2):
        lista_usar_matriz = LISTA[i]
        matriz.append(lista_usar_matriz)
    matriz.extend(matriz)
    random.shuffle(matriz)
    for i in range(dimension):
        minilista = matriz[i*dimension:dimension*i+dimension]
        lista_anidada.append(minilista)             
    return lista_anidada             

def imprimir_puntuacion(score:list)->list:
    '''
    PRE: Ingresa una lista, la cual es el puntaje(sea individual o coop) 
    POST: Imprime una matriz de fila n y columna 2, la cual representa el puntaje de las partidas realizadas previamente ordenados de mayor a menor
    '''
    score = sorted(score, key = lambda x: x[1] , reverse=True) 
    for i in range(len(score)):
        for j in range(2):
            print(score[i][j], end='   ')
        print()

def imprimir_matriz(dimension:int,lista:list)->list:
    '''
    PRE: Ingresa un valor numerico positivo y una matriz. La cual la primera, es la dimension de cierta matriz, y la segunda, es una lista del jugador
    POST: Imprime una matriz, puede ser el tablero del jugador o un tablero incognito
    '''
    for i in range(dimension):
        for j in range(dimension):
            print('\t\t',lista[i][j], end='    ')
        print('\n')

def toti(matriz:list)->list: 
    '''
    PRE: Ingregra una lista como variable, la cual es el tablero del jugador
    POST: Retorna otra lista distinta. La cual es, matricialmente, el espejo horizontal o vertical de la matriz original
    '''
    horizontal_vertical = random.randint(1,2)
    if(horizontal_vertical==1):
        espejo_horizontal = matriz[-1::-1]    
        return espejo_horizontal
    elif(horizontal_vertical==2):
        espejo_vertical = []
        for i in range(len(matriz)):
            espejo_vertical.append(matriz[i][-1::-1])
        return espejo_vertical

def layout(matriz:list)->list: 
    '''
    PRE: Ingresa una lista, la cual es el tablero del jugador
    POST: Retorna la misma lista pero con sus respectivos valores mezclados aleatoriamente
    '''
    for i in matriz:
        random.shuffle(i)
    random.shuffle(matriz)    
    return matriz   
    
def aplicar_layout_incognito(tablero_incognito:list,adivinados:list)->list:
    '''
    PRE: Ingresa 3 listas, la cual importan tres tableros que pertenecen al jugador contrario. El tablero funcional, los caracteres adivinados y una lista anidada incognita alternativa
    POST: Retorna una lista, la cual es la lista anidada alternativa con los caracteres adivinados por el jugador. Esta función es exclusiva para la carta especial Layout
    '''
    for i in range(len(tablero_incognito)):
        for j in range(len(tablero_incognito[i])):
            for valor in adivinados:
                if tablero_incognito[i][j]==valor:
                    tablero_incognito[i][j] = valor
    return tablero_incognito          

def fatality(matriz:list)->list: 
    '''
    PRE: Ingresa una lista como variable, la cual es el tablero del jugador
    POST: Retorna otra lista distinta. La cual es, matricialmente, la transpuesta de la matriz original
    '''
    
    matriz_traspuesta = []
    for i in range(len(matriz)):
        matriz_traspuesta.append([])
        for j in range(len(matriz[i])):
            matriz_traspuesta[i].append(matriz[j][i])
    return matriz_traspuesta     

def cartas_probabilidad(nombre:str,bolsillo_carta:list,probabilidades:tuple)->None:
    '''
    PRE: Ingresa el nombre del jugador que tira el dado, ademas el bolsillo del jugador, cuyo contenido son las cartas especiales que le tocó
    POST: Imprime la carta que le tocó al jugador y guarda la carta en el bolsillo
    '''
    print(f'------------Jugador {nombre} ha tirado dado.------------\n')
    probabilidades_fatality = probabilidades[0]
    probabilidades_replay = probabilidades[1]
    probabilidades_replay += probabilidades_fatality 
    probabilidades_layout = probabilidades[2]
    probabilidades_layout += probabilidades_replay 
    probabilidades_toti = probabilidades[3]
    probabilidades_toti += probabilidades_layout
    prob = random.randint(0,100)
    if(prob>=0 and prob<=probabilidades_fatality):
        print('\tTe toco carta FATALITY')
        carta1 = 'fatality'
        bolsillo_carta.append(carta1)
    elif(prob>=probabilidades_fatality and prob<=probabilidades_replay):
        print('\tTe toco carta REPLAY')
        carta2 = 'replay'
        bolsillo_carta.append(carta2)
    elif(prob>=probabilidades_replay and prob<=probabilidades_layout): 
        print('\tTe toco carta LAYOUT')
        carta3 = 'layout'
        bolsillo_carta.append(carta3)
    elif(prob>=probabilidades_layout and prob<=probabilidades_toti):
        print('\tTe toco carta TOTI')
        carta4 = 'toti'
        bolsillo_carta.append(carta4)
    else:
        print('\tNo te toco nada.')
    
def configurar_probabilidades()->tuple:
    '''
    PRE: ---
    POST: Retorna una tupla que contiene las probabilidades por defecto o las elegidas por el usuario
    '''
    parametros = input('Desea modificar las probabilidades de cartas especiales? (si/no): ')
    while not (parametros.isalpha() and parametros=='si' or parametros=='no'):
        parametros = input('Error!!. Desea modificar las probabilidades de cartas especiales? (si/no): ')
    if parametros == 'si':    
        probabilidades_lista = []
        cartas = ['FATALITY','REPLAY','LAYOUT','TOTI']
        for i in cartas:
            probabilidades = input(f'Ingrese las probabilidades para {i}: ')
            while not (probabilidades.isnumeric() and int(probabilidades)>=0 and int(probabilidades)<=20):
                probabilidades = input('Ingreso probabilidades erroneas. Ingrese de nuevo: ')
            probabilidades = int(probabilidades)
            probabilidades_lista.append(probabilidades)
        probabilidades_tupla = tuple(probabilidades_lista)
        return probabilidades_tupla  
    else:
        probabilidades_tupla = (10,10,10,10)
        return probabilidades_tupla     

def usar_layout(bolsillo_cartas:list,nombre_b:str,mi_tablero_b:list,adivinados_b:list,tablero_incognito:list)->tuple:
    '''
    PRE: Ingresan como valores las variables que influenciaran en el tablero oponente. Ademas el bolsillo del jugador
    POST: Retorna una tupla con los tableros modificados
    '''
    if('layout' in bolsillo_cartas):    
        print(f'Aplicando LAYOUT al jugador {nombre_b}...')
        mi_tablero = layout(mi_tablero_b)
        mi_tablero_incognito = aplicar_layout_incognito(tablero_incognito,adivinados_b) 
        bolsillo_cartas.remove('layout')
        return mi_tablero, mi_tablero_incognito  

def usar_fatality(bolsillo_cartas:list,nombre_b:str,mi_tablero_b:list,tablero_incognito_b:list):
    '''
    PRE: Ingresan como valores las variables que influenciaran en el tablero oponente. Ademas el bolsillo del jugador
    POST: Retorna una tupla con los tableros modificados
    '''
    if('fatality' in bolsillo_cartas):
        print(f'Aplicando FATALITY al jugador {nombre_b}...')
        mi_tablero = fatality(mi_tablero_b)
        mi_tablero_incognito = fatality(tablero_incognito_b)
        bolsillo_cartas.remove('fatality')
        return mi_tablero, mi_tablero_incognito

def usar_toti(bolsillo_cartas:list,nombre_b:str,mi_tablero_b:list,tablero_incognito_b:list):
    '''
    PRE: Ingresan como valores las variables que influenciaran en el tablero oponente. Ademas el bolsillo del jugador
    POST: Retorna una tupla con los tableros modificados
    '''
    if('toti' in bolsillo_cartas):
        print(f'Aplicando TOTI al jugador {nombre_b}...')        
        mi_tablero = toti(mi_tablero_b)
        mi_tablero_incognito = toti(tablero_incognito_b)
        bolsillo_cartas.remove('toti')
        return mi_tablero, mi_tablero_incognito  

def cartas_especiales(bolsillo_cartas:list,nombre:str,mi_tablero:list,tablero_incognito:list,adivinados:list)->tuple: 
    '''
    PRE: Ingresan como valores las variables que influenciaran en el tablero oponente. Ademas el bolsillo del jugador
    POST: Retorna una tupla con los tableros modificados
    '''
    preguntar_carta = validar_cartas(bolsillo_cartas)
    if(len(bolsillo_cartas)!=0 and preguntar_carta=='si'):
        print('Cartas especiales: Layout--Toti--Fatality')
        print('1.Carta Layout')
        print('2.carta fatality')
        print('3.Carta Toti')
        usar_carta = validar_opcion_cartas()
        if(usar_carta==1):
            tableros = usar_layout(bolsillo_cartas,nombre,mi_tablero,adivinados,tablero_incognito)   
            return tableros
        elif(usar_carta==2):
            tableros = usar_fatality(bolsillo_cartas,nombre,mi_tablero,tablero_incognito)
            return tableros
        elif(usar_carta==3):
            tableros = usar_toti(bolsillo_cartas,nombre,mi_tablero,tablero_incognito)
            return tableros   
    elif(len(bolsillo_cartas)==0 or preguntar_carta=='no'):
        print('No tiene cartas para utilizar')
        tableros = mi_tablero,tablero_incognito
        return tableros

def ejecutar_replay(bolsillo_cartas:list)->bool:
    '''
    PRE: Ingresan como valor el bolsillo del jugador
    POST: Retorna un valor booleano, la cual es el estado del jugador correspondiente
    '''
    if('replay' in bolsillo_cartas):   
        turno_nuevo = input('Desea utilizar carta especial Replay? (si/no): ')
        while not(turno_nuevo.isalpha() and turno_nuevo=='si' or turno_nuevo=='no'): 
            turno_nuevo = input('Ingreso invalido. Vuelva a ingresar su respuesta (si/no): ') 
        if turno_nuevo=='si':
            bolsillo_cartas.remove('replay')
            estado = True   
            return estado
        elif turno_nuevo=='no':
            estado = False
            print('No tiene ninguna carta especial --Replay-- en su bolsillo')  
            return estado  
    else:
        estado = False
        return estado               

def si_adivina(tablero_incognito:list,fila1:int,fila2:int,columna1:int,columna2:int,mi_tablero:list,adivinados:list,dimension:int)->None:
    '''
    PRE: Ingresan como valores las variables los tableros del jugador(list), las coordenadas(int) y la dimension del tablero del juego(int)
    POST: Imprime el tablero del jugador(list)
    '''
    tablero_incognito[fila1][columna1] = mi_tablero[fila1][columna1]
    tablero_incognito[fila2][columna2] = mi_tablero[fila2][columna2]
    adivinados.append(tablero_incognito[fila1][columna1])
    imprimir_matriz(dimension,tablero_incognito)
    
def no_adivina(tablero_incognito:list,fila1:int,fila2:int,columna1:int,columna2:int,mi_tablero:list,dimension:int)->None:    
    '''
    PRE: Ingresan como valores las variables los tableros del jugador(list), las coordenadas(int) y la dimension del tablero del juego(int)
    POST: Imprime el tablero del jugador(list), ademas 'da vuelta' las fichas(valores) del tablero
    '''
    tablero_incognito[fila1][columna1] = mi_tablero[fila1][columna1]
    tablero_incognito[fila2][columna2] = mi_tablero[fila2][columna2]
    imprimir_matriz(dimension,tablero_incognito)
    retroceso1 = ('·') 
    retroceso2 = ('·')
    tablero_incognito[fila1][columna1] = retroceso1
    tablero_incognito[fila2][columna2] = retroceso2

def ganador_coop(puntaje1:int,puntaje2:int,dimension:int,nombre1:str,nombre2:str,score_coop:list)->None: #involucra solo a modo cooperativo
    '''
    PRE: Ingresan como valores las variables nombres de jugadores, la dimension del tablero, puntaje de ambos jugadores y el score
    POST: Imprime el nombre del ganador y lo guarda en el score
    '''
    if(puntaje1==((dimension**2)/2)):
        datos_guardar = [nombre1,puntaje1]
        score_coop.append(datos_guardar)
        print(f'El ganador es {nombre1}')
    elif(puntaje2==((dimension**2)/2)):
        datos_guardar = [nombre2,puntaje2]
        score_coop.append(datos_guardar)
        print(f'El ganador es {nombre2}')    

def jugador(bolsillo_cartas1:list,nombre_b:str,mi_tablero_b:list,tablero_incognito_b:list,adivinados_a:list,dimension:int,tablero_incognito_a:list,mi_tablero_a:list,puntaje:int)->tuple: #Involucra a modo cooperativo
    '''
    PRE: Ingresan todas las variables de ambos jugadores y la dimension del tablero
    POST: Retorna una tupla con el puntaje del jugador, el estado en el que se encontrará y los tableros modificados o no
    '''
    imprimir_matriz(dimension,tablero_incognito_a)
    print('Tus cartas especiales disponibles son: ',bolsillo_cartas1)
    tableros = cartas_especiales(bolsillo_cartas1,nombre_b,mi_tablero_b,tablero_incognito_b,adivinados_a)      
    coordenadas = validar_filas_columnas(dimension,tablero_incognito_a)
    fila1 = coordenadas[0]
    columna1 = coordenadas[1]
    fila2 = coordenadas[2]
    columna2 = coordenadas[3]
    if(mi_tablero_a[fila1][columna1]==mi_tablero_a[fila2][columna2]):
        si_adivina(tablero_incognito_a,fila1,fila2,columna1,columna2,mi_tablero_a,adivinados_a,dimension)
        puntaje += 1
        estado = True
        return puntaje,estado,tableros
    else:  
        no_adivina(tablero_incognito_a,fila1,fila2,columna1,columna2,mi_tablero_a,dimension)      
        estado = False
        estado = ejecutar_replay(bolsillo_cartas1)
        return puntaje,estado,tableros

def jugar_coop(score_coop:list)->None: 
    '''
    PRE: Ingresa una lista, la cual es el score donde se guardara el puntaje y ganador
    POST: ----
    '''
    bolsillo_cartas1 = []
    bolsillo_cartas2 = []
    print('--Ingrese nombre de jugador 1--')
    nombre1 = nombre_jugador()
    print('--Ingrese nombre de jugador 2--')
    nombre2 = nombre_jugador()
    dimension = validar_tablero()
    probabilidades = configurar_probabilidades()
    mi_tablero1 = crear_matriz(dimension) 
    mi_tablero_incognito1 = crear_matriz_incognito(dimension)
    adivinados_jugador1 = []
    mi_tablero2 = crear_matriz(dimension) 
    mi_tablero_incognito2 = crear_matriz_incognito(dimension)
    adivinados_jugador2 = []
    puntaje1 = 0
    puntaje2 = 0
    estado1 = True
    estado2 = True
    while(puntaje1 < ((dimension**2)/2) and puntaje2 < ((dimension**2)/2)):
        if estado1 == True:
            print(mi_tablero_incognito1)
            cartas_probabilidad(nombre1,bolsillo_cartas1,probabilidades)   
            print(f'\n\n\t\t\t\t\tJugador: {nombre1}\n')  
            turno1 = jugador(bolsillo_cartas1,nombre2,mi_tablero2,mi_tablero_incognito2,adivinados_jugador2,dimension,mi_tablero_incognito1,mi_tablero1,puntaje1)
            puntaje1 = turno1[0]
            estado1 = turno1[1]
            if estado1 == False:
                estado2 = True
            mi_tablero2 = turno1[2][0]
            mi_tablero_incognito2 = turno1[2][1]  
        elif estado2 == True:   
            print(mi_tablero_incognito2)
            cartas_probabilidad(nombre2,bolsillo_cartas2,probabilidades)   
            print(f'\n\n\t\t\t\t\tJugador: {nombre2}\n')  
            turno2 = jugador(bolsillo_cartas2,nombre1,mi_tablero1,mi_tablero_incognito1,adivinados_jugador1,dimension,mi_tablero_incognito2,mi_tablero2,puntaje2) 
            puntaje2 = turno2[0]
            estado2 = turno2[1]
            if estado2 == False:
                estado1 = True
            mi_tablero1 = turno2[2][0]
            mi_tablero_incognito1 = turno2[2][1] 
        ganador_coop(puntaje1,puntaje2,dimension,nombre1,nombre2,score_coop)

def jugar_individual(score_individual:list)->None:
    '''
    PRE: Ingresa una lista, la cual es el score donde se guardara el puntaje final
    POST: ----
    '''
    nombre = nombre_jugador()
    intentos = 0
    puntaje = 0
    adivinados = []
    dimension = validar_tablero()
    mi_tablero = crear_matriz(dimension)  #En esta variable guarda la matriz funcional de fichas  
    mi_tablero_incognito = crear_matriz_incognito(dimension) #En esta variable guarda la matriz incognito que el jugador verá en pantalla  
    while(intentos<10 and puntaje<((dimension**2)/2)):
        print('\t\t\t\t\t\t\t\t\t\t\tJugador: {}\n'.format(nombre))
        coordenadas = validar_filas_columnas(dimension,mi_tablero_incognito)
        fila1 = coordenadas[0]
        columna1 = coordenadas[1]
        fila2 = coordenadas[2]
        columna2 = coordenadas[3]
        if(mi_tablero[fila1][columna1]==mi_tablero[fila2][columna2]):
            si_adivina(mi_tablero_incognito,fila1,fila2,columna1,columna2,mi_tablero,adivinados,dimension)
            puntaje += 1
            print(f'\nBien!! Tu puntaje es: {puntaje}')
        else:  
            no_adivina(mi_tablero_incognito,fila1,fila2,columna1,columna2,mi_tablero,dimension)
            intentos += 1
            print('Intento n°',intentos)
        gana_o_pierde(intentos,dimension,mi_tablero,puntaje,nombre,score_individual)

def gana_o_pierde(intentos:int,dimension:int,mi_tablero:list,puntaje:int,nombre:str,score_individual:list)->None: #Involucra solo a modo individual
    '''
    PRE: Ingresan como variables los intentos, tableros, nombres, dimension del tablero, puntaje y el score final
    POST: ----
    '''
    if(intentos==10):
        print('Estuviste cerca. Pero falta ejercitar esa memoria!!')
        imprimir_matriz(dimension,mi_tablero)
        print(f'\nIntentos en total: {intentos}')
    if(puntaje==((dimension**2)/2) or intentos==10):
        datos_guardar = [nombre,puntaje]
        score_individual.append(datos_guardar)

def puntuacion(score_individual:list,score_coop:list)->None:
    '''
    PRE: Ingresa dos listas, la cual son datos de puntuación del jugador y cuantos puntos/partidas ganó
    POST: Retorna el nombre y la puntuacion del jugador
    '''
    print('1.Puntaje individual')
    print('2.Puntaje Vs')
    opcion = input('Ingrese que puntaje desea visualizar 1/2: ')
    while not (opcion.isnumeric() or int(opcion) not in [1,2]):
        opcion = input('Error de ingreso. Ingrese que puntaje desea visualizar 1/2: ')
    opcion = int(opcion)    
    if(opcion==1):
        if(len(score_individual)!=0):
            print('Nombre  Puntaje\n')
            imprimir_puntuacion(score_individual)
        else:
            print('No existen jugadas')     
    elif(opcion==2):
        if(len(score_coop)!=0):
            print('Nombre  Partidas\n')
            imprimir_puntuacion(score_coop)
        else:
            print('No existe jugadas')                   

def salir()->bool:
    '''
    PRO: --
    POST: Retorna un valor booleano condicional. Si se cumple cierta condicion devuelve False, caso contrario, True
    '''
    seguro = input('Seguro que desea salir del juego? SI/NO: ')
    while not(seguro.isalpha() and seguro=='si' or seguro == 'no'):
        seguro = input('Ingrese de nuevo su respuesta (SI/NO): ')
    if(seguro=='si'):    
        return True
    else:
        return False
    
def reglas()->str:
    '''
    PRE: ---
    POST: Retorna una cadena de texto de varias lineas, la cual son las reglas del juego
    '''
    reglas = '''\t\t\t\t\t\t------Reglas del juego------\n\n 
    1. (Un jugador): El juego consiste en adivinar 2(dos) fichas de igual imagen. En caso que adivine podrá seguir jugando, caso contrario perderá una vida. Siendo un máximo de 10 vidas\n 
    2. (jugador vs jugador): En este modo, el jugador 1 empieza y si adivina podrá seguir jugando. Caso contrario sigue el jugador 2. En el juego existen comodines (cartas especiales) que el jugador podra modificar o bien se iniciara el juego con\n\t parametros por defectouna vez iniciado su turno. Primero deberán tirar un dado, la cual indicará si toca o no una carta especial. En caso que le toque, este podra usarlo o bien dejarlo para turnos posteriores.\n
    3. (comodines): Las cartas especiales son Carta Replay (Permite otro intento en caso que falle)//// Carta Layout (Redistribuye las fichas del tablero del oponente de manera aleatoria)
    //// Carta Toti (Espeja el tablero del oponente de forma horizontal o vertical) //// Carta Fatality (Traspone el tablero del oponente)\n
    4. (Duración): El jugador puede elegir de que duración quiere el juego. Un tablero de 4 x 4 // 8 x 8 // 12 x 12\n
    '''
    return reglas

def opciones(score_individual:list,score_coop:list)->None:
    '''
    PRE: Ingresan dos listas, la cual son los score(individual y cooperativo)
    POST: ----
    '''
    cerrado = False
    while not(cerrado):
        print('\n\t\t\t\t---Bienvenido al Memotest2021---')
        print('\t1. Jugar individual')
        print('\t2. Juego jugador1 Vs Jugador2')
        print('\t3. Puntaje')
        print('\t4. Reglas del juego')
        print('\t5. Salir')
        eleccion = validar_opcion()
        if(eleccion==1): 
            jugar_individual(score_individual)
        elif(eleccion==2):
            jugar_coop(score_coop)     
        elif(eleccion==3):
            puntuacion(score_individual,score_coop)
        elif(eleccion==4):
            print(reglas())
        elif(eleccion==5):
            cerrado = salir()

def main()->None:
    score_individual = []
    score_coop = []
    opciones(score_individual,score_coop)

main()    