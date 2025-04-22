import pandas as pd
from codecarbon import EmissionsTracker
from llamarIA import get_llm_response
import time

# Iniciar el rastreador de emisiones
tracker = EmissionsTracker()
tracker.start()
start_time = time.time()

# Tomar consulta para el modelo de IA por consola
print("\033[93mEscribe 'exit' para salir o cualquier otra cosa para continuar:\033[0m", end=" ")
prompt = input()


# Ejecutar el modelo de IA en funcion de la consulta 
while prompt != "exit":
    if prompt != "exit":
        response = get_llm_response(prompt)
        print(f"\033[96mRespuesta del modelo: {response}\n\n\033[0m")
    print("\033[93mEscribe 'exit' para salir o cualquier otra cosa para continuar:\033[0m", end=" ")    
    prompt = input()

end_time = time.time()
tiempo_ejecucion = end_time - start_time  

# Detener el rastreador y obtener las emisiones de carbono
emissions = tracker.stop()

# Verificar si emissions es None
if emissions is None:
    emissions = 0.0

# Imprimir resultados
print('\n\n' + "-" * 50)
print(f'\033[92mEmisiones totales de carbono: {round(emissions, 7)} kg CO₂ en {tiempo_ejecucion:.2f} segundos\033[0m')

# Calcular las horas de procesamiento necesarias para compensar 30 kg de CO2 (kg CO2 por año)
co2_absorbido_por_arbol = 30  

# Calcular el consumo por hora basado en el tiempo de ejecución
emisiones_por_segundo = emissions / tiempo_ejecucion
emisiones_por_hora = emisiones_por_segundo * 3600

# Calcular las horas necesarias para compensar 30 kg de CO2
horas_necesarias = co2_absorbido_por_arbol / emisiones_por_hora

# Guardar resultados en un CSV
df = pd.DataFrame({
    "Métrica": ["Emisiones de carbono (kg CO₂)", "Emisiones por hora (kg CO₂)", "Horas necesarias para emitir 30 kg de CO₂"],
    "Valor": [round(emissions, 7), round(emisiones_por_hora, 7), round(horas_necesarias, 2)]
})

df.to_csv("resultados.csv", index = False)

# Imprimir el resultado
print(f'\033[92mEmisiones por hora: {emisiones_por_hora:.4f} kg CO₂\033[0m')
print(f'\033[92mUn árbol recien plantado (consume 30 kg CO₂/año) compensa aproximadamente {horas_necesarias:.2f} horas de procesamiento.\033[0m')
print('\033[92mResultados guardados en "resultados.csv"\033[0m')
