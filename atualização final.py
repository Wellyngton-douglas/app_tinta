import math
import time
import os
from classC import Calculadora
from defD import *
from banco import *
cal = Calculadora
acao = 0
i = 0
cont = 0
fila = {}
tent = 2
falha = 0
while acao < 3:
    try:        
        os.system('cls' if os.name == 'nt' else 'clear') 
        print('='*54)
        print('|                  AVISO IMPORTANTE                  |')
        print('| Utilize apenas numeros para navegar entre os menus |')
        print('='*54)
        time.sleep(5)

        os.system('cls' if os.name == 'nt' else 'clear')
        empresa = str(input('| Informe o nome da sua empresa |\n'))
        pesquisa = pesquisar_nome_empresa(empresa)        
        if len(pesquisa()) == 0:  # variavel onde vai ver se a empresa esta cadastrada no banco de dados
            os.system('cls' if os.name == 'nt' else 'clear')
            print('| ATENÇÃO NÃO UTILIZE CARACTERES         |\n| ESPECIAIS EX:@,#,!,$                   |')
            newempresa = str(input('| Sua empresa não esta cadastrada        |\n| Informe o nome da sua empresa          |\n'))
            cadastrar_empresa(newempresa) 
            pesquisar_empresa_cadastrada(newempresa) 
            pesquisa2 = pesquisar_empresa_cadastrada(newempresa) 
            empresa_id = (pesquisa2()[0][0])                 
        else:
            empresa_id = (pesquisa()[0][0])            

        os.system('cls' if os.name == 'nt' else 'clear')
        nome_resp = str(input('| Informe o nome do responsavel |\n'))
        pesquisa_resp = pesquisar_nome_responsavel(nome_resp)   
        if len(pesquisa_resp()) == 0:  # variavel onde vai ver se o responsavel esta cadastrada no banco de dados
            os.system('cls' if os.name == 'nt' else 'clear')
            print('| ATENÇÃO NÃO UTILIZE CARACTERES         |\n| ESPECIAIS EX:@,#,!,$                   |')
            nome = str(input('| O responsavel não esta cadastrado      |\n| Informe seu nome                       |\n'))
            cadastrar_comprador(nome)  
            pesquisar_comprador_cadastrado(nome)
            pesquisa3 = pesquisar_comprador_cadastrado(nome) 
            comprador_id = (pesquisa3()[0][0])      
        else:
            comprador_id = (pesquisa_resp()[0][0])

        menu()
        acao = int(input())        
        if acao == 1:
            os.system('cls' if os.name == 'nt' else 'clear') 
            acaoum(empresa_id,comprador_id,empresa,fila)
        elif acao == 2:
            os.system('cls' if os.name == 'nt' else 'clear') 
            print('='*36)
            print('| Você ainda não fez um pedido     |')
            print('|',len(fila), 'Empresas na fila               |' if len(fila) > 0 else 'A fila está vazia              |')
            print('| Tempo medio na fila é: 5 minutos |\n| Fazer um pedido 1-Sim | 2-Não    |')
            print('='*36)
            acao = int(input())            
            if acao == 1:                
                os.system('cls' if os.name == 'nt' else 'clear') 
                acaoum(empresa_id,comprador_id,empresa,fila)
            else:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print('Obrigado pela preferência volte sempre')
        elif acao == 3:
            while falha < tent:
                os.system('cls' if os.name == 'nt' else 'clear') 
                usuario = str(input('| Informe o nome de usuario |\n'))
                senha = int(input('| Informe sua senha         |\n'))            
                if usuario == 'usuario' and senha == 1234: 
                    os.system('cls' if os.name == 'nt' else 'clear')                                           
                    valor = pesquisar_historico()
                    for i in range  (len(valor())) :
                        historico(valor()[i])
                    for i in range (len(lista)) :
                        print(cont,lista[i])
                        cont += 1
                    time.sleep(5)
                elif usuario != 'usuario' or senha != 1234: 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('='*35 if falha < 1 else '='*39)
                    print('| Usuario ou senha incorreto      |\n| Resta apenas mais uma tentativa |'if falha < 1 else '| Usuario ou senha incorreto          |')
                    print('='*35 if falha < 1 else '='*39)
                    falha +=1  
                    time.sleep(3) 
            else:               
                print('| Você atingiu o limite de tentativas |')
                print('| Seu login foi bloqueado             |')  
                print('='*39)
                time.sleep(3)
        else:
            os.system('cls' if os.name == 'nt' else 'clear') 
            print('Obrigado pela preferência volte sempre')
            exit()

    except (ValueError, TypeError):
        print('Tivemos um problema com o tipo de dado informado')