def oblicz_vat(netto, stawka_vat):
    return netto * stawka_vat / 100

# Dane wejściowe
elementy = [
    {"nazwa": "Clean Code, Robert C. Martin", "netto": 100.00, "vat": 8},
    {"nazwa": "Applying UML and Patterns, C. Larman", "netto": 300.00, "vat": 8},
    {"nazwa": "Shipping", "netto": 50.00, "vat": 23}
]

# Inicjalizacja łącznej wartości netto i podatku VAT dla każdej stawki
suma_netto = {}
suma_vat = {}

# Obliczanie łącznej wartości netto i podatku VAT
for i in elementy:
    netto = i["netto"]
    stawka_vat = i["vat"]
    vat = oblicz_vat(netto, stawka_vat)
    
    suma_netto[stawka_vat] = suma_netto.get(stawka_vat, 0) + netto
    suma_vat[stawka_vat] = suma_vat.get(stawka_vat, 0) + vat

# Drukowanie podsumowania w formacie Markdown
print("|  Stawka VAT   | Total netto | Kwota VAT |")
print("|---------------|-------------|-----------|")
for stawka_vat in sorted(suma_netto.keys()):
    print(f"| VAT {stawka_vat}%       | {suma_netto[stawka_vat]:.2f} zł    | {suma_vat[stawka_vat]:.2f} zł  |")
