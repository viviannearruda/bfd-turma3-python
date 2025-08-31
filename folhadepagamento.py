# Sistema de Cadastro de Funcionários com Folha de Pagamento


# Lista para armazenar os funcionários cadastrados
funcionarios = []


# Função para validar campos
# -----------------------------
def validar_campos(campo, tipo="str"):
    """
    Verifica se o campo está preenchido corretamente.
    - Para strings: remove espaços e checa se não está vazio.
    - Para números: converte para float e checa se é maior que 0.
    """
    campo = campo.strip()
    if not campo:
        return None

    if tipo == "float":
        try:
            valor = float(campo)
            if valor <= 0:
                return None
            return valor
        except:
            return None
    return campo

# -----------------------------
# Função para calcular INSS (2025 - alíquotas reais e progressivas)
# -----------------------------
def calcular_inss(salario_bruto):
    if salario_bruto <= 1518.00:
        return salario_bruto * 0.075
    elif salario_bruto <= 2793.88:
        return salario_bruto * 0.09 - 22.77
    elif salario_bruto <= 4190.83:
        return salario_bruto * 0.12 - 106.59
    elif salario_bruto <= 8157.41:
        return salario_bruto * 0.14 - 190.40
    else:
        # aplica o teto máximo
        teto = 8157.41
        return teto * 0.14 - 190.40

# -----------------------------
# Função para calcular IR (Imposto de Renda - 2025)
# -----------------------------
def calcular_ir(salario_bruto):
    if salario_bruto <= 2259.20:
        return 0.0
    elif salario_bruto <= 2826.65:
        return salario_bruto * 0.075 - 169.44
    elif salario_bruto <= 3751.05:
        return salario_bruto * 0.15 - 381.44
    elif salario_bruto <= 4664.68:
        return salario_bruto * 0.225 - 662.77
    else:
        return salario_bruto * 0.275 - 896.00

# -----------------------------
# Função para cadastrar funcionário
# -----------------------------
def cadastrar_funcionario():
    print("Cadastro de Funcionário: ")

    nome_funcionario = validar_campos(input("Digite o nome do funcionário: "), "str")
    if not nome_funcionario:
        print("ERRO: Nome inválido.")
        return

    valor_hora = validar_campos(input("Digite o valor da hora trabalhada: "), "float")
    if not valor_hora:
        print("ERRO: Valor da hora inválido.")
        return

    horas = validar_campos(input("Digite a quantidade de horas trabalhadas no mês: "), "float")
    if not horas:
        print("ERRO: Quantidade de horas inválida.")
        return

    # Cálculos
    salario_bruto = valor_hora * horas
    inss = calcular_inss(salario_bruto)
    ir = calcular_ir(salario_bruto)
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - (inss + ir + sindicato)

    # Armazena no sistema
    funcionario = {
        "nome": nome_funcionario,
        "salario_bruto": salario_bruto,
        "inss": inss,
        "ir": ir,
        "sindicato": sindicato,
        "salario_liquido": salario_liquido
    }
    funcionarios.append(funcionario)

    print(f"Funcionário {nome_funcionario} cadastrado com sucesso!")

# -----------------------------
# Função para listar funcionários
# -----------------------------
def todos_funcionarios():
    print("Lista de Funcionários Cadastrados:")
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    for i, f in enumerate(funcionarios, start=1):
        print(f"""
        {i} - {f['nome']}
        Salário Bruto: R$ {f['salario_bruto']:.2f}
        INSS: R$ {f['inss']:.2f}
        IR: R$ {f['ir']:.2f}
        Sindicato: R$ {f['sindicato']:.2f}
        Salário Líquido: R$ {f['salario_liquido']:.2f}
        """)

# -----------------------------
# Funções de Alterar e Excluir
# -----------------------------
def alterar_funcionario():
    todos_funcionarios()
    if not funcionarios:
        return
    try:
        indice = int(input("Digite o número do funcionário que deseja alterar: ")) - 1
        if indice < 0 or indice >= len(funcionarios):
            print("Funcionário não encontrado.")
            return
        print("Digite os novos dados (ou deixe em branco para não alterar):")
        novo_nome = input("Novo nome: ").strip()
        if novo_nome:
            funcionarios[indice]["nome"] = novo_nome
        print("Funcionário alterado com sucesso!")
    except:
        print("Entrada inválida.")

def excluir_funcionario():
    todos_funcionarios()
    if not funcionarios:
        return
    try:
        indice = int(input("Digite o número do funcionário que deseja excluir: ")) - 1
        if indice < 0 or indice >= len(funcionarios):
            print("Funcionário não encontrado.")
            return
        funcionarios.pop(indice)
        print("Funcionário excluído com sucesso!")
    except:
        print("Entrada inválida.")

# -----------------------------
# Início do Programa
# -----------------------------
while True:
    print("=== MENU PRINCIPAL ===")
    opcao = input("Digite: (1 - Cadastrar, 2 - Alterar, 3 - Excluir, 4 - Listar, 5 - Sair): ")

    if opcao == "1":
        cadastrar_funcionario()
    elif opcao == "2":
        alterar_funcionario()
    elif opcao == "3":
        excluir_funcionario()
    elif opcao == "4":
        todos_funcionarios()
    elif opcao == "5":
        break
    else:
        print("Opção inválida, tente novamente.")

print("Programa finalizado com sucesso!!!")