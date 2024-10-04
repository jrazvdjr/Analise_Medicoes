import tkinter as tk
from tkinter import messagebox
import math
import statistics


def calcular_medidas():
    try:
        entrada = int(entry_numero.get()) # Recebe o número de medidas
        medidas =[] #Lista para armazenar o valor das medidas

        #Recebe as medidas 
        for i in range(entrada):
            
            medida = float(entry_medida[i].get()) # Solicita as medidas
            
            medidas.append(medida) # Adiciona as medidas à lista

            
        # Cálculos
        media = statistics.mean(medidas) #Realiza a operação para média
        
        desvio_padrao = statistics.stdev(medidas) #Calcula o Desvio Padrão
        
        erro_medio = desvio_padrao / math.sqrt(entrada) # Calcula a Erro Médio
        
        

        # Apresenta a medida final
        resultado = f"Média: {media}\nDesvio Padrão: {desvio_padrao}\nErro Médio: {erro_medio}\nMedida Final: {round(media, 3)} ± {round(erro_medio, 3)}"
        messagebox.showinfo("Resultados", resultado)

    except ValueError:
          messagebox.showerror("Erro!", "Não é possível calcular sem antes receber o Nº de medidas.")

# Iniciar Janela
root = tk.Tk()

root.geometry("400x800")
root.config(bg='#10041c')

root.title("Cálculo de Medidas")

entry_width = 15
entry_height = 3 

# Entrada do número de medidas
label_numero = tk.Label(root, text="Informe o Nº de medidas: ", fg='#ffffff', font=('Arial Black', 14), bg='#10041c')
label_numero.pack(pady=10)
entry_numero = tk.Entry(root, width= entry_width , font=('Arial', 14))
entry_numero.config(justify='center')
entry_numero.pack(pady=10)

# Lista para entradas de medidas realizadas
entry_medida = []

# Função para gerar campos de entrada para as medidas
def campo_medidas():
    try:    
        for widget in frame_medidas.winfo_children(): # Limpa o campo para digitar uma nova medida
            widget.destroy() # fecha o widget

        numero = int(entry_numero.get()) 
        
        for i in range(numero):
            label = tk.Label(frame_medidas, text=f"{i + 1}ª medida:", font=('Arial Black', 10), bg='#10041c', fg='#ffffff', borderwidth=0, highlightthickness=0)
            label.grid(row=i // 2, column=(i % 2) * 2, pady=2)
            
            entry = tk.Entry(frame_medidas, width=entry_width, font=('Arial', 10), bg='#ffffff', borderwidth=0, highlightthickness=0)
            entry.config(justify='center')
            entry.grid(row=i // 2, column=(i % 2) * 2 + 1, pady=10)
            entry_medida.append(entry)  
            
    except ValueError:
        messagebox.showerror('Erro!', "Por favor, informe o Nº de medidas.")

def reiniciar():
    #Loop criado para percorrer os frames e limpa-los
    for widget in frame_medidas.winfo_children():
        widget.destroy()  # Remove todos os widgets do frame
    entry_medida.clear()  # Limpa a lista de entradas de medidas       
    entry_numero.delete(0, tk.END)  # Limpa o campo de entrada do número de medidas

# Botão para criar campos de medidas
btn_criar_campos = tk.Button(root, text="Criar Campos de Medida", command=campo_medidas, font=('Arial', 14), fg='#ffffff', bg='#170a45')
btn_criar_campos.pack(pady=20) 

# Frame para armazenar as entradas de medidas
frame_medidas = tk.Frame(root, bg='#10041c')
frame_medidas.pack()

# Botão para calcular resultados
button_calcular = tk.Button(root, text="Calcular", command=calcular_medidas, font=('Arial', 14), fg='#ffffff', bg='#7255b2')
button_calcular.pack(pady=20)  

btn_reiniciar = tk.Button(root,text="Reiniciar", command=reiniciar, font=('Arial', 14), bg='#008000')
btn_reiniciar.pack(pady=20)

root.mainloop() # Finalizar Janela

    

   




    
