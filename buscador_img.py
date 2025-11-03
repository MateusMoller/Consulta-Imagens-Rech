import keyboard
import pyautogui
import pyperclip
import os
import fnmatch
import time
import subprocess

# Caminho da pasta onde procurar os arquivos
PASTA_ALVO = r'M:\RECH\IMAGEM_RECH'

# Atalho definido pelo usuário (pode ser alterado)
ATALHO_USUARIO = 'ctrl+shift+i'

def obter_texto_selecionado():
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    return pyperclip.paste()

def buscar_arquivos_img(nome, pasta):
    resultados = []
    for raiz, dirs, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if arquivo.lower().endswith('.jpg') and nome.lower() in arquivo.lower():
                resultados.append(os.path.join(raiz, arquivo))
    return resultados

def abrir_arquivo(caminho):
    try:
        os.startfile(caminho)  # no Windows, abre com o programa padrão
        print(f"✅ Arquivo aberto: {caminho}")
    except Exception as e:
        print(f"❌ Erro ao abrir o arquivo: {e}")

def ao_acionar_atalho():
    print("\n🔍 Procurando arquivos .img com o nome selecionado...")
    texto = obter_texto_selecionado()
    if not texto.strip():
        print("⚠️ Nenhum texto foi selecionado.")
        return

    resultados = buscar_arquivos_img(texto.strip(), PASTA_ALVO)
    if resultados:
        print(f"✅ {len(resultados)} arquivo(s) encontrado(s). Abrindo o primeiro:")
        abrir_arquivo(resultados[0])
    else:
        print("❌ Nenhum arquivo .img encontrado.")

# Escuta o atalho e executa a função
print(f"Aguardando atalho: {ATALHO_USUARIO}")
keyboard.add_hotkey(ATALHO_USUARIO, ao_acionar_atalho)
keyboard.wait()

