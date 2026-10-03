from langchain_ollama import OllamaLLM
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate


# Aqui cargamos el modelo de IA  de OLLAMA
llm = OllamaLLM(model="ministral-3")

# Inicializamos la memoria
chat_history = ChatMessageHistory()

# Definimos el chat prompt de la IA
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="previous conversation: {chat_history}\n User: {question}\n IA: "
    
)

# Funcion para ejecutar chat con memoria 
def run_chain(question):
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages])

    # Respuesta de la IA
    respuesta = llm.invoke(prompt.format(chat_history= chat_history_text, question= question))
    
    # Almacena la nueva entrada del usuario y la respuesta de la IA
    chat_history.add_user_message(question)
    chat_history.add_ai_message(respuesta)
    
    return respuesta

print("\n IA con memoria")
print("si quieres salir del chat escribe 'salir'")

while True:
    user_input = input("\n Tu: ")
    if user_input.lower() == "salir":
        print("Adios .. .")
        break
    
    respuesta_IA = run_chain(user_input)
    print(f"\n IA: {respuesta_IA}")


    

# Aqui cargamos el modelo de IA  de OLLAMA
"""llm = OllamaLLM(model="ministral-3")

print("Bienvenido a tu agente de IA¡, preguntame cualquier cosa.")

while True:
    pregunta = input("\n tu pregunta: (o escribes 'salir' si quieres parar): ")
    if pregunta.lower() == "salir":
        print("Adios ..")
        break
    respuesta = llm.invoke(pregunta)
    print(f"\n Respuesta IA: {respuesta}")"""