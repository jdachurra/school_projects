"""
autor: Jose Daniel Achurra Santos
fecha: 24/Octubre/2021
version 9.0



Descripcion:
Este proyecto está dedicado a los estudiantes de 3° ESO que van a realizar su prueba PISA,
el programa los ayudará a practicar  mediante problemas totalmente o parcialmente randomizados (depende del estudiante que creo la funcion) y prepararse mejor para 3 secciones del álgebra:
Productos Notables.
Ecuaciones Cuadraticas.
Factorización.

En el proyecto incorporamos varias funciones o "features" que le brindan más vida y dinamismo al programa, como:
- Una función para implementar colores de forma fácil
- Funciones para randomizar como randint_sano(), coin_toss(), o triple_toss()
- Una pantallita "impr_pant()" en la terminal basado en prints, y funciones para facilitar la edicion en esa pantalla, como
  funciones de alineacion de texto o funciones para limpiar el texto almacenado. Ademas, el tamanio de la pantalla es actualizable en la configuracion del mismo programa (Hecho por Jose Achurra).
- Una funcion limpiar_IDE(), la cual fue la única que hicimos enteramente con ayuda de internet, 
  la cual limpia la terminal para que no quede todo feo cada vez que muestra la pantallita.


Entrada:
- Únicamente números del 1 al 9 correspondientes a las opciones mostradas en pantalla
- Para escoger su opción, teclee un numero en la terminal y presione ENTER, si el numero ingresado no correcsponde
  a ninguna de las opciones, no pasará nada, y puede volver a introducir otro número
- Dentro de los ejercicios matematicos, es posible salir al menú o saltar al siguiente ejercicio con las teclas [8] y [9] respectivamente


Proceso de datos:
- Impresion en la terminal: Cada vez que queremos actualizar la pantalla mostrada, guardamos todas los strings que queremos mostrar, dentro de la lista linea[]
  A la hora de actualizar la terminar con impr_pant(), linea_raw[] entra en acción, almacenando de forma temporal los strings
  tal cual como se deben mostrar en la terminal, y se cuentan cuantos caracteres hay en total para posteriormente aniadir espaios en blanco
  dependiendo de la alineación que le toca a cada linea segun la lista diccionario_alineaciones[]
- Flujo del programa: Para poder hacer un programa infinito que regresara al menu como punto de partida, creamos un loop while infiito,
  y asignamos a cada menu un valor numerico, que funciona como llaves (valor numerico), a las puertas (menús), en el camino (loop infinito),
  cuestion de que cada vez que queremos cambiar de menu, lo unico que debemos hacer es actualizar el valor antes de regresar al inicio del loop infinito.
- Funciones matematicas PISA: Asi como hay varios casos de factorizacion, para crear las funciones "randomizadas" incorporamos choice() de la libreria random, para que sea al azar
  la seleccion del caso correspondiente. Ademas de randint() y otras funciones para randomizar las letras y los numeros, y que cada vez que se ejecute el programa, la experiencia
  sea unica y diferente. Así mismo como guardamos la respuesta correcta en una variable, guardamos las respuestas incorrectas parcialmente randomizadas en otra lista, y cada
  vez que se genera una nueva iteracion de la funcion, las preguntas, respuestas correctas y respuestas incorrectas son diferentes. (Disclaimer: El grado de "azar" implementado en cada
  funcion PISA, depende totalmente de cada miembro del equipo, porque creamos nuestras funciones casi que por separado)

Salida:
- Vista de la pantalla: En la terminal siempre se mostrará un cuadrado representando una pantallita, dentro de la cual se verán los mensajes y opciones a escoger
- Correctas e incorrectas: El conteo de respuestas correctas e incorrectas se guarda de manera global, y se muestra unicamente al ingresar a los ejercicios matematicos PISA
  Ademas podras ver la respuesta correcta e incorrecta de cada ejercicio al finalizar cada uno de estos, incluso si decides saltar el ejercicio

Caso de prueba:
+————————————————————————————————————+
|           Menu Principal           |
|                                    |
|         Ingrese un numero          |
|                                    |
| 1 ➞  Configuracion                |
| 2 ➞  PISA Factorizacion           |
| 3 ➞  PISA Ecuaciones cuadraticas  |
| 4 ➞  PISA 3                       |
+————————————————————————————————————+
|                                    |
+————————————————————————————————————+
>>> 9     *no pasa nada*
>>> 2     *se imprime la siguiente pantalla*

+————————————————————————————————————+
|           ✓ = 0    x = 0           |
|         (11q - 5h)³   = ?          |
|                                    |
|[1]: (9q² - 220qh + 7h²)            |
|[2]: (8q² - 9h²)                    |
|[3]: (8q³ - 1815q²h + 825qh² - 6h³) |
|[4]: (9q² + 55qh + 7h²)             |
| [8]: Salir al menu    [9]: Saltar  |
+————————————————————————————————————+
|                                    |
+————————————————————————————————————+
>>> 8   *sale al menu*

+————————————————————————————————————+
|           Menu Principal           |
|                                    |
|         Ingrese un numero          |
|                                    |
| 1 ➞  Configuracion                |
| 2 ➞  PISA Factorizacion           |
| 3 ➞  PISA Ecuaciones cuadraticas  |
| 4 ➞  PISA 3                       |
+————————————————————————————————————+
|                                    |
+————————————————————————————————————+
>>> 1

+————————————————————————————————————+
|                                    |
| Ingrese el ancho (36 min, 50 max)  |
|                                    |
|      Ancho predeterminado: 36      |
|          Ancho actual: 36          |
|                                    |
|                                    |
|                                    |
+————————————————————————————————————+
|                                    |
+————————————————————————————————————+
>>> pikachu     *no pasa nada*
>>> 40

+————————————————————————————————————————+
|                                        |
|    Ingrese el alto (8 min, 14 max)     |
|                                        |
|         Alto predeterminado: 8         |
|             Alto actual: 8             |
|                                        |
|                                        |
|                                        |
+————————————————————————————————————————+
|                                        |
+————————————————————————————————————————+
>>> 13

+————————————————————————————————————————+
|             Configuracion              |
|                                        |
|           Ingrese un numero            |
|                                        |
| 1 ➞  Tamaño de Pantalla               |
| 2 ➞  Creditos                         |
| 3 ➞  Regresar al menu                 |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
+————————————————————————————————————————+
|                                        |
+————————————————————————————————————————+

*fin del caso de prueba*
Atte: Para cualquier otra entrada que no sea uno de los numeros que no esta en la pantalla, no pasará nada,
      por lo que no hay muchos "casos límite"
"""


#Proyecto Final

from os import system, name #para la funcion limpiar_ide()
from time import sleep #para que pase un tiempo luego de que se muestre la respuesta correcta
from string import ascii_lowercase as letrasrandom #para randomizar las letras en los problemas matematicos
from random import choice, randint #tambien para randomizar las opciones que escoje en las funciones PISA

paso_la_sanidad = True #Tiene que ser True para salir del ciclo infinito

ancho_de_pantalla = 36
alto_de_pantalla = 8

linea = ["", "", "", "", "", "", "", ""]
linea_raw = ["", "", "", "", "", "", "", ""]
diccionario_alineaciones = ["center", "center", "center", "center", "center", "center", "center", "center"]
diccionario_color_n = [0, 0, 0, 0, 0, 0, 0, 0]

estado_del_programa = 1
correctas = 0
incorrectas = 0


"""--------------------------------------linea-separadora----------------------------------------"""
#Funciones invisibles o "features"

def randint_sano(numero_que_no_quiero): #genera un numero random del 1 al 12, exceptuando el numero que ingreses
    numero_random = numero_que_no_quiero
    while numero_random == numero_que_no_quiero:
        numero_random = randint(1, 12)
        
    return(numero_random)

def coin_toss(): #Cara o sello, devuelve True o False al azar
    posibilidad = [True, False]
    resultado = choice(posibilidad)
    return(resultado)

def triple_toss(): #Lo mismo pero con 3 numeros
    posibilidad = [1, 2, 3]
    resultado = choice(posibilidad)
    return(resultado)

def limpiar_IDE(): # Unica funcion sacada de google, https://www.geeksforgeeks.org/clear-screen-python/

    if name == 'nt': #para windows
        _ = system('cls')
    else: #para mac y linux
        _ = system('clear')
#Esta funcion se ejecuta automaticamente cuando ponen impr_pant(), lo que hace es limpiar la Terminal

def colores(texto, linea_del_texto, color = 0, fondo = 0, estilo_1 = 0, estilo_2 = 0, misma_linea = False):
    global diccionario_color_n
    
    lista_codigos_estilos = [0, 1, 3, 5]
    lista_estilos = ["normal", "bright", "italica_oscuro", "oscuro"]
    lista_codigos_colores = [30, 31, 32, 33, 34, 35, 36, 37]
    lista_colores = ["negro", "rojo", "verde", "amarillo", "azul", "morado", "cian", "blanco"]
    lista_codigos_fondos = [40, 41, 42, 43, 44, 45, 46, 47]
    lista_fondos = ["negro", "rojo", "verde", "amarillo", "azul", "morado", "cian", "blanco"]
    
    texto_modificado = "\033["
    
    if estilo_1 != 0:
        texto_modificado += str(lista_codigos_estilos[lista_estilos.index(estilo_1)])
    else:
        texto_modificado += "0"
    if estilo_2 != 0:
        texto_modificado += ";"
        texto_modificado += str(lista_codigos_estilos[lista_estilos.index(estilo_2)])
    if color != 0:
        texto_modificado += ";"
        texto_modificado += str(lista_codigos_colores[lista_colores.index(color)])
    if fondo != 0:
        texto_modificado += ";"
        texto_modificado += str(lista_codigos_fondos[lista_fondos.index(fondo)])
        
    texto_modificado = texto_modificado + "m" + str(texto) + "\033[0m" 
    
    if misma_linea:
        diccionario_color_n[linea_del_texto] += len(texto_modificado) - len(texto)
    else:
        diccionario_color_n[linea_del_texto] = len(texto_modificado) - len(texto)

    return (texto_modificado) 
#Si van a poner dos textos con colores en una misma linea, tienen que ponerle misma_linea = True al segundo texto

def alinear(n_linea, alineacion): #modifica la alineacion respectiva en las listas
    #entrada: string, string.
    if alineacion == "center":
        diccionario_alineaciones[n_linea] = "center"
    elif alineacion == "right":
        diccionario_alineaciones[n_linea] = "right"
    elif alineacion == "left":
        diccionario_alineaciones[n_linea] = "left"

def alinear_todos(alineacion): #alinea todas las lineas al mismo tiempo pero con una sola alineacion
    #entrada: string
    global diccionario_alineaciones

    if alineacion == "center":
        diccionario_alineaciones = []
        for contador in range(alto_de_pantalla):
            diccionario_alineaciones.append("center")

    elif alineacion == "right":
        diccionario_alineaciones = []
        for contador in range(alto_de_pantalla):
            diccionario_alineaciones.append("right")

    elif alineacion == "left":
        diccionario_alineaciones = []
        for contador in range(alto_de_pantalla):
            diccionario_alineaciones.append("left")

def limpiar_pantalla(): #limpia todas las lineas de linea[]
    global linea
    global diccionario_color_n
    linea = []
    diccionario_color_n = []
    for contador in range(alto_de_pantalla):
        linea.append("")
        diccionario_color_n.append(0)

def impr_pant(): #imprime la pantalla
    global alto_de_pantalla
    global ancho_de_pantalla
    global diccionario_color_n
    global linea_raw
    global linea
    global diccionario_alineaciones
    global diccionario_color_n
     
    for n_linea in range(alto_de_pantalla):
        
        if diccionario_alineaciones[n_linea] == "center":
            if ( len(linea[n_linea]) - diccionario_color_n[n_linea] + ancho_de_pantalla ) % 2 == 0:
                linea_raw[n_linea] = (" " * int( (ancho_de_pantalla - len(linea[n_linea]) + diccionario_color_n[n_linea]) /2) ) + linea[n_linea] + (" " * int((ancho_de_pantalla - len(linea[n_linea]) + diccionario_color_n[n_linea])/2) )
            else:
                linea_raw[n_linea] = (" " * int( (ancho_de_pantalla - len(linea[n_linea]) + diccionario_color_n[n_linea] - 1) /2) ) + linea[n_linea] + (" " * int( (ancho_de_pantalla - len(linea[n_linea]) + diccionario_color_n[n_linea] + 1) /2) )
        elif diccionario_alineaciones[n_linea] == "right":
            linea_raw[n_linea] = (" " * (ancho_de_pantalla - len(linea[n_linea]) + diccionario_color_n[n_linea]))  + linea[n_linea]
        elif diccionario_alineaciones[n_linea] == "left":
            linea_raw[n_linea] = linea[n_linea] + (" " * (ancho_de_pantalla - len(linea[n_linea]) + diccionario_color_n[n_linea])) 

    limpiar_IDE()

    print    ("+" +    ("—"*ancho_de_pantalla)      + "+")  
    for n_linea in range(alto_de_pantalla):
        print("|" + linea_raw[n_linea] + "|")

    print    ("+" +    ("—"*ancho_de_pantalla)      + "+")
    print    ("|" +    (" "*ancho_de_pantalla)      + "|")
    print    ("+" +    ("—"*ancho_de_pantalla)      + "+")  

"""-------------------------------------linea-separadora-------------------------------------"""
#Funciones visibles

def menu():
    global estado_del_programa
    global paso_la_sanidad
    espaciador = 0
    limpiar_pantalla()
    alinear_todos("center")
    
    linea[espaciador + 0] = "Menu Principal"
    
    linea[espaciador + 2] = "Ingrese un numero"
    
    linea[espaciador + 4] = colores(" 1", (espaciador + 4), color = "azul", estilo_1 = "bright") + " ➞  Configuracion"
    linea[espaciador + 5] = colores(" 2", (espaciador + 5), color = "azul", estilo_1 = "bright") + " ➞  PISA Productos Notables"
    linea[espaciador + 6] = colores(" 3", (espaciador + 6), color = "azul", estilo_1 = "bright") + " ➞  PISA Ecuaciones cuadraticas"
    linea[espaciador + 7] = colores(" 4", (espaciador + 7), color = "azul", estilo_1 = "bright") + " ➞  PISA Factorizacion"
    
    alinear((espaciador + 4), "left")
    alinear((espaciador + 5), "left")
    alinear((espaciador + 6), "left")
    alinear((espaciador + 7), "left")
    
    impr_pant()
    
    while True: #Sanidad
        try:
            entrada = int(input())
            if entrada == 1 or entrada == 2 or entrada == 3 or entrada == 4:
                paso_la_sanidad = True
            else:
                paso_la_sanidad = False
        except:
            paso_la_sanidad = False
            
        if paso_la_sanidad == True:
            break
        
    if entrada == 1: #Configuracion
        limpiar_pantalla()
        estado_del_programa = 2
    elif entrada == 2: #Productos Notables
        limpiar_pantalla()
        estado_del_programa = 3
    elif entrada == 3: #Ecuaciones cuadraticas
        limpiar_pantalla()
        estado_del_programa = 4
    elif entrada == 4: #Factorizacion
        limpiar_pantalla()
        estado_del_programa = 5

def configuracion():
    global linea
    global estado_del_programa
    global ancho_de_pantalla
    global alto_de_pantalla
    global linea_raw
    global diccionario_alineaciones
    global diccionario_color_n
    global paso_la_sanidad
    espaciador = 0
    limpiar_pantalla()
    alinear_todos("center")
    
    linea[espaciador + 0] = "Configuracion"
    
    linea[espaciador + 2] = "Ingrese un numero"
    
    linea[espaciador + 4] = colores(" 1", (espaciador + 4), color = "rojo", estilo_1 = "bright") + " ➞  Tamaño de Pantalla"
    linea[espaciador + 5] = colores(" 2", (espaciador + 5), color = "rojo", estilo_1 = "bright") + " ➞  Creditos"
    linea[espaciador + 6] = colores(" 3", (espaciador + 6), color = "rojo", estilo_1 = "bright") + " ➞  Regresar al menu"
    
    alinear((espaciador + 4), "left")
    alinear((espaciador + 5), "left")
    alinear((espaciador + 6), "left")
    
    impr_pant()
    
    while True: #Sanidad
        try:
            entrada = int(input())
            if entrada == 1 or entrada == 2 or entrada == 3:
                paso_la_sanidad = True
            else:
                paso_la_sanidad = False
        except:
            paso_la_sanidad = False
            
        if paso_la_sanidad == True:
            break
    
    if entrada == 1: #submenu de tamanio
        limpiar_pantalla()
        alinear_todos("center")
        linea[1] = "Ingrese el ancho (36 min, 50 max)"
        linea[3] = colores("Ancho predeterminado: 36", 3, color = "cian", estilo_1 = "italica_oscuro")
        linea[4] = colores("Ancho actual: ", 4, color = "cian", estilo_1 = "italica_oscuro") + colores(str(ancho_de_pantalla), 4, color = "cian", estilo_1 = "italica_oscuro", misma_linea = True) 
        
        impr_pant()
        
        while True:
            try:
                entrada = int(input())
                if entrada >= 36 and entrada <= 50:
                    paso_la_sanidad = True
                else:
                    paso_la_sanidad = False
            except:
                paso_la_sanidad = False
            
            if paso_la_sanidad == True:
                break
        
        ancho_de_pantalla = entrada
        
        linea[1] = "Ingrese el alto (8 min, 14 max)"
        linea[3] = colores("Alto predeterminado: 8", 3, color = "cian", estilo_1 = "italica_oscuro")
        linea[4] = colores("Alto actual: ", 4, color = "cian", estilo_1 = "italica_oscuro") + colores(str(alto_de_pantalla), 4, color = "cian", estilo_1 = "italica_oscuro", misma_linea = True) 
        
        impr_pant()
        
        while True:
            try:
                entrada = int(input())
                if entrada >= 8 and entrada <= 14:
                    paso_la_sanidad = True
                else:
                    paso_la_sanidad = False
            except:
                paso_la_sanidad = False
            
            if paso_la_sanidad == True:
                break
        
        if alto_de_pantalla >= entrada:
            for contador in range(alto_de_pantalla - entrada):
                linea.pop(-1)
                linea_raw.pop(-1)
                diccionario_alineaciones.pop(-1)
                diccionario_color_n.pop(-1)
        else:
            for contador in range(entrada - alto_de_pantalla):
                linea.append("")
                linea_raw.append("")
                diccionario_alineaciones.append("center")
                diccionario_color_n.append(0)
        
        alto_de_pantalla = entrada
            
    elif entrada == 2: #submenu de creditos
        ancho_de_pantalla_temporal = ancho_de_pantalla
        ancho_de_pantalla = 55
        limpiar_pantalla()
        alinear_todos("center")
        linea[1] = "Creditos"
        linea[3] = colores(" Jose Achurra", (3), color = "morado", estilo_1 = "bright") + " ➞  Encabezado, Menu, Config, P_notable"
        linea[4] = colores(" Angel Vargas", (4), color = "morado", estilo_1 = "bright") + " ➞  Encabezado, Colores, EQ_cuadraticas"
        linea[5] = colores(" Alfonso Gracian", (5), color = "morado", estilo_1 = "bright") + " ➞ Factorizacion"
        linea[7] = "[8]: Regresar a configuracion"
        alinear(3, "left")
        alinear(4, "left")
        alinear(5, "left")
        
        impr_pant()
    
        while True: #Sanidad
            try:
                entrada = int(input())
                if entrada == 8:
                    paso_la_sanidad = True
                else:
                    paso_la_sanidad = False
            except:
                paso_la_sanidad = False
            
            if paso_la_sanidad == True:
                break
        ancho_de_pantalla = ancho_de_pantalla_temporal
        
    elif entrada == 3: #regresa al menu principal
        limpiar_pantalla()
        estado_del_programa = 1

def p_notable_PISA():
    
    global estado_del_programa 
    global paso_la_sanidad
    global ancho_de_pantalla 
    global alto_de_pantalla
    global linea
    global linea_raw
    global diccionario_alineaciones 
    global diccionario_color_n
    global correctas
    global incorrectas
    
    a_1 = randint(1, 12)
    x_1 = choice(letrasrandom)
    b_1 = randint(1, 12)
    y_1 = choice(letrasrandom)

    a_1_str = str(a_1)
    b_1_str = str(b_1)
    
    #Sanidad
    if a_1 == 1: #Si el numero es 1, en el texto no aparecera
        a_1_str = ""
        a_1_2_str = ""
        a_1_3_str = ""
    else:
        a_1_str = str(a_1)
        a_1_2_str = str(a_1^2)
        a_1_3_str = str(a_1^3)
    if b_1 == 1: #Si el numero es 1, en el texto no aparecera
        b_1_str = ""
        b_1_2_str = ""
        b_1_3_str = ""
    else:
        b_1_str = str(b_1)
        b_1_2_str = str(b_1^2)
        b_1_3_str = str(b_1^3)

    while y_1 == x_1: #las letras no pueden ser iguales
        y_1 = choice(letrasrandom)
    
    
    posibilidad_3 = [1, 2, 3]
    resultado_3 = choice(posibilidad_3)
    
    respuesta_incorrecta_1 = ("(" + a_1_2_str + x_1 + "²" + " + " + b_1_2_str + y_1  + "²" + ")") #a2x2+b2y2
    respuesta_incorrecta_2 = ("(" + a_1_str + x_1 + "²" + " - " + b_1_str + y_1  + "²" + ")") #ax2-by2
    respuesta_incorrecta_3 = ("(" + a_1_2_str + x_1 + " - " + b_1_2_str + y_1  + ")") #a2x-b2x
    
    respuesta_incorrecta_4 = ("(" + str(randint_sano(a_1)^2) + x_1 + "²" + " + " + str(randint_sano(b_1)^2) + y_1  + "²" + ")") #lo mismo pero randint()
    respuesta_incorrecta_5 = ("(" + str(randint_sano(b_1)) + x_1 + "²" + " - " + str(randint_sano(b_1)) + y_1  + "²" + ")")
    respuesta_incorrecta_6 = ("(" + str(randint_sano(a_1)^2) + x_1 + " - " + str(randint_sano(b_1)^2) + y_1  + ")")
    
    respuesta_incorrecta_7 = ("(" + str(randint_sano(a_1)^2) + x_1 + "²" + " - " + str(randint_sano(b_1)^2) + y_1  + "²" + ")")
    
    respuesta_incorrecta_8 = ("(" + a_1_2_str + x_1 + "²" +    " + " +   str(a_1*b_1) + x_1 + y_1     +    " + " + b_1_2_str + y_1  + "²" + ")")
    respuesta_incorrecta_9 = ("(" + a_1_2_str + x_1  +   " - " + str(2*a_1*b_1) + x_1 + y_1     +  " + " + b_1_2_str + y_1  + ")")
    respuesta_incorrecta_10 = ("(" + str(randint_sano(a_1)^2) + x_1 + "²" +    " + " +   str(a_1*b_1) + x_1 + y_1     +    " + " + str(randint_sano(b_1)^2) + y_1  + "²" + ")")
    
    respuesta_incorrecta_11 = ("(" + a_1_2_str + x_1 + "²" +    " - " + str(4*a_1*b_1) + x_1 + y_1     +  " + " + b_1_2_str + y_1  + "²" + ")")
    respuesta_incorrecta_12 = ( "(" + str(randint_sano(a_1)^3) + x_1 + "³" +     " + " + str(6*a_1*b_1*b_1) + x_1 + "²" + y_1   +       " + " + str(a_1*b_1*b_1) + x_1 + y_1 + "²"   + " + "  + b_1_3_str + y_1 + "³" + ")"  )
    respuesta_incorrecta_13 = ( "(" + a_1_3_str + x_1 + "³" +     " - " + str(3*a_1*randint_sano(a_1) *b_1) + x_1 + "²" + y_1   +       " + " + str(4*a_1*b_1*b_1) + x_1 + y_1 + "²"   + " - "  + b_1_3_str + y_1 + "³" + ")" )
    
    
    lista_de_respuestas_incorrectas = [respuesta_incorrecta_1, respuesta_incorrecta_2, respuesta_incorrecta_3, respuesta_incorrecta_4, respuesta_incorrecta_5, respuesta_incorrecta_6, respuesta_incorrecta_7, respuesta_incorrecta_8, respuesta_incorrecta_9, respuesta_incorrecta_10, respuesta_incorrecta_11, respuesta_incorrecta_12, respuesta_incorrecta_13]
    
    if resultado_3 == 1: #ejemplo: (8a + 9b) (5a - 7b)
        texto_de_operacion = ("(" + a_1_str + x_1 + " + " + b_1_str + y_1 + ") (" + a_1_str + x_1 + " - " + b_1_str + y_1 + ") = ?")
        respuesta_correcta = ("(" + a_1_2_str + x_1 + "²" + " - " + b_1_2_str + y_1  + "²" + ")")
    elif resultado_3 == 2: #(a+b) al cuadrado

        if coin_toss():  
            texto_de_operacion = ("(" + a_1_str + x_1 + " + " + b_1_str + y_1 + ")²   = ?")
            respuesta_correcta = ("(" + a_1_2_str + x_1 + "²" +    " + " +   str(2*a_1*b_1) + x_1 + y_1     +    " + " + b_1_2_str + y_1  + "²" + ")")
        else:
            texto_de_operacion = ("(" + a_1_str + x_1     + " - " + b_1_str + y_1 + ")²   = ?")
            respuesta_correcta = ("(" + a_1_2_str + x_1 + "²" +    " - " + str(2*a_1*b_1) + x_1 + y_1     +  " + " + b_1_2_str + y_1  + "²" + ")")
        
    else: #(a+b) al cubo
        if coin_toss():  
            texto_de_operacion = ("(" + a_1_str + x_1 +    " + " + b_1_str + y_1 + ")³   = ?")
            respuesta_correcta = ( "(" + a_1_3_str + x_1 + "³" +     " + " + str(3*a_1*a_1*b_1) + x_1 + "²" + y_1   +       " + " + str(3*a_1*b_1*b_1) + x_1 + y_1 + "²"   + " + "  + b_1_3_str + y_1 + "³" + ")"  )
        else:
            texto_de_operacion = ("(" + a_1_str + x_1 +    " - " + b_1_str + y_1 + ")³   = ?")
            respuesta_correcta = ( "(" + a_1_3_str + x_1 + "³" +     " - " + str(3*a_1*a_1*b_1) + x_1 + "²" + y_1   +       " + " + str(3*a_1*b_1*b_1) + x_1 + y_1 + "²"   + " - "  + b_1_3_str + y_1 + "³" + ")" )
    
    limpiar_pantalla()
    alinear_todos("center")
    
    linea[0] = colores( ("✓ = " + str(correctas) + "    " ), 0, "verde", estilo_1 = "bright") + colores ( ("x = " + str(incorrectas)) , 0, "rojo", estilo_1 = "bright", misma_linea = True)
    linea [1] = texto_de_operacion
    linea[7] = "[8]: Salir al menu    [9]: Saltar"
    
    posibilidad_4 = [1, 2, 3, 4]
    resultado_4 = choice(posibilidad_4)
    
    alinear(3, "left")
    alinear(4, "left")
    alinear(5, "left")
    alinear(6, "left")
    
    while linea[3][3:] == linea[4][3:] or linea[3][3:] == linea[5][3:] or linea[3][3:] == linea[6][3:] or linea[4][3:] == linea[5][3:] or linea[4][3:] == linea[6][3:] or linea[5][3:] == linea[6][3:]: #las opciones no pueden ser iguales
        if resultado_4 == 1:
            linea[3] = "[1]: " + respuesta_correcta
        else:
            linea[3] = "[1]: " + choice(lista_de_respuestas_incorrectas)
    
        if resultado_4 == 2:
            linea[4] = "[2]: " + respuesta_correcta
        else:
            linea[4] = "[2]: " + choice(lista_de_respuestas_incorrectas)
        
        if resultado_4 == 3:
            linea[5] = "[3]: " + respuesta_correcta
        else:
            linea[5] = "[3]: " + choice(lista_de_respuestas_incorrectas)
    
        if resultado_4 == 4:
            linea[6] = "[4]: " + respuesta_correcta
        else:
            linea[6] = "[4]: " + choice(lista_de_respuestas_incorrectas)
        
    impr_pant()
    
    while True: #Sanidad
        try:
            entrada = int(input())
            if entrada == 1 or entrada == 2 or entrada == 3 or entrada == 4 or entrada == 8 or entrada == 9:
                paso_la_sanidad = True
            else:
                paso_la_sanidad = False
        except:
            paso_la_sanidad = False
            
        if paso_la_sanidad == True:
            break
        
    if entrada == resultado_4:
        correctas += 1
        linea[resultado_4 + 2] = colores(linea[resultado_4 + 2], (resultado_4 + 2), "verde", estilo_1 = "bright")
        impr_pant()
        sleep(3)
    elif entrada == 8:
        estado_del_programa = 1
    elif entrada == 9:
        incorrectas += 1
        linea[resultado_4 + 2] = colores(linea[resultado_4 + 2], (resultado_4 + 2), "cian", estilo_1 = "bright")
        impr_pant()
        sleep(3)
    else:
        incorrectas += 1
        linea[resultado_4 + 2] = colores(linea[resultado_4 + 2], (resultado_4 + 2), "verde")
        linea[entrada + 2] = colores(linea[entrada + 2], (entrada + 2), "rojo", estilo_1 = "bright")
        impr_pant()
        sleep(3)
        
    #Si la respuesta fue correcta, sumar 1 punto al contador, dar la opcion de seguir o salir
    #Implementar lo de import OS para borrar el texto del cosa
    #OJO, entre las respuestas incorrectas NO se puede encontrar la correcta

def EQ_cuadraticas_PISA():
    
    global estado_del_programa 
    global paso_la_sanidad
    global ancho_de_pantalla 
    global alto_de_pantalla
    global linea
    global linea_raw
    global diccionario_alineaciones 
    global diccionario_color_n
    global correctas
    global incorrectas
    
    limpiar_pantalla()
    alinear_todos("center")
    
    x_a = randint(0,10)
    y_a = randint(-10,-1)
    a_a = randint(0,12)
    b_a = randint(0,12)
    c_a = randint(-10,-1)
    
    posibilidad_3 = [1, 2, 3]
    resultado_3 = choice(posibilidad_3)
    
    respuesta_incorrecta_1 = ("(" + str(x_a) + ","+ str(y_a) + ")")
    respuesta_incorrecta_2 = ("(" + str(a_a) + ","+ str(x_a) + ")")
    respuesta_incorrecta_3 = ("(" + str(b_a) + ","+ str(c_a) + ")")
    
    respuesta_incorrecta_4 = ("(" + str(c_a) + ","+ str(a_a) + ")")
    respuesta_incorrecta_5 = ("(" + str(b_a) + ","+ str(x_a) + ")") 
    respuesta_incorrecta_6 = ("(" + str(y_a) + ","+ str(b_a) + ")")
    
    respuesta_incorrecta_7 = ("(" + str(a_a) + ","+ str(b_a) + ")")
    
    respuesta_incorrecta_8 = ("(" + str(a_a) + ","+ str(x_a) + ")") 
    respuesta_incorrecta_9 = ("(" + str(x_a) + ","+ str(b_a) + ")")
    respuesta_incorrecta_10 = ("(" + str(a_a) + ","+ str(y_a) + ")")
     
    respuesta_incorrecta_11 =("(" + str(b_a) + ","+ str(y_a) + ")") 
    respuesta_incorrecta_12 = ("(" + str(c_a) + ","+ str(x_a) + ")")
    respuesta_incorrecta_13 = ("(" + str(b_a) + ","+ str(a_a) + ")")
    
    
    lista_de_respuestas_incorrectas = [respuesta_incorrecta_1, respuesta_incorrecta_2, respuesta_incorrecta_3, respuesta_incorrecta_4, respuesta_incorrecta_5, respuesta_incorrecta_6, respuesta_incorrecta_7, respuesta_incorrecta_8, respuesta_incorrecta_9, respuesta_incorrecta_10, respuesta_incorrecta_11, respuesta_incorrecta_12, respuesta_incorrecta_13]
    
    if resultado_3 == 1: 
        texto_de_operacion = ("(x^2  -  9 = ?)")
        respuesta_correcta = ("(-3,3)")
    
    elif resultado_3 == 2: 

        if coin_toss():  
            texto_de_operacion = ("x^2 + 6x + 5 = ?")
            respuesta_correcta = ("(-5,-1)")
        else:
            texto_de_operacion = ("(x^2 + 2x - 24 = ?)")
            respuesta_correcta = ("(-6,4)")
        
    else: 
        if coin_toss():  
            texto_de_operacion = ("(3x^2 + 2x - 5 = ?)")
            respuesta_correcta = ("(5/3,1)")
        else:
            texto_de_operacion = ("(x^2 - 5x + 6)")
            respuesta_correcta = ("(3,2)")
    
    limpiar_pantalla()
    alinear_todos("center")
    
    linea[0] = colores( ("✓ = " + str(correctas) + "    " ), 0, "verde", estilo_1 = "bright") + colores ( ("x = " + str(incorrectas)) , 0, "rojo", estilo_1 = "bright", misma_linea = True)
    linea [1] = texto_de_operacion
    linea[7] = "[8]: Salir al menu    [9]: Saltar"
    
    posibilidad_4 = [1, 2, 3, 4]
    resultado_4 = choice(posibilidad_4)
    
    alinear(3, "left")
    alinear(4, "left")
    alinear(5, "left")
    alinear(6, "left")
    
    while linea[3][3:] == linea[4][3:] or linea[3][3:] == linea[5][3:] or linea[3][3:] == linea[6][3:] or linea[4][3:] == linea[5][3:] or linea[4][3:] == linea[6][3:] or linea[5][3:] == linea[6][3:]: #las opciones no pueden ser iguales
        if resultado_4 == 1:
            linea[3] = "[1]: " + respuesta_correcta
        else:
            linea[3] = "[1]: " + choice(lista_de_respuestas_incorrectas)
    
        if resultado_4 == 2:
            linea[4] = "[2]: " + respuesta_correcta
        else:
            linea[4] = "[2]: " + choice(lista_de_respuestas_incorrectas)
        
        if resultado_4 == 3:
            linea[5] = "[3]: " + respuesta_correcta
        else:
            linea[5] = "[3]: " + choice(lista_de_respuestas_incorrectas)
    
        if resultado_4 == 4:
            linea[6] = "[4]: " + respuesta_correcta
        else:
            linea[6] = "[4]: " + choice(lista_de_respuestas_incorrectas)
        break
    impr_pant()
    
    while True: #Sanidad
        try:
            entrada = int(input())
            if entrada == 1 or entrada == 2 or entrada == 3 or entrada == 4 or entrada == 8 or entrada == 9:
                paso_la_sanidad = True
            else:
                paso_la_sanidad = False
        except:
            paso_la_sanidad = False
            
        if paso_la_sanidad == True:
            break
        
    if entrada == resultado_4:
        correctas += 1
        linea[resultado_4 + 2] = colores(linea[resultado_4 + 2], (resultado_4 + 2), "verde", estilo_1 = "bright")
        impr_pant()
        sleep(3)
    elif entrada == 8:
        estado_del_programa = 1
    elif entrada == 9:
        incorrectas += 1
        linea[resultado_4 + 2] = colores(linea[resultado_4 + 2], (resultado_4 + 2), "cian", estilo_1 = "bright")
        impr_pant()
        sleep(3)
    else:
        incorrectas += 1
        linea[resultado_4 + 2] = colores(linea[resultado_4 + 2], (resultado_4 + 2), "verde")
        linea[entrada + 2] = colores(linea[entrada + 2], (entrada + 2), "rojo", estilo_1 = "bright")
        impr_pant()
        sleep(3)
    return    

def Factorizacion_PISA():
    global estado_del_programa 
    global paso_la_sanidad
    global ancho_de_pantalla 
    global alto_de_pantalla
    global linea
    global linea_raw
    global diccionario_alineaciones 
    global diccionario_color_n
    global correctas
    global incorrectas
    
    limpiar_pantalla()
    alinear_todos("center")
    
    x_2 = randint(0,10)
    a_2 = randint(0,12)
    b_2 = randint(0,12)
    
    
    posibilidad_3 = [1, 2, 3]
    resultado_3 = choice(posibilidad_3)
    
    respuesta_incorrecta_1 = ("(x+" + str(x_2) + ")"+"(x+"+ str(a_2) + ")")
    respuesta_incorrecta_2 = ("(x+" + str(a_2) + ")"+"(x+"+ str(x_2) + ")")
    respuesta_incorrecta_3 = ("(x+" + str(b_2) + ")"+"(x"+ str(a_2) + ")")
    
    respuesta_incorrecta_4 = ("(x+" + str(x_2) + ")"+"(x+"+ str(a_2) + ")")
    respuesta_incorrecta_5 = ("(x+" + str(b_2) + ")"+"(x+"+ str(x_2) + ")") 
    respuesta_incorrecta_6 = ("(x+" + str(a_2) + ")"+"(x+"+ str(b_2) + ")")
    
    respuesta_incorrecta_7 = ("(x+" + str(a_2) + ")"+"(x+"+ str(b_2) + ")")
    
    respuesta_incorrecta_8 = ("(x+" + str(a_2) + ")"+"(x+"+ str(x_2) + ")") 
    respuesta_incorrecta_9 = ("(x+" + str(x_2) + ")"+"(x+"+ str(b_2) + ")")
    respuesta_incorrecta_10 = ("(x+" + str(a_2) + ")"+"(x"+ str(b_2) + ")")
     
    respuesta_incorrecta_11 =("(x+" + str(b_2) + ")"+"(x+"+ str(x_2) + ")") 
    respuesta_incorrecta_12 = ("(x+" + str(a_2) + ")"+"(x+"+ str(x_2) + ")")
    respuesta_incorrecta_13 = ("(x+" + str(b_2) + ")"+"(x+"+ str(a_2) + ")")
    
    
    lista_de_respuestas_incorrectas = [respuesta_incorrecta_1, respuesta_incorrecta_2, respuesta_incorrecta_3, respuesta_incorrecta_4, respuesta_incorrecta_5, respuesta_incorrecta_6, respuesta_incorrecta_7, respuesta_incorrecta_8, respuesta_incorrecta_9, respuesta_incorrecta_10, respuesta_incorrecta_11, respuesta_incorrecta_12, respuesta_incorrecta_13]
    
    if resultado_3 == 1: 
        texto_de_operacion = ("x^3+2x^2-x-2")
        respuesta_correcta = ("(x+2)(x+1)(x-1)")
        
    elif resultado_3 == 2:
        
        if coin_toss():  
            texto_de_operacion = ("4x^4-64x^2")
            respuesta_correcta = ("(x+4)(x-4)")
        else:
            texto_de_operacion = ("(3x^3-3x^2-6x)")
            respuesta_correcta = ("3x(x+1)(x-2)")
        
    else: 
        if coin_toss():  
            texto_de_operacion = ("(8x^4+2x^2)")
            respuesta_correcta = ("2x^2(4x^2+1)")
        else:
            texto_de_operacion = ("(x^2+10x+25)")
            respuesta_correcta = ("(x+5)^2")
    
    limpiar_pantalla()
    alinear_todos("center")
    
    linea[0] = colores( ("✓ = " + str(correctas) + "    " ), 0, "verde", estilo_1 = "bright") + colores ( ("x = " + str(incorrectas)) , 0, "rojo", estilo_1 = "bright", misma_linea = True)
    linea [1] = texto_de_operacion
    linea[7] = "[8]: Salir al menu    [9]: Saltar"
    
    posibilidad_4 = [1, 2, 3, 4]
    resultado_4 = choice(posibilidad_4)
    
    alinear(3, "left")
    alinear(4, "left")
    alinear(5, "left")
    alinear(6, "left")
    
    while linea[3][3:] == linea[4][3:] or linea[3][3:] == linea[5][3:] or linea[3][3:] == linea[6][3:] or linea[4][3:] == linea[5][3:] or linea[4][3:] == linea[6][3:] or linea[5][3:] == linea[6][3:]: #las opciones no pueden ser iguales
        if resultado_4 == 1:
            linea[3] = "[1]: " + respuesta_correcta
        else:
            linea[3] = "[1]: " + choice(lista_de_respuestas_incorrectas)
    
        if resultado_4 == 2:
            linea[4] = "[2]: " + respuesta_correcta
        else:
            linea[4] = "[2]: " + choice(lista_de_respuestas_incorrectas)
        
        if resultado_4 == 3:
            linea[5] = "[3]: " + respuesta_correcta
        else:
            linea[5] = "[3]: " + choice(lista_de_respuestas_incorrectas)
    
        if resultado_4 == 4:
            linea[6] = "[4]: " + respuesta_correcta
        else:
            linea[6] = "[4]: " + choice(lista_de_respuestas_incorrectas)
        break
    impr_pant()
    
    while True: #Sanidad
        try:
            entrada = int(input())
            if entrada == 1 or entrada == 2 or entrada == 3 or entrada == 4 or entrada == 8 or entrada == 9:
                paso_la_sanidad = True
            else:
                paso_la_sanidad = False
        except:
            paso_la_sanidad = False
            
        if paso_la_sanidad == True:
            break
        
    if entrada == resultado_4:
        correctas += 1
        linea[resultado_4 + 2] = colores(linea[resultado_4 + 2], (resultado_4 + 2), "verde", estilo_1 = "bright")
        impr_pant()
        sleep(3)
    elif entrada == 8:
        estado_del_programa = 1
    elif entrada == 9:
        incorrectas += 1
        linea[resultado_4 + 2] = colores(linea[resultado_4 + 2], (resultado_4 + 2), "cian", estilo_1 = "bright")
        impr_pant()
        sleep(3)
    else:
        incorrectas += 1
        linea[resultado_4 + 2] = colores(linea[resultado_4 + 2], (resultado_4 + 2), "verde")
        linea[entrada + 2] = colores(linea[entrada + 2], (entrada + 2), "rojo", estilo_1 = "bright")
        impr_pant()
        sleep(3)

"""------------------------------------linea-separadora------------------------------------"""
#Programa Principal

while True:
    #el "estado_del_programa" cambia al realizar acciones en algunos menus, permitiendo navegar en el programa entero
    while estado_del_programa == 1:
        menu()
        
    while estado_del_programa == 2:
        configuracion()
    
    while estado_del_programa == 3:
        p_notable_PISA()
        
    while estado_del_programa == 4:
        EQ_cuadraticas_PISA()
        
    while estado_del_programa == 5:
        Factorizacion_PISA()