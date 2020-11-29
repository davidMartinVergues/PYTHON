# Course from zero to Hero - Udemy -

## by Jose Portilla

> <span style="font-size:1.5em;"> [_link del curso_](https://www.udemy.com/course/complete-python-bootcamp/) </span>

- # Instalación de Python y SetUp

  - ## Instalación

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

    ![not found](img/img-2.png) 6. Vemos como en el prompt pone base eso es xq es el interprete de anaconda para desactivarlo

    ```
      conda deactivate
    ```

    para volverla a activar

    ```
      conda activate
    ```

    7. Saber versión y donde está instalado python  
       ![not found](img/img-3.png)
    8. Añadir PYTHONPATH
       Abrir en nuestra carpeta personal el archivo .bashrc y al final del archivo añadir lo q nos devuelve which python
       ![not found](img/img-4.png)
    9. Ahora cuando tecleamos

    ![not found](img/img-5.png)

    Y nos tiene q dar la misma respuesta.

  - ## Instalamos el tema para Jupyter

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

- # Introducción a Python

  - ## Usos de python y librerías
    ![not found](img/img-7.png)
  - ## Crear comentarios en Pyhon
    ```
      # comentario monolínea
      '''
        comentario de bloque
      '''
    ```
  - ## Data types
    ![not found](img/img-8.png)
  - ## Uso de variables

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

  - ## Uso del método print()

    Para imprimir contenido usamos el método print(), éste acepta un atributo para indicar que no haga salto de página end=’’.

    ```
      for x in range(10):
        print(x, end='')

      # 0123456789
    ```

  - ## Strings

    Funcionan como arrays así que usando el índice podemos extraer letras del string.
    Está habilitado el reverse index(indice reverso) así sin conocer la longitud del string podemos extraer el último carácter.

    Tamaño de un str usamos la función len()
    Propiedades de los strings
    1.Son inmutables, no podemos modificar un string

    2.Concatenables

    3.Multiplicables

    Métodos de los strings

    1.Slicing [start:stop:step] obtener un subString

    - stop no incluimos ese índice
    - step tamaño del subString a generar

      2..upper() .lower() .split()

      3.format()

      2.1 Float formatting {value:width.precision f}
      Value => ponemos el valor del número
      Width => tamaño que ocupará el número hecho string (nº de caracteres)
      Precision => número de decimales que tendrá

      4.f-string = formated string literal

      5.Casefold()
      Es como un equalsIgnoreCase de java, elimina las distinciones entre mayúsculas y minúsculas en el momeento de comparar strings.

      6.Find()
      Sólo funciona en estrings, para saber si un string contiene a otro y si lo está nos devuelve la posición y si no un -1. Hace distinción entra minusculas y mayúsculas.

      7.Capitalize()
      La primera letra de una palabra en mayúscula.

List
Secuencia ordenada de elementos que pueden ser de diferentes tipos(numbers, string,obj...). Podemos tener distintos tipos de datos almacenados en un list.
Métodos
8.Len()
Conocer el número de elementos de la list.
9.Slicing [start:stop:step]
Funciona igual que en los strings

Podemos concatenar list sumándolas

10.Append() pop()
Nos permite añadir(append) o eliminar (pop) un elemento al final de la list.
El método pop() no solo elimina el último elemento sino que también lo devuelve. Una función más es que puedes pasar el índice del elementos a eliminar, por defecto es el -1 (último elemento).

11.Sort() / sorted() / reverse()
Ninguno de los dos métodos devuelve nada, actúan sobre la list y la modifican

El método sorted() devuelve la lista ordenada pero no modifica la original.

12.Lista de elementos
Si quisiéramos obtener una lista de las letras que forman un string podemos hacer lo siguiente:

Pero una manera de hacerlo más fácil es: subelement for subelemento in element

Range

Podemos aplicar cambios a cada subelemento antes de incluirlo en la list, por ejemplo hacer el cuadrado de cada elemento num\*\*2

Podemos añadir condiciones

Incluso podemos añadir operaciones

Nested loops

13.Count()
Las veces q aparece un elemento en una lista

14.All() any()
Os permite saber si una lista contiene todos (all) los valores o sólo algunos (any) de otra lista

La secuencia de comprobación es la siguiente: primero hace un for (1) sacando cada “elem” de l1 y hace la comprobación en elem in l2 (2)

15.Join()
Permite concatenar los elementos de una lista mediante algún caracter, por ejemplo un espacio en blanco

16.Index()
Nos devuelve la posición de una valor en la list, el primero que encuetra

Dictionaries
Son mapas desordenados (no pueden ser ordenador) para almacenar objetos usando los pares clave-valor.
Normalmente los usamos cuando queremos tener dos valores que están relacionados por ejemplo precios de productos, así no necesitamos saber el índice del producto para saber el precio.

Dentro de los diccionarios podemos almacenar listas y otros diccionarios.

Añadir / sobreescribir / borrar (del) elementos de un diccionario

Métodos
1.keys() / values() / items()
Obtener todas las claves/ valores del diccionario y obtener una array de los pares clave-valor en forma de duplas.

Tuples
Son muy similares a las listas pero tiene la diferencia que son inmutables.

Métodos

Sólo hay dos métodos asociados a tuplas.
1.Count() / index()

Count devulve cuantas veces se encuentra un elemento en la tupla y index cual es la posición de un elemento dado si aparece más de una vez nos devuelve el índice del primero que encuentra.

2.Sum()
Podemos sumar el contenido de las tuplas. Sólo para valores numéricos

Sets
Son colecciones sin un orden y de elementos no repetidos.
Podemos crear un set a partir de una list, e esta manera nos aseguramos que los elementos repetidos de la list no se guardan en el set

Si hacemos un set de un string éste guardará cada carácter por separado sin repeticiones.

Métodos
1.Add()

Añadir nuevo elemento

2.Issubset()

Para saber si un set contiene a otro set.

In/Out with basic Files
Como generar entrada y salida de datos usando un fichero .txt

Crear un fichero - %%writefile

Después de la sentencia podemos escribir directamente que se nos guardará en el archivo.

Éste se genera en el path donde se encuentra nuestro script de python. Para saber cual es nuestro path usamos el comando pwd.

Abrir el fichero - open()

Cuando abrimos un archivo la función acepta estos parámetros:

El modo puede ser:

A (append) mode
Añade texto al final del documento

W (write) mode
Abrirá o creará en su defecto un archivo con ese nombre, si ya existe lo sobreescribe

Almacenamos el contenido en una variable. Aquí podemos cometer dos errores:
1.Que escribamos mal el nombre del fichero obteniendo un Errno 2

2.Que lo busquemos en un path equivocado

Leer el fichero - .read()

Nos devuelve en un único string todo el contenido del fichero. Este método funciona con un cursor de tal modo que cuando lo utilizamos por primera vez el cursor va desde el inicio al final del texto, así si volvemos a utilizar el método, como el cursor está al final, no nos devolverá nada.

.seek(0)
Si queremos resetear este cursor utilizamos el método:

.readlines()
Permite guardar en una lista cada línea del texto. Tenemos que tener en cuenta que al final de cada línea hay un salto de línea \n

.close()
Una vez terminamos el trabajo con el fichero debemos cerrarlo

With...as
Si no nos queremos preocupar por cerrar archivos podemos utilizar esta sentencia que abrirá el archivo y después de hacer las operaciones pertinentes lo vuelve a cerrar automáticamente.

File location
Crear el fichero en una localización concreta

Para abrir un archivo es lo mismo, hay que tener en cuenta si trabajamos en windows entonces usamos los ‘\\’ como separadores o si utilizamos linux o MacOS que usaremos ‘/’

Operadores
En python no existe la expresión ++x o x++ hay que escribirlo como x+=1

Aritméticos

Comparación

Lógicos

Identidad

Condicionales e Iteraciones
If -elif-else statement

Ternary operator

For loops
El más sencillo, establecemos un rango.

Podemos iterar un string como array de caracteres.

Una list

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
Normalmente lo usamos en los loops, permite crear un rango (strat,stop[, step]) con un inicio, final y opcionalmente unos saltos. Este rango puede ser convertido en un List.

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
