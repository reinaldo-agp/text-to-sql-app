📊 Text-to-SQL App — Habla con tu Base de Datos en Lenguaje Natural
Una aplicación con inteligencia artificial que convierte preguntas en lenguaje natural a consultas SQL y las ejecuta sobre una base de datos SQLite — sin necesidad de saber SQL.
Construida con LangChain, Ollama (Llama 3) y Streamlit.

🎯 ¿Qué hace esta app?
Escribe una pregunta como "¿Quién sacó la nota más alta en Matemáticas?" y la app:

Analiza el esquema de tu base de datos automáticamente
Genera la consulta SQL correcta usando un LLM local (Llama 3)
Ejecuta la consulta y muestra los resultados al instante


🛠️ Stack Tecnológico
CapaTecnologíaInterfaz / UIStreamlitOrquestación LLMLangChain (LCEL)Modelo de LenguajeOllama — Llama 3 (corre localmente)Base de DatosSQLiteLenguajePython 3.10+

🚀 Cómo ejecutarlo
Requisitos previos

Python 3.10+
Ollama instalado y corriendo
Modelo Llama 3 descargado: ollama pull llama3

Instalación
bash# 1. Clona el repositorio
git clone ](https://github.com/reinaldo-agp/text-to-sql-app.git
cd text-to-sql-app

# 2. Instala las dependencias
pip install -r requirements.txt

# 3. Crea la base de datos de ejemplo
python create_db.py

# 4. Ejecuta la app
streamlit run app.py
Luego abre tu navegador en http://localhost:8501

💬 Ejemplos de preguntas que puedes hacer

"¿Quién sacó la nota más alta en Matemáticas?"
"¿Cuántos estudiantes aprobaron con nota B o superior?"
"¿Cuál es el promedio de puntaje por materia?"
"Lista todos los estudiantes que reprobaron (puntaje menor a 70)."


🗃️ Esquema de la Base de Datos
sqlCREATE TABLE grades (
    id       INTEGER PRIMARY KEY,
    name     TEXT,
    subject  TEXT,
    score    INTEGER,
    grade    TEXT
)

🏗️ Arquitectura
Pregunta del usuario
        │
        ▼
ChatPromptTemplate  ←  Esquema de BD (inyectado automáticamente)
        │
        ▼
ChatOllama (Llama 3)
        │
        ▼
Consulta SQL (texto)
        │
        ▼
SQLDatabase.run()
        │
        ▼
Resultado mostrado en Streamlit

🔑 Conceptos clave demostrados

LangChain LCEL (LangChain Expression Language) — composición de cadenas con el operador |
Inferencia local con Ollama — sin API key, sin enviar datos a la nube
Ingeniería de prompts — inyección de esquema + generación SQL en zero-shot
SQLDatabase de LangChain — extracción automática del esquema y ejecución segura de consultas


🔭 Posibles extensiones

 Soporte para esquemas multi-tabla con JOINs
 Agregar historial de consultas y memoria conversacional
 Reemplazar Llama 3 por GPT-4 o Claude vía API
 Deploy en Streamlit Cloud o Hugging Face Spaces
 Agregar visualizaciones de datos (gráficos a partir de los resultados)


👤 Autor
Reinaldo — Data Scientist
LinkedIn · GitHub

📄 Licencia
Licencia MIT — siéntete libre de usar y adaptar este proyecto.
