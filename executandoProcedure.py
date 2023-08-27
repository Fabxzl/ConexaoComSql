from conexaoSql import ConexaoComSql

# Criar uma instância da classe
conexao = ConexaoComSql(database="SEU_BANCO_DE_DADOS", autenticacao_windows=True)

# Parâmetros para a procedure
num1 = 5
num2 = 10
num3 = 15

# Executando a procedure com parâmetros
try:
    conexao.executa_procedure("nome_da_sua_procedure", num1, num2, num3)
finally:
    # Encerrar a conexão
    conexao.remover_conexao()

# Executando a procedure sem parâmetros
try:
    conexao.executa_procedure("nome_da_sua_procedure")
finally:
    # Encerrar a conexão
    conexao.remover_conexao()

