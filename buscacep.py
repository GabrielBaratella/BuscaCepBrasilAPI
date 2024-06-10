import requests
import tkinter as tk
from tkinter import messagebox

def buscar_cep():
    cep = entry_cep.get()
    if not cep:
        messagebox.showwarning("Aviso", "Por favor, informe um CEP.")
        return

    url = f'https://brasilapi.com.br/api/cep/v2/{cep}'
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        exibir_resultados(dados)
    else:
        messagebox.showerror("Erro", f"Erro na requisição: {response.status_code}")

def exibir_resultados(dados):
    resultado_window = tk.Toplevel(root)
    resultado_window.title("Resultado da Busca")

    tk.Label(resultado_window, text=f"CEP: {dados['cep']}").pack()
    tk.Label(resultado_window, text=f"Estado: {dados['state']}").pack()
    tk.Label(resultado_window, text=f"Cidade: {dados['city']}").pack()
    tk.Label(resultado_window, text=f"Bairro: {dados['neighborhood']}").pack()
    tk.Label(resultado_window, text=f"Rua: {dados['street']}").pack()

    btn_voltar = tk.Button(resultado_window, text="Voltar", command=resultado_window.destroy)
    btn_voltar.pack()

root = tk.Tk()
root.title("Consulta de CEP")

tk.Label(root, text="Informe o CEP:").pack(pady=10)
entry_cep = tk.Entry(root)
entry_cep.pack(pady=5)

btn_buscar = tk.Button(root, text="Buscar", command=buscar_cep)
btn_buscar.pack(pady=10)

root.mainloop()
