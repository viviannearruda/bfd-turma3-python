class Departamento:
    
    def __init__(self, nome: str, codigo: str, quantidade_funcionarios: int = 0):
        self.nome = nome
        self.codigo = codigo
        self.quantidade_funcionarios = quantidade_funcionarios
        self.funcionarios = []  # Associação com funcionários

    def __str__(self) -> str:
        return (f"Departamento: {self.nome}\n"
                f"Código: {self.codigo} | "
                f"Quantidade de Funcionários: {self.quantidade_funcionarios}")

    def adicionar_funcionario(self, funcionario) -> None:
        """Adiciona funcionário ao departamento (não é CRUD, apenas mantém consistência)."""
        self.funcionarios.append(funcionario)
        self.quantidade_funcionarios = len(self.funcionarios)

    def remover_funcionario(self, funcionario) -> None:
        """Remove funcionário do departamento (não é CRUD, apenas mantém consistência)."""
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)
            self.quantidade_funcionarios = len(self.funcionarios)
