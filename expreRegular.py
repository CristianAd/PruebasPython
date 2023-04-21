import re

texto = "Este es un texto, con algunos caracteres@#! que deben ser eliminados"

texto_limpio = re.sub(r'[^a-zA-Z,\s]', '', texto)

print(texto_limpio)
