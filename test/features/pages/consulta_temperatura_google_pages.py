import time
from features.support.ambiente import *
from features.support.elementos import *
from features.support.page_utils import PageUtils
pageutils = PageUtils()


class PesquisaTemperatura:
    def acessar_site_google(context):
        pageutils.abrir_um_browser(URL_GOOGLE)

    def pesquisar_temperatura(context):
        pageutils.clicar_elemento_pagina(PESQ_GOOGLE)

        time.sleep(5)

    def inserir_texto_no_elemento(context):
        pageutils.inserir_dados_no_elemento(PESQ_GOOGLE, DESC_PESQ)

        time.sleep(5)

    def clicar_para_realizar_pesquisa(context):
        pageutils.clicar_elemento_pagina(BTN_DESC_PESQ)

        time.sleep(5)
