"""
5)Imprimir el segon element
Imprimir l’últim element
Imprimir l’àrea de la terrassa
Imprimir del primer element al tercer element
Imprimir del tercer element a l’últim
Imprimir el total de l'àrea de les dues habitacions
Modificar l’àrea del lavabo i imprimir la nova list area
Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.

"""
areas = ['cuina', 7.88, 'menjador', 13.0, 'terrassa', 20.34, 'lavabo', 6.55, 'habitació1', 7.98, 'habitació2', 12, 'rebedor', 4.23]
print(areas[1:2])
print(areas[13:14])
print(areas[5:6])
print(areas[0:3])
print(areas[9]+areas[11])
areas[7] = 4
print(areas)
areas.append('pati interior')
areas.append(2.78)
print(areas)

