from tkinter import *
import mysql.connector
from mysql.connector import Error

# Estabelece conexão com o banco de dados
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345678',
            database="senha"
        )
        if connection.is_connected():
            print("Conexão com o banco de dados MySQL estabelecida com sucesso")
        return connection
    except Error as e:
        print(f"Erro ao conectar com o banco de dados MySQL: {e}")
        return None

# ---------- GERADOR DE SENHA ---------- #
# (Adicione sua lógica de gerador de senha aqui)

# ------------ SALVAR SENHA ----------- #
def salvar():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO tabela_senhas (site, user, senha) VALUES (%s, %s, %s)", (website, email, password))
            connection.commit()
            cursor.close()
            connection.close()
            print("Dados inseridos com sucesso no banco de dados MySQL")
        else:
            print("Falha ao inserir dados no banco de dados MySQL")
    except Error as e:
        print(f"Erro ao inserir dados no banco de dados MySQL: {e}")

    # Limpa os campos de entrada
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------- INTERFACE GRÁFICA ---------------- #
window = Tk()
window.title("Gerenciador de Senhas")
window.config(padx=50, pady=50)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Senha")
password_label.grid(row=3, column=0)

# Campos de entrada
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Botões
generate_password_button = Button(text="Gerar Senha")
generate_password_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Adicionar", width=36, command=salvar)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

# ---------------- SQL ---------------- #

# Lógica de conexão e criação da tabela
def create_table():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS tabela_senhas (site VARCHAR(255), user VARCHAR(255), senha VARCHAR(20))"
        )
        cursor.close()
        connection.close()

# Cria a tabela quando o script é executado
create_table()