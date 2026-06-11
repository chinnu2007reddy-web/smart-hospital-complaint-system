import streamlit as st


def success_message(message):

    st.success(message)


def error_message(message):

    st.error(message)


def warning_message(message):

    st.warning(message)


def info_message(message):

    st.info(message)