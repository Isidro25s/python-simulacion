def guardarNumeros(nombreArchivo, numerosArray):
    f1 = open(f'../files/{nombreArchivo}','w')
    for temp in numerosArray:
        f1.write(str(temp) + ', ')
    f1.close()