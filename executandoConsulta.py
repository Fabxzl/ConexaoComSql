from conexaoSql import ConexaoComSql

# Criar uma instância da classe
conexao = ConexaoComSql(database="SEU_BANCO_DE_DADOS", autenticacao_windows=True)
try:
    # Buscar dados
    query_busca = "SELECT * FROM Tabela"
    dados = conexao.busca_dados(query_busca)
    print(dados)
finally:
    # Encerrar a conexão
    conexao.remover_conexao()

