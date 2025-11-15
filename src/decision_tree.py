#Ashley Dayane Alfaro Aguilar
#Carne 202301982 ing en sistemas 100% virtual

"""
Módulo decision_tree
---------------------
Implementa un árbol de decisión simple con un único nodo que clasifica
números como 'Alto' o 'Bajo' en función de un umbral.
"""

UMBRAL = 50  # Valor por defecto


def clasificar_numero(numero, umbral=UMBRAL):
    """
    Clasifica un número como 'Alto' o 'Bajo' dependiendo del umbral.

    Args:
        numero (int): Número a clasificar.
        umbral (int): Umbral para la clasificación. Por defecto 50.

    Returns:
        str: "Alto" si numero >= umbral, "Bajo" en caso contrario.
    """
    return "Alto" if numero >= umbral else "Bajo"

