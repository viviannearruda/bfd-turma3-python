from controle import Empresa, Departamento, Funcionario

def main():
    empresa = Empresa("Tech Solutions", "01.100.100/0001/10",
                      "Rua da Paz, 123 - Recife", "(81) 9988-7766")

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Empresa")
        print("2. Departamentos")
        print("3. Funcionários")
        print("0. Sair")
        opcao = input("Escolha: ")

        # Empresa
        if opcao == "1":
            print("\n--- Dados da Empresa ---")
            print(empresa)

        # Departamentos
        elif opcao == "2":
            print("\n--- Menu Departamentos ---")
            print("1. Cadastrar")
            print("2. Listar")
            print("3. Atualizar")
            print("4. Remover")
            sub = input("Escolha: ")

            if sub == "1":
                nome = input("Nome: ")
                codigo = input("Código: ")
                qnt = int(input("Qtd. Funcionários: "))
                empresa.adicionar_departamento(Departamento(nome, codigo, qnt))
                print("Departamento adicionado!")
            elif sub == "2":
                for dep in empresa.listar_departamentos():
                    print(dep)
            elif sub == "3":
                codigo = input("Código do depto: ")
                nome = input("Novo nome: ")
                qnt = int(input("Nova qtd.: "))
                if empresa.atualizar_departamento(codigo, nome, qnt):
                    print("Atualizado!")
                else:
                    print("Não encontrado.")
            elif sub == "4":
                codigo = input("Código do depto: ")
                empresa.remover_departamento(codigo)
                print("Removido!")

        # Funcionários
        elif opcao == "3":
            print("\n--- Menu Funcionários ---")
            print("1. Cadastrar")
            print("2. Listar")
            print("3. Atualizar")
            print("4. Remover")
            sub = input("Escolha: ")

            if sub == "1":
                nome = input("Nome: ")
                matricula = input("Matrícula: ")
                cargo = input("Cargo: ")
                salario = float(input("Salário: "))
                data = input("Admissão: ")

                if not empresa.departamentos:
                    print("Cadastre um departamento antes.")
                    continue

                print("\nDepartamentos disponíveis:")
                for dep in empresa.departamentos:
                    print(f"{dep.codigo} - {dep.nome}")

                codigo_dep = input("Código do depto: ")
                dep = next((d for d in empresa.departamentos if d.codigo == codigo_dep), None)

                if dep:
                    empresa.adicionar_funcionario(Funcionario(nome, matricula, cargo, salario, data, dep))
                    print("Funcionário cadastrado!")
                else:
                    print("Depto não encontrado.")

            elif sub == "2":
                for func in empresa.listar_funcionarios():
                    print(func)
                    print()

            elif sub == "3":
                mat = input("Matrícula: ")
                nome = input("Novo nome: ")
                cargo = input("Novo cargo: ")
                salario = float(input("Novo salário: "))
                data = input("Nova admissão: ")
                if empresa.atualizar_funcionario(mat, nome, cargo, salario, data):
                    print("Atualizado!")
                else:
                    print("Funcionário não encontrado.")

            elif sub == "4":
                mat = input("Matrícula: ")
                empresa.remover_funcionario(mat)
                print("Funcionário removido!")

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()