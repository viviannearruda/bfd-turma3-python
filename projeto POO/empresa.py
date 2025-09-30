class Empresa:
    def __init__(self, nome: str, cnpj: str, endereco: str, telefone: str):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.telefone = telefone
        self.departamentos = []
        self.funcionarios = []

    def __str__(self) -> str:
        return (f"Empresa: {self.nome}\n"
                f"CNPJ: {self.cnpj}\n"
                f"Endereço: {self.endereco}\n"
                f"Telefone: {self.telefone}")

    def adicionar_departamento(self, departamento) -> None:
        """Mantém a associação de departamentos à empresa."""
        self.departamentos.append(departamento)

    def adicionar_funcionario(self, funcionario) -> None:
        """Mantém a associação de funcionários à empresa."""
        self.funcionarios.append(funcionario)
