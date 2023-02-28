# PRINTAR A LAS POSICIONS EN UNA LISTA DE AREAS
areas = ["cuina", 7.88, "menjador", 13.0, "terrassa", 20.34, "lavabo",
         6.55, "habitació1", 7.98, "habitació2", 12, "rebedor", 4.23]


print(areas[1])
print(areas[-1])
print(areas[5])
print(areas[0:3])
print(areas[2:])
print(areas[9]+areas[11])
areas[7] = 7
print(areas)

areas.extend(["pati interior", 2.78])
print(areas)
