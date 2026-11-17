"""Funciones matematicas simples para la demo de pytest."""


def dividir(a: float, b: float) -> float:
    """Divide a por b. Lanza ValueError si b es cero."""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def es_par(numero: int) -> bool:
    """Devuelve True si el numero es par."""
    return numero % 2 == 0
