import platform
import os
import sys

info_entorno = {
    "Sistema": platform.system(),
    "Versión Núcleo Linux": platform.release(),
    "Versión SO": platform.version(),
    "Arquitectura": platform.machine(),
    # muchas plataformas no proveen esta información o 
    # simplemente retorna los mismos valores que para machine(), 
    # como hace NetBSD.
    "Procesador": platform.processor(),
    "Hostname": platform.node(),
    "Versión de Python": platform.python_version(),
    "Build de Python": platform.python_build(),
    "Implementación": platform.python_implementation(),
    "Info completa": platform.uname(),
    #"Variables de entorno": os.environ,
    "Ejecutable": sys.executable
}

for item in info_entorno:
    print(item, "\t\t", info_entorno[item])
    print("\t\t")


with open("entorno.log", "w") as archivo:
    for clave, valor in info_entorno.items():
        archivo.write(f"{clave}: {valor}\n ")
