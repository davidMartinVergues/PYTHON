from decimal import Decimal

# Basics Math

print(2+1)

# powers (exponentes)

print(2**3)

print(round(1.55559, 3))  # redondeamos a 3 decimales

# con el módulo deciaml vemos el número real q almacena el pc

print("2.675 es almacenado el pc como =>" + str(Decimal(2.675)))

print('0.1 es almacenado el pc como =>'+str(Decimal(0.1)))

sum = 0.0

for i in range(10):
    sum += 0.1

print(sum)
