import tkinter as tk
from tkinter import ttk
import random
import string

# Lógica do Gerador
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

# --- Interface Gráfica ---
def criar_interface():
    janela = tk.Tk()
    janela.title("Gerador de Senhas")
    janela.geometry("350x300") # Aumente a janela para acomodar o padding

    var_maiusculas = tk.BooleanVar(value=True)
    var_minusculas = tk.BooleanVar(value=True)
    var_numeros = tk.BooleanVar(value=True)
    var_simbolos = tk.BooleanVar(value=True)

    # Adicionando padding (padx e pady) a cada widget

    ttk.Label(janela, text="Tamanho da Senha:").pack(pady=5)

    tamanho_entrada = ttk.Entry(janela)
    tamanho_entrada.insert(0, "12")
    tamanho_entrada.pack(pady=5, padx=10)

    # Use 'anchor="w"' para alinhar os checkboxes à esquerda
    ttk.Checkbutton(janela, text="Letras Maiúsculas", variable=var_maiusculas).pack(anchor="w", padx=10)
    ttk.Checkbutton(janela, text="Letras Minúsculas", variable=var_minusculas).pack(anchor="w", padx=10)
    ttk.Checkbutton(janela, text="Números", variable=var_numeros).pack(anchor="w", padx=10)
    ttk.Checkbutton(janela, text="Símbolos", variable=var_simbolos).pack(anchor="w", padx=10)

    # Fonte Monospace para a senha
    fonte_senha = ("Courier", 14)
    senha_gerada = tk.StringVar()
    senha_label = ttk.Entry(janela, textvariable=senha_gerada, state='readonly', width=40, font=fonte_senha)
    senha_label.pack(pady=10, padx=10)

    mensagem_copiado = tk.StringVar()
    mensagem_label = ttk.Label(janela, textvariable=mensagem_copiado)
    mensagem_label.pack(pady=(0, 5))

    def ao_clicar_gerar():
        try:
            tamanho = int(tamanho_entrada.get())
            senha = gerar_senha(
                tamanho,
                var_maiusculas.get(),
                var_minusculas.get(),
                var_numeros.get(),
                var_simbolos.get()
            )
            senha_gerada.set(senha)

            janela.clipboard_clear()
            janela.clipboard_append(senha)

            mensagem_copiado.set("Senha copiada para a área de transferência!")

        except ValueError:
            senha_gerada.set("Erro: Digite um número válido para o tamanho.")
            mensagem_copiado.set("")

    ttk.Button(janela, text="Gerar e Copiar Senha", command=ao_clicar_gerar).pack(pady=10, padx=10)

    janela.mainloop()

if __name__ == "__main__":
    criar_interface()