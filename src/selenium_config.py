"""
SELENIUM CONFIG - Configuração que funciona em qualquer ambiente
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import streamlit as st
from functools import wraps

@st.cache_resource
def get_driver():
    """Retorna driver Chrome configurado para o ambiente atual"""
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        st.warning(f"Usando fallback: {e}")
        options.binary_location = "/usr/bin/chromium-browser"
        driver = webdriver.Chrome(options=options)
    
    return driver

def with_driver(func):
    """Decorator para operações Selenium com cleanup automático"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        driver = None
        try:
            driver = get_driver()
            return func(driver, *args, **kwargs)
        finally:
            if driver:
                driver.quit()
    return wrapper
