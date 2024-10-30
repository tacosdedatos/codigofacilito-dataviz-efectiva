[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tacosdedatos/codigofacilito-dataviz-efectiva/HEAD?urlpath=lab)
***
# codigofacilito-dataviz-efectiva
Materiales para la clase "Visualización de Datos Efectiva con Altair"

***
#### Notas sobre el gráfico final se encuentran en [tacosdedatos.github.io/codigofacilito-dataviz-efectiva](https://tacosdedatos.github.io/codigofacilito-dataviz-efectiva/)
***

## Recursos
* Galería de Altair: [altair-viz.github.io/gallery](https://altair-viz.github.io/gallery)
* Creación de datos sínteticos: 
    - [mockaroo.com](https://mockaroo.com)
    - [drawdata.xyz](https://drawdata.xyz)
* Datawrapper, una herramienta para crear visualizaciones de datos (estáticas e interactivas) muy lindas rápidamente: 
    - sitio web: [datawrapper.de](https://datawrapper.de)
    - blog: [blog.datawrapper.de](https://blog.datawrapper.de)
    - academia: [academy.datawrapper.de](https://academy.datawrapper.de)
* Curso de Altair/Vega-lite de la Universidad de Washington: 
    - sitio web: https://uwdata.github.io/visualization-curriculum/intro.html
    - GitHub: https://github.com/uwdata/visualization-curriculum
* Conjuntos de datos interesantes: [data-is-plural.com](https://data-is-plural.com) 
* Escalas de colores: [colorbrewer2.org](https://colorbrewer2.org) 

## Como usar este repositorio
La manera mas sencilla de utilizar este repositorio es haciendo click en el enlace a Binder al inicio de este README. Si deseas trabajar localmente necesitarás:
1. Clonar este repositorio
2. Crear un entorno virtual de python
3. Instalar los paquetes necesarios
4. ¡Escribir tu código!

La manera recomendada de manejar tus entornos virtuales es con la herramienta `uv` [docs](https://docs.astral.sh/uv/)
en Mac/Linux
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```
en Windows
```shell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Clonar el repositorio
Utiliza `git`
```shell
git clone https://github.com/tacosdedatos/codigofacilito-dataviz-efectiva
```

### Crear un entorno virtual de python
Entra al repositorio **c**ambiando de **d**irectorio (`cd`) y ejecuta uv sync
```shell
cd codigofacilito-dataviz-efectiva
uv sync
```
Esto va a crear un entorno virtual en `.venv/` e instalar los paquetes necesarios

Si deseas usar `venv` (el paquete incluido con tu python)
```shell
cd codigofacilito-dataviz-efectiva
python3 -m venv .venv
```
Y para instalar los paquetes
```shell
python3 -m pip install altair vega_datasets ipykernel
```

Utilizar `uv sync` es el equivalente de ejecutar esos dos comandos.