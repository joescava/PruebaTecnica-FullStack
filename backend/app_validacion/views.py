import os
import sqlite3
from django.http import JsonResponse
from scripts.extract_cufe import extract_cufe_from_pdf, save_to_db
from .utils import validar_csv
from django.views.decorators.csrf import csrf_exempt


# Ruta de la base de datos SQLite
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../static/cufe_data.db")

@csrf_exempt
def upload_file(request):
    """ Maneja la subida y validación de archivos TXT """
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    archivo = request.FILES.get("archivo")

    if not archivo:
        return JsonResponse({"error": "No se envió ningún archivo"}, status=400)

    if not archivo.name.endswith('.txt'):
        return JsonResponse({"mensaje": "Solo se permiten archivos .txt"}, status=400)

    errores = validar_csv(archivo)
    if errores:
        return JsonResponse({
            "mensaje": "Errores en el archivo",
            "errores": errores
        }, status=400)

    return JsonResponse({"mensaje": "Archivo validado correctamente."}, status=200)


@csrf_exempt
def upload_pdfs(request):
    """ Procesa y extrae información desde archivos PDF """
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    archivos = request.FILES.getlist("pdfs")
    
    if not archivos:
        return JsonResponse({"error": "No se enviaron archivos PDF"}, status=400)

    datos_extraidos = []

    try:
        for archivo in archivos:
            temp_path = f"temp_{archivo.name}"
            with open(temp_path, "wb+") as destino:
                for chunk in archivo.chunks():
                    destino.write(chunk)

            cufe, paginas, peso = extract_cufe_from_pdf(temp_path)

            # Guardar en SQLite
            save_to_db(archivo.name, paginas, cufe, peso)

            datos_extraidos.append({
                "nombre": archivo.name,
                "paginas": paginas,
                "cufe": cufe if cufe else "No encontrado",
                "peso": peso
            })

            os.remove(temp_path)

        return JsonResponse({"mensaje": "Procesamiento completado", "datos": datos_extraidos}, safe=False, status=200)

    except Exception as e:
        return JsonResponse({"error": "Error procesando los archivos", "detalle": str(e)}, status=500)

@csrf_exempt
def listar_facturas(request):
    """
    Devuelve todas las facturas almacenadas en la base de datos SQLite.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, cufe, paginas, peso FROM facturas")
        facturas = [{"nombre": row[0], "cufe": row[1], "paginas": row[2], "peso": row[3]} for row in cursor.fetchall()]
        conn.close()

        return JsonResponse({"facturas": facturas})

    except Exception as e:
        return JsonResponse({"error": "Error al consultar la base de datos", "detalle": str(e)}, status=500)