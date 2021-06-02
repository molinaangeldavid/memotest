import random

LISTA = ['⌚','⌛','⏩','⏪','⏫','⏬','⏭','⏮','⏯','⏰','⏳','⏸','⏹','⏺','◧','◨','◩','◪','☔','☕','♈','♉','♊','♋','♌','♍','♎','♏','♐','♑','♒','♓','⚽','⚾','⚿','⛄','⛅','⛉','⛊','⛋','⛌','⛍','⛔','⛝','⛞','⛟','⛡','⛢','⛣','⛨','⛩','⛪','⛫','⛰','⛱','⛲','⛳','⛴','⛵','⛶','⛷','⛸','⛹','⛺','✅','✆','✇','✈','✉','✊','✋','✌','✍','⨀','⨁','⨂','⨃','⨅','⨆','⨇','⨈','⨉','⨊','⨍','⨎','⨏','✐','✑','✒','✓','✔','✘','✜','✞','✟','❶','❷','❸','❹','❺','❻','❼','❽','❾','❿','➔','➕','➖','➗','➘','⚋','⚌','⚍','⚎','⚏','⚐','⚑','⚒','⚓','⚔','⚕','⚖','⚗','⚘','⚙','⚚','⚛','⚜','⚝','⚞','⚟''℁','ℂ','℃','℄','℆','ℇ','℈','℉','ℊ','ℋ','ℌ','ℍ','ℏ','ℐ','ℑ','ℒ','ℓ','℔','ℕ','№','℗','℘','℞','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','X','Z']

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

def validar_filas_columnas(dimension:int)->int: #Modificar a fila y columna
    '''
    PRE: Ingresa un valor numerico positivo, la cual es la dimension de la matriz a jugar
    POST: Retorna la coordenada de la matriz a adivinar
    '''
    coord = input('\tIngrese la coordenada de la ficha: ')
    while not(coord.isnumeric() and int(coord)<=dimension):
        coord = input('\tCoordenada incorrecta. Ingrese la coordenada de la ficha: ')
    coord = int(coord) 
    coord -= 1
    return coord

def validar_cartas(bolsillo_cartas)->int:
    '''
    PRE: Ingresa la lista del jugador, cuya lista pertenece al bolsillo del jugador 
    POST: Retorna la opcion del jugador si desea utilizar una carta especial
    '''
    preguntar_carta1 = input('Desea utilizar una carta especial de su bolsillo? si/no: ')
    while not (preguntar_carta1.isalpha() and preguntar_carta1=='si' or preguntar_carta1=='no'):
        if(len(bolsillo_cartas)==0):
            print('No tiene cartas disponibles')
        preguntar_carta1 = input('Vuelva a ingresar su respuesta si/no: ')
    return preguntar_carta1    

def crear_matriz_incognito(dimension:int)->list: #modularizar mucho con respecto a la creacion de ?
    '''
    PRE: Ingresa un valor numérico positivo, la cual es la dimensión de una matriz
    POST: Crea una matriz cuadrada con valores de coordenadas de fila y columna
    '''
    matriz_final_inc = []
    lista_incognito = []
    for i in range(dimension):
        lista_incognito = []
        for j in range(dimension):
            lista_incognito.append('?')
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

def imprimir_puntuacion(score)->list:
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
            print(lista[i][j], end='    ')
        print('\n')

def replay(jugador1,jugador2)->list: 
    '''
    PRE: Ingresa dos valores booleanos, la cual es jugador1 y jugador2
    POST: Retorna dos valores booleanos modificados. Basicamente si es el turno del jugador1, este vuelve a jugador y viceversa si es jugador2
    '''
    if(jugador1):
        return jugador1
    elif(jugador2):    
        return jugador2

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
    PRE: Ingresa una lista como variable, la cual es el tablero del jugador
    POST: Retorna la misma lista pero con sus respectivos valores mezclados aleatoriamente
    '''
    for i in matriz:
        random.shuffle(i)
    random.shuffle(matriz)    
    return matriz   
    
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

def cartas_probabilidad(nombre:str,bolsillo_carta:list)->None:
    print(f'Jugador {nombre} ha tirado dado.\n')
    probabilidades = random.randint(0,100)
    if(probabilidades>=0 and probabilidades<=5):
        print('\tTe toco carta FATALITY')
        carta1 = 'fatality'
        bolsillo_carta.append(carta1)
    elif(probabilidades>=6 and probabilidades<=16):
        print('\tTe toco carta REPLAY')
        carta2 = 'replay'
        bolsillo_carta.append(carta2)
    elif(probabilidades>=17 and probabilidades<=30):
        print('\tTe toco carta LAYOUT')
        carta3 = 'layout'
        bolsillo_carta.append(carta3)
    elif(probabilidades>=31 and probabilidades<=40):
        print('\tTe toco carta TOTI')
        carta4 = 'toti'
        bolsillo_carta.append(carta4)
    else:
        print('\tNo te toco nada.')

def usar_cartas(bolsillo_cartas:list,nombre:str,tablero:list)->None:
    '''
    PRE: Ingresa una lista, la cual seria el bolsillo del jugador; un string, la cual es el nombre del jugador; y una lista, la cual es la lista del jugador la cual se aplicará la carta especial
    POST: Imprime a quien afecta la carta comodin. En caso que no haya carta, imprime la inexistencia de la carta en el bolsillo del jugador
    '''
    preguntar_carta1 = validar_cartas(bolsillo_cartas)
    if(len(bolsillo_cartas)!=0 and preguntar_carta1=='si'):
        print('Cartas especiales: Layout--Toti--Fatality')
        print('1.Carta Layout')
        print('2.carta fatality')
        print('3.Carta Toti')
        usar_carta1 = validar_opcion_cartas()
        if(usar_carta1==1):
            if('layout' in bolsillo_cartas):
                print(f'Aplicando LAYOUT al jugador {nombre}...')
                mi_tablero2 = layout(tablero)
                bolsillo_cartas.remove('layout')
            else:
                print('No existe esa carta (layout) en su bolsillo')
        elif(usar_carta1==2):
            if('fatality' in bolsillo_cartas):
                print(f'Aplicando FATALITY al jugador {nombre}...')
                mi_tablero2 = fatality(tablero)
                bolsillo_cartas.remove('fatality')
            else: 
                print('No existe esa carta (fatality) en su bolsillo')  
        elif(usar_carta1==3):
            if('toti' in bolsillo_cartas):
                print(f'Aplicando TOTI al jugador {nombre}...')        
                mi_tablero2 = toti(tablero)
                bolsillo_cartas.remove('toti')
            else:
                print('No existe esa carta (toti) en su bolsillo')
    elif(len(bolsillo_cartas)==0):
        print('No tiene cartas para utilizar')      

def puntuacion(score_individual,score_coop)->None:
    print('1.Puntaje individual')
    print('2.Puntaje Vs')
    opcion = input('Ingrese que puntaje desea visualizar 1/2: ')
    while not (opcion.isnumeric() or int(opcion) not in [1,2]):
        opcion = input('Error de ingreso. Ingrese que puntaje desea visualizar 1/2: ')
    opcion = int(opcion)    
    if(opcion==1):
        if(score_individual!=None):
            print('Nombre  Puntaje\n')
            imprimir_puntuacion(score_individual) 
    elif(opcion==2):
        if(score_coop!=None):
            print('Nombre  Partidas\n')
            imprimir_puntuacion(score_coop)    

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
    
def reglas()->None:
    '''
    PRE: ---
    POST: Retorna una cadena de texto de varias lineas, la cual son las reglas del juego
    '''
    reglas = '''\t\t\t\t\t\t------Reglas del juego------\n\n 
    1. (Un jugador): El juego consiste en adivinar 2(dos) fichas de igual imagen. En caso que adivine podrá seguir jugando, caso contrario perderá una vida. Siendo un máximo de 10 vidas\n 
    2. (jugador vs jugador): En este modo, el jugador 1 empieza y si adivina podrá seguir jugando. Caso contrario sigue el jugador 2. En el juego existen comodines(cartas especiales) que podrán usar los jugadores\n\tuna vez iniciado su turno. Primero deberán tirar un dado, la cual indicará si toca o no una carta especial. En caso que le toque, este podra usarlo o bien dejarlo para turnos posteriores.\n
    3. (comodines): Las cartas especiales son Carta Replay (Permite otro intento en caso que falle)//// Carta Layout (Redistribuye las fichas del tablero del oponente de manera aleatoria)
    //// Carta Toti (Espeja el tablero del oponente de forma horizontal o vertical) //// Carta Fatality (Traspone el tablero del oponente)\n
    4. (Duración): El jugador puede elegir de que duración quiere el juego. Un tablero de 4 x 4 // 8 x 8 // 12 x 12\n
    '''
    print(reglas)

def main()->None:
    score_individual = []
    score_coop = []
    cerrado = False
    while not(cerrado):
        print('\n\t\t\t\t---Bienvenido al Memotest2021---')
        print('\t1. Jugar individual')
        print('\t2. Juego jugador1 Vs Jugador2')
        print('\t3. Puntaje')
        print('\t4. Reglas del juego')
        print('\t5. Salir')
        eleccion = validar_opcion()
        #Aqui empieza la jugabilidad de juego individual
        if(eleccion==1): 
            tablero_incognito = [] 
            intentos = 0
            puntaje = 0
            nombre = nombre_jugador()
            dimension = validar_tablero()
            mi_tablero = crear_matriz(dimension)  #En esta variable guarda la matriz funcional de fichas  
            mi_tablero_incognito = crear_matriz_incognito(dimension) #En esta variable guarda la matriz incognito que el jugador verá en pantalla  
            while(intentos<10 and puntaje<=((dimension**2)/2)):
                print('\t\t\t\t\t\t\t\t\t\t\tJugador: {}\n'.format(nombre))
                print('--Ahora ingrese fila y columna de la ficha 1')
                fila1 = validar_filas_columnas(dimension)
                columna1 = validar_filas_columnas(dimension)
                print('--Ahora ingrese fila y columna de la ficha 2')
                fila2 = validar_filas_columnas(dimension)
                columna2 = validar_filas_columnas(dimension)
                if(mi_tablero[fila1][columna1]==mi_tablero[fila2][columna2]):
                    mi_tablero_incognito[fila1][columna1] = mi_tablero[fila1][columna1]
                    mi_tablero_incognito[fila2][columna2] = mi_tablero[fila2][columna2]
                    tablero_incognito = mi_tablero_incognito
                    imprimir_matriz(dimension,mi_tablero_incognito)
                    puntaje += 1
                    print(f'\nBien!! Tu puntaje es: {puntaje}')
                else:  
                    mi_tablero_incognito[fila1][columna1] = mi_tablero[fila1][columna1]
                    mi_tablero_incognito[fila2][columna2] = mi_tablero[fila2][columna2]
                    imprimir_matriz(dimension,mi_tablero_incognito)
                    retroceso1 = ('?') 
                    retroceso2 = ('?')
                    mi_tablero_incognito[fila1][columna1] = retroceso1
                    mi_tablero_incognito[fila2][columna2] = retroceso2
                    intentos += 1
                    if(intentos==10):
                        print('Estuviste cerca. Pero falta ejercitar esa memoria!!')
                        imprimir_matriz(dimension,mi_tablero)
                    print(f'\nIntentos en total: {intentos}')
                if(intentos==10 or puntaje==dimension*2):
                    puntaje_final = [nombre,puntaje]
                    score_individual.append(puntaje_final)
        #Aqui empieza la jugabilidad de jugador1 vs jugador2
        elif(eleccion==2): 
            bolsillo_cartas1 = []
            bolsillo_cartas2 = []
            tablero_incognito1 = []
            tablero_incognito2 = []
            print('--Ingrese nombre de jugador 1--')
            nombre1 = nombre_jugador()
            print('--Ingrese nombre de jugador 2--')
            nombre2 = nombre_jugador()
            dimension = validar_tablero()
            mi_tablero1 = crear_matriz(dimension) 
            mi_tablero_incognito1 = crear_matriz_incognito(dimension)
            mi_tablero2 = crear_matriz(dimension) 
            mi_tablero_incognito2 = crear_matriz_incognito(dimension)
            puntaje1 = 0
            puntaje2 = 0
            jugador1 = True
            jugador2 = True
            juego = 0
            while(puntaje1 < ((dimension**2)/2) and puntaje2 < ((dimension**2)/2)):
                while(jugador1 == True):
                    cartas_probabilidad(nombre1,bolsillo_cartas1)   
                    print('\t\t\t\t\tJugador: {}\n'.format(nombre1))
                    usar_cartas(bolsillo_cartas1,nombre1,mi_tablero1)              
                    print('--Ahora ingrese fila y columna de la ficha 1')
                    fila1 = validar_filas_columnas(dimension)
                    columna1 = validar_filas_columnas(dimension)
                    print('--Ahora ingrese fila y columna de la ficha 2')
                    fila2 = validar_filas_columnas(dimension)
                    columna2 = validar_filas_columnas(dimension)
                    if(mi_tablero1[fila1][columna1]==mi_tablero1[fila2][columna2]):
                        mi_tablero_incognito1[fila1][columna1] = mi_tablero1[fila1][columna1]
                        mi_tablero_incognito1[fila2][columna2] = mi_tablero1[fila2][columna2]
                        tablero_incognito1 = mi_tablero_incognito1
                        imprimir_matriz(dimension,mi_tablero_incognito1)  
                        puntaje1 += 1
                    else:  
                        mi_tablero_incognito1[fila1][columna1] = mi_tablero1[fila1][columna1]
                        mi_tablero_incognito1[fila2][columna2] = mi_tablero1[fila2][columna2]
                        imprimir_matriz(dimension,mi_tablero_incognito1)  
                        retroceso1 = ('?') 
                        retroceso2 = ('?')
                        mi_tablero_incognito1[fila1][columna1] = retroceso1
                        mi_tablero_incognito1[fila2][columna2] = retroceso2
                        jugador1 = False
                        jugador2 = True
                        if('replay' in bolsillo_cartas1):   
                            turno_nuevo1 = input('Desea utilizar carta especial Replay? si/no: ')
                            while not(turno_nuevo1.isalpha() and turno_nuevo1=='si' or turno_nuevo1=='no'): 
                                turno_nuevo1 = input('Ingreso invalido. Vuelva a ingresar su respuesta si/no ') 
                            if(turno_nuevo1=='si'):
                                jugador1 = replay(jugador1,jugador2)
                                bolsillo_cartas1.remove('replay')
                        else:
                            print('No tiene ninguna carta especial --Replay-- en su bolsillo')    
                    if(puntaje1==((dimension**2)/2)):
                        juego += 1
                        datos_guardar = [f'{nombre1}',juego]
                        score_coop.append(datos_guardar)
                        jugador1=False
                        jugador2=False          
                        print(f'El ganador es {nombre1}')  
                while(jugador2 == True):
                    cartas_probabilidad(nombre2,bolsillo_cartas2)        
                    print('\t\t\t\t\tJugador: {}\n'.format(nombre2))
                    usar_cartas(bolsillo_cartas2,nombre2,mi_tablero2)     
                    print('--Ahora ingrese fila y columna de la ficha 1')
                    fila1 = validar_filas_columnas(dimension)
                    columna1 = validar_filas_columnas(dimension)
                    print('--Ahora ingrese fila y columna de la ficha 2')
                    fila2 = validar_filas_columnas(dimension)
                    columna2 = validar_filas_columnas(dimension)
                    if(mi_tablero2[fila1][columna1]==mi_tablero2[fila2][columna2]):
                        mi_tablero_incognito2[fila1][columna1] = mi_tablero2[fila1][columna1]
                        mi_tablero_incognito2[fila2][columna2] = mi_tablero2[fila2][columna2]
                        tablero_incognito2 = mi_tablero_incognito2
                        imprimir_matriz(dimension,mi_tablero_incognito2)      
                        puntaje2 += 1
                    else:  
                        mi_tablero_incognito2[fila1][columna1] = mi_tablero2[fila1][columna1]
                        mi_tablero_incognito2[fila2][columna2] = mi_tablero2[fila2][columna2]
                        imprimir_matriz(dimension,mi_tablero_incognito2)  
                        retroceso1 = ('?') 
                        retroceso2 = ('?')
                        mi_tablero_incognito2[fila1][columna1] = retroceso1
                        mi_tablero_incognito2[fila2][columna2] = retroceso2
                        jugador2 = False
                        jugador1 = True
                        if('replay' in bolsillo_cartas2):
                            turno_nuevo2 = input('Desea utilizar carta especial Replay? si/no: ')
                            while not(turno_nuevo2.isalpha() and turno_nuevo2=='si' or turno_nuevo2=='no'): 
                                turno_nuevo2 = input('Ingreso invalido. Vuelva a ingresar su respuesta si/no ')    
                            if(turno_nuevo2=='si'):
                                jugador2 = replay(jugador1,jugador2)
                                bolsillo_cartas2.remove('replay')
                        else:
                            print('No tiene ninguna carta especial --Replay-- en su bolsillo')    
                    if(puntaje2==((dimension**2)/2)):
                        juego += 1
                        datos_guardar = [f'{nombre2}',juego]
                        score_coop.append(datos_guardar)    
                        jugador1=False
                        jugador2=False
                        print(f'El ganador es {nombre2}')     
        elif(eleccion==3):
            puntuacion(score_individual,score_coop)
        elif(eleccion==4):
            reglas()
        elif(eleccion==5):
            cerrado = salir()
main()    

