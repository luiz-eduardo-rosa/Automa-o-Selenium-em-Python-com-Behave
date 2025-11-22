
import unittest
import base64
import time
import os
import subprocess
import pytz
import allure
import json
import urllib3
import behave
import behave_html_formatter
from behave import *
from selenium import webdriver
from .ambiente import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PageUtils(unittest.TestCase):
    # Configurações e opções Crhome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-site-isolation-trials')
    chrome_options.add_argument('--ignore-certifate-erros')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)

    def abrir_um_browser(context, base_url):
        context.driver.get(base_url)

    def limpar_browser(context):
        context.driver.delete_all_cookies()

    def fechar_browser(context):
        context.driver.quit()

    def clicar_elemento_pagina(context, pesquisa):
        context.driver.find_element(By.XPATH, pesquisa).click()

    def inserir_dados_no_elemento(context, xpath_elemento, texto):
        context.driver.find_element(By.XPATH, xpath_elemento).send_keys(texto)

