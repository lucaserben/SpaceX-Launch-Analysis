# SpaceX Data ETL Pipeline

Una solución ETL modular para extraer, transformar y cargar datos de SpaceX a una base de datos PostgreSQL, con análisis de tasas de éxito de lanzamientos.

## 🎯 Características

- **Extract**: Obtiene datos de lanzamientos y cohetes desde la API de SpaceX
- **Transform**: Limpia y transforma los datos en un DataFrame estructurado
- **Load**: Guarda los datos en CSV y en una base de datos PostgreSQL
- **Analyze**: Calcula estadísticas y visualiza patrones de éxito por año y cohete
- **Logging**: Registro detallado de cada etapa del proceso en consola y archivo

## 📁 Estructura del Proyecto

```
.
├── main.py              # Orquestador principal del pipeline
├── extract.py           # Módulo de extracción de datos desde APIs
├── transform.py         # Módulo de transformación y limpieza de datos
├── load.py              # Módulo de carga en CSV y PostgreSQL
├── analyst.py           # Módulo de análisis y visualización
├── logs.py              # Módulo centralizado de logging
├── requirements.txt     # Dependencias del proyecto
├── .gitignore           # Archivos a ignorar en Git
└── README.md            # Este archivo
```

## 🚀 Instalación

### Requisitos previos
- Python 3.8+
- PostgreSQL 12+ (si usarás la carga a BD)
- pip o conda

### Pasos

1. **Clonar el repositorio**
   ```bash
   git clone <tu-repo>
   cd vulnerabilidades
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar base de datos (opcional)**
   - Asegúrate de tener PostgreSQL corriendo
   - Crea una base de datos llamada `spacex`
   - Actualiza las credenciales en `load.py` si es necesario

## 📊 Uso

Ejecuta el pipeline completo:

```bash
python main.py
```

### Etapas del Pipeline

1. **EXTRACT**: Descarga datos de dos endpoints de SpaceX
2. **TRANSFORM**: Limpia, estructura y enriquece los datos
3. **LOAD**: Guarda en CSV (`data/spacex_launches.csv`) y en PostgreSQL
4. **ANALYSIS**: Calcula tasas de éxito y genera gráficos

### Salida esperada

- **Archivo CSV**: `data/spacex_launches.csv`
- **Base de datos**: Tabla `launches` en PostgreSQL
- **Logs**: `logs.txt` con registro detallado de cada paso
- **Gráficos**: Se muestran gráficos interactivos de análisis

## 📋 Descripción de Módulos

### `main.py`
Orquestador principal que:
- Coordina el flujo de datos entre módulos
- Maneja excepciones en la carga a BD
- Registra el progreso de cada etapa

### `extract.py`
```python
def fetch(url)
```
Realiza peticiones HTTP con timeout configurado.

### `transform.py`
- `map_rockets()`: Crea diccionario de IDs a nombres de cohetes
- `clean_data()`: Extrae campos relevantes de cada lanzamiento
- `make_df()`: Construye DataFrame con transformaciones (fechas, años, nombres)

### `load.py`
- `save_to_csv()`: Guarda DataFrame en archivo CSV
- `create_connection()`: Establece conexión a PostgreSQL
- `save_launches_to_db()`: Carga datos a tabla `launches`

### `analyst.py`
Calcula y visualiza:
- Tasa de éxito global
- Tasa de éxito por año
- Número de lanzamientos por año
- Tasa de éxito por cohete

Genera gráficos interactivos para cada análisis.

### `logs.py`
Sistema de logging centralizado que:
- Imprime mensajes con timestamp en consola
- Persiste los registros en `logs.txt`

## 📈 Datos Analizados

El pipeline procesa más de 200 lanzamientos de SpaceX con:
- **Tasa de éxito general**: ~97%
- **Rango temporal**: Desde los primeros lanzamientos hasta presente
- **Cohetes**: Falcon 1, Falcon 9, Falcon Heavy, Starship

## 🔧 Configuración

### Credenciales de PostgreSQL
En `load.py`, ajusta la cadena de conexión:
```python
"postgresql+psycopg2://usuario:contraseña@localhost:5432/spacex"
```

### URLs de API
Las URLs de los endpoints se definen en `main.py`:
- Lanzamientos: `https://api.spacexdata.com/v5/launches`
- Cohetes: `https://api.spacexdata.com/v4/rockets`

## 📝 Logging

Todos los eventos se registran con timestamp:
```
[2026-05-25 18:40:52] Starting extract process
[2026-05-25 18:40:52] Fetching URL: https://api.spacexdata.com/v5/launches
```

Los logs se guardán en `logs.txt` automáticamente.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios mayores, abre un issue primero.

## 📄 Licencia

Este proyecto está bajo licencia MIT.

## 👤 Autor

Proyecto de análisis de datos de SpaceX by **Lucas Erben**

## 📞 Soporte

Si encuentras problemas, revisa:
1. El archivo `logs.txt` para mensajes de error detallados
2. La conexión a PostgreSQL (si usas carga a BD)
3. Las dependencias en `requirements.txt`

---

# SpaceX Data ETL Pipeline

A modular ETL solution to extract, transform, and load SpaceX data into a PostgreSQL database, with analysis of launch success rates.

## 🎯 Features

- **Extract**: Fetches launch and rocket data from SpaceX API
- **Transform**: Cleans and transforms data into a structured DataFrame
- **Load**: Saves data to CSV and PostgreSQL database
- **Analyze**: Calculates statistics and visualizes success rate patterns by year and rocket
- **Logging**: Detailed logging of each stage in console and file

## 📁 Project Structure

```
.
├── main.py              # Main pipeline orchestrator
├── extract.py           # Data extraction module from APIs
├── transform.py         # Data transformation and cleaning module
├── load.py              # CSV and PostgreSQL loading module
├── analyst.py           # Analysis and visualization module
├── logs.py              # Centralized logging module
├── requirements.txt     # Project dependencies
├── .gitignore           # Files to ignore in Git
└── README.md            # This file
```

## 🚀 Installation

### Prerequisites
- Python 3.8+
- PostgreSQL 12+ (if using database loading)
- pip or conda

### Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo>
   cd vulnerabilidades
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database (optional)**
   - Ensure PostgreSQL is running
   - Create a database named `spacex`
   - Update credentials in `load.py` if needed

## 📊 Usage

Run the complete pipeline:

```bash
python main.py
```

### Pipeline Stages

1. **EXTRACT**: Downloads data from two SpaceX endpoints
2. **TRANSFORM**: Cleans, structures, and enriches the data
3. **LOAD**: Saves to CSV (`data/spacex_launches.csv`) and PostgreSQL
4. **ANALYSIS**: Calculates success rates and generates charts

### Expected Output

- **CSV File**: `data/spacex_launches.csv`
- **Database**: `launches` table in PostgreSQL
- **Logs**: `logs.txt` with detailed execution log
- **Charts**: Interactive analysis visualizations

## 📋 Module Descriptions

### `main.py`
Main orchestrator that:
- Coordinates data flow between modules
- Handles exceptions in database loading
- Logs progress of each stage

### `extract.py`
```python
def fetch(url)
```
Performs HTTP requests with configured timeout.

### `transform.py`
- `map_rockets()`: Creates dictionary of rocket IDs to names
- `clean_data()`: Extracts relevant fields from each launch
- `make_df()`: Builds DataFrame with transformations (dates, years, names)

### `load.py`
- `save_to_csv()`: Saves DataFrame to CSV file
- `create_connection()`: Establishes PostgreSQL connection
- `save_launches_to_db()`: Loads data to `launches` table

### `analyst.py`
Calculates and visualizes:
- Overall success rate
- Success rate by year
- Number of launches per year
- Success rate by rocket

Generates interactive charts for each analysis.

### `logs.py`
Centralized logging system that:
- Prints timestamped messages to console
- Persists records in `logs.txt`

## 📈 Analyzed Data

The pipeline processes over 200 SpaceX launches with:
- **Overall success rate**: ~97%
- **Time range**: From first launches to present
- **Rockets**: Falcon 1, Falcon 9, Falcon Heavy, Starship

## 🔧 Configuration

### PostgreSQL Credentials
In `load.py`, adjust the connection string:
```python
"postgresql+psycopg2://user:password@localhost:5432/spacex"
```

### API URLs
The endpoint URLs are defined in `main.py`:
- Launches: `https://api.spacexdata.com/v5/launches`
- Rockets: `https://api.spacexdata.com/v4/rockets`

## 📝 Logging

All events are logged with timestamps:
```
[2026-05-25 18:40:52] Starting extract process
[2026-05-25 18:40:52] Fetching URL: https://api.spacexdata.com/v5/launches
```

Logs are automatically saved to `logs.txt`.

## 🤝 Contributing

Contributions are welcome. For major changes, please open an issue first.

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

SpaceX data analysis project by **Lucas Erben**

## 📞 Support

If you encounter issues, check:
1. The `logs.txt` file for detailed error messages
2. PostgreSQL connection (if using database loading)
3. Dependencies in `requirements.txt`
