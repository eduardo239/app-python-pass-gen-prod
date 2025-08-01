# Instalação do Tkinter

O Tkinter é a biblioteca padrão para interfaces gráficas em Python. Ele geralmente já vem instalado com o Python, mas em alguns sistemas pode ser necessário instalar manualmente.

## Verificando se o Tkinter está instalado

Execute o seguinte comando no terminal Python:

```python
import tkinter
print(tkinter.TkVersion)
```

Se não houver erro, o Tkinter está instalado.

---

## Instalação no Windows

No Windows, o Tkinter normalmente já está incluído na instalação padrão do Python. Caso não esteja, reinstale o Python a partir do site oficial ([python.org](https://www.python.org/downloads/)) e certifique-se de marcar a opção "tcl/tk and IDLE".

---

## Instalação no Linux

Em algumas distribuições Linux, o Tkinter pode não estar instalado por padrão. Use o comando correspondente à sua distribuição:

### Ubuntu/Debian

```bash
sudo apt-get update
sudo apt-get install python3-tk
```

### Fedora

```bash
sudo dnf install python3-tkinter
```

### Arch Linux

```bash
sudo pacman -S tk
```

---

## Referências

- [Documentação oficial do Tkinter](https://docs.python.org/pt-br/3/library/tkinter.html)
- [Tkinter no PyPI](https://pypi.org/project/tk/)
