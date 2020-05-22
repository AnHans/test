""" statistische Kennzahlen ermitteln: Maximum, Minimum und arithmetisches Mittel """
def get_max(liste):
    """
    Maximum einer Liste ermitteln
    """
    if len(liste) == 0:
        raise ValueError("Die Liste darf nicht leer sein.")
    for element in liste:
        if type(element) not in [int, float]: # pylint: disable=unidiomatic-typecheck
                                              # isinstance()  funktioniert hier nicht
            raise ValueError("Die Elemente der Liste dürfen nur ganze oder Gleitkommazahlen sein.")
    max_wert = liste[0]
    for wert in liste[1:]:
        if wert > max_wert:
            max_wert = wert
    return max_wert
