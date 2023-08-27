# ConexaoComSql - Classe Python para Conexão com Banco de Dados SQL Server

A classe `ConexaoComSql` oferece uma maneira simples e eficiente de estabelecer e gerenciar conexões com bancos de dados SQL Server em aplicações Python. Ela abstrai os detalhes de conexão, execução de consultas e chamadas de procedures, tornando a interação com o banco de dados mais conveniente.


## Uso Básico Para Autenticação do Windows

1. Adicione as informações do seu servidor local no arquivo `.env`


```dotenv
# Não é necessário passar nenhum tipo de informação adicional.
SERVIDOR=SEU_SERVIDOR
```
Para realizar a autenticação pelo usuário do Windows, passe o valor `final_ip=None` e `autenticacao_windows=True` para a classe identificar que a autenticação é local.

```python
from conexaoSql import ConexaoComSql

conexao = ConexaoComSql(database='SEU_BANCO', final_ip=None, autenticacao_windows=True)
```

## Autenticação no SQL Server

1. Adicione as informações do seu servidor no arquivo `.env`

**Para a classe identificar o seu servidor, adicione o final do seu ip no final da variável.**

```dotenv
# Neste exemplo estou passando o final 34
SERVIDOR34=192.1.1.34
USUARIO34=SEU_USUARIO
SENHA34=SUA_SENHA
```
Para realizar a autenticação no código, basta você chamar a Classe passando os parametros abaixo:

```python
from conexaoSql import ConexaoComSql

conexao = ConexaoComSql(database='SEU_BANCO', final_ip=34)
```

## Exemplos de uso básico

```python
from conexaoSql import ConexaoComSql
# Para conexão Sql Server
conexao = ConexaoComSql(database='SEU_BANCO', final_ip=34)

# Para Autenticação do Windows
conexao = ConexaoComSql(database='SEU_BANCO', final_ip=None, autenticacao_windows=True)

# Executar uma consulta
consulta = "UPDATE Tabela SET Coluna = Valor WHERE AlgumaCondicao"
conexao.executa_query(consulta)

# Buscar dados
query_busca = "SELECT * FROM Tabela"
dados = conexao.busca_dados(query_busca)
print(dados)


# Parâmetros para a procedure
num1 = 5
num2 = 10
num3 = 15

# Executando a procedure com parametros

conexao.executa_procedure("Nome_da_procedure", num1, num2, num3)

# Executando a procedure

conexao.executa_procedure("Nome_da_procedure")
```

## Benefícios

Ao utilizar a classe `ConexaoComSql` deste repositório, você desfrutará de diversos benefícios ao trabalhar com bancos de dados SQL Server em Python:

- **Simplicidade de Uso:** A classe encapsula a complexidade da configuração e gerenciamento de conexões, permitindo que você se concentre nas consultas e operações de banco de dados.

- **Flexibilidade:** A classe suporta a execução de consultas SQL, busca de dados e execução de stored procedures, abrangendo uma variedade de necessidades de acesso a dados.

- **Segurança:** Através do uso de variáveis de ambiente e do módulo `python-dotenv`, suas informações sensíveis, como senhas, são protegidas e mantidas fora do código-fonte.

- **Gestão de Conexões:** A classe gerencia automaticamente as conexões, garantindo que você possa realizar operações sem se preocupar com a abertura e fechamento manual das conexões.

- **Aprendizado:** Ao explorar e utilizar esta classe, você terá a oportunidade de aprender sobre conexões de banco de dados, uso do PyODBC e boas práticas de segurança no gerenciamento de informações sensíveis.

Não hesite em aproveitar esses benefícios e adaptá-los ao seu contexto específico. Se você tiver ideias adicionais para destacar os pontos positivos do seu repositório, sinta-se à vontade para adicioná-las a esta seção.

## Pré-requisitos

- Python 3.x
- Biblioteca `pyodbc`
- Biblioteca `python-dotenv` para carregar variáveis de ambiente a partir de um arquivo `.env`

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/Fabxzl/conexaoComSql.git
    ```
2. Instale as bibliotecas necessárias:
    ```
    pip install pyodbc python-dotenv
    ```
