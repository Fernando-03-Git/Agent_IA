import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(model="Ministral-3")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatMessageHistory()
    
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="previous conversation: {chat_history}\n User: {question}\n IA: "
)

def run_chain(question):
    chat_history_text = "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.messages])

    # Respuesta de la IA
    respuesta = llm.invoke(prompt.format(chat_history= chat_history_text, question= question))
    
    # Almacena la nueva entrada del usuario y la respuesta de la IA
    st.session_state.chat_history.add_user_message(question)
    st.session_state.chat_history.add_ai_message(respuesta)
    
    return respuesta

# Streamlit IU

st.title(" IA con memoria ")
st.write("Hazme una pregunta")

user_input= st.text_input("Tu pregunta: ")
if user_input:
    respuesta = run_chain(user_input)
    st.write(f"**Tu:** {user_input}")
    st.write(f"**IA:** {respuesta}")
    
st.subheader(" historial de chat ")
for msg in st.session_state.chat_history.messages:
    st.write(f"**{msg.type.capitalize()}**: {msg.content}")