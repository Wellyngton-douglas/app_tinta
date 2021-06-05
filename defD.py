import math
import time
import os
from banco import *

lista = {}

def menu():    
    os.system('cls' if os.name == 'nt' else 'clear') 
    print('='*29)
    print('| 1-Fazer pedido            |')
    print('| 2-Acompanhar pedido       |')
    print('| 3-Olhar historico do dia  |')    
    print('| 4-Sair                    |')
    print('='*29) 

def calculo(tinta):
    conta = tinta/3.6                        
    suvinil = math.ceil(conta)*89.90
    coral = math.ceil(conta)*104.92
    lukscolor = math.ceil(conta)*75.22
    os.system('cls' if os.name == 'nt' else 'clear') 
    print('=='*53) 
    print('| Preço unitario pela lata de tinta de 3,6 litros: suvinil: 89,90 | coral: 104,92 | lukscolor: 75,22     |')
    print('=='*53) 
    print('| Você vai precisar de:',math.ceil(conta),'latas de tinta                                                                |')
    print('=='*53)  
    print('| Valor total da sua compra: suvinil:',round(suvinil,2),'coral:',round(coral,2),'lukscolor:',round(lukscolor,2),'                            |')
    print('=='*53)    
    time.sleep(1.5)

    return conta, suvinil, coral, lukscolor

def perguna_se_vai_comprar(result):
    conta = result[0]                       
    suvinil = result[1]
    coral = result[2]
    lukscolor = result[3]
    print('| Qual marca você vai querer: 1-suvinil | 2-coral | 3-lukscolor | 4-desistir da compra                   |')
    print('=='*53) 
    pergunta_compra = int(input())    
    if pergunta_compra == 1:   
        os.system('cls' if os.name == 'nt' else 'clear')              
        print('='*35)
        print('|       Forma de pagamento        |')
        print('='*35)
        print('|         (1) A vista - 15%       |')
        print('|         (2) Credito + 15%       |')
        print('='*35)
        print('|AINDA NÃO TRABALHAMOS COM ENTREGA|')
        print('='*35)
        print('| Escolha uma forma de pagamento  |')
        print('='*35)
        forma_pagamento = int(input())
        print('='*35)        
        if forma_pagamento == 1:
            os.system('cls' if os.name == 'nt' else 'clear')  
            calc = suvinil * 0.15
            calc2 = suvinil - calc
            print('='*42)
            print('| Valor da sua conta avista é:', round(calc2,2),'   |')
            print('='*42) 
        else:
            os.system('cls' if os.name == 'nt' else 'clear')  
            calc = suvinil * 0.15
            calc2 = suvinil + calc
            print('='*46)
            print('| Valor da sua conta no credito é:', round(calc2,2),'   |')  
            print('='*46)  
            
        
    elif pergunta_compra == 2: 
        os.system('cls' if os.name == 'nt' else 'clear')        
        print('='*35)
        print('|       Forma de pagamento        |')
        print('='*35)
        print('|         (1) A vista - 15%       |')
        print('|         (2) Credito + 15%       |')
        print('='*35)
        print('|AINDA NÃO TRABALHAMOS COM ENTREGA|')
        print('='*35)
        print('| Escolha uma forma de pagamento  |')
        print('='*35)
        forma_pagamento = int(input())
        print('='*35)        
        if forma_pagamento == 1:
            os.system('cls' if os.name == 'nt' else 'clear') 
            calc = coral * 0.15
            calc2 = coral - calc
            print('='*42)
            print('| Valor da sua conta avista é:', round(calc2,2),'   |')
            print('='*42) 
        else:
            os.system('cls' if os.name == 'nt' else 'clear') 
            calc = coral * 0.15
            calc2 = coral + calc
            print('='*46)
            print('| Valor da sua conta no credito é:', round(calc2,2),'   |')  
            print('='*46)   

        
    elif pergunta_compra == 3:  
        os.system('cls' if os.name == 'nt' else 'clear')       
        print('='*35)
        print('|       Forma de pagamento        |')
        print('='*35)
        print('|         (1) A vista - 15%       |')
        print('|         (2) Credito + 15%       |')
        print('='*35)
        print('|AINDA NÃO TRABALHAMOS COM ENTREGA|')
        print('='*35)
        print('| Escolha uma forma de pagamento  |')
        print('='*35)
        forma_pagamento = int(input())
        print('='*35)        
        if forma_pagamento == 1:
            os.system('cls' if os.name == 'nt' else 'clear') 
            calc = lukscolor * 0.15
            calc2 = lukscolor - calc
            print('='*42)
            print('| Valor da sua conta avista é:', round(calc2,2),'   |')
            print('='*42)
        else:
            os.system('cls' if os.name == 'nt' else 'clear') 
            calc = lukscolor * 0.15
            calc2 = lukscolor + calc
            print('='*46)
            print('| Valor da sua conta no credito é:', round(calc2,2),'   |')  
            print('='*46)   

          
    else:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print('                    ========================================')
        print('                    |Obrigado pela preferência volte sempre|')
        print('                    ========================================')
        time.sleep(2.0) 
        exit()
           
def adicGent(fila,valor):      
    aux = {len (fila): valor}
    fila.update(aux)
    
def movGent(fila):
    time.sleep(2)
    if len(fila) > 0:
        for i in range(len(fila)-1):
            fila[i] = fila[i+1]
        del(fila[len(fila)-1])
    else:
        print('Fila Vazia')                 

def acaoum(empresa_id,comprador_id,empresa,fila):    
    litragem = int(input('| Você sabe a litragem de tinta necessaria 1-Sim | 2-Não | 3-Sair |\n'))
    if litragem == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        tinta = float(input('| Informe a litragem de tinta desejada |\n'))
        result = calculo(tinta)
        compra(empresa_id, comprador_id, result)
        time.sleep(2)
        perguna_se_vai_comprar(result)    
        time.sleep(2)            
        adicGent(fila,empresa)  
        os.system('cls' if os.name == 'nt' else 'clear')      
        print('Você foi adicionado a fila', fila, '\nTempo medio na fila é 5 minutos')
        time.sleep(1.5)
        while len(fila) > 0:
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Representante da empresa', fila[0], 'É a sua vez dirija-se ao local de carga e descarga')
            movGent(fila)

    elif litragem == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        largura: float = float(input('Qual a largura da parede\n'))
        profundidade: float = float(input('Qual o comprimento da parede\n'))
        altura = float(2.9)
        print('A area das paredes é:', cal.calcular_area_parede(largura, profundidade, altura))
        print('A area do teto é:', cal.calcular_area_teto(largura, profundidade))
        print('A litragem de tinta necessaria é de:',
              cal.calcular_cal_litragem(cal.calcular_area_teto(largura, profundidade),
                                        cal.calcular_area_parede(largura, profundidade, altura)))
        tinta = cal.calcular_cal_litragem(cal.calcular_area_teto(largura, profundidade),
                                          cal.calcular_area_parede(largura, profundidade, altura))
        result = calculo(tinta)
        compra(empresa_id, comprador_id, result)
        time.sleep(2)    
        perguna_se_vai_comprar(result)      
        time.sleep(2)              
        adicGent(fila,empresa)  
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Você foi adicionado a fila', fila, '\nTempo medio na fila é 5 minutos')
        time.sleep(1.5)
        while len(fila) > 0:
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Representante da empresa', fila[0], 'É a sua vez dirija-se ao local de carga e descarga')
            movGent(fila)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Obrigado pela preferência volte sempre')
        # voltar para a parte da ação\menu principal

def historico(valor):
    if len(lista) > 0:
        antes = len(lista) - 1
        depois = len(lista) + 1
    else:
        antes = None
        depois = 1

    lista_enca = {'antes': antes, 'informações do comprador': valor, 'depois': depois}

    aux = {len(lista): lista_enca}
    lista.update(aux)
    return lista


