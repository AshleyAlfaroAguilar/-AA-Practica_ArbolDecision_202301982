#Ashley Dayane Alfaro Aguilar
#Carne 202301982 ing en sistemas 100% virtual
"""
Módulo data_loader
-------------------
Se encarga de verificar, generar y cargar el archivo
data/numeros_1000.txt con 1000 números aleatorios entre 1 y 100.
Cumple con las reglas de la práctica y utiliza docstrings PEP-257.
"""

import os
import random
from pathlib import Path


FILE_PATH = Path("data/numeros_1000.txt")


def generar_archivo_si_no_existe():
    """
    Genera el archivo numeros_1000.txt
    Usa una semilla fija para que los resultados sean reproducibles.
    """
    if FILE_PATH.exists():
        return False, None  # No se generó nada

    random.seed(42)
    numeros = [str(random.randint(1, 100)) for _ in range(1000)]

    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(numeros))

    return True, 42  # Archivo generado y semilla usada


def cargar_numeros():
    """
    Carga los números desde numeros_1000.txt y los devuelve como lista de enteros.
    """
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return [int(line.strip()) for line in f.readlines()]
