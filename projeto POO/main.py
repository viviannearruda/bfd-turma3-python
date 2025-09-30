from empresa import Empresa
from departamento import Departamento
from funcionario import Funcionario


def menu_principal():
    print("\n=== Sistema de Gestão ===")
    print("1. Empresa")
    print("2. Departamentos")
    print("3. Funcionários")
    print("0. Sair")
    return input("Escolha uma opção: ")


def submenu_empresa(empresa):
    while True:
        print("\n--- Menu Empresa ---")
        print("1. Exibir dados da Empresa")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Dados da Empresa ---")
            print(empresa)
        elif opcao == "0":
            break
        else:
            print("⚠ Opção inválida!")


def submenu_departamentos(empresa):
    while True:
        print("\n--- Menu Departamentos ---")
        print("1. Cadastrar Departamento")
        print("2. Listar Departamentos")
        print("3. Atualizar Departamento")
        print("4. Remover Departamento")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Cadastrar Departamento ---")
            nome = input("Nome: ")
            codigo = input("Código: ")
            quantd = int(input("Quantidade de funcionários: "))
            dep = Departamento(nome, codigo, quantd)
            empresa.adicionar_departamento(dep)
            print("✅ Departamento cadastrado com sucesso!")

        elif opcao == "2":
            print("\n--- Lista de Departamentos ---")
            if not empresa.departamentos:
                print("Nenhum departamento cadastrado.")
            for dep in empresa.departamentos:
                print(dep)
                print()

        elif opcao == "3":
            print("\n--- Atualizar Departamento ---")
            codigo = input("Informe o código do departamento: ")
            for dep in empresa.departamentos:
                if dep.codigo == codigo:
                    dep.nome = input("Novo nome: ")
                    dep.quantd_funcio = int(input("Nova quantidade de funcionários: "))
                    print("✅ Departamento atualizado!")
                    break
            else:
                print("⚠ Departamento não encontrado.")

        elif opcao == "4":
            print("\n--- Remover Departamento ---")
            codigo = input("Informe o código do departamento: ")
            empresa.departamentos = [d for d in empresa.departamentos if d.codigo != codigo]
            print("✅ Departamento removido (se existia).")

        elif opcao == "0":
            break
        else:
            print("⚠ Opção inválida!")


def submenu_funcionarios(empresa):
    while True:
        print("\n--- Menu Funcionários ---")
        print("1. Cadastrar Funcionário")
        print("2. Listar Funcionários")
        print("3. Atualizar Funcionário")
        print("4. Remover Funcionário")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Cadastrar Funcionário ---")
            nome = input("Nome: ")
            matricula = input("Matrícula: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            data_admissao = input("Data de admissão: ")

            if not empresa.departamentos:
                print("⚠ Nenhum departamento cadastrado! Cadastre um primeiro.")
                continue

            print("\nDepartamentos disponíveis:")
            for dep in empresa.departamentos:
                print(f"{dep.codigo} - {dep.nome}")

            codigo_dep = input("Escolha o código do departamento: ")
            dep_escolhido = next((d for d in empresa.departamentos if d.codigo == codigo_dep), None)

            if dep_escolhido:
                func = Funcionario(nome, matricula, cargo, salario, data_admissao, dep_escolhido)
                empresa.adicionar_funcionario(func)
                print("✅ Funcionário cadastrado com sucesso!")
            else:
                print("⚠ Departamento não encontrado.")

        elif opcao == "2":
            print("\n--- Lista de Funcionários ---")
            if not empresa.funcionarios:
                print("Nenhum funcionário cadastrado.")
            for func in empresa.funcionarios:
                print(func)
                print()

        elif opcao == "3":
            print("\n--- Atualizar Funcionário ---")
            matricula = input("Informe a matrícula do funcionário: ")
            for func in empresa.funcionarios:
                if func.matricula == matricula:
                    func.nome = input("Novo nome: ")
                    func.cargo = input("Novo cargo: ")
                    func.salario = float(input("Novo salário: "))
                    func.data_admissao = input("Nova data de admissão: ")
                    print("✅ Funcionário atualizado!")
                    break
            else:
                print("⚠ Funcionário não encontrado.")

        elif opcao == "4":
            print("\n--- Remover Funcionário ---")
            matricula = input("Informe a matrícula do funcionário: ")
            empresa.funcionarios = [f for f in empresa.funcionarios if f.matricula != matricula]
            print("✅ Funcionário removido (se existia).")

        elif opcao == "0":
            break
        else:
            print("⚠ Opção inválida!")


def main():
    # Empresa fixa, apenas exibição
    empresa = Empresa(
        nome="Tech Solutions",
        cnpj="01.100.100/0001/10",
        endereco="Rua da Paz, 123, Centro - Recife/PE",
        telefone="(81) 9988-7766"
    )

    while True:
        opcao = menu_principal()

        if opcao == "1":
            submenu_empresa(empresa)
        elif opcao == "2":
            submenu_departamentos(empresa)
        elif opcao == "3":
            submenu_funcionarios(empresa)
        elif opcao == "0":
            print("Saindo do sistema... 👋")
            break
        else:
            print("⚠ Opção inválida!")


if __name__ == "__main__":
    main()
