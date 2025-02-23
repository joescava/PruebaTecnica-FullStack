import csv
import re

def validar_csv(csv_file):
    errores = []
    csv_file.seek(0)
    reader = csv.reader(csv_file.read().decode("utf-8").splitlines())

    for i, row in enumerate(reader):
        # Validación de cantidad de columnas
        if len(row) < 5:
            errores.append({
                "fila": i,
                "columna": "N/A",
                "error": "Error de Formato Registro con Más de 5 columnas"
            })
            continue  
        elif len(row) > 5:
            errores.append({
                "fila": i,
                "columna": "N/A",
                "error": "Error de Formato Registro con Más de 5 columnas"
            })
            continue 
        if len(row) >= 1: 
            if not row[0].isdigit() or not (3 <= len(row[0]) <= 10):
                errores.append({"fila": i, "columna": "1", "error": "Número inválido"})

        if len(row) >= 2:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", row[1]):
                errores.append({"fila": i, "columna": "2", "error": "Correo inválido"})

        if len(row) >= 3:
            if row[2] not in ["CC", "TI"]:
                errores.append({"fila": i, "columna": "3", "error": "Valor incorrecto"})

        if len(row) >= 4:
            try:
                valor_numerico = int(row[3].strip())
                if not (500000 <= valor_numerico <= 1500000):
                    errores.append({"fila": i, "columna": "4", "error": f"Valor fuera de rango"})
            except ValueError:
                errores.append({"fila": i, "columna": "4", "error": "Valor no numérico"})
    return errores