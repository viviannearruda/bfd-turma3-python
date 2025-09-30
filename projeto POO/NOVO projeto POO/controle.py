class Departamento:
    def __init__(self, nome, codigo, quantd_funcio=0):
        self.nome = nome
        self.codigo = codigo
        self.quantd_funcio = quantd_funcio

    def atualizar(self, nome=None, quantd_funcio=None):
        if nome:
            self.nome = nome
        if quantd_funcio is not None:
            self.quantd_funcio = quantd_funcio

    def __str__(self):
        return f"Departamento: {self.nome} | Código: {self.codigo} | Funcionários: {self.quantd_funcio}"


class Funcionario:
    def __init__(self, nome, matricula, cargo, salario, data_admissao, departamento):
        self.nome = nome
        self.matricula = matricula
        self.cargo = cargo
        self.salario = salario
        self.data_admissao = data_admissao
        self.departamento = departamento

    def atualizar(self, nome=None, cargo=None, salario=None, data_admissao=None):
        if nome:
            self.nome = nome
        if cargo:
            self.cargo = cargo
        if salario is not None:
            self.salario = salario
        if data_admissao:
            self.data_admissao = data_admissao

    def __str__(self):
        return (f"Funcionário: {self.nome} | Matrícula: {self.matricula}\n"
                f"Cargo: {self.cargo} | Departamento: {self.departamento.nome}\n"
                f"Salário: R${self.salario:.2f} | Admissão: {self.data_admissao}")


class Empresa:
    def __init__(self, nome, cnpj, endereco, telefone):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.telefone = telefone
        self.departamentos = []
        self.funcionarios = []

    # --- CRUD DEPARTAMENTO ---
    def adicionar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def listar_departamentos(self):
        return self.departamentos

    def atualizar_departamento(self, codigo, nome=None, quantd_funcio=None):
        for dep in self.departamentos:
            if dep.codigo == codigo:
                dep.atualizar(nome, quantd_funcio)
                return True
        return False

    def remover_departamento(self, codigo):
        self.departamentos = [d for d in self.departamentos if d.codigo != codigo]

    # --- CRUD FUNCIONÁRIO ---
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        return self.funcionarios

    def atualizar_funcionario(self, matricula, nome=None, cargo=None, salario=None, data_admissao=None):
        for func in self.funcionarios:
            if func.matricula == matricula:
                func.atualizar(nome, cargo, salario, data_admissao)
                return True
        return False

    def remover_funcionario(self, matricula):
        self.funcionarios = [f for f in self.funcionarios if f.matricula != matricula]

    # --- EXIBIR EMPRESA ---
    def __str__(self):
        return (f"Empresa: {self.nome} | CNPJ: {self.cnpj}\n"
                f"Endereço: {self.endereco} | Telefone: {self.telefone}")