# CyberSniper

Este proyecto es un prototipo para monitorear tiendas de comercio electrónico chilenas durante eventos como CyberDay y detectar anomalías de precios.

## Componentes

- **scraper**: funciones de ejemplo para extraer productos de diversas tiendas (Falabella, Paris, Ripley, etc.).
- **analyzer**: detección simple de anomalías (por ejemplo, descuentos superiores al 80 %).
- **main.py**: aplicación FastAPI que expone endpoints para obtener todos los productos y las anomalías.

## Empezar

1. Instala las dependencias:
   pip install -r requirements.txt

2. Ejecuta el servidor:
   uvicorn main:app --reload

Esto iniciará la API en http://localhost:8000

## Notas

- El scraper actualmente devuelve datos de ejemplo. Implementa la lógica real de scraping para cada tienda.
- El detector de anomalías usa un umbral simple. Puedes reemplazarlo por un modelo más sofisticado.
