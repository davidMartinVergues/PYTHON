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
    - [Algunas operaciones](#algunas-operaciones)
  - [Uso de variables](#uso-de-variables)
  - [Uso del método print()](#uso-del-método-print)
  - [String](#string)
    - [Propiedades de los strings](#propiedades-de-los-strings)
    - [Métodos de los strings](#métodos-de-los-strings)
      - [Slicing](#slicing)
      - [upper() lower() split()](#upper-lower-split)
      - [format](#format)
      - [Casefold](#casefold)
      - [find](#find)
      - [Capitalize](#capitalize)
  - [List](#list)
    - [Métodos](#métodos)
      - [len()](#len)
      - [Slicing](#slicing-1)
      - [Append() pop()](#append-pop)
      - [Sort() sorted() reverse()](#sort-sorted-reverse)
      - [Lista de elementos](#lista-de-elementos)
      - [Count()](#count)
      - [All() any()](#all-any)
      - [Join()](#join)
      - [Index()](#index)
  - [Dictionaries](#dictionaries)
    - [Métodos](#métodos-1)
      - [keys() / values() / items()](#keys--values--items)
  - [Tuples](#tuples)
    - [Métodos](#métodos-2)
      - [Count() / index()](#count--index)
      - [Sum()](#sum)
  - [Sets](#sets)
    - [Métodos](#métodos-3)
      - [Add()](#add)
      - [Issubset()](#issubset)
- [In/Out with basic Files](#inout-with-basic-files)
  - [Crear un fichero - %%writefile](#crear-un-fichero---writefile)
  - [Abrir el fichero - open()](#abrir-el-fichero---open)
  - [Leer el fichero - .read()](#leer-el-fichero---read)
  - [seek()](#seek)
  - [readlines()](#readlines)
  - [close()](#close)
  - [With...as](#withas)
  - [open() - extendido](#open---extendido)
    - ['a' (append) mode](#a-append-mode)
    - [w (write) mode](#w-write-mode)
  - [File location](#file-location)
- [Operadores](#operadores)
  - [Aritméticos](#aritméticos)
  - [Comparación](#comparación)
  - [Lógicos](#lógicos)
  - [Identidad](#identidad)
- [Condicionales e Iteraciones](#condicionales-e-iteraciones)
  - [If -elif-else statement](#if--elif-else-statement)
    - [Ternary operator](#ternary-operator)
  - [For loops](#for-loops)

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

```
  # comentario monolínea
  '''
    comentario de bloque
  '''
```

## Fundamental Data Types
Son los tipos especificados en el core de python tales como :  
![not found](img/img-8.png)

Tenemos otros tipos de datos como:  

- ### Custom Types - Class
  Podemos crear nuestros propios tipos de datos, para ello construimos clases.
- ### Specialized Data Type
  Son aquellos que están especificados en paquetes externos, los llamados `modules`.
- ### None - type  
    Indica ausencia de valor

### Algunas operaciones

    ```
      # para hacer potencias de un número

      print(2**3) # 8

      # Para obtener la parte entera de una división decimal //

      print(2//4 ) # 0
      print(5//4 ) #  1

      # Para obtener el resto de una división el módulo %

      print(5 % 4) # 1
      print(6 % 4 )# 2
    ```
## Uso de variables

Python usa tipado dinámico como JavaScript esto significa que no es necesario especificar el tipo de dato que contendrá dicha variable.
Por ejemplo Java tiene un tipado estático porque requiere que especifiquemos durante la declaración el tipo de dato que contendrá la variable.  
 Podemos usar `type()` para saber el tipo de variable  
 Usamos la función `str()` para **castear** a string.

```
  # Tipado dinámico

  my_dogs = 2

  print('tipo de mi variable ' + str(type(my_dogs))) # tipo de mi variable <class 'int'>

  my_dogs = ['sammy','frankie']

  print('mi variable ha cambiado de tipo, ahora es una list ' + str(type(my_dogs)) +' -> ' +str(my_dogs))
  # mi variable ha cambiado de tipo, ahora es una list <class 'list'> -> ['sammy', 'frankie']
```

## Uso del método print()

Para imprimir contenido usamos el método print(), éste acepta un atributo para indicar que no haga salto de página end=’’.

```
  for x in range(10):
    print(x, end='')

  # 0123456789
```

## String

Funcionan como arrays así que usando el índice podemos extraer letras del string.
Está habilitado el reverse index(indice reverso) así sin conocer la longitud del string podemos extraer el último carácter(poner el índice en negativo: -1).

```
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

### Propiedades de los strings

- 1. Son inmutables, no podemos modificar un string

     ```
       name = 'David'
       name[0]= 'P'

       # 'str' object does not support item assignment por lo tanto strings inmutables
     ```

- 2. Concatenables

     ```
       x = "hello world"

       y = ' is beatifull outside'

       x+= y
       print(x) #hello world is beatifull outside

       name = 'David'

       name = 'P'+ name[1:]
       name #'Pavid'
     ```

- 3. Multiplicables

     ```
      name = 'd'

      name\*10 # dddddddddddd

     ```

### Métodos de los strings

#### Slicing

- [start:stop:step] nos permite obtener un subString  
   stop - indica hasta dnd se extrae pero sin incluir ese caracter  
   step - divide en str en grupos de X carcateres y nos devuelve el
  primer caracter de cada grupo

  ```
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

#### upper() lower() split()

- ```
    x = "hi this is a string"
    print(x.upper()) #HI THIS IS A STRING
    print(x.lower()) #hi this is a string
    print(x.split()) #['hi', 'this', 'is', 'a', 'string']
    print(x.split('i')) #['h', ' th', 's ', 's a str', 'ng']
  ```

#### format

- Format method
    ```
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
- Float formatting
  {value:width.precision f}  
   Value => ponemos el valor del número  
   Width => tamaño que ocupará el número hecho string (nº de caracteres)  
   Precision => número de decimales que tendrá
    ```
        result = 1.2987012987012987

        print('mi valor es {r:1.3f}'.format(r=result))
        #mi valor es 1.299
        print('mi valor es {r:10.3f}'.format(r=result))
        #mi valor es      1.299
    ```
- f-string = formated string literal
    ```
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

#### Casefold
- Es como un equalsIgnoreCase de java, elimina las distinciones entre mayúsculas y minúsculas en el momento de comparar strings.
    ```
      str1 = 'david'
      str2 = 'DAVID'

      if str1 == str2:
        print('son iguales')
      else:
        print('son diferentes')
      # son diferentes
    ```
  usando casefold()
    ```
      str1 = 'david'
      str2 = 'DAVID'

      if str1 == str2.casefold():
        print('son iguales')
      else:
        print('son diferentes')
      # son iguales
    ```
#### find
- Sólo funciona en estrings, para saber si un string contiene a otro y si lo está nos devuelve la posición y si no un -1. Hace distinción entra minusculas y mayúsculas.
    ```
      str1 = 'david'
      str2 = 'hello david'

      str2.find(str1) #6
      str2.find('ello') #1
      str2.find('Hello') #-1
    ```
#### Capitalize
- La primera letra de una palabra en mayúscula.
    ```
      def old_macdonald(name):
          first_part = name[:3]
          second_part = name[3:]

          return first_part.capitalize()+second_part.capitalize()

      old_macdonald('macdonald') #'MacDonald'
    ```
## List
Secuencia ordenada de elementos que pueden ser de diferentes tipos(numbers, string,obj...). Podemos tener distintos tipos de datos almacenados en un list.  

### Métodos

#### len()
- Conocer el número de elementos de la list.  

    ```
      my_List = []

      my_List = ['string', 100, 20.3,1,2,3]

      # len()
      len(my_List)
    ```
#### Slicing

- [start:stop:step]  
  Funciona igual que en los strings.

    ```
      my_List[-1]     # 3
      my_List[4:]     #  [2, 3]
      my_List[:3]     #  ['string', 100, 20.3]
      my_List[::2]    #  ['string', 20.3, 2]
      my_List*2       # ['string', 100, 20.3, 1, 2, 3, 'string', 100, 20.3, 1, 2, 3]
    ```

  Podemos concatenar list sumándolas

    ```
      my_list_1 = [1,2,3,4,5]
      my_list_2 = [6,7,8,9,10]

      my_list_1+=my_list_2

      my_list_2 # [6, 7, 8, 9, 10]
      my_list_1 # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ```

#### Append() pop()

- Nos permite añadir(append) o eliminar (pop) un elemento al final de la list.
  El método pop() no solo elimina el último elemento sino que también lo devuelve. Una función más es que puedes pasar el índice del elementos a eliminar, por defecto es el -1 (último elemento).

    ```
      my_list = ['one', 'two','three','four','five','six']

      my_list.append('eight')

      my_list # ['one', 'two', 'three', 'four', 'five', 'six', 'eight']

      element_deleted = my_list.pop()

      element_deleted # 'eight'

      my_list # ['one', 'two', 'three', 'four', 'five', 'six']

      my_list.pop(0) # 'one'
      my_list         # ['two', 'three', 'four', 'five', 'six']
    ```

#### Sort() sorted() reverse()

- Ninguno de los dos métodos devuelve nada, actúan sobre la list y la modifican

    ```
      char_list = ['a','d','c','e','f','b']
      num_list = [10,2,4,1,0]

      char_list.sort()
      num_list.reverse()

      print(char_list) # ['a', 'b', 'c', 'd', 'e', 'f']
      print(num_list)  # [0, 1, 4, 2, 10]
    ```

  El método sorted() devuelve la lista ordenada pero no modifica la original.

    ```
      list4 = [5,3,4,6,1]

      listOrdenada = sorted(list4)

      print(list4)        # [5, 3, 4, 6, 1]
      print(listOrdenada) # [1, 3, 4, 5, 6]
    ```
#### Lista de elementos
- Si quisiéramos obtener una lista de las letras que forman un string podemos hacer lo siguiente:

    ```
      word = 'word'

      l = []

      for letter in word:
          l.append(letter)

      print(l) # ['w', 'o', 'r', 'd']
    ```

  Pero una manera de hacerlo más fácil es:
  subelement **for** subelemento **in** element

    ```
      word = 'word'

      l = [letter for letter in word]

      l # ['w', 'o', 'r', 'd']
    ```

  Range

    ```
      l=  [num for num in range(0,10)]
      l # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```

  Podemos aplicar cambios a cada subelemento antes de incluirlo en la list, por ejemplo hacer el cuadrado de cada elemento **num**2\*\*

    ```
      l=  [num**2 for num in range(0,10)]
      l # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```

  Podemos añadir condiciones

    ```
      l=  [num**2 for num in range(0,10) if num%2 ==0]
      l # [0, 4, 16, 36, 64]

    ```

  incluso if else

    ```
      l=  [num if num%2==0 else 'impar' for num in range(0,10)]
      l # [0, 'impar', 2, 'impar', 4, 'impar', 6, 'impar', 8, 'impar']

    ```

  Incluso podemos añadir operaciones

    ```
      celcius = [0,10,20,34.5]

      fahrenheit = [ ((9/5)*temp+32) for temp in celcius ]

      fahrenheit #[32.0, 50.0, 68.0, 94.1]


    ```

  Nested loops

    ```
      l = []

      for x in [2,4,6]:
          for y in [1,10,100]:
              l.append(x*y)
      l # [2, 20, 200, 4, 40, 400, 6, 60, 600]
    ```

#### Count()

- Las veces q aparece un elemento en una lista

    ```
      l = [0,2,2,10,20,34.5]

      print(l.count(2)) # 2
    ```
#### All() any()

- Nos permite saber si una lista contiene todos (all) los valores o sólo algunos (any) de otra lista

    ```
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

#### Join()

- Permite concatenar los elementos de una lista mediante algún caracter, por ejemplo un espacio en blanco

    ```
      l = ['hola','david']

      ' '.join(l) # 'hola david'

    ```
#### Index()

- Nos devuelve la posición de una valor en la list, el primero que encuetra
    ```
      l1 = [1,2,3]
      l1.index(3) # 2
    ```

## Dictionaries

Son mapas desordenados (no pueden ser ordenador) para almacenar objetos usando los pares **clave-valor**.
Normalmente los usamos cuando queremos tener dos valores que están relacionados por ejemplo precios de productos, así no necesitamos saber el índice del producto para saber el precio.   

    ```
        prices_lookup = {'apple':2.88, 'oranges':3.56, 'milk':6.12}

        print('precio de las manzanas {:<10.5f} €'.format(prices_lookup['apple']))
        # precio de las manzanas 2.88000    €

        prices_lookup # {'apple': 2.88, 'oranges': 3.56, 'milk': 6.12}

    ```

Dentro de los diccionarios podemos almacenar listas y otros diccionarios.

    ```
      d = {'numbers':123,'list':[1,2,3],'dict':{'nombre':'david','apellido':'martin'}}

      d['numbers'] # 123
      d['list'][0] #1
      print('me llamo {} {} '.format(d['dict']['nombre'], d['dict']['apellido'])) # me llamo david martin
    ```

Añadir / sobreescribir / borrar (del) elementos de un diccionario

    ```
      prices_lookup = {'apple':2.88, 'oranges':3.56, 'milk':6.12}

      prices_lookup['melon'] = 5.86

      prices_lookup['apple']= 3.30

      prices_lookup # {'apple': 3.3, 'oranges': 3.56, 'milk': 6.12, 'melon': 5.86}

      del prices_lookup['melon']

      prices_lookup # {'apple': 3.3, 'oranges': 3.56, 'milk': 6.12}

    ```
### Métodos

#### keys() / values() / items()

- Obtener todas las claves/ valores del diccionario y obtener una array de los pares clave-valor en forma de duplas.

    ```
      prices_lookup = {'apple':2.88, 'oranges':3.56, 'milk':6.12}
      prices_lookup.keys() # dict_keys(['apple', 'oranges', 'milk'])

      prices_lookup.values() # dict_values([3.3, 3.56, 6.12])

      prices_lookup.items() # dict_items([('apple', 3.3), ('oranges', 3.56), ('milk', 6.12)])
    ```

## Tuples

Son muy similares a las listas pero tiene la diferencia que son inmutables.

    ```
      t = ('one',2,3, 2)

      t.count(2) # 2
      t.index('one') # 0

      type(t) # tuple

      t[0]   # 'one'
      t[-1]  #3
      len(t) # 4
    ```

### Métodos

Sólo hay dos métodos asociados a tuplas.

#### Count() / index()

- Count devulve cuantas veces se encuentra un elemento en la tupla y index cual es la posición de un elemento dado si aparece más de una vez nos devuelve el índice del primero que encuentra.

    ```
      t = ('one',2,3, 2)

      t.count(2) # 2
      t.index('one') # 0

    ```

#### Sum()

- Podemos sumar el contenido de las tuplas. Sólo para valores numéricos

    ```
    r = sum((10,10))  # 20

    ```

## Sets

Son colecciones sin **un orden** y de elementos **no repetidos**.
Podemos crear un set a partir de una list, de esta manera nos aseguramos que los elementos repetidos de la list no se guardan en el set

    ```
      myList = [1,1,1,1,2,2,2,2,3,3,3]

      mySet2 = set(myList)

      mySet2 # {1, 2, 3}

      A = set('qwerty')
      A.add('z')
      print(A) # {'t', 'z', 'w', 'y', 'q', 'r', 'e'}
    ```

Si hacemos un set de un string éste guardará cada carácter por separado sin repeticiones.

    ```
      s = set("paralel")
      s # {'a', 'e', 'l', 'p', 'r'}
    ```

### Métodos

#### Add()

- Añadir nuevo elemento
    ```
      s = set("paralel")
      s # {'a', 'e', 'l', 'p', 'r'}
    ```

#### Issubset()

- Para saber si un set contiene a otro set.

    ```
      s = set("paralel")

      {'a', 'r'}.issubset(s) # True
    ```

# In/Out with basic Files

Como generar entrada y salida de datos usando un fichero .txt

## Crear un fichero - %%writefile

    ```
      %%writefile 'myFile2.txt'
      hello this is a text file
      this is a second line
      this is the third line
    ```
Después de la sentencia `%%writefile 'myFile2.txt` podemos escribir el texto que contendrá el archivo.

Éste se genera en el path donde se encuentra nuestro script de python. Para saber cual es nuestro path usamos el comando `pwd`.

    ```
      pwd
      #'/home/david/Programacion/PYTHON/Python_Course_from_Zero_to_hero/Code/1.Basics/1.Data structures and Objects'
    ```

## Abrir el fichero - open()

    ```
      myFile = open('myFile.txt')
    ```
Una vez abierto el fichero se vuelca su contenido en una variable en mi caso **myFile**.  
Aquí podemos cometer dos errores:

1. Que escribamos mal el nombre del fichero obteniendo un Errno 2  
   ![not found](img/img-11.png)
2. Que lo busquemos en un path equivocado


## Leer el fichero - .read()

El contenido del fichero lo tenemos en la variable, para leer su contenido usamos read()

    ```
      myFile.read()
      #'hello this is a text file \nthis is a second line\nthis is the third line\n'
    ```

Este método funciona con un cursor de tal modo que cuando lo utilizamos por primera vez el cursor va desde el inicio al final del texto, así si volvemos a utilizar el método, como el cursor está al final, no nos devolverá nada.

## seek()

Si queremos resetear este cursor utilizamos el método seek()

    ```
      myFile.seek(0)

    ```

## readlines()

Permite guardar en una lista cada línea del texto. Tenemos que tener en cuenta que al final de cada línea hay un salto de línea \n

    ```
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

    ```
      myFile.close()
      # si quiero volver a leerlo m da error
      myFile.read() # ValueError: I/O operation on closed file.
    ```

## With...as

Si no nos queremos preocupar por cerrar archivos podemos utilizar esta sentencia que abrirá el archivo y después de hacer las operaciones pertinentes lo vuelve a cerrar automáticamente.

    ```
      with open('myFile.txt') as my_new_File:
          content = my_new_File.read()

      content # #'hello this is a text file \nthis is a second line\nthis is the third line\n'
    ```

## open() - extendido

Cuando abrimos un archivo la función acepta estos parámetros:  
![not found](img/img-9.png)

El modo puede ser:  
![not found](img/img-10.png)

    ```
      with open('my_new_file.txt', mode='r') as f:
          print(f.read())
      '''
      ONE ON FIRST
      TWO ON SECOND
      THREE ON THIRD
      FOUR ON FOURTH
      '''
    ```

### 'a' (append) mode

- Añade texto al final del documento
    ```
      with open('my_new_file.txt',mode='a') as f:
          f.write('FOUR ON FOURTH')
    ```

### w (write) mode

- Abrirá o creará en su defecto un archivo con ese nombre, si ya existe lo sobreescribe
    ```
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

## Comparación

![not found](img/img-14.png)

## Lógicos

![not found](img/img-15.png)

![not found](img/img-16.png)

## Identidad

![not found](img/img-17.png)

# Condicionales e Iteraciones

## If -elif-else statement

    ```
    result = 5

    if result<2 :
        print('it < 2')
    elif result ==5 :
        print('result is equal to 5')
    else :
        print('result is bigger than 2')
    # result is equal to 5
    ```

### Ternary operator

    ```
    b = True
    r = "hello" if b else "GoodGbye"
    r # hello
    ```

## For loops

El más sencillo, establecemos un rango.

    ```
    for num in range(0,10):
        print(num, end='')
    # 0123456789
    ```

Con un tercer parámetro (step)

    ```
    for num in range(0,10,2):
        print(num, end='')
    # 02468
    ```

Podemos iterar un string como array de caracteres.

    ```
    list2 = []

    for caracter in 'David':
        #print(f'{caracter.upper()}', end='') # DAVID
        #list2.append(caracter) # ['D', 'a', 'v', 'i', 'd']
        print(type(caracter)) # nos devuelve tipo string
    ```

Podemos iterar una list

Para conocer el índice de cada elemento lo podemos hacer así:

Un truco para obtener el índice de cada elemento de cualquier iterable es transformarlo previamente a un enumerado – enumerate()

Podemos iterar tuples

Un dictionary

    Podemos obtener solo los valores con .values()

Nested loops

For loop reverse

While loops
Versión normal

Versión con else

While not

3 Keywords importantes en los loops
Pass
no hace nada, es decir en python si ejecutamos un loop el programa espera una identación y algo de código...si no hay nada arroja un error, EOF (end of file) para q el programa haga un salto se pone pass

Continue
Esta instrucción permite continuar el loop sin ejecutar el códi la ejecución del loop

Break
Detiene la ejecución del loop.

Useful operators

Range()
Normalmente lo usamos en los loops, permite crear un rango (start,stop[, step]) con un inicio, final y opcionalmente unos saltos. Este rango puede ser convertido en un List.

El tercer valor de range() el step puede ser negativo para hacer que el loop decrezca

enumerate()
Transforma los elementos en iterable y lo separa en tupples formadas por el elemento y su índice.

zip()
Permite unir listas y generar tupples con los elementos de cada lista coioncidentes en sus posiciones. Zip se ajusta a la lista más corta, si una lisa tiene pej 4 elementos el cuarto no aparecerá. Se puede castear a una lista de tuplas

In / not in
Permita saber si un elemento se encuentra en una lista, un diccionario

Min() max()
Permite detectar el menor valor de una list.

Random library
shuffle
Es una librería incluida en python que contienen multitud de funciones.
Para usarla primero hay q importarla

Esta función nos permitirá desordenar la lista aleatoriamente. Modifica nuestra lista, no devuelve otra

Randint
Obtener un integer aleatorio entro de un rango concreto, incluyendo los limites inferior y superior.

Input
Permite al usuario entrar datos. Devuelve un string, podemos castear con int() o float()

Methods and Functions
Métodos
Documentación de python https://docs.python.org/3/

Con argumentos por defecto

Return keyword

Argumentos \*args (arguments) / \*\*kwargs(eywords arguments)
Tenemos dos tipos de argumentos en las funciones, los argumentos posicionales

De tal manera que si paso más parmetros que los definidos en la función voy a tener un error

Para evitar eso usamos los \*args, internamente python transforma todos los argumentos pasados a la función como una tupla.

El uso de \*\*kwargs nos contruye un dictionary con los argumentos pasados

Una función puede aceptar como argumentos un \*args y un \*\*kwargs

Esto será útil cuando usemos librerías externas.

Lo que no podemos hacer es colocar un nuevo elemento después del kwargs pq python lo coge como argumento posicional. Así que primero los argumentos y después los key word arguments

Lambda expressions Map and Filter

Definición:
Las expresiones lambdas es como construir una función anónima, es una función que usaremos durante el código pero que no nos interesa definirla como tal.
El contenido de la función lambda debe ser una única expresión en lugar de un bloque de acciones.

Map(func,iterable)
Es una función que nos permite mapear otra función sobre un objeto iterable. Cuando decimos mapear significa emparejar un elemento con otro, en este caso aplicamos una función a cada uno de los elementos que integran el objeto iterable(lista o tupla) devolviendo un nuevo iterador cuyos elementos son el resultado de dicha operación.

Para ver lo que almacena el objeto map podemos hacer un for

Si quisieramos obtener los resultados en forma de lista podemos hacer un cast del objeto map directamente

Otro ejemplo con strings

Filter(function, iterable)
Es muy parecido a map en el sentido que aplicará una función a cada uno de los elementos de un objeto iterable, con dos diferencias:
1.La función que pasamos debe devolver True or False
2.Nos devolverá un objeto filter únicamente con los elementos del iterable que devuelan True en la función.

Lambda
