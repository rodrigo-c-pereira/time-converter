def time_converter():
    x = int(input("Insira o valor:"))
    y = input("Escolha entre 'horas', 'minutos' ou 'segundos' para determinar o valor:")
    z = input("Escolha entre 'horas', 'minutos' ou 'segundos' para determinar: ")

    if y == "horas":
        if z == "minutos":
            result = x * 60
        elif z == "segundos":
            result = x * 3600
        else:
            result = x

    elif y == "minutos":
        if z == "horas":
            result = x / 60
        elif z == "segundos":
            result = x * 60

    elif y == "segundos":
        if z == "horas":
            result = x / 3600
        elif z == "minutos":
            result = x /60
        else:
            result = x

    print(x, y, "é igual a ", result, z)

time_converter()
