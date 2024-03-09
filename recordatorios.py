recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"],]

recordatorios.append(["2021-02-01","06:00","Empezar el año"])

recordatorios[2]=["2021-07-16", "13:00", "no hacer nada es feriado"]
recordatorios.pop(1)
recordatorios.append(["2021-12-25","22:00", "cena de navidad"])
recordatorios.append(["2021-12-31","22:00", "cena de Año nuevo"])


# nueva_agenda=[
#     recordatorios[0],
#     recordatorios[4],
#     recordatorios[1],
#     recordatorios[2],
#     recordatorios[5],
#     recordatorios[3],
#     recordatorios[6]
   
# ]
for fechas in sorted(recordatorios):
    print(fechas)


