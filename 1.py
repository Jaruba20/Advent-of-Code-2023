with open('1.txt', 'r') as file:
    data = file.read()


l = []
for c in data:
    l.append(c)

ns = [0]
ns.extend([i for i, valor in enumerate(l) if valor == "\n"])

nums = [i for i, valor in enumerate(l) if valor.isdigit()]

def devuelve_valor(mi_ns, mi_nums):
    suma = 0
    i = 0
    while i < len(mi_ns) - 1:
        lista_intervalo = []
        for val in mi_nums:
            if (val >= mi_ns[i] and val <= mi_ns[i+1]):
                lista_intervalo.append(l[val])
        if len(lista_intervalo) > 1:
            valor = int(str(lista_intervalo[0]) + str(lista_intervalo[-1]))
        elif len(lista_intervalo) == 1:
            valor = int(str(lista_intervalo[0]) + str(lista_intervalo[0]))
        else:
            valor = 0
        suma += valor

        i += 1
    return suma


resultado = devuelve_valor(ns, nums)
print(resultado)
