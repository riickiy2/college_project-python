def escolher_veiculo(auto_tipo):
    print("=======Pedagio=======")
    print("-" * 23)
    
    for codigo, (nome, preco) in auto_tipo.items():
        print(f"[{codigo}] - {nome} = R${preco:.2f}")
        
    print("-" * 23)
    
    while True:
        try:
            escolha = int(input("Identifique seu automovel: "))
            if escolha in auto_tipo:     
                return auto_tipo[escolha]
            else:
                print("Escolha uma das opções")
            
        except ValueError:
            print("Digite um número valido.")


def pegar_horario():
    while True:
        try:
            hora = int(input("Horario de passagem: "))
            if 6 <= hora <= 8 or 17 <= hora <= 20:
                return True
            else:
                return False
        
        except ValueError:
                print("\033[31mDigite um número valido.\033[m")
                

def calculo_taxa(nome, preco, tempo):
    if tempo:
        preco_final = preco + (preco * 0.20)     
    else:
        preco_final = preco
        
    return f"Automóvel: \033[32m {nome}\033[m \nValor total: \033[32mR${preco_final} \033[m"

# ==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--   

veiculos = {
    1 : ("Carro de Passeio", 10.00),
    2 : ("Caminhão", 15.00),
    3 : ("Motocicleta", 5.00),
    4 : ("Veiculo oficial", 0),
}


tudo = escolher_veiculo(veiculos)
tempo = pegar_horario()
resultado = calculo_taxa(tudo[0], tudo[1], tempo)
print(resultado)

