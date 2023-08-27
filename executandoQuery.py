from conexaoSql import ConexaoComSql

# Criar uma instância da classe
conexao = ConexaoComSql(database="SEU_BANCO_DE_DADOS", autenticacao_windows=True)

try:
    # Executar uma consulta
    consulta = "UPDATE Tabela SET Coluna = Valor WHERE AlgumaCondicao"
    conexao.executa_query(consulta)
finally:
    # Encerrar a conexão
    conexao.remover_conexao()