class Funcionario:
    def __init__(self, nome: str, matricula: str, cargo: str, salario: float, data_admissao: str, departamento):
        self.nome = nome
        self.matricula = matricula
        self.cargo = cargo
        self.salario = salario
        self.data_admissao = data_admissao
        self.departamento = departamento  # Associação com Departamento

    def __str__(self) -> str:
        return (f"Funcionário: {self.nome} | Matrícula: {self.matricula}\n"
                f"Cargo: {self.cargo} | Departamento: {self.departamento.nome}\n"
                f"Salário: R${self.salario:.2f} | "
                f"Data de admissão: {self.data_admissao}")

    def obter_salario_anual(self) -> float:
        """Exemplo de método útil para a classe, sem ser CRUD."""
        return self.salario * 12
