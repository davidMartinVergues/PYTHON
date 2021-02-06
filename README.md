- [Course from zero to Hero - Udemy -](#course-from-zero-to-hero---udemy--)
  - [by Jose Portilla](#by-jose-portilla)
  - [by Andrei Neagoie](#by-andrei-neagoie)
- [Instalación de Python y SetUp](#instalación-de-python-y-setup)
  - [Instalación](#instalación)
  - [Instalamos el tema para Jupyter](#instalamos-el-tema-para-jupyter)
- [Introducción a Python](#introducción-a-python)
  - [Usos de python y librerías](#usos-de-python-y-librerías)
  - [Crear comentarios en Pyhon](#crear-comentarios-en-pyhon)
  - [Fundamental Data Types](#fundamental-data-types)
    - [**Algunas operaciones**](#algunas-operaciones)
      - [potencias](#potencias)
      - [Parte entera de una división decimal](#parte-entera-de-una-división-decimal)
      - [Resto de una división entera](#resto-de-una-división-entera)
    - [Funciones matemáticas](#funciones-matemáticas)
      - [**round**](#round)
      - [**abs**](#abs)
      - [**bin / int**](#bin--int)
  - [Uso de variables](#uso-de-variables)
  - [Uso del método print()](#uso-del-método-print)
  - [Ordered vs unordered](#ordered-vs-unordered)
  - [String](#string)
    - [**Propiedades de los strings**](#propiedades-de-los-strings)
    - [**Métodos de los strings**](#métodos-de-los-strings)
      - [**Slicing**](#slicing)
      - [**strip()**](#strip)
      - [**upper() lower() split()**](#upper-lower-split)
      - [**format**](#format)
      - [**Casefold**](#casefold)
      - [**find**](#find)
      - [**Capitalize**](#capitalize)
      - [**replace**](#replace)
      - [generar el alfabeto (inglés)](#generar-el-alfabeto-inglés)
  - [List - (data structure)](#list---data-structure)
    - [**Métodos**](#métodos)
      - [**len()**](#len)
      - [**Slicing**](#slicing-1)
      - [**Append() pop()**](#append-pop)
      - [**remove(element_value)**](#removeelement_value)
      - [**clear()**](#clear)
      - [**insert(index,value)**](#insertindexvalue)
      - [**extend([])**](#extend)
      - [**Sort() sorted() reverse()**](#sort-sorted-reverse)
      - [**Lista de elementos o comprehension**](#lista-de-elementos-o-comprehension)
      - [**Count()**](#count)
      - [**All() any()**](#all-any)
      - [**Join()**](#join)
      - [**Index(value,start,stop)/in**](#indexvaluestartstopin)
      - [**copy**](#copy)
      - [**List unpacking**](#list-unpacking)
  - [Dictionaries - dict (data structure)](#dictionaries---dict-data-structure)
    - [**Métodos**](#métodos-1)
      - [comprehension](#comprehension)
      - [get()](#get)
      - [**keys() / values() / items()**](#keys--values--items)
      - [**clear()**](#clear-1)
      - [**copy()**](#copy-1)
      - [**pop()**](#pop)
      - [**update()**](#update)
  - [Tuples - data structure -](#tuples---data-structure--)
    - [**Métodos**](#métodos-2)
      - [**Count() / index()**](#count--index)
      - [**Sum()**](#sum)
  - [Sets - data structure -](#sets---data-structure--)
    - [**Métodos**](#métodos-3)
      - [**Add()**](#add)
      - [**clear() / copy()**](#clear--copy)
      - [difference()](#difference)
      - [discard()](#discard)
      - [difference_update()](#difference_update)
      - [intersection() o &](#intersection-o-)
      - [isdisjoint()](#isdisjoint)
      - [union() o |](#union-o-)
      - [issuperset()](#issuperset)
      - [**Issubset()**](#issubset)
- [In/Out with basic Files](#inout-with-basic-files)
  - [Crear un fichero - %%writefile](#crear-un-fichero---writefile)
  - [Abrir el fichero - open()](#abrir-el-fichero---open)
  - [Leer el fichero - .read()](#leer-el-fichero---read)
  - [seek()](#seek)
  - [readlines()](#readlines)
  - [close()](#close)
  - [With...as](#withas)
  - [open() - extendido](#open---extendido)
    - [**'a' (append) mode**](#a-append-mode)
    - [**w (write) mode**](#w-write-mode)
  - [File location](#file-location)
- [Operadores](#operadores)
  - [Aritméticos](#aritméticos)
  - [Asignación](#asignación)
  - [Comparación](#comparación)
  - [Lógicos](#lógicos)
  - [Identidad](#identidad)
  - [is vs '=='](#is-vs-)
    - [==](#)
    - [is](#is)
- [Condicionales e Iteraciones](#condicionales-e-iteraciones)
  - [If -elif-else statement](#if--elif-else-statement)
    - [**Ternary operator**](#ternary-operator)
  - [For loops](#for-loops)
    - [**While not**](#while-not)
  - [Keywords importantes en los loops](#keywords-importantes-en-los-loops)
    - [**Pass**](#pass)
    - [**Continue**](#continue)
    - [**Break**](#break)
- [Buil-in function útiles](#buil-in-function-útiles)
  - [Map(func,iterable)](#mapfunciterable)
  - [Filter(function, iterable)](#filterfunction-iterable)
  - [Reduce(function, iterable, [initial_value] )](#reducefunction-iterable-initial_value-)
  - [zip()](#zip)
  - [Lambda](#lambda)
  - [Range()](#range)
  - [enumerate()](#enumerate)
  - [In / not in](#in--not-in)
  - [Min() max()](#min-max)
  - [Random library](#random-library)
    - [**shuffle**](#shuffle)
    - [Randint](#randint)
  - [**Input**](#input)
    - [Validación input](#validación-input)
- [Methods and Functions](#methods-and-functions)
  - [Métodos](#métodos-4)
    - [**Argumentos vs parámetros**](#argumentos-vs-parámetros)
    - [**Tipos de argumentos**](#tipos-de-argumentos)
  - [Argumentos \*args (arguments) / \*\*kwargs(keywords arguments)](#argumentos-args-arguments--kwargskeywords-arguments)
      - [\*args](#args)
      - [\*\*kwargs(keywords arguments)](#kwargskeywords-arguments)
- [Scoope](#scoope)
  - [LEGB Rule](#legb-rule)
  - [global keyword](#global-keyword)
- [OOP - Object Oriented Programming](#oop---object-oriented-programming)
  - [Introspección de objetos](#introspección-de-objetos)
    - [isinstance() y issubclass](#isinstance-y-issubclass)
    - [dir()](#dir)
  - [Creación de una clase](#creación-de-una-clase)
    - [Añadimos los métodos](#añadimos-los-métodos)
      - [constructor **init**](#constructor-init)
  - [Características de la Programación Objetos](#características-de-la-programación-objetos)
    - [Encapsulación](#encapsulación)
    - [Herencia](#herencia)
      - [Herencia múltuple](#herencia-múltuple)
    - [Polimorfismo](#polimorfismo)
    - [Abstracción](#abstracción)
  - [Métodos especiales or magic methods or dunder methods](#métodos-especiales-or-magic-methods-or-dunder-methods)
    - [String representation **str()**](#string-representation-str)
    - [tamaño del objeto **len**](#tamaño-del-objeto-len)
    - [del method **del**](#del-method-del)
- [Functional Programing](#functional-programing)
  - [¿Que es?](#que-es)
- [Modules and Packages](#modules-and-packages)
  - [Python Collections Module](#python-collections-module)
    - [Counter](#counter)
      - [Métodos](#métodos-5)
        - [elements()](#elements)
        - [most_common()](#most_common)
        - [substract([iterable-or-mapping])](#substractiterable-or-mapping)
    - [defaultdict](#defaultdict)
    - [OrderedDict](#ordereddict)
  - [PIP](#pip)
  - [PyPI (python package index)](#pypi-python-package-index)
  - [Escribiendo nuestros propios Módulos y paquetes](#escribiendo-nuestros-propios-módulos-y-paquetes)
    - [creando un módulo](#creando-un-módulo)
    - [creando un paquete](#creando-un-paquete)
  - [**name**](#name)
- [Decorators](#decorators)
  - [First class citizens](#first-class-citizens)
  - [HOC - Higher Order Function](#hoc---higher-order-function)
  - [Decorators syntaxi](#decorators-syntaxi)
  - [Para que usamos los decorators](#para-que-usamos-los-decorators)
- [Errores y gestión de excepciones](#errores-y-gestión-de-excepciones)
  - [Lanzar nuestras propias excepciones](#lanzar-nuestras-propias-excepciones)
- [Unit testing](#unit-testing)
  - [Pylint](#pylint)
  - [unittest](#unittest)
  - [!not found](#-1)
- [pygame](#pygame)
  - [Estructura del archivo](#estructura-del-archivo)
  - [Ventana de juego](#ventana-de-juego)
  - [Fijar tamaño, titulo, icono](#fijar-tamaño-titulo-icono)
  - [Establecemos el fondo de la ventana de juego](#establecemos-el-fondo-de-la-ventana-de-juego)
  - [mostramos Info](#mostramos-info)

# Course from zero to Hero - Udemy -

## by Jose Portilla

> <span style="font-size:1.5em;"> [_link del curso_](https://www.udemy.com/course/complete-python-bootcamp/) </span>

## by Andrei Neagoie

> <span style="font-size:1.5em;"> [_link del curso_](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/) </span>

# Instalación de Python y SetUp

## Instalación

Bajaremos un paqueta q se llama anaconda compuesto por python y una serie de librerías útiles junto con editores de texto como Jupiter. Lo bajamos desde

<span style="font-size:1em;">[_link anaconda.com_](https://www.anaconda.com/distribution/)</span>

1. Vamos a en nuestro direcotrio
2. Ejecutamos el archivo descargado en el link

   ```
     bash Anaconda3-5.2.0-Linux-x86_64.sh
   ```
   Durante la instalación nos va a preguntar:
   
   The installer prompts “Do you wish the installer to initialize Anaconda3 by running conda init?” 
   
   Se recomienda poner [yes]
   
   si le damos a no hay q hacer los siguiente para iniciar anaconda:
   ```
   source /home/david/anaconda3/bin/activate
   
   conda init

   ```

   ```
     source .bashrc
   ```

3. Comprobamos que se ha instalado adecuadamente  
   ![not found](img/img-1.png)
4. Lanzamos interfaz gráfica de Anaconda

   ```
       anaconda-navigator
   ```

5. Para ver info de anaconda

   ```
       conda info
   ```

![not found](img/img-2.png)

6. Vemos como en el prompt pone base eso es xq es el interprete de anaconda para desactivarlo

   ```
     conda deactivate
   ```

   para volverla a activar

   ```
    conda activate
   ```

1. Saber versión y donde está instalado python  
   ![not found](img/img-3.png)
1. Añadir PYTHONPATH
   Abrir en nuestra carpeta personal el archivo .bashrc y al final del archivo añadir lo q nos devuelve which python

   ![not found](img/img-4.png)

1. Ahora cuando tecleamos

   ![not found](img/img-5.png)

Y nos tiene q dar la misma respuesta.

## Instalamos el tema para Jupyter

Source https://github.com/dunovank/jupyter-themes
https://medium.com/@rbmsingh/making-jupyter-dark-mode-great-5adaedd814db

1. actualizamos anaconda

   ```
   conda update anaconda
   ```

2. instalamos los temas
   ```
     pip install jupyterthemes
   ```
   ```
     pip install --upgrade jupyterthemes
   ```
3. Seleccionamos monokai  
   ![not fond](img/img-6.png)
4. Modificamos el tema
   Con esa modificación los ejes de los gráficos se ven mal para rectificarlo:
   Make a file named 00_startup.py in ~/.ipython/profile_default/startup and stick the following snippet into it, and restart Jupyter, details are here
   import os
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   import seaborn as sns
   from jupyterthemes import jtplot
   jtplot.style(theme=’monokai’, context=’notebook’, ticks=True, grid=False)

# Introducción a Python

## Usos de python y librerías

![NOT FOUND](img/img-j-1.png)

Para poder ejectar código python necesitamos un intérprete que lee línea a línea nuestro código y una viertual machine. Si lo bajamos de la web oficial ambos estarán escritos en C por eso se llama c-virtual machine y cpython.

![not found](img/img-7.png)

## Crear comentarios en Pyhon

```python
  # comentario monolínea
  '''
    comentario de bloque
  '''
```

Las 3 comillas tb pueden servir para escribit un string de múltiples líneas, así q lo adecuado en py para comentarios de múltiples líneas es usar # antes de cada una

## Fundamental Data Types

Son los tipos especificados en el core de python tales como :  
![not found](img/img-8.png)

Tenemos otros tipos de datos como:

- ### **Custom Types - Class**
  Podemos crear nuestros propios tipos de datos, para ello construimos clases.
- ### **Specialized Data Type**
  Son aquellos que están especificados en paquetes externos, los llamados `modules`.
- ### **None - type**
  Indica ausencia de valor

### **Algunas operaciones**

#### potencias

```python
# para hacer potencias de un número
print(2**3) # 8
```

#### Parte entera de una división decimal

```python
# Para obtener la parte entera de una división decimal //

print(2//4 ) # 0 => 0.5
print(5//4 ) #  1  =>1.25
```

#### Resto de una división entera

```python
# Para obtener el resto de la división entera es el módulo %

print(5 % 4) # 1
print(6 % 4 )# 2
```

### Funciones matemáticas

#### **round**

Permite redondear el número

```python
round(3.1) # 3
round(3.9) # 4
```

#### **abs**

Obtener el valor absolute de un valor

```python
abs(3)  # 3
abs(-3) # 3
```

#### **bin / int**

representación binaria bin()

```python
bin(5) # '0b101'
```

Pasar un número en base 'x' a integer (base 10).
El método funciona como: este número '0b101' en base 2 (binaria) pásalo a int

```python
int('0b101', 2) # 5
```

## Uso de variables

Hay q tener claro que en python no hay tipos primitivos, todo el python son objetos!

Python usa tipado dinámico como JavaScript esto significa que no es necesario especificar el tipo de dato que contendrá dicha variable.
Por ejemplo Java tiene un tipado estático porque requiere que especifiquemos durante la declaración el tipo de dato que contendrá la variable.  
 Podemos usar `type()` para saber el tipo de variable  
 Usamos la función `str()` para **castear** a string, lo que llamamos `type conversion`. Podemos usar `int()` `float()` `bool` ...

```python
  # Tipado dinámico

  my_dogs = 2

  print('tipo de mi variable ' + str(type(my_dogs))) # tipo de mi variable <class 'int'>

  my_dogs = ['sammy','frankie']

  print('mi variable ha cambiado de tipo, ahora es una list ' + str(type(my_dogs)) +' -> ' +str(my_dogs))
  # mi variable ha cambiado de tipo, ahora es una list <class 'list'> -> ['sammy', 'frankie']

  # type conversion

  number = 5
  name = 'david'
  print(name+number) # eso da error
  print(name+str(number))
```

## Uso del método print()

Para imprimir contenido usamos el método print(), éste acepta un atributo para indicar que no haga salto de página end=’’.

```python
  for x in range(10):
    print(x, end='')

  # 0123456789
```

## Ordered vs unordered

Por ejemplo una `list` es un objeto **ordenado** y un `dict` es un objeto **desordenado** (en python todo son objetos). El concepto ordenado/desordenado hace referencia a como se almacena la info en memoria.
Los elementos de una lista se guardan en memoria uno al lado del otro tal como los vamos especificando, pero n una dict los elementos se guardan en diferentes puntos de la memoria. Si hacemos un dict pequeño

```python
      user = {
        'nombre':'dabid',
        'edad':36
      }
```

y lo imprimimos probablemente los campos se impriman cn ese orden pero diccionarios de mayor tamaño muy probablemente los campos se presenten en distinto orden.

## String

Funcionan como arrays así que usando el índice podemos extraer letras del string.
Está habilitado el reverse index(indice reverso) así sin conocer la longitud del string podemos extraer el último carácter(poner el índice en negativo: -1).

```python
  my_name = "david"
  my_name[0] # 'd'
  my_name[1] # 'a'
  # len() function

  print('utilizando la función len() => '+my_name[len(my_name)-1])

  # utilizando la función len() => d

  # última letra sin saber la longitud del str

  # Reverse index

  print('utilizando el indice reverso => '+my_name[-1])
  #utilizando el indice reverso => d
```

Tamaño de un str usamos la función len()

### **Propiedades de los strings**

- 1. Son inmutables, no podemos modificar un string

     ```python
       name = 'David'
       name[0]= 'P'

       # 'str' object does not support item assignment por lo tanto strings inmutables
     ```

- 2. Concatenables, solo funciona con strings no le puedo concatenar un número, para ello debo castearlo a `str` previamente

     ```python
       x = "hello world"

       y = ' is beatifull outside'

       x+= y
       print(x) #hello world is beatifull outside

       name = 'David'

       name = 'P'+ name[1:]
       name #'Pavid'

       number = 5
       name = 'david'
       print(name+number) # eso da error
       print(name+str(number)) # david5

     ```

- 3. Multiplicables

     ```python
      name = 'd'

      name\*10 # dddddddddddd

     ```

### **Métodos de los strings**

#### **Slicing**

- [start:stop:step] nos permite obtener un subString  
   stop - indica hasta dnd se extrae pero sin incluir ese caracter  
   step - divide en str en grupos de X carcateres y nos devuelve el
  primer caracter de cada grupo

  ```python
    # slicing [start:stop:step]

        my_string = "abcdefghijk"

        print(' substring desde el índice 0 hasta el final [::] => '+my_string[::])
        print(' substring desde el índice 2 hasta el final => '+my_string[2:])
        print(' substring desde el índice 0 hasta el índice 3 (NO incluido)) => '+my_string[:3])
        print(' substring desde el índice 2 hasta al 5(No incluido) => '+my_string[2:5])

        # uso del tercer parámetro, divide en str en grupos de X carcateres y nos devuelve el primer caracter de cada grupo

        # por ejemplo si ponemos 2 ab - cd - ef - gh - ij - k null

        print(' substring dividido en grupos de a 2 => '+my_string[::2])

        # por ejemplo si ponemos 3 abc - def - ghi - jk null

        print(' substring dividido en grupos de a 3 => '+my_string[::3])

        # lo mismo pero de un subString cd - ef

        print(' substring del 2 al 5 dividido en grupos de a 2 => '+my_string[2:6:2])

        # utilizando el 3 como negativo -1 invierte el string kjihgfedcba

        print('separador de grupo en - empieza por el final(INVIERTE EL STRING) => '+my_string[::-1])

        # utilizando el 3 como negativo -1 Ab - Cd - Ef - Gh - Ij - K null <-

        print(' usando el separador de grupo en - empieza a contar por el final=> '+my_string[::-2])

        '''
            substring desde el índice 0 hasta el final [::]              => abcdefghijk
            substring desde el índice 2 hasta el final                   =>   cdefghijk
            substring desde el índice 0 hasta el índice 3 (NO incluido)) => abc
            substring desde el índice 2 hasta al 5(No incluido)          =>   cde
            substring dividido en grupos de a 2                          => acegik
            substring dividido en grupos de a 3                          => adgj
            substring  del 2 al 5 dividido en grupos de a 2               => ce
            separador de grupo en - empieza por el final(INVIERTE EL STRING) => kjihgfedcba
            usando el separador de grupo en - empieza a contar por el final=> kigeca
        '''
  ```

#### **strip()**

Permite eliminar los espacios en blanco por delante y detrás de un string. Puede aceptar como argumento los caracteres a eliminar

```python
string = '  xoxo love xoxo   '

# eliminamos los espacios en blanco
print(string.strip()) # xoxo love xoxo

# los siguientes caracteres serán eliminados
#  <whitespace>,x,o,e
print(string.strip(' xoe'))  #lov

# el argumento no contiene espacios en blanco
#ni ningún otro caracter coincidente en el string
# así q el string se mantiene igual
print(string.strip('stx')) #  xoxo love xoxo

string = 'android is awesome'
print(string.strip('an')) # droid is awesome

```

#### **upper() lower() split()**

```python
    x = "hi this is a string"
    print(x.upper()) #HI THIS IS A STRING
    print(x.lower()) #hi this is a string
    print(x.split()) #['hi', 'this', 'is', 'a', 'string']
    print(x.split('i')) #['h', ' th', 's ', 's a str', 'ng']
```

#### **format**

```python
print('hello {}'.format('world')) #hello world

name= 'David'
apellido1 = 'Martin'
apellido2 = 'Vergues'

print('me llamo {} {} {}'.format('David', 'Martin', 'Vergues'))
#me llamo David Martin Vergues

print('me llamo {2} {1}, {0}'.format('David', 'Martín', 'Vergues'))
#me llamo Vergues Martín, David

#podemos especificar el número de caracteres q ocupara cada string y si cómo estará alineado

print('alineación: {0:<15} {1:^15} {2:>15}'.format('izq', 'centro', 'drcha'))
# izq                 centro                drcha
# 0 el primer valor 'izq'
# < indica hacia la izq
# 15 número de esacios a ocupar

print('alineación: {0:=<15} {1:-^15} {2:.>15}'.format('izq', 'centro', 'drcha'))
# alineación: izq============ ----centro----- ..........drcha

#podemos usar keyword
print('me llamo {v} {m}, {d}'.format(d='David', m='Martín', v='Vergues'))
#me llamo Vergues Martín, David

#podemos usar referencias a variables
print('me llamo {2} {1}, {0} y tengo {3}'.format(name,apellido1,apellido2, '35'))
#me llamo Vergues Martin, David y tengo 35

#podemos truncar los strings con la notación del punto
print('me llamo {0:.3} '.format(name)) #me llamo Dav
```

- ##### Float formatting

  {value:width.precision f}  
   Value => ponemos el valor del número  
   Width => tamaño que ocupará el número hecho string (nº de caracteres)  
   Precision => número de decimales que tendrá

  ```python
  result = 1.2987012987012987

  print('mi valor es {r:1.3f}'.format(r=result))
  #mi valor es 1.299
  print('mi valor es {r:10.3f}'.format(r=result))
  #mi valor es      1.299
  ```

- ##### f-string = formated string literal

  ```python
  name = "David"
  age = 3
  print(f'hello, his name is {name} and he is {age} years old')
  # hello, his name is David and he is 3 years old

  result = 1.459029
  result2 = 1.45

  print(f'este es mi resultado => {result:1.2f}')
  # este es mi resultado => 1.46

  print(f'este es mi resultado => {result2:1.4f}')
  # con notación de .format() este es mi resultado => 1.4500

  print(f'este es mi resultado => {result2:<{10}.{3}}')
  # con notación de f-string este es mi resultado =>  1.45

  print(f'este es mi resultado => {result2:^{10}.{3}}')
  # con notación de f-string este es mi resultado =>    1.45
  ```

  {3} En este caso hace referencia al número total de dígitos que tendrá el número, no como en .format() que hace referencia al número de dígitos decimales

#### **Casefold**

- Es como un equalsIgnoreCase de java, elimina las distinciones entre mayúsculas y minúsculas en el momento de comparar strings.

  ```python
    str1 = 'david'
    str2 = 'DAVID'

    if str1 == str2:
      print('son iguales')
    else:
      print('son diferentes')
    # son diferentes
  ```

  usando casefold()

  ```python
    str1 = 'david'
    str2 = 'DAVID'

    if str1 == str2.casefold():
      print('son iguales')
    else:
      print('son diferentes')
    # son iguales
  ```

#### **find**

- Sólo funciona en estrings, para saber si un string contiene a otro y si lo está nos devuelve la posición y si no un -1. Hace distinción entra minusculas y mayúsculas.

  ```python
    str1 = 'david'
    str2 = 'hello david'

    str2.find(str1) #6
    str2.find('ello') #1
    str2.find('Hello') #-1
  ```

#### **Capitalize**

- La primera letra de una palabra en mayúscula.

  ```python
    def old_macdonald(name):
        first_part = name[:3]
        second_part = name[3:]

        return first_part.capitalize()+second_part.capitalize()

    old_macdonald('macdonald') #'MacDonald'
  ```

#### **replace**

- reemplazar partes del texto.

```python
       quote= 'to be or not to be'
       print(quote.replace('be','me'))
       # to me or not to me
```

#### generar el alfabeto (inglés)

importamos la librerio string

```python
import string

string.ascii_lowercase
#'abcdefghijklmnopqrstuvwxyz'
```

`Aplicando todos estos métodos sobre un string nunca alteramos el string original, son inmutables!, pero podemos asignar el resultado a una nueva variable`

## List - (data structure)

Secuencia ordenada de elementos que pueden ser de diferentes tipos(numbers, string,obj...). Podemos tener distintos tipos de datos almacenados en un list.

### **Métodos**

#### **len()**

- Conocer el número de elementos de la list.

```python
    my_List = []

    my_List = ['string', 100, 20.3,1,2,3]

    # len()
    len(my_List)
```

#### **Slicing**

- [start:stop:step]  
  Funciona igual que en los strings. No altera el array original pero devuelve un nuevo array.

```python
    my_List[-1]     # 3
    my_List[4:]     #  [2, 3]
    my_List[:3]     #  ['string', 100, 20.3]
    my_List[::2]    #  ['string', 20.3, 2]
    my_List*2       # ['string', 100, 20.3, 1, 2, 3, 'string', 100, 20.3, 1, 2, 3]
```

Podemos concatenar list sumándolas

```python
    my_list_1 = [1,2,3,4,5]
    my_list_2 = [6,7,8,9,10]

    my_list_1+=my_list_2

    my_list_2 # [6, 7, 8, 9, 10]
    my_list_1 # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

#### **Append() pop()**

- Nos permite añadir(append) o eliminar (pop) un elemento al final de la list.
  El método pop() no solo elimina el último elemento sino que también lo devuelve. Una función más es que puedes pasar el índice del elementos a eliminar, por defecto es el -1 (último elemento).
  A pop le podemos pasar el índice del elemento a borrar.

```python
    my_list = ['one', 'two','three','four','five','six']

    my_list.append('eight')

    my_list # ['one', 'two', 'three', 'four', 'five', 'six', 'eight']

    element_deleted = my_list.pop()

    element_deleted # 'eight'

    my_list # ['one', 'two', 'three', 'four', 'five', 'six']

    my_list.pop(0) # 'one'
    my_list         # ['two', 'three', 'four', 'five', 'six']
```

#### **remove(element_value)**

- Nos permite borrar un elemento de a lista especificando el valor de dicho elemento. Cambia nuestra list, no devuelve el valor eliminado como sí lo hace pop()

```python
    list2 = ['david','martin','vergues']
    list2.remove('david')
    print(list2)   # ['martin', 'vergues']
```

#### **clear()**

- Vacia la lista

```python
    list2 = ['david','martin','vergues']
    list2.clear()
    print(list2)
```

#### **insert(index,value)**

- Nos permite introducir un elemento en la lista en un índice concreto

```python
    list = [1,2,3,4]
    list.insert(4,100)
    print(list) #[0, 1, 2, 3,4,100]

    list2 = [1,2,3,4]
    list2.insert(0,5)
    print(list2) # [5, 1, 2, 3, 4]
```

#### **extend([])**

- Permite extender el array con nuevos elementos necesitamos pasarlos como un iterable, en lugar de hacer 'x' appends.

```python
    list2 = [1,2,3,4]
    list2.extend([0,5])
    print(list2) # [1, 2, 3, 4, 0, 5]
```

#### **Sort() sorted() reverse()**

- sort() y reverse() actúan sobre la list y la modifican

```python
    char_list = ['a','d','c','e','f','b']
    num_list = [10,2,4,1,0]

    char_list.sort()
    num_list.reverse()

    print(char_list) # ['a', 'b', 'c', 'd', 'e', 'f']
    print(num_list)  # [0, 1, 4, 2, 10]
```

El método sorted() devuelve la lista ordenada pero no modifica la original.

    ```python
      list4 = [5,3,4,6,1]

      listOrdenada = sorted(list4)

      print(list4)        # [5, 3, 4, 6, 1]
      print(listOrdenada) # [1, 3, 4, 5, 6]
    ```

Tanto a sort() o sorted podemos indicar en base a que elemento se hace la ordenación y si queremos q sea reversa. Siempre que el iterable sea una tupla o un dictionari

```python
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sorted(student_tuples, key=lambda student: student[2])
# sort by age
#   [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

si queremos modificar la list original

```python
student_tuples.sort(key=lambda student: student[2])   # sort by age

```

#### **Lista de elementos o comprehension**

- Si quisiéramos obtener una lista de las letras que forman un string podemos hacer lo siguiente:

  ```python
    word = 'word'

    l = []

    for letter in word:
        l.append(letter)

    print(l) # ['w', 'o', 'r', 'd']
  ```

  Pero una manera de hacerlo más fácil es:
  subelement **for** subelemento **in** element

  ```python
    word = 'word'

    l = [letter for letter in word]

    l # ['w', 'o', 'r', 'd']
  ```

- Range

  ```python
    l=  [num for num in range(0,10)]
    l # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```

  También podemos hacer lo siguiente:

  ```python
    new_list = list(range(100))
  ```

- Podemos aplicar cambios a cada subelemento antes de incluirlo en la list, por ejemplo hacer el cuadrado de cada elemento **num** \*\*2

  ```python
    l=  [num**2 for num in range(0,10)]
    l # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  ```

  Podemos añadir condiciones

  ```python
    l=  [num**2 for num in range(0,10) if num%2 ==0]
    l # [0, 4, 16, 36, 64]

  ```

  incluso if else

  ```python
    l=  [num if num%2==0 else 'impar' for num in range(0,10)]
    l # [0, 'impar', 2, 'impar', 4, 'impar', 6, 'impar', 8, 'impar']

  ```

  Incluso podemos añadir operaciones

  ```python
    celcius = [0,10,20,34.5]

    fahrenheit = [ ((9/5)*temp+32) for temp in celcius ]

    fahrenheit #[32.0, 50.0, 68.0, 94.1]

  ```

  ```python
    s = ['a','b','c','b','d','m','n','n']

    l = list({ c for c in s if s.count(c)>1 })

    l # ['b','n']
  ```

- Nested loops

  ```python
    l = []

    for x in [2,4,6]:
        for y in [1,10,100]:
            l.append(x*y)
    l # [2, 20, 200, 4, 40, 400, 6, 60, 600]
  ```

#### **Count()**

- Las veces q aparece un elemento en una lista

  ```python
    l = [0,2,2,10,20,34.5]

    print(l.count(2)) # 2
  ```

#### **All() any()**

- Nos permite saber si una lista contiene todos (all) los valores o sólo algunos (any) de otra lista

  ```python
    l1 = [1,2,3]
    l2 = [1,2,3,4,5,6]
    l3 = [1,2,45,6,8]
              (2)               (1)
    r = all(element in l2 for element in l1)
    r #true

    r = all(element in l3 for element in l1)
    r #false

    r = any(element in l3 for element in l1)
    r #true

  ```

  La secuencia de comprobación es la siguiente:  
  primero hace un for (1) sacando cada “elem” de l1 y hace la comprobación en elem in l2 (2)

#### **Join()**

- Permite concatenar los elementos de una lista mediante algún caracter, por ejemplo un espacio en blanco

  ```python
    l = ['hola','david']

    ' '.join(l) # 'hola david'

  ```

#### **Index(value,start,stop)/in**

- Nos devuelve la posición de una valor en la list, el primero que encuetra

  ```python
    l1 = [1,2,3]
    l1.index(3) # 2
  ```

  Podemos pasar parámetros adicionales, como el índice dónde empezamos a buscar y el índice dónde paramos la búsqueda

  ```python
  list5 =  ['a','b','c','d','e','f']

  print(list5.index('e',3,5)) # 4

  ```

  Cuando busco un valor que no existe en la lista este método me arroja un error

  ```python
    list5 =  ['a','b','c','d','e','f']

    print(list5.index('x',3,5)) # error
  ```

  ![not found](img/img-j-19.png)

- Para evitar este error usaremos la `keyword` `in` que nos permite saber si un valor está en una list o tb funciona con str.

  ```python
    list5 =  ['a','b','c','d','e','f']
    print('x' in list5) # False

    # en str

    print('d' in 'David') # True
  ```

#### **copy**

- Hace una copia de la lista. Nos crea una nueva list. Pero... si esta lista contiene n objeto (otra lista, dictionary,...) no genera uno nuevo si no que `copia la referencia` así si modifico valores de ese objeto en la nueva lista en la lista original quedan modificados también.

  ```python
    list5 =  ['a','b','c','d','e','f', [1,2,3], {'fruta':'manzana','precio':5}]
    list6 = list5.copy()
    print(list5)
    list6[6][0]=0
    list6[0]='x'
    print(list5)
    print(list6)
  ```

  ![not found](img/img-j-20.png)

#### **List unpacking**

- Nos permite extraer valores de una lista de diferentes modos

  a,b,c, \*other, d = [1,2,3,4,5,6,7,8,9]

  print(a) #1
  print(b) #2
  print(c) #3
  print(other) # [4, 5, 6, 7, 8]
  print(d) # 8

## Dictionaries - dict (data structure)

Es una manera de mantener nuestros datos estructurados (`data structure`)

Son mapas desordenados (no pueden ser ordenados) para almacenar objetos usando los pares **clave-valor**.
Normalmente los usamos cuando queremos tener dos valores que están relacionados por ejemplo precios de productos, así no necesitamos saber el índice del producto para saber el precio.  
La clave de los diccionarios debe ser un elemento `inmutable`. Por lo que podemos usar booleans, num,... pero no una list. Aunque el 99 % de las veces la clave será un string.
Otro punto es que las claves deben ser únicas, si se repiten serán sobreescritas por la última.

```python
d = {
      123:[1,2,3],
      True:[1,2,3],
      [100]: True # este nos dará error
      }
```

Otra manera de crear dictionaries, no muy común, es usando una in-built function `dict()`

```python
      user2 = dict(name='Laura')
      user2 #
```

Para acceder los valores se utiliza el corchete con la clave

```python
      prices_lookup = {
        'apple':2.88,
        'oranges':3.56,
        'milk':6.12
       }

      print('precio de las manzanas {:<10.5f} €'.format(prices_lookup['apple']))
      # precio de las manzanas 2.88000    €

      prices_lookup # {'apple': 2.88, 'oranges': 3.56, 'milk': 6.12}

```

Dentro de los diccionarios podemos almacenar listas y otros diccionarios.

```python
      d = {
        'numbers':123,
        'list':[1,2,3],
        'dict':{
          'nombre':'david',
          'apellido':'martin'
          }
        }

      d['numbers'] # 123
      d['list'][0] #1
      print('me llamo {} {} '.format(d['dict']['nombre'], d['dict']['apellido'])) # me llamo david martin
```

Añadir / sobreescribir / borrar (del) elementos de un diccionario

```python
      prices_lookup = {'apple':2.88, 'oranges':3.56, 'milk':6.12}

      prices_lookup['melon'] = 5.86

      prices_lookup['apple']= 3.30

      prices_lookup # {'apple': 3.3, 'oranges': 3.56, 'milk': 6.12, 'melon': 5.86}

      del prices_lookup['melon']

      prices_lookup # {'apple': 3.3, 'oranges': 3.56, 'milk': 6.12}
```

Una manera para saber si una clave existe en un dict es usar la keyword `in` como en las list y en los strings

```python

      user = {
      'name': 'David',
      'age' : 36
    }

    'name' in user # True
```

Podemos usar `in` para checkear tanto las llaves como los valores

```python
        user = {
    'name': 'David',
    'age' : 36
    }

    'name' in user.keys() # True
    36 in user.values() # True
```

Si intentamos acceder a una clave que no existe, mediante la sintaxi del corchete `[valor]` el intérprete de py ns dará un error, así que para evitarlo podemos usar otra manera de acceder que es utilizando el método `get()`

```python
    user = {
    'name': 'David',
    'age' : 36
    }

    print(user['job'])
```

![not found](img/img-j-21.png)

### **Métodos**

#### comprehension

```python

simple_dict = {
  'a':2,
  'b':3
}

lista = { key:value**2 for key,value in simple_dict.items()  }

print(lista)# {'a': 4, 'b': 9}

```

#### get()

- Nos permite acceder a claves del diccionario, si no existen nos devuelve un `None`

  ```python
    print(user.get('job')) # None

  ```

- Así evitamos que nos dé un **error**

- Otra función de `get()` es especificar un valor por defecto a esa clave, `pero este valor no se guardará en el dict`

  ```python
    user = {
        'name': 'David',
        'age' : 36
    }

    print(user.get('job','lab')) # lab

    print(user) # {'name': 'David', 'age': 36}

  ```

- Ahora bien si resulta que sí contiene esa clave nos dará el valor contenido en el dict

  ```python
    user = {
        'name': 'David',
        'age' : 36,
        'job' : 'developer'
    }

    print(user.get('job','lab')) # developer
  ```

#### **keys() / values() / items()**

- Obtener todas las claves (keys()) / valores (values() ) del diccionario y obtener una array de los pares clave-valor en forma de tuplas (items()).

  ```python
    prices_lookup = {'apple':2.88, 'oranges':3.56, 'milk':6.12}
    prices_lookup.keys() # dict_keys(['apple', 'oranges', 'milk'])

    prices_lookup.values() # dict_values([3.3, 3.56, 6.12])

    prices_lookup.items() # dict_items([('apple', 3.3), ('oranges', 3.56), ('milk', 6.12)])
  ```

#### **clear()**

- Permite vaciar el diccionario.

  ```python
    user.clear()
    user # {}
  ```

#### **copy()**

- Nos permite hacer copias de diccionarios pero si tenemos objetos dentro se copia la referencia, así que si modificamos uno de estos objetos en la copia del diccionario tb se alterará.

  ```python
  user = {
      'name': 'David',
      'age' : 36,
      'hobbies': ['read', 'play'],
      'job' : 'developer'
  }
  user2 = user.copy()
  user2['hobbies'].append('swing')
  print(user['hobbies']) # ['read', 'play', 'swing']
  ```

- Lo que no afecta es el clear se vaciará un diccionario y el oto se mantendrá inalterado

  ```python
  user = {
      'name': 'David',
      'age' : 36,
      'hobbies': ['read', 'play'],
      'job' : 'developer'
  }
  user2 = user.copy()
  user2['hobbies'].append('swing')
  print(user['hobbies']) # ['read', 'play', 'swing']

  user.clear()

  print(user) # {}
  print(user2)
  # {'name': 'David', 'age': 36, 'hobbies': ['read', 'play', 'swing'], 'job': 'developer'}
  ```

#### **pop()**

- Permite eliminar un item (clave-valor) del diccionario, y nos devuelve el valor

  ```python
  user = {
      'name': 'David',
      'age' : 36,
      'hobbies': ['read', 'play'],
      'job' : 'developer'
  }
  print(user.pop('job')) # developer
  print(user) # {'name': 'David', 'age': 36, 'hobbies': ['read', 'play']}

  ```

#### **update()**

- Permite actulizar un valor pasándole una clave

  ```python
  user = {
      'name': 'David',
      'age' : 36,
      'hobbies': ['read', 'play']
  }

  user.update( {'age':37} )
  print(user) # {'name': 'David', 'age': 37, 'hobbies': ['read', 'play']}

  ```

- si esa clave no existe en el dict se añadirá

  ```python
  user = {
      'name': 'David',
      'age' : 36,
      'hobbies': ['read', 'play']
  }

  user.update( {'job':'developer'} )
  print(user)
  # {'name': 'David', 'age': 36, 'hobbies': ['read', 'play'], 'job': 'developer'}
  ```

## Tuples - data structure -

- Son muy similares a las listas pero tiene la diferencia que son `inmutables`.

      ```python
        t = ('one',2,3, 2)

        t.count(2) # 2
        t.index('one') # 0

        type(t) # tuple

        t[0]   # 'one'
        t[-1]  #3
        len(t) # 4
      ```

  Podemos usar la keyword `in`

      2 in t # True

Podemos usar tb `slicing`

```python
    t = ('one',2,3, 2)
    new_tupple = t[1:3]
    new_tupple #(2, 3)
```

y `unpack`

```python
     x,y,z,*others= (1,2,3,4,5)
     print(others) #[4, 5] como una lista
```

### **Métodos**

Sólo hay dos métodos asociados a tuplas.

#### **Count() / index()**

- Count devulve cuantas veces se encuentra un elemento en la tupla y index cual es la posición de un elemento dado si aparece más de una vez nos devuelve el índice del primero que encuentra.

  ```python
    t = ('one',2,3,2)

    t.count(2) # 2
    t.index('one') # 0

  ```

#### **Sum()**

- Podemos sumar el contenido de las tuplas. Sólo para valores numéricos

  ```python
  r = sum((10,10))  # 20

  ```

## Sets - data structure -

Son colecciones **unordered** y de elementos **no repetidos**.
Podemos crear un set a partir de una list, de esta manera nos aseguramos que los elementos repetidos de la list no se guardan en el set

Tiene esta apariencia:

```python

my_set = {1,2,3,4}
```

```python
      myList = [1,1,1,1,2,2,2,2,3,3,3]

      mySet2 = set(myList)

      mySet2 # {1, 2, 3}

      A = set('qwerty')
      A.add('z')
      print(A) # {'t', 'z', 'w', 'y', 'q', 'r', 'e'}
```

Si hacemos un set de un string éste guardará cada carácter por separado sin repeticiones.

```python
      s = set("paralel")
      s # {'a', 'e', 'l', 'p', 'r'}
```

### **Métodos**

#### **Add()**

- Añadir nuevo elemento

```python
      s = set("paralel")
      s # {'a', 'e', 'l', 'p', 'r'}
      s.add('z')
      s # {'a', 'e', 'l', 'p', 'r', 'z'}

```

#### **clear() / copy()**

- Lo de simpre

#### difference()

- Permite comparar dos sets y ontener las diferencias

```python
    my_set = {1,2,3,4,5}
    your_set = {4,5,6,7,8,9,10}

    print(my_set.difference(your_set))
```

#### discard()

- Elimina un elemento del set, modifica el set

```python
    my_set = {1,2,3,4,5}
    my_set.discard(5)
    print(my_set) # {1, 2, 3, 4}
```

#### difference_update()

- Modifica el set con los elementos que difieren al compararlo con otro

```python
    my_set = {1,2,3,4,5}
    your_set = {4,5,6,7,8,9,10}
    my_set.difference_update(your_set)
    print(my_set) # {1, 2, 3}
```

#### intersection() o &

- Nos da información de los elementos que coinciden entre dos sets
  ```python
  print(my_set.intersection(your_set)) # {4,5}
  print(my_set & your_set) # {4,5}
  ```

#### isdisjoint()

- Nos devuele True (no coiniden elementos ) or False(hay elementos coincidentes) si hay elementos coincidentes entre dos sets
  ```python
  print(my_set.intersection(your_set)) # False el 4 y 5
  ```

#### union() o |

- Permite fusionar dos sets, sin incluir los elementos repetidos claro.

  ```python
  new_set = my_set.union(your_set)
  new_set = my_set | your_set
  new_set # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
  ```

#### issuperset()

- Es para evaluar lo opuesto al subset, si en nuestro set de mayor tamaño se incluye un set menor

  ```python
  my_set = {4,5}
  your_set = {4,5,6,7,8,9,10}

  print(your_set.issuperset(my_set)) # True

  ```

#### **Issubset()**

- Para saber si un set contiene a otro set.

  ```python
    s = set("paralel")

    {'a', 'r'}.issubset(s) # True
  ```

# In/Out with basic Files

Como generar entrada y salida de datos usando un fichero .txt

## Crear un fichero - %%writefile

```python
      %%writefile 'myFile2.txt'
      hello this is a text file
      this is a second line
      this is the third line
```

Después de la sentencia `%%writefile 'myFile2.txt` podemos escribir el texto que contendrá el archivo.

Éste se genera en el path donde se encuentra nuestro script de python. Para saber cual es nuestro path usamos el comando `pwd`.

```python
      pwd
      #'/home/david/Programacion/PYTHON/Python_Course_from_Zero_to_hero/Code/1.Basics/1.Data structures and Objects'
```

## Abrir el fichero - open()

```python
      myFile = open('myFile.txt')
```

Una vez abierto el fichero se vuelca su contenido en una variable en mi caso **myFile**.  
Aquí podemos cometer dos errores:

1. Que escribamos mal el nombre del fichero obteniendo un Errno 2  
   ![not found](img/img-11.png)
2. Que lo busquemos en un path equivocado

## Leer el fichero - .read()

El contenido del fichero lo tenemos en la variable, para leer su contenido usamos read()

```python
      myFile.read()
      #'hello this is a text file \nthis is a second line\nthis is the third line\n'
```

Este método funciona con un cursor de tal modo que cuando lo utilizamos por primera vez el cursor va desde el inicio al final del texto, así si volvemos a utilizar el método, como el cursor está al final, no nos devolverá nada.

## seek()

Si queremos resetear este cursor utilizamos el método seek()

```python
      myFile.seek(0)

```

## readlines()

Permite guardar en una lista cada línea del texto. Tenemos que tener en cuenta que al final de cada línea hay un salto de línea \n

```python
      listLines = myFile.readlines()
      listLines

      '''
      ['hello this is a text file \n',
      'this is a second line\n',
      'this is the third line\n']
      '''
```

## close()

Una vez terminamos el trabajo con el fichero debemos cerrarlo

```python
      myFile.close()
      # si quiero volver a leerlo m da error
      myFile.read() # ValueError: I/O operation on closed file.
```

## With...as

Si no nos queremos preocupar por cerrar archivos podemos utilizar esta sentencia que abrirá el archivo y después de hacer las operaciones pertinentes lo vuelve a cerrar automáticamente.

```python
      with open('myFile.txt') as my_new_File:
          content = my_new_File.read()

      content # #'hello this is a text file \nthis is a second line\nthis is the third line\n'
```

## open() - extendido

Cuando abrimos un archivo la función acepta estos parámetros:  
![not found](img/img-9.png)

El modo puede ser:  
![not found](img/img-10.png)

```python
with open('my_new_file.txt', mode='r') as f:
    print(f.read())
'''
ONE ON FIRST
TWO ON SECOND
THREE ON THIRD
FOUR ON FOURTH
'''
```

### **'a' (append) mode**

- Añade texto al final del documento
  ```python
  with open('my_new_file.txt',mode='a') as f:
      f.write('FOUR ON FOURTH')
  ```

### **w (write) mode**

- Abrirá o creará en su defecto un archivo con ese nombre, si ya existe lo sobreescribe
  ```python
  with open('my_new_file2.txt', mode='w') as f:
    f.write('i created this file')
  ```

## File location

Crear el fichero en una localización concreta

Para abrir un archivo es lo mismo, hay que tener en cuenta si trabajamos en windows entonces usamos los ‘\\’ como separadores o si utilizamos linux o MacOS que usaremos ‘/’
![not found](img/img-12.png)

# Operadores

En python no existe la expresión ++x o x++ hay que escribirlo como x+=1

## Aritméticos

![not found](img/img-13.png)

## Asignación

![not found](img/img-j-22.png)

## Comparación

![not found](img/img-14.png)

## Lógicos

![not found](img/img-15.png)

![not found](img/img-16.png)

## Identidad

![not found](img/img-17.png)

## is vs '=='

### ==

Chequea la igualdad en cuanto a valor

```python
      print(True == 1) #True True == bool(1)
      print('1' == 1 ) # False
      print([] == 1)   # False
      print(10 == 10.0) # True se hace un cast implícito int(10.0)
      print([1,2,3] == [1,2,3])   # True xq compara el valor y son dos list vacías

```

### is

```python
      print(True is 1)            # False
      print('1' is 1 )            # False
      print([] is 1)              # False
      print(10 is 10.0)           # False
      print([1,2,3] is [1,2,3])   # False
```

Chequea la posición de memoria, si el espacio de memoria dnd se almacena el valor es el mismo, en definitiva comparo si ambas variables son el mismo objeto, comparas sus `id()` Hay que tener algo en cuenta, para integers pequeños python cachea sus valores y les da la misma posicion en memeria por eso

```python
    x =1000
    y = 1000

    print(x is y) #False
    print(id(x))  # 140548319852944
    print(id(y)) # 140548319854096
```

en cambio

```python
    x =1
    y = 1

    print(x is y) #True
    print(id(x)) #94354877690624
    print(id(y)) #94354877690624
```

# Condicionales e Iteraciones

## If -elif-else statement

```python
      result = 6

      if result<2 :
          print('it < 2')
      elif result>2 and result < 5:
          print('result is between 2 and 5')
      elif result ==5 :
          print('result is equal to 5')
      elif result == 6 or result== 7:
          print('result can be 6 r 7')
      else :
          print('result is bigger than 2')
```

### **Ternary operator**

```python
    b = True
    r = "hello" if b else "GoodGbye"
    r # hello
```

## For loops

El más sencillo, establecemos un rango.

```python
    for num in range(0,10):
        print(num, end='')
    # 0123456789
```

cuando creo la variable `item` para el loop, ésta sobrevive fuera del loop y como el último elemento es 3 sige conteniendo su valor.

```python
for item in (1,2,3):
    print(item, end="")
print(item, end="") # 1233
```

Con un tercer parámetro (step)

```python
    for num in range(0,10,2):
        print(num, end='')
    # 02468
```

Podemos iterar un **string** como array de caracteres.

```python
      list2 = []

      for caracter in 'David':
          #print(f'{caracter.upper()}', end='') # DAVID
          #list2.append(caracter) # ['D', 'a', 'v', 'i', 'd']
          print(type(caracter)) # nos devuelve tipo string
```

Podemos iterar una **list**

```python
        myList = [1,2,3,4,5,6,7,8,9,10]

        for item in myList:
          print(f'{item}', end=' - ') # 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 -
```

Para conocer el índice de cada elemento lo podemos hacer así:

```python
        myList = [1,2,3,4,5,6,7,8,9,10]

        for index in range(0, len(myList)):
          print(f'{myList[index]}', end=' - ') # 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 -
```

Un truco para obtener el índice de cada elemento de cualquier iterable es transformarlo previamente a un enumerado – enumerate()

```python
      myList = [1,2,3,4,5,6,7,8,9,10]

      for (indice,valor) in enumerate(myList):
        print(f'indice:{indice} => valor:{valor} ')
      '''
        indice:0 => valor:1
        indice:1 => valor:2
        indice:2 => valor:3
        indice:3 => valor:4
        indice:4 => valor:5
        indice:5 => valor:6
        indice:6 => valor:7
        indice:7 => valor:8
        indice:8 => valor:9
        indice:9 => valor:10
      '''
```

Podemos iterar **tuples**

```python
    d = (10, 20, 30)

    for x in d:
      print(f' {x} ', end='')
    #  10  20  30
    #------------------------
        t = [(1,2),(3,4),(5,6),(7,8),(9,10)]

            for (a,b) in t:
                print(f'{a} - {b}')
        '''
          1 - 2
          3 - 4
          5 - 6
          7 - 8
          9 - 10
        ''''
```

Un **dictionary**

Cuando queremos iterar un dictionary, éstos tienen 3 métodos importante : `.values()` `.keys()` `.items()` este último nos devuelve los pares clave-valor en forma de tuples

```python
      d = {"k1":10, "k2":20, "k3":30}

      # como nos devuelve una tuple, se puede hacer unpack y asignar a variables esos pares valor
      for key,value in d.items():
        print(f' {key} - {value} ', end='')
      # k1 - 10  k2 - 20  k3 - 30

      for keys in d.keys(): # values()
        print(f' {keys} ', end='')

      # Por defecto te da las keys
      for x in d:
        print(f' {x} ', end='')
        #k1  k2  k3
```

Podemos obtener solo los valores con .values()

```python
      d = {"k1":1, "k2":2, "k3":3}

      for value in d.values():
          print(f' {value} ', end='')
        # 1  2  3
```

Nested loops

```python
        l= []
        for x in [2,4,6]:
          for y in [1,10,100]:
            l.append(x*y)
        # l = [2,20,200,4,40,400,6,60,600]
```

For loop reverse

```python
      for i in range(len('david')-1,-1,-1):
        print('david'[i], end='')

      # divad
```

anaconda## **While loops**

Versión normal

```python
          x = 0

      while x<5:
          print(f' {x} ', end='')
          x+=1
    # 0  1  2  3  4
```

Versión con else

```python
          x = 0

      while x<5:
          print(f' {x} ', end='')
          x+=1
      else:
        print(f' \nX no es menor q 5')
    # 0  1  2  3  4
    # X no es menor q 5
```

### **While not**

```python
    r = 0

    while not r == 5:
        print(r, end='')
        r+=1
    # 01234
```

## Keywords importantes en los loops

### **Pass**

no hace nada, es decir en python si ejecutamos un loop el programa espera una identación y algo de código...si no hay nada arroja un error, EOF (end of file) para q el programa haga un salto se pone pass  
![not found](img/img-j-2.png)

```python
      x = [1,2,3]

      for item in x:
          # comment
          pass
```

### **Continue**

Esta instrucción permite continuar cn la ejecución del loop sin ejecutar el código que hay por debajo de `continue` (vuelve al loop)

```python
    for c in mystring:
    if c == 'a':
        continue
    print(c)
```

### **Break**

Detiene la ejecución del loop donde está contenido.

```python
    x = 0
    while x<5:
        if x==2:
            break
        print(x)
        x+=1
    # 0
    # 1
```

# Buil-in function útiles

## Map(func,iterable)

Es una función que nos permite mapear otra función sobre un objeto iterable. Cuando decimos mapear significa emparejar un elemento con otro, en este caso aplicamos una función a cada uno de los elementos que integran el objeto iterable(lista o tupla) devolviendo un nuevo iterador tipo `map` cuyos elementos son el resultado de dicha operación.

![not found](img/img-j-14.png)

Para ver lo que almacena el objeto map podemos hacer un for

![not found](img/img-j-15.png)

Si quisieramos obtener los resultados en forma de lista podemos hacer un cast del objeto map directamente  
![not found](img/img-j-16.png)

Otro ejemplo con strings

![not found](img/img-j-17.png)

## Filter(function, iterable)

Es muy parecido a map en el sentido que aplicará una función a cada uno de los elementos de un objeto iterable, con dos diferencias:

1. La función que pasamos debe devolver True or False
2. Nos devolverá un objeto filter únicamente con los elementos del iterable que devuelan True en la función.

![not found](img/img-j-18.png)

## Reduce(function, iterable, [initial_value] )

Nos permite aplicar una función a un iterable y reducir sus items a un único valor `acumulativo`. Ese único valor se obtiene dependiendo de la función pasada.

Para usarlo tenemos que importarlo.

```python
from functools import reduce
```

Funcionamiento:

1. se pasa a la función los dos primeros elementos de la secuencia y se obtiene el resultado.
2. El siguiente paso es aplicar la misma función al resultado obtenido anteriormente y el número que sigue al segundo elemento y el resultado se almacena nuevamente.
3. Este proceso continúa hasta que no quedan más elementos en el contenedor.
   El resultado final devuelto se devuelve y se imprime en la consola.

```python
def accumulator(a, b):
    return a+b


result = reduce(accumulator,['d'+'a'+'v'+'i'+'d'])

print(result) # david
```

```python
def accumulator(a, b):
    return a+b


result = reduce(accumulator,[1,2,3],10)

print(result) #16 =  6 + 10
```

```python
def accumulator(a, b):
    return a if a>b else b


result = reduce(accumulator,[1,2,3,4])

print(result) # 4
```

Podemos definir un valor inicial

## zip()

Permite unir listas y generar tupples con los elementos de cada lista coincidentes en sus posiciones. Zip se ajusta a la lista más corta, si una lisa tiene pej 4 elementos el cuarto no aparecerá. Se puede castear a una lista de tuplas

```python
    list1 = [1,2,3]
    list2 = ['a','b','c']
    lista3 = ['alba','Boni','carlos']

    t = zip(list1,list2, lista3)

    print(t) # <zip object at 0x7f2172294aa0>

    for item in t:
        print(item)
    #(1, 'a', 'alba')
    #(2, 'b', 'Boni')
    #(3, 'c', 'carlos')

    list = list(zip(list1,list2, lista3))
    list # [(1, 'a', 'alba'), (2, 'b', 'Boni'), (3, 'c', 'carlos')]
```

## Lambda

Las expresiones lambdas es como construir una función anónima, es una función que usaremos durante el código pero que no nos interesa definirla como tal.
El contenido de la función lambda debe ser una única expresión en lugar de un bloque de acciones.

```python
def square(num):
    result= num**2
    return result
```

Dada la función de arriba vamos a transformarla en una `lambda`, para ello usamos la keyword `lambda` y eliminamos def y el nombre

Esto se lee como entra un valor **num** y se devuelve el cuadrado de éste

```python
lambda num: num**2
```

Podemos usarla así en nuestro código o asignarla a una variable lo que no es muy habitual

```python
square = lambda num: num**2

square(3) # 9
```

Lo que se hace más habitualmente es usarla junto a otras funciones tipo map o filter

```python
list(map(lambda num: num**2, [1,2,3]))
# [1, 4, 9]
```

```python
list(filter(lambda num: num%2==0, [1,2,3]))
# [2]
```

```python
list(map(lambda name: name[0], ['david','nuri','laura']))
# ['d', 'n', 'l']
```

```python
reduce(lambda x , y : x+y, [1,2,3] )
# 6
```

## Range()

Normalmente lo usamos en los loops, permite crear un rango (start,stop[, step]) con un inicio, final y opcionalmente unos saltos. Este rango puede ser convertido en un List.

```python
    for num in range(0,10,2):
        print(num, end='')
    # 02468
```

Generamos una list con la ayuda de range()

```python
    myList = list(range(0,10,2))
    myList
    # [0, 2, 4, 6, 8]
```

    si no especificamos un número de inicio, range empieza por el 0

```python
    print(list(range(100))) # genera una lista de 0 a 99
```

El tercer valor de `range()` el step puede ser negativo para hacer que el loop decrezca, para ello el primer valor del `range` tiene que ser el mayor

```python
    for i in range(10,0,-1):
        print(i, end=' ')
    # 10 9 8 7 6 5 4 3 2 1
```

## enumerate()

Solo se puede aplicar a objetos iterables y su función es crear un índice para cada elemento del objeto iterable, cada elemento del objeto es separado en tuples formadas por el valor del elemento y su índice.

```python
    for item in enumerate("abcde"):
        print(f"{item}")
    '''
    (0, 'a')
    (1, 'b')
    (2, 'c')
    (3, 'd')
    (4, 'e')
    '''
```

## In / not in

Permita saber si un elemento se encuentra en una lista, un diccionario

```python
    'x' in [1,2,3,4] # False
    1   in [1,2,3,4] # True
    'A' in 'David'  # False
    'a' in 'David'  # True

    d = {'name':'david', 'edad':36}

    'david' in d.values() # True
    'edad'  in d.keys()   # True
```

## Min() max()

Permite detectar el menor valor de una list.

```python
    myList = [1,2,3,20,10,5]
    min(myList) # 1
    max(myList) # 20
```

## Random library

### **shuffle**

Es una librería incluida en python que contienen multitud de funciones.
Para usarla primero hay q importarla

```python
    from random import shuffle  # de la libreria random importa la función shuffle
```

Esta función nos permitirá desordenar la lista aleatoriamente. `Modifica nuestra lista`, no devuelve otra

```python
    from random import shuffle
    myList = [1,2,3,4,5,6,7,8,9,10]

    shuffle(myList)
    myList
    # [9, 8, 3, 10, 2, 4, 6, 5, 7, 1]
```

### Randint

Obtener un integer aleatorio entro de un rango concreto, incluyendo los limites inferior y superior.

```python
    from random import randint

    randint(0,10)
```

## **Input**

Permite al usuario entrar datos. Devuelve un string, podemos castear con int() o float()

```python
    result = input('enter your age: ')

    int(result) #  30
    float(result) #  30.0
```

### Validación input

Hantes de hacer el cast del input nos debemos de asegurar que es convertible.

# Methods and Functions

## Métodos

Documentación de python https://docs.python.org/3/

Para crear una función usamos la keyword `def`(define).  
Para llamar a la función debemos usar los paréntesis (name_function())

En python a diferencia de JavaScript tenemos que definir previamente la función para poderla ejecutar.

El `DOCSTRING` tiene que ir dentro de la función

```python
# Primero la definimos
def name_function():
    '''
    DOCSTRING
    Info: Information about the function
    INPUT: no input...
    OUTPUT: Hello
    '''
    print('Hello')
# ahora la podemos ejecutar
name_function()
```

Podemos usar la función `help()` sobre una función para conocer info sobre ella `help(name_function)`
otra manera de acceder a esta información es usando `magic method`

```python
help(name_function)

print(name_function.__doc__)
```

![not found](img/img-j-3.png)

- Con argumentos por defecto

  ![not found](img/img-j-4.png)

- Return keyword

  **Automáticamente return sale de la función.**

  ![not found](img/img-j-6.png)  
  ![not found](img/img-j-7.png)

### **Argumentos vs parámetros**

Diferncias enre argumento y parámetro:

- Parámetro : es el nómbre que aparece en la definición de la función

```python
def add (param1, param2):
```

- argumento : es el valor que se le pasa a la función

### **Tipos de argumentos**

Tenemos dos tipos de argumentos en las funciones, los argumentos posicionales (positional argument) y argumentos nombrados (keyword argument)

- Posicionales: Los argumentos posicionales deben aparecer al principio de una lista de argumentos o ser pasados como elementos de un iterable precedido por \*.

  ![not found](img/img-j-8.png)

- Nombrados o keyword argument: es un argumento precedido por un identificador (por ejemplo, nombre=) en una llamada a una función o pasado como valor en un diccionario precedido por \*\*. No confundir con argumentos por defecto que es similar pero se usan en la difinición de la función. Aquí sirven si no recordamos el orden de los parámetros usamos la asignación en el momento de la llamada a la función.

  ```python
  complex(real=3, imag=5)
  complex(**{'real': 3, 'imag': 5})
  ```

si paso más parmetros que los definidos en la función voy a tener un error

![not found](img/img-j-9.png)

## Argumentos \*args (arguments) / \*\*kwargs(keywords arguments)

#### \*args

con `*args` estamos diciendo que la función acepta tantos argumentos posicionales como queramos pasarle,
internamente python mete todos los argumentos pasados a la función en una tupla.

![not found](img/img-j-10.png)

#### \*\*kwargs(keywords arguments)

Transforma en un dictionary cualquier número de keyword arguments pasados a la función.
El uso de `**kwargs` nos construye un dictionary con los argumentos pasados

![not found](img/img-j-11.png)

Una función puede aceptar como argumentos un `*args` y un `**kwargs`

![not found](img/img-j-12.png)

Esto será útil cuando usemos librerías externas.

Lo que no podemos hacer es colocar un nuevo elemento después del kwargs pq python lo coge como argumento posicional. Así que primero los argumentos y después los keyword arguments

![not found](img/img-j-13.png)

# Scoope

cuando creamos una variable esta se guarda en lo q llamamos `namespace`. Cada una de estas variables tiene un scope. El scope hace referencia a la visibilidad de ese variable por otras partes de tu código, desde donde es accesible cada variable/función de nuestro programa.  
Básicamente en py tenemos un scoope global, el propio script y un scoope local que es el q se genera cuando creamos una función.

```python
# scoope global o global namespace
x = 0

def some_func():
  # scoope local o namespace local
  x = 20
  return x

print(x)            # 0
print(some_func()) #  20
```

## LEGB Rule

Orden que sigue py para determinar el scoope:

1. L = local(dentro de la función)
2. E = Enclosing function locals (si la función está contenido en otra función)
3. G = global
4. B = built-in python function (son las funiones propias de py)

Cada vez que creamos una función `def some_function():...` definimos un nuevo scope, delimitado por la identación, dentro del global.

Ejemplo de enclosing function:

```python
# global
name = 'this is a global string'

def greet():
  # enclosing function
  name = 'david'
  def hello():
  # local
    print('hello '+name)
  hello()

greet() # hello david
```

Coge el nombre de la función que encierra a hello()

## global keyword

Nos permite acceder a una variable global desde dentro de una función (scoope local)

```python

total = 0

def count():
  global total
  total+=1
  return total

count()
count()
print(count()) #3

```

# OOP - Object Oriented Programming

![not found](img/img-j-25.png)

Repetimos la idea de que todo en python es un objeto, es decir todo está definido como una clase así que todos ellos tienen nos métodos asociados.

Todos los objetos tiene métodos y atributos, a los cuales se puede acceder con notaión de punto.

## Introspección de objetos

Son función propia de python me permite analizar el objeto,comprobar que un objeto es instancia de una clase concreta, conocer sus métdos,...

### isinstance() y issubclass

Todo en python es un objeto, eso es así porque todo hereda de la clase `object`

```python

class Animal:

    def __init__(self, name):
        self.name = name
        print('animal created, with name '+ self.name)

#   CLASE HIJA
class Dog (Animal):
    def __init__(self, name, age):
        Animal.__init__(self,name)
        self.age = age
        print(f'dog created, with name {self.name} and i am {self.age } years old')

my_naimal = Animal('max')
my_dog = Dog('max',10)

isinstance(my_dog,Dog) # True
isinstance(my_dog,Animal) # True
isinstance(my_dog,object) # True

issubclass(Dog,Animal) # True
issubclass(Animal,Dog) # Flase


```

### dir()

Nos da información de todos los métodos y atributos del objeto

```python
dir(my_naimal)
'''
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'age',
 'name',
 'talk']
 '''
```

## Creación de una clase

Podemos definir una clase como :

```python
class MyClass:
  pass
```

o

```python
class MyClass():
  pass
```

Ambas funcionan pero lo más correcto es escribirlo sin '()', los paréntesis solo se usan cuando queremos indicar que nuestra clase deriva de una clase base

```python
class MyClass(BaseClass):
  pass
```

Un ejemplo:

```python
class NameOfClase:

  #-------contructor
  def __init__(self, param1,param2):
    self.param1 = param1
    self.param2 = param2
  #------FIN contructor

  #------Métodos

  def some_method(self):
    #some action
    print(self.param1)
```

Respecto otros lenguajes cambia el uso de la keyword `self` ésta se usa para concretar q el parámetro pasado al contructor formará parte del objeto mismo (de la instancia de la clase) y no es una variable global.

De hecho el resto de lenguajes también tienen este parámetro pero se le pasa autométicamente al constructor sin que lo tengamos que especificar, es el `this` de java o javascript.

Entonces lo que estamos haciendo es decirle estos argumentos que le estoy pasando quiero que formen parte del contenido del objeto.

Lo mismo sucede con los métodos, debemos pasar siempre `self` para poder utilizar los parámetros propios del objeto.

Una vez creada la clase para instanciarla:

```python
# creación de la clase
class Sample:
    pass
# instanciación
s = Sample()
#
type(s)
# __main__.Sample
```

La keyword `__main__` significa que nuestra instancia está asociada a un tipo de clase que se encuentra en nuestro main script.

Si queremos definir un atributo de clase, auqellos que son comunes para todas las instancias de la clase, se debe definir antes del constructor y sin usar self.

Para acceder a este atributo desde dentro de la clase usamos igualmente self.

### Añadimos los métodos

#### constructor **init**

Se ejecuta cuando instanciamos la clase, siempre empieza con la keyword `self` que permite conectar este método a la instancia de la clase y nos permite referirnos al propio objeto, posteriormente le pasamos los atributos que queramos

```python
class Dog:

    # class attribute
    species= 'mammal'

    # constructor
    def __init__ (self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    # definimos métodos
    def bark(self,number):
        print(f'woof! my name is {self.name} and the number is {number} and i\'m ownn to species {self.species}')

```

Para acceder a los atributos de clase usamos notación de punto con la clase o con self : `Circle.pi` o `self.pi`
Como el atributo number no forma parte del objeto no usamos self para referirnos a el.

En el costuctor podemos pasar valores por defecto Dentro del constructor podemos poner un poco de lógica tb

```python
import math
class Circle:
    # class attribute
    pi = math.pi
    # constructor
    def __init__(self,radius=1):
        self.radius= radius
        self.area = self.pi*self.radius**2
        # Circle.pi*self.radius**2

    # class method
    @classmethod
    def printPi(cls):
        cls(10)
        print(Circle.pi)

    @staticmethod
      def printPi():
        print(Circle.pi)


    # instance method
    def get_Circumference(self):
        return 2* self.pi*self.radius
        # 2* Circle.pi*self.radius

    def get_area(self):
        return self.area
```

Método de clase:

Son los métodos que podemos usar sin instanciar un objeto.
Para definir un método de clase tenemos que usar los `decorators` son tags para indicar diferentes cosos, en este caso el tag a utilizar es `@classmethod` y como argumento en lugar de pasar self, que hace referencia al objeto, pasamos `cls` que hace referencia a la clase. Con cls podemos usarlo para instanciar un nuevo objeto dentro del método.

Método statico:

Es la misma idea q un class method pero con la diferencia de que en los static no reciben como parámetro `cls`

Para referirnos a atributos de clase dentro de métodos de un objeto, se les pasa `self`como parámetro, tenemos que utilizar self.attributeName si el método es de clase, no se pasa self como parámetro, entonces tenemos que usar el NombreClase.attribute.

## Características de la Programación Objetos

### Encapsulación

Usando OOP en Python, podemos restringir el acceso a métodos y variables. Esto evita que los datos se modifiquen directamente, lo que se denomina encapsulación. En Python, denotamos atributos privados usando un doble guión bajo como prefijo, es decir, con `__`.

```python
class Sample:
    def __init__(self,name='anonimo', age= 0):
        self.__name = name
        self.__age = age
    def greet(self):
        return f'hello! my name is {self.__name} an i am {self.__age}'

s1 = Sample('david',10)
```

vemos como no he sido capaz de modificar el nombre, lo mismo con métodos

```python
s1.__name = 'ffff'
s1.greet()
# 'hello! my name is david an i am 10'
```

Aunque le hemos asiganado el string 'ffff' sigue poniendo el nombre original

### Herencia

Es cuando creamos una clase usando otra que ya ha sido definida previamente.
Eso nos permite reutilizar código ya que la clase hija hereda las propiedades (métodos y atributos) de la clase padre.

Pasamos la clase madre y luego en el constructor de la hija ejecutamos el métdo `__init__` de la madre.

```python

# CLASE MADRE

class Animal:

    def __init__(self, name):
        self.name = name
        print('animal created, with name '+ self.name)

    def who_i_am(self):
        return f'my name is {self.name}'

    def eat(self):
        print('i am eating')

#   CLASE HIJA
class Dog (Animal):
    def __init__(self, name, age):
        # constructor del padre
        Animal.__init__(self,name)
        # atributo propio de la clase hija
        self.age = age
        print(f'dog created, with name {self.name} and i am {self.age } years old')
     # overwrite method
    def who_i_am(self):
        return f'{Animal.who_i_am(self)} and i am {self.age}')

```

La clase hija Dog hereda el atributo name, aunq no haya hecho un `self.name`.

Para llamar métodos de la clase base podemos usar el nombre (Animal) o usar `super()`, si lo hacemos con super hay algunas diferencias:

1. cuando usas el nombre de la clase base, como en `Animal.__init__(self)` tienes que pasar self (el objeto que está siendo instanciado) como primer argumento. Cuando usas `super().__init__()` en cambio ese argumento no se pone porque super() ya retorna el objeto adecuado que será pasado implícitamente como primer parámetro.

2. También hay diferencias en el caso de la herencia múltiple (una clase que hereda de dos o más clases). En ese caso super() te permite invocar un método de cualquiera de sus clases base sin necesidad de especificar cuál de las clases base lo contiene (super() buscaría cuál de ellas es). Si dos o más clases de las que heredas implementan el mismo método, super() invocará el de la primera que encuentre, siguiendo el Method resolution order (**MRO**), que habitualmente es el orden en que se declararon las clases base (aunque la cosa se puede complicar si estas a su vez heredaron de otras y hay "herencia en diamante").

Herencia en diamente sería este ejemplo:

```python
class A:
  num= 10

class B(A):
  pass

class C(A):
  pass

class D(B,C):
  pass

'''
  A
|   \
B   C
 \D/
'''
```

Para averiguar el orden pdemos usar `nombreObjeto.__mro__` o `nombreObjeto.mro()`
Tiene ese orden por cómo paso las clase `class D(B,C)`primero paso la B así que empieza a buscar primero por la propia (D) y luego va a la B y así...

![not found](img/img-j-26.png)

el ejemplo con **super()**

```python
class Dog (Animal):
    def __init__(self, name, age):

        super().__init__(name)
        self.age = age
        print(f'dog created, with name {self.name} and i am {self.age } years old')
    def who_i_am(self):
       return f'{super().who_i_am()} and i am {self.age}'
```

#### Herencia múltuple

Prmite heredar de más de una clase

```python
class User:
  def sign_in(self):
    print('logged in')

class Wizard(User):

  def __init__(self,name,power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'attacking with power of {self.power}')

class Archer(User):

  def __init__(self,name,arrows):
    self.name = name
    self.arrows = arrows

  def check_arrows(self):
    print(f'arrows left {self.arrows}')

  def run(self):
    print('run very fast')

# Herencia múltiple

class Hybrid(Wizard, Archer):

  def __init__(self,name,power, arrows):
    Wizard.__init__(self,name,power)
    Archer.__init__(self,name,arrows)

```

### Polimorfismo

Está muy relacionado con la herencia. Ya que se base en proveer de un funcionalidad en la clase base y en las clases derivadas sobreescribirán ese método para darle una funcionalidad más específica.

Hay varios tipo de polimorfismo:

1. Sobrecarga de métodos en clases distintas

Cuando dos clases totalmente independientes tienen una funcionalidad(método) con el mismo nombre, si esto sucede podemos usar un mismo objeto para ejecutar dicho método

```python

# DOS CLASES NO RELACIONADAS
class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f'{self.name} says, WOOF! '


class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f'{self.name} says, MEOW! '

# creamos los objetos
niko = Dog('niko')
felix = Cat('felix')
```

podemos iterarlo usando el mismo objeto

```python
for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())
'''
<class '__main__.Dog'>
niko says, WOOF!
<class '__main__.Cat'>
felix says, MEOW!
'''
```

2. Sobrecarga de métodos en clases en herencia
   La diferencia con el punto de arriba es q en este caso las clases están relacionadas así que existe un proceso de sobreescritura de métodos.

```python
class Animal:

    def __init__(self, name):
        self.name = name
        print('animal created, with name '+ self.name)
    def talk(self):
        pass

#   CLASE HIJA
class Dog (Animal):
    def __init__(self, name, age):
        Animal.__init__(self,name)
        self.age = age
        print(f'dog created, with name {self.name} and i am {self.age } years old')
    # overwriting method
    def talk(self):
        pass

```

3. Polymorphism with a Function and objects:

```python
# scoope global

def pet_speak(pet):
    print(pet.speak())

pet_speak(felix)
# felix says, MEOW!
```

Lo más habitual es que se utilice el polimorfismo con clases abstractas.

### Abstracción

es una clase que no puede ser instanciada y que contiene al menos un métodos abstracto (declarados pero sin implementación, éstos tendrán que ser imlementados por las clases derivadas).

Las clases abstractas se usan como clases base para otras clases que derivan de ellas. Con atributos y métodos que puedan compartir cn las sublcases y con métodos abstractos para q éstas los implementen

Para crear una clase abstarcta en python debemos importar la clase `ABC` (Abstract Base Class) del modulo `abc` y hacer q la clase herede esta clase.

```python

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass
        #raise NotImplementedError('SUBCLASS MUST IMPLEMENTED THIS ABSTRACT METHOD')
```

si intentamos instanciar la clase ns saltará el error

![not found](img/img-j-23.png)

Ahora podemos crear una nueva clase que herede de la abstracta, no hace falta q creemos un constructor, lo hereda de la abstracta

````python

class Dog(Animal):

    def speak(self):
        return f'{self.name} says WOOF!'

```python
my_dog = Dog('django')
````

```python
my_dog.name # django
```

```python
my_dog.speak() # 'django says WOOF!'
```

## Métodos especiales or magic methods or dunder methods

Estos métodos nos permiten usar las built-in functions de python en nuestras clases.
Hay una convención para escribir estos métodos mágicos, van entre `__magicMethod__`, por ejemplo `__init__`

### String representation **str()**

Este se usa para mostrar en pantalla nuestro objeto, es la representación en string de nuestro objeto. Para ello debemos sobreescribir el método `__str()__` de nuestra clase. Si no lo sobreescribimos nos devuele el id de la memoria dnd se almacena el onjeto.
Estos nos permite usar estos métodos de la siguiente manera

```python
print(my_dog.__str__()) # <__main__.Dog object at 0x7fc7e32e78d0>
print(str(my_dog)) # <__main__.Dog object at 0x7fc7e32e78d0>
```

### tamaño del objeto **len**

Nos da la idea de "tamaño" de nuestro objeto

### del method **del**

Todos los bjetos en python responden a una acción delete ejecutada por la keyword `del`, podemos sobreescribir este método para que haga algo al eliminar nuestro objeto

```python

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author= author
        self.pages = pages

    # magic methods
    def __str__(self):
        return f'{self.title} by {self.author} with {self.pages} pages'

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')
```

```python
b = Book('Python rocks','david',500)

print(b) # Python rocks by david with 500 pages

len(b) # 500

del b # A book object has been deleted

b

'''
---------------------------------------------------------------------------
NameError          Traceback (most recent call last)
<ipython-input-14-89e6c98d9288> in <module>
----> 1 b

NameError: name 'b' is not defined
'''

```

# Functional Programing

## ¿Que es?

Organiza el código en datos y funciones. Se basa en el concepto de **pure function**.

- Pure function

Tiede dos características:

1. para un mismo input devuelve siempre el mismo output
2. no tiene ningún efecto colateral, no afecta al resto del código

Un ejemplo de programación funcional sería:

```python

# definimos nuestra función
def multiply_by2(li):
    #return [num*2 for num in li]
    return list(map(lambda num:num*2,li ))

# Data
my_list = [1,2,3]
# Funtion
print(multiply_by2(my_list)) # [2, 4, 6]

# comprobamos q no hemos afectado a los datos
print(my_list) # [1,2,3]

```

# Modules and Packages

source: https://stackabuse.com/introduction-to-pythons-collections-module/

## Python Collections Module

Las colecciones son contenedores para almacenar datos, ejemplos de collections son las list, set, tuple, dict, etc Estas son las llamadas built-in collections, colecciones propias de python.

Se han desarrollado varios módulos que proporcionan estructuras de datos adicionales para almacenar colecciones de datos. Uno de esos módulos es el `Collection Module` de Python.

Este módulo contiene varios tipos de estructura de datos las más conocidas son:

1. Counter
2. namedtuple
3. OrderedDict
4. defaultdict
5. deque
6. ChainMap

Para poder usarlos tenemos que importarlos

```python
from collections import defaultdict
from collections import Counter
#...
```

### Counter

Es una subclase de dictionary. Acepta como argumento un objeto iterable o un map y devuelve un dictionary.
En este dictionary tenemos como:

- **clave** los elementos del objeto iterable/map
- **valor** las veces que aparece este elemento en el objeto map/iterable

Para acceder a los elementos usamos

```python
from collections import Counter

iterable_obj = 'aaaaabbbbbccc'

count = Counter(iterable_obj)

count['a'] # 5
```

```python
from collections import Counter

iterable_obj = 'aaaaabbbbbccc'

count = Counter(iterable_obj)

count
# Counter({'a': 5, 'b': 5, 'c': 3})
```

Podemos crear un counter directamente

```python
from collections import Counter

count = Counter({'david':3,'martin':5})

count
# Counter({'david': 3, 'martin': 5})
```

#### Métodos

Counter como es subclase de dict tiene todos los métodos de éste y además tres adicionales:

##### elements()

Nos devuelve los elementos que componen el Counter, tenemos que castearlo a list.

```python
from collections import Counter

count = Counter({'david':2,'martin':2})

print((count.elements())) # <itertools.chain object at 0x7f3ea4a7ab50>
print(list(count.elements())) # count = Counter({'david':2,'martin':2})

```

##### most_common()

Permite ordenar el dictionary resultante, poniendo primero la clave con mayor número de repeticiones

```python
from collections import Counter

iterable_obj = 'aaaaabbbbbccc'
count = Counter(iterable_obj)

print(count.most_common())
# [('a', 5), ('b', 5), ('c', 3)]
```

##### substract([iterable-or-mapping])

Permite restar conteo a las diferentes elementos del counter

```python
from collections import Counter

iterable_obj = 'aaaaabbbbbccc'
count = Counter(iterable_obj)

count.subtract({'a':1,'b':1})

print(count)
 # Counter({'a': 4, 'b': 4, 'c': 3})
print(list(count.elements()))
# ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']
```

### defaultdict

El defaultdict funciona exactamente como un diccionario de Python, excepto que no arroja KeyError cuando intenta acceder a una clave inexistente.

En su lugar, inicializa la clave con el elemento del tipo de datos que pasa como argumento en la creación de defaultdict. El tipo de datos se llama `default_factory`.

Cuando creas un defaultdict tenemos que pasarle como argumento un data type.

```python
from collections import defaultdict

nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2

print(nums['three']) # 0

```

En este ejemplo, int se pasa como `default_factory`. A continuación, se definen los valores para las dos claves, a saber, 'uno' y 'dos', pero en la siguiente línea intentamos acceder a una clave que aún no se ha definido.

En un diccionario normal, esto forzará un KeyError. Pero defaultdict inicializa la nueva clave con el valor predeterminado de `default_factory`, que es 0 para int. Por lo tanto, cuando se ejecute el programa, se imprimirá 0.

- Ejemplo 1 - contar nombres

  ```python
  from collections import defaultdict

  count = defaultdict(int)
  names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
  for names in names_list:
      count[names] +=1

  print(count)
  #defaultdict(<class 'int'>, {'Mike': 5, 'Britney': 1, 'John': 3, 'Smith': 2, 'Anna': 2})
  ```

- Ejemplo 2 - conteo de mayúsculas minúsculas

  ```python
  from collections import defaultdict
  count = defaultdict(int)

  def up_low(s):
      for letter in s:
          if letter.isupper():
              count['upper']+=1
          elif letter.islower():
              count['lower']+=1
          else:
              continue
      print(f'Original String : {s} \n No. of Upper case characters : {count["upper"]} \n No. of Lower case Characters :{count["lower"]} ')

  s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
  up_low(s)
  ```

### OrderedDict

source: https://stackabuse.com/introduction-to-pythons-collections-module/

## PIP

Es un gestor de paquetes para python tipo npm para nodeJS. Se instala cuando instalamos anaconda.

## PyPI (python package index)

Si queremos usar pip fuera del entorno de `anaconda` tenemos que usarlo como:
```
pip3 install nombrePaquete
```
Esto es xq en linux el comando pip hace referencia a python2 y nosotros ya tenemos instalado python 3.

Es un repositorio open-source de paquetes de terceros para python.
Para instalar estor paquetes usamos `pip install `

Instalamos un paquete como ejemplo:

1. colorama
   Espara poder poner texto en distintos colores
   en la terminal

```
pip install colorama
```

```python
from colorama import init

init()

from colorama import Fore

print(Fore.RED+ "some red text")
```

## Escribiendo nuestros propios Módulos y paquetes

En primer lugar un módulo es un archivo .py que contiene un script hecho en python y que lo importamos en otro script.
En cambio un paquete es una colección de módulos, es una carpeta que contiene uno o más módulos.

### creando un módulo

Tenemos un script llamado `myprogram.py` y otro `mymodule.py`.

En mymodule tenemos las siguiente función:

```python

def my_func():
    print('hello from my python module ')

```

y en el programa importamos este módulo. Hay dos maneras

```python

import mymodule

mymodule.my_func()

```

ó

```python

from mymodule import my_func

my_func()

```

### creando un paquete

Para que python reconozca el directorio como un package tenemos que crear en la carpeta principal y en las subcarpetas un archivo `__init__.py`.

No es necesario escribir nada en ese archivo, sólo estar resente.

![not found](img/img-j-24.png)

Una vez creado el package tenemos que importarlo y tenemos varias opciones:

1. importamos el módulo deseado

   1. del package principal principal

      ```python

      from MyMainPackage import some_main_script

      some_main_script.report_main()
      # hey! i am in some_main_script in main package

      ```

   2. del subPackage

      ```python

      from MyMainPackage.SubPackage import my_sub_script

      my_sub_script.sub_report()
      # hey! i am a function inside mysubPackage
      ```

2. podemos importar una función concreta

   ```python

   from MyMainPackage.SubPackage import my_sub_script

   my_sub_script.sub_report()
   # hey! i am a function inside mysubPackage
   ```

3. podemos importar funciones directamente desde el módulo

   1. Para ello usamos el archivo `__init__.py` en eĺ hacemos los imports de las funciones que queramos

      ```python
      from .some_main_script import report_main
      from .SubPackage.my_sub_script import sub_report
      ```

   2. Y en el archivo del programa importamos el package directamente y ya puedo usar las funciones del archivo `__init__.py`

      ```python
      import MyMainPackage

      MyMainPackage.report_main()
      MyMainPackage.sub_report()
      ```

   3. o bien puedo importar las funciones

      ```python
      from  MyMainPackage import  report_main, sub_report

      report_main()
      sub_report()
      ```

## **name**

Igual que tenemos buil-in function tipo print() también hay built-in varibales, y una de ellas es `__name__` .

Cuando ejecutamos un script directamente esta variable se le asigna el string `__main__`

Se usa con un propósito organizativo del código, sería algo así:

```python

def func():
  pass

def func2():
  pass

if __name__ == '__main__':
    func2()
    func()
```

# Decorators

## First class citizens

Se usan junto con funciones. En python las funciones son lo que llamas `first class citizens` esto es que actuan como variables, tienen un nombre que hace de apuntado a una localización de memoria, incluso se pueden pasar como argumento de otra función.

Si yo tengo

```python
def hello():
  return 'hellllooo'
# así almaceno la referencia hacia el espacio de memoria dnd se encuentra la función
greet = hello
# así guardo el resultado ('hellooo') en la variable greet2
greet2 = hello()
```

Ahora quiero eliminar la función hello()

```python
del hello
```

Python elimina la referencia hello pero la función sigue estando en el espacio de memoria pq hay otra referencia (greet) que está apuntando.

Una vez explicado esto con los `decorators` nos permiten potenciar las funciones, dotarlas de funciones extra.

## HOC - Higher Order Function

Las funcoines de alto grado son aquellas que acceptan otras funciones como argumento. Por ejemplo `map()` sería una HOC

## Decorators syntaxi

Potencian funciones tipo `HOC`
Tienen esta sintaxis:

1. una función HOC (my_decorator)
2. En ésta definimos otra función que ejecuta la función pasada por agumento (wrap_func)
3. Devolvemos la wrap_func

```python
def my_decorator(func):

    def wrap_func(str, emoji):
        print('*********')
        func(str, emoji)
        print('*********')
    return wrap_func
```

Esta estructura es reconocida por python y la podemos emplear como decorator poniendo una @ delante

```python
@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)

print(hello('hellooo', ':)'))

'''
*********
hellooo :)
*********
'''
```

El decorator funciona como si ejecutara la función wrap_func, por lo que imprime los asteríscos y ejecuta mi función (hello).

Si lo hicieramos manual sería algo así:

```python
my_decorator(hello)()
```

ejecutamos lo q devuelve my_decorator

Lo más habitual es que la sintaxi para definir el decorator y no tener q ir modificando según el número de argumentos q le pasamos a la función es usando `*args` and `**kwars`:

Patrón decorator:

```python
def my_decorator2(func):

    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func


@my_decorator2
def hello(greeting, emoji=':p'):
    print(greeting, emoji)

print(hello('hellooo'))
'''
*********
hellooo :p
*********
'''
```

## Para que usamos los decorators

```python
from time import  time

def performance(fn):
    def wrapper(*args,**kwargs):
        t1 = time()
        fn(*args,**kwargs)
        t2 = time()
        print(f'it took {t2-t1}')
    return wrapper

@performance
def long_time():
    for x in range(100000000):
        x*5

long_time()
```

# Errores y gestión de excepciones

Cuando en nuestro código se realizan ciertas funciones que pueden ocasionar un error, como por ejemplo leer un archivo, tenemos que gestionar ese posible error, ya que cuando se produce el error se detiene la ejecución del programa.

Los diferentes tipos de errores/excepciones que se pueden generar son:
[Buil-in exception](https://docs.python.org/3.8/library/exceptions.html#bltin-exceptions)

Para ello utilizamos el bloque `try-except-else` o `try-except-finally`.

- try:
  en este bloque escribimos el código que es susceptible de generar un error
- except:
  bloque que contiene el código que se ejecutará en el caso que el try falle.
- else:
  Se ejecuta cuando no se genera ningún error
- finally:
  código que se ejecutará siempre al terminar el bloque, haya o no generado un error.

```python
try:
    result = 10+10
except:
    print('something went wrong!')
else:
    print('add went well')
    print(result)

print('el programa sigue...')

'''
add went well
20
el programa sigue...
'''
```

cuando hay un error

```python
try:
    result = 10+ '10'
except:
    print('something went wrong!')
else:
    print('add went well')
    print(result)

print('el programa sigue...')

'''
something went wrong!
el programa sigue..
'''
```

- Bloque try-except-finally

```python
try:
    with open('testFile.txt','w') as f:
        f.write('write a test line')
except TypeError:
   print('there was a type error')
except OSError: # cuando hayun error relacionado con manipulación de archivos
    print('hey you have an OS error')
except: # se ejecutará ante cualquier otro tipo de error
    print('cualquier otro tipo de error')
else: # se ejecuta cuando el try tiene éxito
    with open('testFile.txt','r') as f:
       print(f.read())
finally:
    print(' i always run')
'''
write a test line
i always run
'''
```

si forzamos un error, vemos como el bloque finally se ejecuta siempre

```python
try:
    with open('testFile.txt','r') as f:
        f.write('write a test line')
except TypeError:
   print('there was a type error')
except OSError: # cuando hay un error relacionado con manipulación de archivos
    print('hey you have an OS error')
except:
    print('cualquier otro tipo de error')
finally:
    print(' i always run')

'''
hey you have an OS error
i always run
'''
```
Si queremos saber de qué tipo es el error que nos está generando el código podemos utilizar la función 
`{sys.exc_info()`. Es de tipo tupla y contiene `(type, value, traceback)` 

Para capturar cualquier error y poder imprimir una explicación podemos utilizar en el bloque except la clase base de la q heredan el resto de excepciones `BaseException` or `Exception` con la sugiente sintaxi `except BaseException as err:` en este caso err contiene una explcación del error.

Si como usuarios debemos crear una clase que genere errores heredará de `Exception` no de `BaseException`.

```python
try:
    result = 10+'10'
except BaseException as err:
    print('something went wrong!\n')
    print(f'sys.exc_info() es una => {type(sys.exc_info())}')
    print(f'{sys.exc_info()}\n')
    print(f'{err} \n')
else:
    print('add went well')
    print(result)

print('el programa sigue...')

'''
something went wrong!

sys.exc_info() es una => <class 'tuple'>
(
  <class 'TypeError'>, 
  TypeError("unsupported operand type(s) for +: 'int' and 'str'"), 
  <traceback object at 0x7f089108fc30>
)

unsupported operand type(s) for +: 'int' and 'str' 

el programa sigue..

'''

```

También podemos combinar diferentes tipos de errores en except

```python
def dividir(x,y):
    try:
        return x/y
    except (TypeError, ZeroDivisionError) as err:
        print(err)

dividir(5,'0')
'''
unsupported operand type(s) for /: 'int' and 'str'
'''
```

```python
dividir(5,0)
'''
division by zero
'''
```



```python

try:
    with open('testFile.txt','r') as f:
        f.write('write a test line')
except TypeError:
   print('there was a type error')
except:
    print(f'cualquier otro tipo de error {sys.exc_info()}')
else:
    with open('testFile.txt','r') as f:
       print(f.read())
finally:
    print(' i always run')
'''
cualquier otro tipo de error
 (<class 'io.UnsupportedOperation'>,
 UnsupportedOperation('not writable'),
 <traceback object at 0x7f6efd31aac0>)
 i always run
'''
```

Este ejemplo nos permite mediante la combinación de `while` y `try-except` preguntar tantas veces por un número hasta que facilitemos uno correcto

```python
def ask_for_int():
    while True:
        try:
            result = int(input('say a number: '))
        except:
            print('thats not a number')
            print('i am gonna ask u again!')
        else:
            print('thaks you!')
            print(f'your number in : {result}')
            break

```

## Lanzar nuestras propias excepciones

Para lanzar una excepción usamos la keyword `raise()`

```python
raise Exception('hey cut it out')
```

![not found](img/img-j-30.png)


# Unit testing

Hay varias librerías dedicadas a ello pero dos de las más habituales son:

- Pylint
  Revisa tu código y nos reporta posibles errores

- unittest
  Permite testear nuestro programa comproando si obtenemos los outputs deseados. 

## Pylint

instalamos pylint

```
pip install pylint
```
escribimos algo de código

```python
a = 1
b = 2
print(a)
print(B) # tenemos un error

```

Para analizar el código con pylint tecleamos en terminal

```
pylint simple1.py -r y
```
Y no imprime en consola un report con errores de estilo, de sintaxi,...

![not found](img/img-j-27.png)

Para mejorar el código:

```python

'''
a very simple script
'''
    
def myfunc():
    '''
    simple function
    '''
    first = 1
    second = 2
    print(first)
    print(second)
    
myfunc()

```

## unittest

Es una libreria built-in python, por lo que debemos importarla para poder utilizarla. 

Para escribir test unitarios y probar nuestro programa debemos crear una clase en un script a parte. Esta clase heredará de `unittest.testCase`.

 Debemos también importar el script que queramos testear.

 ```python
def cap_text(text):
    '''
    input a string
    Output a string capitalized
    '''
    return text.capitalize()

 ```

Escribimos nnuestros test en un script a parte


```python
import unittest
import cap

class Test_cap(unittest.TestCase):
    
    def test_cap(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Monty Python')

if __name__ == '__main__':
    unittest.main()
```

Ejecutamos el test

![not fond](img/img-j-28.png)

arreglamos el error 

 ```python
def cap_text(text):
    '''
    input a string
    Output a string capitalized
    '''
    return text.title()

 ```

 ![not found](img/img-j-29.png)
---
---

# pygame

source [video youtube](https://www.youtube.com/watch?v=FfWpgLFMI7w&t=4370s)  

Instalamos el móduo `pygame`para crear juegos con python

```
pip install pygame
```
## Estructura del archivo

Tendremos dos partes bien diferenciadas:

1. Donde hacemos los imports y cargamos las imagenes q necesitaremos durante el juego
   ```python
    # Imports
    import pygame
    import os
    import time
    import random
    #--------FIN IMPORTS

    # habilitamos fuentes 
    pygame.font.init()
    #-------------------
    # create The screen
    WIDTH,HEIGHT = 750,750
    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
    ## title and icon on windows game
    pygame.display.set_caption('Space Invaders')
    icon = pygame.image.load(os.path.join('utils','ufo.png'))
    pygame.display.set_icon(icon)
    #-----------------------------------

    # Load images
    ## LOAD ENEMY IMAGES
    RED_SPACE_SHIP = pygame.image.load(os.path.join("utils","enemy_1.png"))
    GREEN_SPACE_SHIP = pygame.image.load(os.path.join("utils","enemy_2.png"))
    BLUE_SPACE_SHIP = pygame.image.load(os.path.join("utils","enemy_3.png"))
    ## LOAD PLAYER SHIP
    PLAYER_SHIP = pygame.image.load(os.path.join("utils","player.png"))
    ## lASER ENEMY
    RED_LASER = pygame.image.load(os.path.join('utils','pixel_laser_red.png'))
    GREEN_LASER = pygame.image.load(os.path.join('utils','pixel_laser_green.png'))
    BLUE_LASER = pygame.image.load(os.path.join('utils','pixel_laser_blue.png'))
    ## PLAYER laser
    PLAYER_LASER = pygame.image.load(os.path.join('utils','bullet.png'))
    ## BACKGROUND IMAGES
    BG = pygame.transform.scale(pygame.image.load(os.path.join('utils','background.png')), (WIDTH,HEIGHT))
    #-----------------END LOAD IMAGES
   ``` 

2. Definimos una función `main()` que contendrá la lógica del juego y que llamaremos al final del script.
   ```python
    def main():
        run = True
        FPS = 60

        level = 1
        lives= 5
        main_font = pygame.font.SysFont('comcsans',50)
        
        clock = pygame.time.Clock()
        
        def redraw_window():
            SCREEN.blit(BG,(0,0))
            pygame.display.update()
        
        while run:
            clock.tick(FPS) # para q se actualiza a la vez q el refresco de panatalla
            redraw_window()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


    main()
   ```  

## Ventana de juego

## Fijar tamaño, titulo, icono

```python
import pygame
import os

# create The screen
WIDTH,HEIGHT = 750,750
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
## title and icon on windows game
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load(os.path.join('utils','ufo.png'))
pygame.display.set_icon(icon)
#-----------------------------------
```
## Establecemos el fondo de la ventana de juego

Creamos una función que llamaremos repetidamente para mostar la imagen de fondo.

- blit()
  llamamos al método `blit()`de la pantalla para dibujar la imagen de fondo (BG) a cogiendo como coordenadas (X=0,y=0) como la imagen puede q no coincida en tamaño la transformamos
- display.update()
  Hace q la imagen se muestre en la ventana  

```python
BG = pygame.transform.scale(pygame.image.load(os.path.join('utils','background.png')), (WIDTH,HEIGHT))

def redraw_window():
    SCREEN.blit(BG,(0,0))
    pygame.display.update()
```

## mostramos Info

Para ello necesitamos habilitar fuentes , lo hacemos justo después de los imports.

```python
pygame.font.init()
```
Generamos un reloj, para contabilizar el tiempo

```python
clock = pygame.time.Clock()
```





