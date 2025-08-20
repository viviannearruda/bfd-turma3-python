# Sistema de Recomendação de Consumo de Água Diária (com funções)

def nomear_pessoa():
    nome = input("Digite seu nome: ")
    return nome

def numero_whatsapp():
    whatsapp = input("Digite seu número do WhatsApp: ")
    return whatsapp

def peso_pessoa():
    peso = float(input("Digite seu peso em kg: "))
    return peso

def altura_pessoa():
    altura = float(input("Digite sua altura em metros: "))
    return altura

# constante
MEDIDA_CALCULA_CONSUMO_AGUA = 35  # ml por kg

def consumo_agua(peso):
    agua = (peso * MEDIDA_CALCULA_CONSUMO_AGUA) / 1000  # litros
    return agua

def calcula_imc(peso, altura):
    return peso / (altura ** 2)


# -------- Programa principal --------
nome = nomear_pessoa()
whatsapp = numero_whatsapp()
peso = peso_pessoa()
altura = altura_pessoa()

agua_diaria = consumo_agua(peso)
imc = calcula_imc(peso, altura)

print("\n--- Resultados ---")
print(f"Nome: {nome}")
print(f"WhatsApp: {whatsapp}")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {imc:.2f}")
print(f"Quantidade de água recomendada por dia: {agua_diaria:.2f} litros")