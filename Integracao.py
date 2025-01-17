import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função de cálculo do peso e dias para abate
def calcular_dias_para_abate():
    try:
        # Tentando converter os valores de entrada para números
        idade_lote = int(entrada_idade.get())
        gpd = float(entrada_gpd.get())
        mortalidade_total = int(entrada_mortalidade.get())
        aves_iniciais = int(entrada_quantidade_aves.get())
        peso_abate = 3300  # Peso desejado para abate (3,300 gramas)

        # Verificando se os valores são positivos
        if idade_lote < 0 or gpd < 0 or mortalidade_total < 0 or aves_iniciais < 0:
            raise ValueError("Valores não podem ser negativos!")

        # Calculando o peso atual do lote (GPD * Idade)
        peso_atual = gpd * idade_lote

        # CCalculando os dias restantes para atingir o peso de abate
        if peso_atual >= peso_abate:
            dias_necessarios = 0  # Já atingiu o peso de abate
        else:
            dias_necessarios = (peso_abate - peso_atual) / gpd  # Calcular dias restantes

        # Calculando as aves restantes após a mortalidade
        aves_restantes = aves_iniciais - mortalidade_total

        # CaCalculando a mortalidade média (por dia)
        mortalidade_media = (mortalidade_total / idade_lote) * dias_necessarios

        # Calculando a mortalidade no dia de abate
        mortalidade_abate = mortalidade_media + mortalidade_total

        # Criar tabela de resultados
        tabela.delete(*tabela.get_children())  # Limpar a tabela antes de inserir novos dados
        tabela.insert("", "end", values=(
            idade_lote, gpd, mortalidade_total, aves_restantes, round(peso_atual, 4), round(dias_necessarios, 2),
            round(mortalidade_abate, 2)))

        # Exibindo o texto de dias restantes para abate
        if dias_necessarios > 0:
            texto_dias_restantes = f"Faltam {round(dias_necessarios, 2)} dias para o abate"
        else:
            texto_dias_restantes = "Já atingiu o peso de abate"
        label_dias_restantes.config(text=texto_dias_restantes)

        # Exibindo a mortalidade média adicional nos dias restantes
        label_mortalidade_media.config(text=f"Mortalidade Abate: {round(mortalidade_abate, 2)} aves")

    except ValueError as ve:
        messagebox.showerror("Erro de Entrada", f"Entrada inválida: {ve}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criando a interface gráfica com bb Tkinter
root = tk.Tk()
root.title("Programa de Ração para Abate")

# Definindo os widgets de entrada de dados
label_idade = tk.Label(root, text="Idade do Lote (dias):")
label_idade.grid(row=0, column=0, padx=10, pady=5)

entrada_idade = tk.Entry(root)
entrada_idade.grid(row=0, column=1, padx=10, pady=5)

label_quantidade_aves = tk.Label(root, text="Quantidade de Aves:")
label_quantidade_aves.grid(row=1, column=0, padx=10, pady=5)

entrada_quantidade_aves = tk.Entry(root)
entrada_quantidade_aves.grid(row=1, column=1, padx=10, pady=5)

label_gpd = tk.Label(root, text="GPD (Ganho de Peso Diário):")
label_gpd.grid(row=2, column=0, padx=10, pady=5)

entrada_gpd = tk.Entry(root)
entrada_gpd.grid(row=2, column=1, padx=10, pady=5)

label_mortalidade = tk.Label(root, text="Mortalidade Total do Lote:")
label_mortalidade.grid(row=3, column=0, padx=10, pady=5)

entrada_mortalidade = tk.Entry(root)
entrada_mortalidade.grid(row=3, column=1, padx=10, pady=5)

# Botão para calcular e gerar a tabela
botao_calcular = tk.Button(root, text="Calcular", command=calcular_dias_para_abate)
botao_calcular.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# tabela para exitir todos os resultados 
colunas = ("Idade Lote", "GPD", "Mortalidade", "Aves Restantes", "Peso Atual", "Dias para Abate", "Mortalidade Abate")
tabela = ttk.Treeview(root, columns=colunas, show="headings")
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=120, anchor='center')

tabela.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Label para mostrar os dias restantes para abate
label_dias_restantes = tk.Label(root, text="")
label_dias_restantes.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Label para mostrar a mortalidade adicional nos dias restantes
label_mortalidade_media = tk.Label(root, text="")
label_mortalidade_media.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Rodando a face gráfica
root.mainloop()