import postgresql

host = 'localhost'
user = 'postgres'
database = 'postgres'
password = 'postgres'

def cadastrar_comprador(nome):    
    cpf = str(input('| Informe o CPF                          |\n'))
    conexao = postgresql.open(host = host, user =  user, database=  database, password =  password)
    sql = f"INSERT INTO comprador (nome, cpf) VALUES ('{nome}', '{cpf}')"
    usuario = conexao.execute(sql)

    conexao.close()

def pesquisar_comprador_cadastrado(nome):
    query = f"SELECT * FROM comprador WHERE nome = '{nome}'"
    conexao = postgresql.open(host = host, user =  user, database=  database, password =  password)
    usuario = conexao.prepare(query)
    return usuario

def pesquisar_nome_empresa(empresa):
    query = f"SELECT * FROM empresa WHERE nome = '{empresa}'"
    conexao = postgresql.open(host = host, user =  user, database=  database, password =  password)
    usuario = conexao.prepare(query)
    return usuario

def pesquisar_nome_responsavel(nome_resp):
    query = f"SELECT * FROM comprador WHERE nome = '{nome_resp}'"
    conexao = postgresql.open(host = host, user =  user, database=  database, password =  password)
    usuario = conexao.prepare(query)
    return usuario

def cadastrar_empresa(newempresa):    
    cnpj = str(input('| Informe o CNPJ                         |\n'))
    nomefantasia = str(input('| Informe o nome fantasia da sua empresa |\n'))

    conexao = postgresql.open(host = host, user =  user, database=  database, password =  password)
    usuarios = conexao.execute(f"INSERT INTO empresa (nome, nome_fantasia, cnpj) VALUES ('{newempresa}','{nomefantasia}','{cnpj}')")
    
    
    conexao.close()

def pesquisar_empresa_cadastrada(newempresa):    
    query = f"SELECT * FROM empresa WHERE nome = '{newempresa}'"
    conexao = postgresql.open(host = host, user =  user, database=  database, password =  password)
    usuario = conexao.prepare(query)
    return usuario

def compra(empresa_id,comprador_id,result):
    conta = result[0]
    conexao = postgresql.open(host = host, user =  user, database=  database, password =  password)
    usuarios = conexao.execute(f"INSERT INTO compra (empresa_id, comprador_id, quantidade) VALUES ({empresa_id},{comprador_id},{conta})")

    conexao.close()

def pesquisar_historico():
    query = f"SELECT * FROM compra"
    conexao = postgresql.open(host=host, user=user, database=database, password=password)
    usuario = conexao.prepare(query)
    return usuario

