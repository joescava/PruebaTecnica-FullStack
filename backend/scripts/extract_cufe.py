import os
import sqlite3
import PyPDF2
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../static/cufe_data.db")

def create_table():
    """ Crea la tabla si no existe """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS facturas (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            paginas INT,
            cufe TEXT,
            peso INT
        )
    """)
    conn.commit()
    conn.close()

def limpiar_texto(texto):
    """ Elimina saltos de línea y espacios innecesarios """
    return re.sub(r"\s+", "", texto)

def extract_cufe_from_pdf(pdf_path):
    """ Extrae el CUFE del PDF y maneja correctamente los saltos de línea """
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        texto = "".join([page.extract_text() or "" for page in reader.pages])

    # Limpiar texto antes de aplicar la expresión regular
    texto_limpio = limpiar_texto(texto)

    # Expresión regular ajustada para CUFE
    match = re.search(r"([0-9a-fA-F]{95,100})", texto_limpio)

    return match.group(0) if match else "No encontrado", len(reader.pages), os.path.getsize(pdf_path)

def save_to_db(filename, pages, cufe, size):
    """ Guarda la información extraída en SQLite """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    create_table()
    cursor.execute("INSERT INTO facturas (nombre, paginas, cufe, peso) VALUES (?, ?, ?, ?)",
                   (filename, pages, cufe, size))
    conn.commit()
    conn.close()