def index_of(target, lst):
    """
    Retorna el indice de la primera ocurrencia de target en lst.
    Si no se encuentra, retorna -1.

    Ejemplo: index_of("Black", ["Red", "Green", "Black"]) -> 2
    """
    indice = -1
    for n in lst:
        if target in lst:
            if target != n:
                indice = indice + 1
            elif target == n:
                indice = indice + 1
                return indice
        else:
            return -1
    return indice

def index_of_by_index(target, lst, start):
    """
    Retorna el indice de la primera ocurrencia de target en lst,
    buscando a partir del indice start (inclusive).
    Si no se encuentra, retorna -1.

    Ejemplo: index_of_by_index("Black", ["Red", "Black", "Green", "Black"], 2) -> 3
    """
    lista = lst[start:]

    if target in lista:
        return index_of(target,lista) + start
    else:
        return -1





def index_of_empty(lst):
    """
    Retorna el indice del primer string vacio ("") en lst.
    Si no hay ninguno, retorna -1.

    Ejemplo: index_of_empty(["Red", "", "Green"]) -> 1
    """
    indice = -1
    if "" not in lst:
        return -1
    for n in lst:
        if n == "":
            indice = indice + 1
            return indice
        else:
            indice += 1
    return indice
