"""Demo de Rich: colores, tabla y barra de progreso."""
from time import sleep

from rich import print
from rich.progress import track
from rich.table import Table

print("[bold green]OK[/] Dataset cargado: [cyan]150 filas[/]")

tabla = Table(title="Resultados de los tests")
tabla.add_column("Test")
tabla.add_column("Estado", justify="center")
tabla.add_row("test_dividir_enteros", "[green]PASSED[/]")
tabla.add_row("test_dividir_por_cero", "[green]PASSED[/]")
tabla.add_row("test_password_segura", "[red]FAILED[/]")
print(tabla)

for _ in track(range(5), description="Procesando..."):
    sleep(0.2)
