import random
import string

def gerar_senha(tamanho, maiusculas, minusculas, numeros, simbolos):
    caracteres = ""
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Erro: Selecione pelo menos um tipo de caractere."

    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha