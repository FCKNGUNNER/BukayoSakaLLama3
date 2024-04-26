import streamlit as st
from transformers import pipeline

# Загрузка модели Llama-3
saiga_pipeline = pipeline("text-generation", model="IlyaGusev/saiga_llama3_8b")

# Функция для генерации текста с использованием модели Llama-3
def generate_text(prompt):
    return saiga_pipeline(prompt, max_length=100, do_sample=True, temperature=0.9)[0]['generated_text']

# Главная часть приложения
st.title('Генератор текста с помощью модели Llama-3')
prompt = st.text_input("Введите ваш запрос:", "Начните вводить текст...")
if st.button('Сгенерировать'):
    generated_text = generate_text(prompt)
    st.write(generated_text)
