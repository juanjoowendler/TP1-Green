# Seguimiento de Emisiones de CO₂ con CodeCarbon

## 📘 Contexto
Este proyecto forma parte de un trabajo práctico que busca cuantificar la huella de carbono generada por la ejecución de un código en Python. Se utiliza la biblioteca [CodeCarbon](https://github.com/mlco2/codecarbon) para rastrear el consumo energético y las emisiones de CO₂ asociadas.

Además, se calcula cuántas horas de procesamiento pueden ser compensadas por un árbol recién plantado, considerando que este absorbe aproximadamente 30 kg de CO₂ en su primer año de vida.

## 🚀 Enfoque del Trabajo
1. **Inicialización del Rastreador:** Se inicia un objeto `EmissionsTracker` de CodeCarbon al comienzo de la ejecución.  
2. **Medición de Tiempo:** Se registra el tiempo de ejecución del código para calcular la tasa de emisión por segundo y por hora.  
3. **Interacción con el Usuario:** Se realiza un bucle que permite al usuario enviar consultas a un modelo de IA (módulo `llamarIA.get_llm_response`) hasta que escriba `exit`.  
4. **Cálculo de Emisiones:** Al finalizar, se detiene el rastreador y se obtienen las emisiones totales de carbono (kg CO₂).  
5. **Cálculo de Compensación:** A partir de las emisiones por hora, se determina cuántas horas de procesamiento equivale a los 30 kg de CO₂ absorbidos por un árbol en un año.  
6. **Exportación de Resultados:** Se almacenan las métricas en un archivo `resultados.csv` y se muestran por consola.

## 🛠️ Requisitos
- Python 3.7 o superior  
- Dependencias en `requirements.txt`:
  ```plaintext
  pandas
  codecarbon
  llamarIA  # Biblioteca o módulo local para interacción con el modelo
