"""
Programa: divisio_entera.py. Programa que demana a l'usuari dos nombres enters (dividend i divisor) i els divideix

Institut Icaria
Programació - 1r Batxillerat - Curs 2025-2026
"""
__author__ = "Albert Angelet"
__email__ = "aangelet@instituticaria.cat"
__date__ = "2025-10-17"

dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))
if divisor == 0:
    print("Error: no es pot dividir entre zero.")
else:
    divisio = dividend/divisor
    quocient = dividend//divisor
    residu = dividend%divisor
 
    print(f"Divisió: {dividend}/{divisor}")
    print(f"Quocient: {quocient}")
    print(f"Residu: {residu}")