import pyodbc
import os
from dotenv import load_dotenv

class ConexaoComSql:
    def __init__(self, database, final_ip=None, autenticacao_windows=False):
        load_dotenv()

        self.autenticacao_windows = autenticacao_windows
        self.servidor = self.get_servidor(final_ip)
        self.usuario = self.get_usuario(final_ip)
        self.senha = self.get_senha(final_ip)

        self.connection_string = self.get_connection_string(database)
        self.conexao = None
        self.cursor = None

    def get_servidor(self, final_ip):
        if not self.autenticacao_windows:
            return os.getenv(f"SERVIDOR{final_ip}")
        return os.getenv("SERVIDOR")

    def get_usuario(self, final_ip):
        if not self.autenticacao_windows:
            return os.getenv(f"USUARIO{final_ip}")
        return ""

    def get_senha(self, final_ip):
        if not self.autenticacao_windows:
            return os.getenv(f"SENHA{final_ip}")
        return ""

    def get_connection_string(self, database):
        if self.autenticacao_windows:
            return f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.servidor};DATABASE={database};Trusted_Connection=yes"
        else:
            return f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.servidor};DATABASE={database};UID={self.usuario};PWD={self.senha}"

    def check_odbc_driver(self):
        try:
            pyodbc.connect(self.connection_string)
        except pyodbc.Error as erro:
            if 'no driver' in str(erro).lower():
                raise RuntimeError("Driver ODBC 17 não encontrado. Instale o driver ODBC 17 para SQL Server.")
            else:
                raise erro

    def get_connection(self):
        self.check_odbc_driver()  # Verifica se o driver ODBC 17 está instalado
        if self.conexao is None or self.conexao.connected == 0:
            self.conexao = pyodbc.connect(self.connection_string)
            self.cursor = self.conexao.cursor()
        return self.conexao, self.cursor

    def executa_query(self, query):
        conexao, cursor = self.get_connection()
        try:
            cursor.execute('SET NOCOUNT ON')
            cursor.execute(query)
            conexao.commit()
        except pyodbc.Error as erro:
            raise RuntimeError("Erro ao executar a query:", str(erro))

    def busca_dados(self, query):
        conexao, cursor = self.get_connection()
        try:
            cursor.execute('SET NOCOUNT ON')
            cursor.execute(query)
            return cursor.fetchall()
        except pyodbc.Error as erro:
            raise RuntimeError("Erro ao buscar dados:", str(erro))
            return []

    def executa_procedure(self, procedure_name, *args):
        conexao, cursor = self.get_connection()
        try:
            if not args:
                consultaCompleta = f"EXEC {procedure_name}"
                cursor.execute(consultaCompleta)
            else:
                parametro_string = ",".join(["?" for _ in args])
                full_query = f"EXEC {procedure_name} {parametro_string}"
                cursor.execute(full_query, args)
            conexao.commit()
        except pyodbc.Error as erro:
            raise RuntimeError("Erro ao executar a procedure:", str(erro))

    def remover_conexao(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conexao is not None:
            self.conexao.close()