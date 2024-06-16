from os import system
system("cls")

op = int(input("rut a buscar: "))

personas = [[215880435, 139586050, 123035755], ['Mauricio', 'Maria', 'Carlos'], ['Gajardo', 'Vega', 'Gajardo']]


for i in range(len(personas)):
    for j in range(len(personas[i])):
        if personas[0][j] == op:
            print(personas[1][j])
            print(personas[2][j])
            break