# Alunos: Luana, Eduarda e Murilo
# Data: 25/04/2025
# Disciplina: Software básico, 1º semestre, M2
# Professor: Luiz
# Tema: Agendamento de consultas médicas

from tkinter import *           # Tkinter: biblioteca padrão do Python para criar interfaces gráficas (janelas, botões, campos de texto, etc)
from tkinter import messagebox  # messagebox: módulo do Tkinter para exibir caixas de mensagem (alertas, avisos, erros) para o usuário
import os                      # os: fornece funções para interagir com o sistema operacional, como manipulação de arquivos e caminhos
import json                    # json: permite ler e salvar dados em formato JSON, facilitando a persistência de dados estruturados (listas/dicionários)
from tabulate import tabulate  # tabulate: formata listas de dados em tabelas bonitas, útil para exibir relatórios na interface
import uuid                    # uuid: gera identificadores únicos universais (não está sendo usada no momento, pois o ID é sequencial)
import re                      # re: módulo de expressões regulares, usado para validar formatos de entrada (como data e horário)  
from datetime import datetime  # datetime: módulo para manipulação e validação de datas e horas
from PIL import Image, ImageTk  # PIL: biblioteca para manipulação de imagens, usada para exibir imagens na interface 
# Variável global que armazena todas as consultas em memória
# Cada consulta é um dicionário com os campos: ID, Paciente, Data, Horário, Médico, Especialidade
Minha_Lista = []

def Logo():
    #Lê a imagem do logo usando a biblioteca PIL (Pillow)
    image = Image.open("logo1.png")
    #Redimensiona a imagem para 100x100 pixels
    resize_image = image.resize((100, 100))
    img = ImageTk.PhotoImage(resize_image)
    #Cria um rótulo (Label) para exibir a imagem do logo
    Logo = Label(image=img)
    Logo.image = img 
    Logo.place(x=100, y=10)  # Define a posição do logo na janela

def validar_data_hora(data, hora):
    """
    Valida se a data e a hora fornecidas são válidas.
    :param data: String no formato 'dd/mm/yyyy'
    :param hora: String no formato 'HH:MM'
    :return: True se ambos forem válidos, False caso contrário
    """
    try:
        # Valida a data no formato 'dd/mm/yyyy'
        datetime.strptime(data, "%d/%m/%Y")
        # Valida a hora no formato 'HH:MM'
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False

def carregar_dados():
    """
    Carrega as consultas do arquivo 'dados.txt' para a variável global Minha_Lista.
    Se o arquivo existir, lê os dados em formato JSON.
    Corrige os IDs para serem sequenciais (1, 2, 3, ...).
    """
    global Minha_Lista
    if os.path.exists("dados.txt"):
        with open("dados.txt", "r", encoding="utf-8") as arquivo:
            try:
                # Aqui o arquivo é lido e convertido de JSON para lista de dicionários Python
                Minha_Lista = json.load(arquivo)
                # Corrige indìces antigos para numeração sequencial
                for idx, consulta in enumerate(Minha_Lista, start=1):
                    consulta["ID"] = str(idx)
                salvar_dados()
            except json.JSONDecodeError:
                Minha_Lista = []

def salvar_dados():
    """
    Salva a lista de consultas (Minha_Lista) no arquivo 'dados.txt' em formato JSON.
    O formato JSON facilita a leitura e escrita dos dados estruturados.
    """
    with open("dados.txt", "w", encoding="utf-8") as arquivo:
        # Aqui a lista de dicionários é convertida para texto JSON e salva no arquivo
        json.dump(Minha_Lista, arquivo, ensure_ascii=False, indent=4)

def limpar_frame_conteudo():
    """
    Limpa todos os widgets do frame de conteúdo (área principal da interface).
    Usado antes de desenhar novas telas.
    """
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

def relatorio_geral():
    """
    Mostra um relatório geral de todas as consultas cadastradas.
    Usa a biblioteca 'tabulate' para formatar a tabela.
    """
    limpar_frame_conteudo()
    if Minha_Lista:
        Colunas1 = ["ID", "Paciente", "Data", "Horário", "Médico", "Especialidade"]
        Tabela1 = [[consulta["ID"], consulta["Paciente"], consulta["Data"], consulta["Horário"], consulta["Médico"], consulta["Especialidade"]]
            for consulta in Minha_Lista]
        relatorio1 = tabulate(Tabela1, headers=Colunas1, tablefmt="double_grid")

        frame_texto = Frame(frame_conteudo, bg="white")
        frame_texto.pack(expand=True, fill="both")

        scrollbar_y = Scrollbar(frame_texto, orient="vertical")
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x = Scrollbar(frame_texto, orient="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")

        text_widget = Text(
            frame_texto,
            font=("Consolas", 13),
            wrap="none",
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set,
            bg="white",
            fg="#1a237e"
        )
        text_widget.pack(expand=True, fill="both")
        text_widget.insert("1.0", relatorio1)
        text_widget.config(state="disabled")

        scrollbar_y.config(command=text_widget.yview)
        scrollbar_x.config(command=text_widget.xview)
    else:
        Label(frame_conteudo, text="Nenhuma consulta agendada.",
              font=("Segoe UI", 14, "bold"), fg="#b71c1c", bg="white", pady=15, justify="center").pack(anchor="center")

def proximo_id():
    """
    Retorna o próximo ID disponível para uma nova consulta.
    O ID é sempre um número sequencial, baseado nos IDs já existentes.
    """

    # Se a lista de consultas estiver vazia, retorna "1" como o primeiro ID disponível
    if not Minha_Lista:
        return "1"
    
    # Cria uma lista com todos os IDs existentes, convertendo-os para inteiro (apenas se forem dígitos)
    ids = [int(c["ID"]) for c in Minha_Lista if c["ID"].isdigit()]

    # Retorna o próximo ID disponível (maior ID + 1), ou "1" se não houver IDs válidos
    return str(max(ids) + 1) if ids else "1"

def agendar_consulta():
    """
    Tela para agendar uma nova consulta.
    Coleta dados do usuário, valida e adiciona à Minha_Lista.
    O ID é gerado automaticamente.
    """
    def salvar_consulta():
        paciente = entrada_paciente.get()
        data = entrada_data.get()
        horario = entrada_horario.get()
        medico = entrada_medico.get()
        especialidade = entrada_especialidade.get()

        # Validação do formato da data e horário usando a função validar_data_hora
        if not validar_data_hora(data, horario):
            messagebox.showerror("Erro", "Data ou horário inválidos! Use DD/MM/YYYY para data e HH:MM para horário.")
            return

        if paciente and data and horario and medico and especialidade:
            nova_consulta = {
                "ID": proximo_id(),
                "Paciente": paciente,
                "Data": data,
                "Horário": horario,
                "Médico": medico,
                "Especialidade": especialidade
            }
            Minha_Lista.append(nova_consulta)
            salvar_dados()
            messagebox.showinfo("Sucesso", "Consulta agendada com sucesso!")
            agendar_consulta()
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        
    limpar_frame_conteudo()

    # Bloco de interface para agendamento de consulta 
    # Título da tela
    Label(frame_conteudo, text="Agendar Nova Consulta", font=("Segoe UI", 18, "bold"),
          fg="#07254b", bg="white", pady=15, justify="center").pack(anchor="center")
    
    # Campo para nome do paciente
    Label(frame_conteudo, text="Nome do Paciente:", font=("Segoe UI", 14, "bold"),
          fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
    entrada_paciente = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
    entrada_paciente.pack(pady=(0, 10))

    # Campo para data da consulta
    Label(frame_conteudo, text="Data da Consulta (DD/MM/YYYY):", font=("Segoe UI", 14, "bold"),
          fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
    entrada_data = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
    entrada_data.pack(pady=(0, 10))

    # Campo para horário da consulta
    Label(frame_conteudo, text="Horário da Consulta (HH:MM):", font=("Segoe UI", 14, "bold"),
          fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
    entrada_horario = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
    entrada_horario.pack(pady=(0, 10))

    # Campo para nome do médico
    Label(frame_conteudo, text="Nome do Médico:", font=("Segoe UI", 14, "bold"),
          fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
    entrada_medico = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
    entrada_medico.pack(pady=(0, 10))

    # Campo para especialidade
    Label(frame_conteudo, text="Especialidade:", font=("Segoe UI", 14, "bold"),
          fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center") 
    entrada_especialidade = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
    entrada_especialidade.pack(pady=(0, 10))

    # Botão para salvar a nova consulta
    Button(frame_conteudo, text="Salvar", font=("Segoe UI", 13, "bold"),
           bg="#94c8ce", fg="white", command=salvar_consulta).pack(pady=15)

def alterar_consulta():
    """
    Tela para alterar uma consulta existente.
    Busca a consulta pelo ID informado.
    Permite alterar qualquer campo, mantendo os antigos se não for digitado nada novo.
    """
    if Minha_Lista:
        def salvar_alteracao():
            try:
                id_busca = entrada_id.get().strip()
                # Procura na lista 'Minha_Lista' a primeira consulta cujo campo "ID" seja igual ao valor de 'id_busca'.
                # Se encontrar, retorna o dicionário da consulta; se não encontrar, retorna None.
                consulta = next((c for c in Minha_Lista if c["ID"] == id_busca), None)

                if consulta:
                    paciente = entrada_paciente.get() or consulta["Paciente"]
                    data = entrada_data.get() or consulta["Data"]
                    horario = entrada_horario.get() or consulta["Horário"]
                    medico = entrada_medico.get() or consulta["Médico"]
                    especialidade = entrada_especialidade.get() or consulta["Especialidade"]

                    # Validação do formato da data e horário usando a função validar_data_hora
                    if not validar_data_hora(data, horario):
                        messagebox.showerror("Erro", "Data ou horário inválidos! Use DD/MM/YYYY para data e HH:MM para horário.")
                        return
                    
                    consulta.update({
                        "Paciente": paciente,
                        "Data": data,
                        "Horário": horario,
                        "Médico": medico,
                        "Especialidade": especialidade
                    })
                    salvar_dados()
                    messagebox.showinfo("Sucesso", "Consulta alterada com sucesso!")
                    alterar_consulta()
                else:
                    messagebox.showerror("Erro", "ID não encontrado!")
            except Exception:
                messagebox.showerror("Erro", "Erro ao alterar consulta!")

        limpar_frame_conteudo()

        Label(frame_conteudo, text="Alterar Consulta", font=("Segoe UI", 18, "bold"),
              fg="#07254b", bg="white", pady=15, justify="center").pack(anchor="center")
        Label(frame_conteudo, text="ID da Consulta:", font=("Segoe UI", 14, "bold"),
              fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
        entrada_id = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
        entrada_id.pack(pady=(0, 10))

        Label(frame_conteudo, text="Nome do Paciente:", font=("Segoe UI", 14, "bold"),
              fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
        entrada_paciente = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
        entrada_paciente.pack(pady=(0, 10))

        Label(frame_conteudo, text="Data da Consulta (DD/MM/YYYY):", font=("Segoe UI", 14, "bold"),
              fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
        entrada_data = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
        entrada_data.pack(pady=(0, 10))

        Label(frame_conteudo, text="Horário da Consulta (HH:MM):", font=("Segoe UI", 14, "bold"),
              fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
        entrada_horario = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
        entrada_horario.pack(pady=(0, 10))

        Label(frame_conteudo, text="Nome do Médico:", font=("Segoe UI", 14, "bold"),
              fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
        entrada_medico = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
        entrada_medico.pack(pady=(0, 8))

        Label(frame_conteudo, text="Especialidade:", font=("Segoe UI", 14, "bold"),
              fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
        entrada_especialidade = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
        entrada_especialidade.pack(pady=(0, 10))

        Button(frame_conteudo, text="Salvar Alteração", font=("Segoe UI", 13, "bold"),
               bg="#94c8ce", fg="white", command=salvar_alteracao).pack(pady=10)
    else:
        messagebox.showinfo("Alterar Consulta", "Nenhuma consulta agendada.")

def excluir_consulta():
    """
    Tela para excluir uma consulta pelo ID.
    Busca o índice da consulta na lista e remove se encontrado.
    """
    if Minha_Lista:
        def confirmar_exclusao():
            id_busca = entrada_id.get().strip()
            idx = next((i for i, c in enumerate(Minha_Lista) if c["ID"] == id_busca), None)
            if idx is not None:
                Minha_Lista.pop(idx)
                salvar_dados()
                messagebox.showinfo("Sucesso", "Consulta excluída com sucesso!")
                excluir_consulta()
            else:
                messagebox.showerror("Erro", "ID não encontrado!")

        limpar_frame_conteudo()

        Label(frame_conteudo, text="Excluir Consulta", font=("Segoe UI", 18, "bold"),
              fg="#07254b", bg="white", pady=15, justify="center").pack(anchor="center")
        Label(frame_conteudo, text="ID da Consulta:", font=("Segoe UI", 14, "bold"),
              fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
        entrada_id = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
        entrada_id.pack(pady=(0, 10))

        Button(frame_conteudo, text="Excluir", font=("Segoe UI", 13, "bold"),
               bg="#b71c1c", fg="white", command=confirmar_exclusao).pack(pady=15)
    else:
        messagebox.showinfo("Excluir Consulta", "Nenhuma consulta agendada.")

def consultar_por_id():
    """
    Tela para consultar uma consulta específica pelo ID.
    Mostra os dados da consulta encontrada.
    """
    def desenhar_formulario():
        limpar_frame_conteudo()
        Label(frame_conteudo, text="Consultar por ID", font=("Segoe UI", 18, "bold"),
              fg="#07254b", bg="white", pady=15, justify="center").pack(anchor="center")
        Label(frame_conteudo, text="ID da Consulta:", font=("Segoe UI", 14, "bold"),
              fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
        entrada_id = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
        entrada_id.pack(pady=(0, 10))

        def buscar_consulta():
            id_busca = entrada_id.get().strip()
            consulta = next((c for c in Minha_Lista if c["ID"] == id_busca), None)
            limpar_frame_conteudo()
            if consulta:
                Colunas1 = ["ID", "Paciente", "Data", "Horário", "Médico", "Especialidade"]
                Tabela1 = [[
                    consulta["ID"],
                    consulta["Paciente"],
                    consulta["Data"],
                    consulta["Horário"],
                    consulta["Médico"],
                    consulta["Especialidade"]
                ]]
                relatorio1 = tabulate(Tabela1, headers=Colunas1, tablefmt="double_grid")

                Button(frame_conteudo, text="Atualizar", font=("Segoe UI", 13, "bold"),
                       bg="#94c8ce", fg="white", command=desenhar_formulario).pack(pady=10)
                frame_texto = Frame(frame_conteudo, bg="white")
                frame_texto.pack(expand=True, fill="both")

                scrollbar_y = Scrollbar(frame_texto, orient="vertical")
                scrollbar_y.pack(side="right", fill="y")
                scrollbar_x = Scrollbar(frame_texto, orient="horizontal")
                scrollbar_x.pack(side="bottom", fill="x")

                text_widget = Text(
                    frame_texto,
                    font=("Consolas", 13),
                    wrap="none",
                    yscrollcommand=scrollbar_y.set,
                    xscrollcommand=scrollbar_x.set,
                    bg="white",
                    fg="#1a237e"
                )
                text_widget.pack(expand=True, fill="both")
                text_widget.insert("1.0", relatorio1)
                text_widget.config(state="disabled")

                scrollbar_y.config(command=text_widget.yview)
                scrollbar_x.config(command=text_widget.xview)
            else:
                Label(frame_conteudo, text="Erro, ID não encontrado!", font=("Segoe UI", 14, "bold"),
                      fg="#b71c1c", bg="white", pady=15, justify="center").pack(anchor="center")
                Button(frame_conteudo, text="Atualizar", font=("Segoe UI", 13, "bold"),
                       bg="#94c8ce", fg="white", command=desenhar_formulario).pack(pady=10)

        Button(frame_conteudo, text="Buscar", font=("Segoe UI", 13, "bold"),
               bg="#94c8ce", fg="white", command=buscar_consulta).pack(pady=10)
        Button(frame_conteudo, text="Atualizar", font=("Segoe UI", 13, "bold"),
               bg="#94c8ce", fg="white", command=desenhar_formulario).pack(pady=10)

    desenhar_formulario()

def listar_por_data():
    """
    Tela para listar todas as consultas de uma data específica.
    """
    def desenhar_formulario():
        limpar_frame_conteudo()
        Label(frame_conteudo, text="Listar Consultas por Data", font=("Segoe UI", 18, "bold"),
              fg="#07254b", bg="white", pady=15, justify="center").pack(anchor="center")
        Label(frame_conteudo, text="Data da Consulta (DD/MM/YYYY):", font=("Segoe UI", 14, "bold"),
              fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
        entrada_data = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
        entrada_data.pack(pady=(0, 10))

        def buscar_por_data():
            data = entrada_data.get()
            consultas = [consulta for consulta in Minha_Lista if consulta["Data"] == data]

            limpar_frame_conteudo()

            if consultas:
                colunas1 = ["Paciente", "Data", "Horário", "Médico", "Especialidade"]
                Tabela1 = [[consulta["Paciente"], consulta["Data"], consulta["Horário"], consulta["Médico"], consulta["Especialidade"]]
                           for consulta in consultas]
                relatorio1 = tabulate(Tabela1, headers=colunas1, tablefmt="double_grid")
                Button(frame_conteudo, text="Atualizar", font=("Segoe UI", 13, "bold"),
                       bg="#1976d2", fg="white", command=desenhar_formulario).pack(pady=10)
                frame_texto = Frame(frame_conteudo, bg="white")
                frame_texto.pack(expand=True, fill="both")

                scrollbar_y = Scrollbar(frame_texto, orient="vertical")
                scrollbar_y.pack(side="right", fill="y")
                scrollbar_x = Scrollbar(frame_texto, orient="horizontal")
                scrollbar_x.pack(side="bottom", fill="x")

                text_widget = Text(
                    frame_texto,
                    font=("Consolas", 13),
                    wrap="none",
                    yscrollcommand=scrollbar_y.set,
                    xscrollcommand=scrollbar_x.set,
                    bg="white",
                    fg="#1a237e"
                )
                text_widget.pack(expand=True, fill="both")
                text_widget.insert("1.0", relatorio1)
                text_widget.config(state="disabled")

                scrollbar_y.config(command=text_widget.yview)
                scrollbar_x.config(command=text_widget.xview)

            else:
                messagebox.showinfo("Nenhuma Consulta", "Nenhuma consulta encontrada para essa data.")

            # Validação do formato da data usando a função validar_data_hora
            if not validar_data_hora(data, "00:00"):
                messagebox.showerror("Erro", "Data inválida! Use DD/MM/YYYY para data.")
                return
    
            
        Button(frame_conteudo, text="Buscar", font=("Segoe UI", 13, "bold"),
               bg="#94c8ce", fg="white", command=buscar_por_data).pack(pady=10)
        Button(frame_conteudo, text="Atualizar", font=("Segoe UI", 13, "bold"),
               bg="#94c8ce", fg="white", command=desenhar_formulario).pack(pady=10)

    desenhar_formulario()

def verificar_disponibilidade():
    """
    Tela para verificar se existe consulta marcada para uma data e horário.
    """
    def checar_disponibilidade():
        data = entrada_data.get()
        horario = entrada_horario.get()
        limpar_frame_conteudo()
        if not data or not horario:
            messagebox.showerror("Erro", "Preencha data e horário!")
            return

        # Validação do formato da data e horário usando a função validar_data_hora
        if not validar_data_hora(data, horario):
            messagebox.showerror("Erro", "Data ou horário inválidos! Use DD/MM/YYYY para data e HH:MM para horário.")
            return

        indisponivel = any(
            consulta["Data"] == data and consulta["Horário"] == horario
            for consulta in Minha_Lista
        )

        if indisponivel:
            Label(frame_conteudo, text="Indisponível: Já existe uma consulta marcada.",
                  font=("Segoe UI", 14, "bold"), fg="#b71c1c", bg="white", pady=15, justify="center").pack(anchor="center")
        else:
            Label(frame_conteudo, text="Disponível: Horário livre.",
                  font=("Segoe UI", 14, "bold"), fg="#388e3c", bg="white", pady=15, justify="center").pack(anchor="center")

        Button(frame_conteudo, text="Atualizar", font=("Segoe UI", 13, "bold"),
               bg="#94c8ce", fg="white", command=verificar_disponibilidade).pack(pady=10)

    limpar_frame_conteudo()
    Label(frame_conteudo, text="Verificar Disponibilidade", font=("Segoe UI", 18, "bold"),
          fg="#07254b", bg="white", pady=15, justify="center").pack(anchor="center")
    Label(frame_conteudo, text="Data da Consulta (DD/MM/YYYY):", font=("Segoe UI", 14, "bold"),
          fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
    entrada_data = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
    entrada_data.pack(pady=(0, 10))
    Label(frame_conteudo, text="Horário da Consulta (HH:MM):", font=("Segoe UI", 14, "bold"),
          fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
    entrada_horario = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
    entrada_horario.pack(pady=(0, 10))
    Button(frame_conteudo, text="Buscar", font=("Segoe UI", 13, "bold"),
           bg="#94c8ce", fg="white", command=checar_disponibilidade).pack(pady=15)

def pesquisar_por_nome_ou_especialidade():
    """
    Tela para pesquisar consultas pelo nome do paciente ou especialidade.
    """
    def desenhar_formulario():
        limpar_frame_conteudo()
        Label(frame_conteudo, text="Pesquisar por Nome ou Especialidade", font=("Segoe UI", 18, "bold"),
              fg="#07254b", bg="white", pady=15, justify="center").pack(anchor="center")
        Label(frame_conteudo, text="Nome ou Especialidade:", font=("Segoe UI", 14, "bold"),
              fg="#3B93BC", bg="white", pady=2, justify="center").pack(anchor="center")
        entrada_termo = Entry(frame_conteudo, width=50, font=("Segoe UI", 12))
        entrada_termo.pack(pady=(0, 10))

        def buscar_por_termo():
            termo = entrada_termo.get().lower()
            resultados = [consulta for consulta in Minha_Lista if termo in consulta["Paciente"].lower() or termo in consulta["Especialidade"].lower()]
            limpar_frame_conteudo()
            if resultados:
                colunas1 = ["Paciente", "Data", "Horário", "Médico", "Especialidade"]
                Tabela1 = [[consulta["Paciente"], consulta["Data"], consulta["Horário"], consulta["Médico"], consulta["Especialidade"]]
                           for consulta in resultados]
                relatorio1 = tabulate(Tabela1, headers=colunas1, tablefmt="double_grid")
                Button(frame_conteudo, text="Atualizar", font=("Segoe UI", 13, "bold"),
                       bg="#94c8ce", fg="white", command=desenhar_formulario).pack(pady=10)
                frame_texto = Frame(frame_conteudo, bg="white")
                frame_texto.pack(expand=True, fill="both")

                scrollbar_y = Scrollbar(frame_texto, orient="vertical")
                scrollbar_y.pack(side="right", fill="y")
                scrollbar_x = Scrollbar(frame_texto, orient="horizontal")
                scrollbar_x.pack(side="bottom", fill="x")

                text_widget = Text(
                    frame_texto,
                    font=("Consolas", 13),
                    wrap="none",
                    yscrollcommand=scrollbar_y.set,
                    xscrollcommand=scrollbar_x.set,
                    bg="white",
                    fg="#1a237e"
                )
                text_widget.pack(expand=True, fill="both")
                text_widget.insert("1.0", relatorio1)
                text_widget.config(state="disabled")

                scrollbar_y.config(command=text_widget.yview)
                scrollbar_x.config(command=text_widget.xview)
            else:
                messagebox.showinfo("Nenhuma Consulta", "Não encontrada consulta para o termo informado.")

        Button(frame_conteudo, text="Buscar", font=("Segoe UI", 13, "bold"),
               bg="#94c8ce", fg="white", command=buscar_por_termo).pack(pady=10)
        Button(frame_conteudo, text="Atualizar", font=("Segoe UI", 13, "bold"),
               bg="#94c8ce", fg="white", command=desenhar_formulario).pack(pady=10)

    desenhar_formulario()


def iniciar_interface():
    """
    Função principal que inicializa a interface gráfica (Tkinter).
    Cria os frames, botões do menu e chama carregar_dados().
    """
    global root, frame_conteudo  # root e frame_conteudo são globais para serem acessados em outras funções

    root = Tk()  # Janela principal da aplicação
    root.title("Agendamento")
    root.geometry("1000x700")
    root.configure(bg="lightblue")

    #Obtém a largura e altura da tela do usuário
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    
    largura_janela = root.winfo_screenwidth()
    altura_janela = root.winfo_screenheight()

   # Centraliza a janela na tela
    largura_janela = 1000
    altura_janela = 700
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    # Frame topo (título)
    frame_topo = Frame(root, bg="lightblue", padx=20, pady=20)
    frame_topo.pack(fill="x")

    Label(
        frame_topo,
        text="Agendamento de Consultas Médicas 🩺",
        font=("Garamond", 20, "bold"),
        fg="#07254b",
        bg="lightblue"
    ).pack(pady=10)

    # Frame principal que contém o menu lateral e o conteúdo principal
    frame_principal = Frame(root, bg="#3B93BC")
    frame_principal.pack(fill="both", expand=FALSE)

    # Frame de menu lateral (botões em coluna, lado esquerdo)
    frame_menu = Frame(frame_principal, bg="lightblue")
    frame_menu.pack(side="left", fill="y", padx=5, pady=70)

    # Frame do conteúdo à direita, onde as telas são desenhadas dinamicamente
    # Este frame é global para ser manipulado por outras funções (ex: limpar_frame_conteudo)
    frame_conteudo = Frame(frame_principal, bg="white", padx=10, pady=10)
    frame_conteudo.pack(side="right", fill="both", expand=True, padx=30, pady=30)

    # Botões do menu - lado esquerdo
    Button(frame_menu, text="Relatório Geral", font=("Arial", 12), width=40, bg="white", command=relatorio_geral).pack(pady=10, padx=50)
    Button(frame_menu, text="Agendar Consulta", font=("Arial", 12), width=40, bg="white", command=agendar_consulta).pack(pady=10)
    Button(frame_menu, text="Alterar Consulta", font=("Arial", 12), width=40, bg="white", command=alterar_consulta).pack(pady=10)
    Button(frame_menu, text="Excluir Consulta", font=("Arial", 12), width=40, bg="white", command=excluir_consulta).pack(pady=10)
    Button(frame_menu, text="Consultar Consulta por ID", font=("Arial", 12), width=40, bg="white", command=consultar_por_id).pack(pady=10)
    Button(frame_menu, text="Listar Consultas por Data", font=("Arial", 12), width=40, bg="white", command=listar_por_data).pack(pady=10)
    Button(frame_menu, text="Verificar Disponibilidade", font=("Arial", 12), width=40, bg="white", command=verificar_disponibilidade).pack(pady=10)
    Button(frame_menu, text="Pesquisar por Nome ou Especialidade", font=("Arial", 12), width=40, bg="white", command=pesquisar_por_nome_ou_especialidade).pack(pady=10)
    Button(frame_menu, text="Fim do Programa", font=("Arial", 12), width=40, bg="white", command=root.destroy).pack(pady=10)


    Logo()
    
    carregar_dados()
    root.mainloop()


# Chama a função principal para iniciar o programa
iniciar_interface()