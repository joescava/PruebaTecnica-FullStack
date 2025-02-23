# PRUEBA TÉCNICA - DESARROLLADOR FULL STACK

### **Descripción**
Este proyecto es una **prueba técnica** que evalúa habilidades en **Django** y **Python**. Se divide en **dos partes**:

**Validación de Archivos** con Django.  
**Extracción de CUFE de Facturas PDF** con un script en Python.

---

##  **Tecnologías Utilizadas**
### **Backend (Django)**
- **Python 3.13**
- **Django 5.1.6**
- **SQLite3** (Base de datos)
- **PyPDF2** (Extracción de texto de PDFs)
- **Expresiones Regulares (Regex)** para extraer CUFE

### **Frontend**
- **JavaScript (Vanilla)**
- **HTML5 / CSS3**
- **Fetch API** (Para comunicar con el backend)

---

## **Estructura del Proyecto**

| Carpeta/ Archivo |	Descripción |
|---------|------------|
|PruebaTecnica-FullStack/ | Carpeta principal del proyecto
├── 📄 README.md | Documentación del proyecto
├── 📄 requirements.txt | Dependencias del backend
├── 📂 backend/	Backend | desarrollado en Django
│   ├── 📄 manage.py | Script principal de Django
│   ├── 📂 django_app/ | Configuración del proyecto Django
│   ├── 📂 app_validacion/ | Aplicación principal del backend
│   │   ├── 📄 models.py | Modelos de la base de datos
│   │   ├── 📄 views.py | Vistas de la API
│   │   ├── 📄 urls.py | Rutas de la API
│   │   ├── 📄 utils.py | Funciones auxiliares
│   │   ├── 📂 templates/ | Archivos HTML del backend
│   │   └── 📂 migrations/ | Migraciones de la base de datos
│   ├── 📂 scripts/ | Scripts de procesamiento de PDF
│   │   ├── 📄 extract_cufe.py | Script para extraer CUFE de PDFs
│   ├── 📂 static/ | Archivos estáticos del backend
│   │   ├── 📄 cufe_data.db | Base de datos SQLite
│   ├── 📄 requirements.txt | Dependencias del backend
├── 📂 frontend/ | Frontend en HTML, CSS y JavaScript
│   ├── 📄 index.html | Interfaz principal
│   ├── 📄 app.js | Lógica de frontend
│   ├── 📄 styles.css | Estilos CSS

## **Validación de Archivos**

El sistema permite **subir un archivo** con 5 columnas y **validar su estructura**.  
Si hay errores, se muestran en la interfaz web.

### **Reglas de Validación**

| Columna | Restricción |
|---------|------------|
|**Número ID** | Enteros entre 3 y 10 caracteres |
|**Correo Electrónico** | Debe ser un email válido |
|**Tipo de Documento** | Solo valores "CC" o "TI" |
|**Monto** | Entre 500,000 y 1,500,000 |
|**Cualquier Valor** | Se permite cualquier dato |

### **Pasos para probar**
1. Subir un archivo txt desde el **frontend**.
2. Se validará su contenido en el **backend**.
3. Se mostrará un mensaje de **éxito o errores detallados**.

---

##  **Extracción de CUFE desde Facturas PDF**
El sistema permite **subir archivos PDF** y extraer el **CUFE** usando **Expresiones Regulares**.  
Los datos se guardan en **SQLite**.

### **Datos almacenados en la BD**
| Campo | Descripción |
|---------|------------|
| **Nombre del archivo** | Nombre del PDF subido |
| **Número de páginas** | Cantidad de páginas del documento |
| **CUFE** | Código único extraído con Regex |
| **Peso del archivo** | Tamaño del archivo en bytes |

### **Pasos para probar**
1. Subir archivos **PDF** desde el **frontend**.
2. El **backend** extrae el **CUFE** y almacena los datos.
3. Se pueden visualizar las facturas en un **modal de la interfaz**.

---

## **Instalación y Configuración**
### **1 Clonar el repositorio**
```sh
git clone https://github.com/joescava/PruebaTecnica-FullStack.git
cd PruebaTecnica-FullStack

Configurar el Backend (Django)
	1.	Activar un entorno virtual en Python:

    cd backend
    python -m venv venv  # Crear entorno virtual
    source venv/bin/activate  # Activar entorno en macOS/Linux
    # En Windows usa: venv\Scripts\activate
    pip install -r requirements.txt  # Instalar dependencias

    2.	Instalar dependencias:

    pip install -r requirements.txt

    3.	Configurar la base de datos y aplicar migraciones:

    python manage.py migrate

    4.	Ejecutar el servidor:

    python manage.py migrate  # Aplicar migraciones
    python manage.py runserver  # Iniciar servidor en http://127.0.0.1:8000

Accede al backend en http://127.0.0.1:8000


Configurar el Frontend

No se requiere instalación. Simplemente abre el archivo index.html en el navegador.


Uso de la Aplicación

 Subir archivos
	•	TXT → Validación de estructura.
	•	PDFs → Extracción del CUFE.
Ver facturas procesadas
	•	Se pueden visualizar en un modal en el frontend.
API Endpoints
    Método	URL	                        Descripción
    POST	/api/upload/	            Subir y validar archivos TXT
    POST	/api/upload-pdf/	        Subir facturas en PDF y extraer CUFE
    GET	    /api/listar-facturas/	    Obtener todas las facturas almacenadas
Requerimientos Técnicos
	•	Python 3.13 o superior
	•	Django 5.1.6
	•	SQLite (viene incluido con Python)
	•	PyPDF2 para extraer texto de PDFs
    •	Se debe activar el entorno virtual antes de ejecutar Django.
Cómo Reiniciar la Base de Datos
    Si necesitas limpiar la base de datos, ejecuta:
        rm backend/static/cufe_data.db  # Elimina la base de datos
        python manage.py migrate        # Vuelve a crear las tablas

Autores
	•	Johan Estiven Cante Valero - Senior Software Developer
