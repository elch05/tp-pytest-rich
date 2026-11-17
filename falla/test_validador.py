from validador import es_segura


def test_password_de_8_caracteres_es_segura():
    assert es_segura("Python12") is True
