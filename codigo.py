import tkinter as tk
from tkinter import messagebox

# Função para calcular a duração da ração restante
def calcular_duracao():
    try:
        # Obtendo os dados inseridos pelo usuário
        quantidade_restante_kg = float(entry_quantidade_restante.get())  # Quantidade de ração restante em kg
        numero_aves = int(entry_numero_aves.get())  # Número de aves no lote
        sexo = combo_sexo.get().upper()  # Sexo do lote (Só aceita F, S ou M)

        # Convertendo a quantidade de ração de kg para gramas
        quantidade_restante = quantidade_restante_kg * 1000  # 1 kg = 1000 gramas

        # Verificando o sexo e definindo o consumo diário por ave
        if sexo == 'M':
            consumo_diario_ave = 220  # Macho consome 220 gramas por dia
        elif sexo == 'F':
            consumo_diario_ave = 200  # Fêmea consome 200 gramas por dia
        elif sexo == 'S':
            consumo_diario_ave = 220  # Misto consome 220 gramas por dia
        else:
            messagebox.showerror("Erro", "Sexo inválido! Use M para Macho, F para Fêmea ou S para Misto.")
            return

        # Calculando o consumo total diário de ração para todas as aves
        consumo_diario_total = consumo_diario_ave * numero_aves
        
        # Calculando a quantidade de dias que a ração restante vai durar
        dias = quantidade_restante // consumo_diario_total  # Número de dias inteiros que a ração vai durar
        horas = (quantidade_restante % consumo_diario_total) / consumo_diario_total * 24  # Convertendo o restante em horas

        # Exibindo o resultado para o usuário
        resultado_texto = (f"Quantidade Restante: {quantidade_restante_kg} kg ({quantidade_restante} gramas)\n"
                           f"Número de Aves: {numero_aves}\n"
                           f"Sexo: {sexo}\n"
                           f"Consumo Diário Total: {consumo_diario_total} gramas\n"
                           f"A ração durará: {int(dias)} dias e {int(horas)} horas.\n")
        
        # Adicionando a recomendação para o usuário
        if dias <= 2:
            resultado_texto += "URGENTE: Peça ração agora, pois a ração durará menos de 2 dias!"
        elif dias <= 3:
            resultado_texto += "Peça ração quando tiver apenas 3 dias restantes."

        # Atualizando o texto do resultado na interface
        label_resultado.config(text=resultado_texto)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos nos campos!")

# Criando a interface gráfica
root = tk.Tk()
root.title("Calculadora de Duração de Ração para Aviário")

# Labels
label_quantidade_restante = tk.Label(root, text="Quantidade Restante de Ração (kg):")
label_quantidade_restante.grid(row=0, column=0, padx=10, pady=5, sticky='w')
entry_quantidade_restante = tk.Entry(root)
entry_quantidade_restante.grid(row=0, column=1, padx=10, pady=5)

label_numero_aves = tk.Label(root, text="Número de Aves:")
label_numero_aves.grid(row=1, column=0, padx=10, pady=5, sticky='w')
entry_numero_aves = tk.Entry(root)
entry_numero_aves.grid(row=1, column=1, padx=10, pady=5)

label_sexo = tk.Label(root, text="Sexo (M para Macho, F para Fêmea, S para Misto):")
label_sexo.grid(row=2, column=0, padx=10, pady=5, sticky='w')
combo_sexo = tk.Entry(root)
combo_sexo.grid(row=2, column=1, padx=10, pady=5)

# Botão para calcular
botao_calcular = tk.Button(root, text="Calcular Duração", command=calcular_duracao)
botao_calcular.grid(row=3, column=0, columnspan=2, pady=20)

# Label para exibir os resultados
label_resultado = tk.Label(root, text="", justify="left")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Iniciar a interface gráfica
root.mainloop()
