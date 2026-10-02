from langchain_ollama import OllamaLLM

# Aqui cargamos el modelo de IA  de OLLAMA
llm = OllamaLLM(model="ministral-3")

print("Bienvenido a tu agente de IA¡, preguntame cualquier cosa.")

while True:
    pregunta = input("\n tu pregunta: (o escribes 'salir' si quieres parar): ")
    if pregunta.lower() == "salir":
        print("Adios ..")
        break
    respuesta = llm.invoke(pregunta)
    print(f"\n Respuesta IA: {respuesta}")