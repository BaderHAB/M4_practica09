"""
Imprimir el total dels diners acumulats
després de 7 anys, utilitzant variables (comentari a afegir al codi)
"""
savings = 100
increase = savings * 1.1
x = 0
while x < 7:
    increase = savings * 1.1
    savings = increase
    x += 1
result = savings
print(result)
