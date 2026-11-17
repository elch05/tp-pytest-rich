"""Tests de calculadora.py - se corren con: pytest -v"""
import pytest
from calculadora import dividir, es_par


def test_dividir_enteros():
    assert dividir(10, 2) == 5


def test_dividir_flotantes():
    assert dividir(7, 2) == 3.5


def test_dividir_por_cero_lanza_error():
    with pytest.raises(ValueError):
        dividir(10, 0)


@pytest.mark.parametrize("numero, esperado", [
    (2, True),
    (7, False),
    (0, True),
    (-4, True),
])
def test_es_par(numero, esperado):
    assert es_par(numero) == esperado
