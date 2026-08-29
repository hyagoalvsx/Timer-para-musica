import time
import sys

DOURADO = "\033[33m"
RESET = "\033[0m"

def carregar_letras(arquivo):
    letras = []

    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()

            if not linha:
                continue
            
            if not linha.startswith("[") or "]" not in linha:
                continue

            tempo_str, texto = linha[1:].split("]", 1)

            try:
                minutos, segundos = tempo_str.split(":")
                tempo = int(minutos) * 60 + float(segundos)
            except ValueError:
                continue

            letras.append((tempo, texto.strip()))
        return letras

def escrever_suave(texto, velocidade=0.035):
    for caractere in texto:
        sys.stdout.write(DOURADO + caractere + RESET)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def tocar_letras(letras):
    inicio = time.time()

    for tempo, texto in letras:
        while time.time() - inicio < tempo:
            time.sleep(0.01)
        escrever_suave(texto)

print(DOURADO + "═══════════════════════════════════════════════" + RESET)
print(DOURADO + " POTE DE OURO (part. Priscila Senna) - Liniker" + RESET)
print(DOURADO + "═══════════════════════════════════════════════" + RESET)

time.sleep(1)
letras = carregar_letras("potedeouro.txt")
tocar_letras(letras)
time.sleep(2)
