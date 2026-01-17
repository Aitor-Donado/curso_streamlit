def convertir_a_atmosferas(valor, unidad):
    if unidad == "pascales":
        return valor / 101325  # 1 atm = 101325 Pa
    elif unidad == "mm de mercurio":
        return valor / 760  # 1 atm = 760 mmHg
    elif unidad == "milibares":
        return valor / 1013.25  # 1 atm = 1013.25 mbar
    else:
        return valor  # Si la unidad ya es atmósferas, no se convierte
    
def convertir_a_pascales(valor, unidad):
    if unidad == "atmósferas":
        return valor * 101325  # 1 atm = 101325 Pa
    elif unidad == "mm de mercurio":
        return valor * 133.322  # 1 mmHg = 133.322 Pa
    elif unidad == "milibares":
        return valor * 100  # 1 mbar = 100 Pa
    else:
        return valor  # Si la unidad ya es pascales, no se convierte

def convertir_a_mm_de_mercurio(valor, unidad):
    if unidad == "pascales":
        return valor / 133.322  # 1 mmHg = 133.322 Pa
    elif unidad == "atmósferas":
        return valor * 760  # 1 atm = 760 mmHg
    elif unidad == "milibares":
        return valor * 760 / 1013.25  # 1 mbar = 0.750062 mmHg
    else:
        return valor  # Si la unidad ya es mmHg, no se convierte

def convertir_a_milibares(valor, unidad):
    if unidad == "pascales":
        return valor / 100  # 1 mbar = 100 Pa
    elif unidad == "atmósferas":
        return valor * 1013.25  # 1 atm = 1013.25 mbar
    elif unidad == "mm de mercurio":
        return valor * 1013.25 / 760  # 1 mmHg = 1.33322 mbar
    else:
        return valor  # Si la unidad ya es mbar, no se convierte

def convertir_presion(valor, unidad):
    atmosferas = convertir_a_atmosferas(valor, unidad)
    mm_de_mercurio = convertir_a_mm_de_mercurio(valor, unidad)
    milibares = convertir_a_milibares(valor, unidad)
    pascales = convertir_a_pascales(valor, unidad)
    
    return atmosferas, mm_de_mercurio, milibares, pascales

if __name__ == "__main__":
    # Ejemplo de uso:
    valor = 2.1
    unidad = "mm de mercurio"
    resultado = convertir_presion(valor, unidad)
    print(f"Presión en atmósferas: {resultado[0]}")
    print(f"Presión en mm de mercurio: {resultado[1]}")
    print(f"Presión en milibares: {resultado[2]}")