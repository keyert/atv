##############
# Atividade Newton
##############

#Valores e produto

produto=['salgado','refri','suco','sorvete','cafe','capp','bolo','dad']
preco=[4.00,4.50,5.00,6.00,4.00,6.00,4.50,0.50]

#exercicio um
def cardapio():
    print ("1- SALGADO")
    print ("2-refri")
    print ("3-suco")
    print ("4-sorv")
    print ("5-caf")
    print ("6-capp ")
    print ("7-bolo")
    print ("8-dadinho")
    
    card = int(input("Digite o numero do produto"))
    #booleano 
    if card == 1:
        print ('4.00')
    if card == 2:
        print ('4.50')
    if card == 3:
        print ('5.00')
    if card == 4:
        print ('6.00')
    if card == 5:
        print ('4.00')
    if card == 6:
        print ('6.00')
    if card == 7:
        print ('4.50')
    if card == 8:
        print ('4.50')


#exercicio dois
def cantina():
    gente=[] #lista vazia
    comando=[] #lista vazia
    for i in range(7): 
        nome = str(input("seu nome? "))
        pedido = str(input(" o que voce quer{}? ".format(nome)))
        gente.append(nome)
        comando.append(pedido)
        print (nome, pedido)
    return nome, pedido

def soma(preco):
    gente=[]
    comando=[] 
    for i in range(7): 
        nome = str(input("seu nome? "))
        pedido = str(input(" o que voce quer{}? ".format(nome)))
        gente.append(nome)
        comando.append(pedido)
        print (nome, pedido)
        soma = preco+comando
        
    return nome, pedido, soma(preco)




cardapio()  
cantina()
soma()


