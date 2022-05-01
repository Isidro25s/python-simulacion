def extraerNumeros(nombreArchivo):
    numeros = []
    with open(f'../files/{nombreArchivo}') as f:
        for line in f:
            temp = line.strip().split(',')  
        for num in temp:
            if num != '':
                numeros.append(float(num))
    return numeros