# TP Colaborativo — pytest + Rich

Material de la presentación del TP Colaborativo de **Programación 1** (Ciencia de Datos, ISTEA).

Tema: dos librerías de terceros de Python — **pytest** (tests automatizados) y **Rich**
(salida con formato en la terminal) — más una herramienta de IA (Claude Code).

Todo el código de las diapositivas está acá, y las salidas que se ven en la
presentación son las salidas reales de ejecutar estos archivos.

## Estructura

| Archivo | Qué es |
|---|---|
| `calculadora.py` | Módulo de ejemplo: `dividir()` y `es_par()` |
| `test_calculadora.py` | Tests con pytest: asserts simples, `pytest.raises` y `@pytest.mark.parametrize` |
| `falla/validador.py` | Validador de contraseñas con un bug a propósito (`>` en vez de `>=`) |
| `falla/test_validador.py` | Test que falla, para mostrar el reporte de errores de pytest |
| `demo_rich.py` | Demo de Rich: texto con color, tabla y barra de progreso |

## Cómo ejecutarlo

```
python -m venv venv
venv\Scripts\activate        (Windows)
source venv/bin/activate     (Linux / Mac)

pip install -r requirements.txt

pytest -v            # corre los tests que pasan
cd falla
pytest               # muestra el test que falla y el reporte detallado
cd ..
python demo_rich.py  # demo de Rich
```
