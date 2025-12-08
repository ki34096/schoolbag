import streamlit as st
import pandas as pd

st.set_page_config(page_title="Accuracy Calculator", layout="wide")

st.title("⚽ Accuracy Calculator + Astrology (UMKA Edition)")

st.sidebar.header("Настройки анализа")

# Переключатель режима выбора Home (ручной / по силе планет)
dynamic_home = st.sidebar.checkbox("Определять Home по силе команд (динамически)", value=False)

uploaded_match_file = st.sidebar.file_uploader(
    "Загрузите MATCH INFO (.txt)",
    type=["txt"]
)

if uploaded_match_file:
    try:
        # читаем файл как обычный текст
        content = uploaded_match_file.read().decode("utf-8")
        st.subheader("📄 Данные матча")
        st.text(content)

        # В будущем: парсинг файла и определение команд
        st.info("✔️ Файл загружен успешно. Анализ будет добавлен на следующих этапах.")

    except Exception as e:
        st.error(f"Ошибка чтения файла: {e}")
else:
    st.warning("⬆️ Загрузите файл с данными матча, чтобы начать анализ.")

st.markdown("---")
st.caption("Version 0.1 — Carcass Only. Astrology + Statistics будет добавлено шаг за шагом.")

