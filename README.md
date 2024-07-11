# iol_py
 Es una librería de Python diseñada para obtener información de la API de Invertir Online. Esta herramienta facilita la integración y el acceso a los datos proporcionados por la plataforma, permitiendo a los desarrolladores trabajar de manera más eficiente con la información financiera.


## Instalación

```bash
pip install iol_py_package_joseph0001

```


# Clase IOL

La clase `IOL` proporciona métodos para interactuar con la API de Invertir Online.

## Métodos

### `__init__()`

Inicializa una instancia de la clase `IOL` con las credenciales de usuario y contraseña obtenidas del archivo `.env`.

### `obtener_estado_de_cuenta()`

Obtiene el estado de cuenta actual del usuario autenticado en Invertir Online.

- **Parámetros:** Ninguno.
- **Devuelve:** No devuelve explícitamente ningún valor. Presenta los resultados del estado de cuenta utilizando la función `presentar_resultados_estado()` del módulo `utils`.

### `mi_portafolio()`

Obtiene los detalles del portafolio de inversiones del usuario en Argentina.

- **Parámetros:** Ninguno.
- **Devuelve:** Un DataFrame de pandas con los siguientes campos para cada activo en el portafolio:
  - Descripción
  - Símbolo
  - Nominales
  - Cotización
  - Moneda
  - Variación desde Compra (%)
  - Valorizado
  - Variación Diaria (%)
  - Ganancia Nominal

### `mis_operaciones(tipo='todas', fechadesde='2020-02-01', fechahasta='2024-07-01', pais='argentina')`

Obtiene las operaciones realizadas por el usuario en un rango de fechas y país específicos.

- **Parámetros:**
  - `tipo`: Tipo de operaciones a filtrar (opcional, por defecto `'todas'`).
  - `fechadesde`: Fecha desde la cual filtrar las operaciones (opcional, por defecto `'2020-02-01'`).
  - `fechahasta`: Fecha hasta la cual filtrar las operaciones (opcional, por defecto `'2024-07-01'`).
  - `pais`: País donde se realizaron las operaciones (opcional, por defecto `'argentina'`).
  
- **Devuelve:** Un DataFrame de pandas con las operaciones filtradas.

### `hist_precio(mercado='bcba', simbolo='ko', desde='2020-02-01', hasta='2024-07-01', ajustada='sinAjustar')`

Obtiene el histórico de precios para un símbolo específico en un mercado determinado en un rango de fechas.

- **Parámetros:**
  - `mercado`: Mercado donde se cotiza el símbolo (opcional, por defecto `'bcba'`).
  - `simbolo`: Símbolo del título para el cual se desea obtener el histórico de precios (obligatorio).
  - `desde`: Fecha desde la cual obtener el histórico de precios (opcional, por defecto `'2020-02-01'`).
  - `hasta`: Fecha hasta la cual obtener el histórico de precios (opcional, por defecto `'2024-07-01'`).
  - `ajustada`: Tipo de ajuste de precios (opcional, por defecto `'sinAjustar'`).

- **Devuelve:** Una lista de objetos JSON con el histórico de precios para el símbolo especificado.

## Ejemplo de Uso

```python
from iol_py_package_joseph0001.iol_py import IOL
from dotenv import load_dotenv
load_dotenv()


    try:
        # Obtener las credenciales desde las variables de entorno
        usuario = os.environ.get('USUARIO')
        clave = os.environ.get('CLAVE')

        # Crear una instancia de la clase IOL con las credenciales obtenidas
        iol = IOL(usuario, clave)

        # Obtener el estado de cuenta
        print("Estado de cuenta actual:")
        iol.obtener_estado_de_cuenta()

        # Obtener el portafolio en Argentina
        print("\nObteniendo datos del portafolio en Argentina:")
        df_portafolio = iol.mi_portafolio()
        if df_portafolio is not None:
            print(df_portafolio)

        # Obtener las operaciones
        print("\nObteniendo operaciones:")
        df_operaciones = iol.mis_operaciones()
        if df_operaciones is not None:
            print(df_operaciones)

        # Obtener datos históricos de precios
        print("\nObteniendo datos históricos de precios:")
        hist_precios = iol.hist_precio(simbolo='GGAL', desde='2020-01-01', hasta='2021-01-01')
        if hist_precios is not None:
            print(hist_precios)

    except Exception as e:
        print(f"Error general: {e}")
```

## Contribución

¡Gracias por considerar contribuir a iol_py! Si quieres mejorar esta librería, por favor envía un pull request. Estamos abiertos a sugerencias y mejoras.