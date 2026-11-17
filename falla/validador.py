"""Validador de contrasenas (con un bug a proposito)."""


def es_segura(password: str) -> bool:
    """Segura = 8 o mas caracteres y al menos una mayuscula."""
    tiene_largo = len(password) > 8      # BUG: deberia ser >=
    tiene_mayuscula = password != password.lower()
    return tiene_largo and tiene_mayuscula
