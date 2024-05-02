import streamlit as st
from transformers import pipeline

# Загрузка модели Llama-3
saiga_pipeline = pipeline("text-generation", model="IlyaGusev/saiga_llama3_8b")

# Функция для генерации ответа с использованием модели Llama-3
def generate_response(prompt):
    # Генерация текста с помощью модели Llama-3
    generated_text = saiga_pipeline(prompt, max_length=100, do_sample=True, temperature=0.9)[0]['generated_text']
    return generated_text

# Главная часть приложения
st.title('Генератор ответов от Ламы')
prompt = st.text_input("Ваш вопрос:", "Задайте вопрос Ламе...")
if st.button('Ответить'):
    response = generate_response(prompt)
    st.markdown(f"**Ответ:** {response}")
