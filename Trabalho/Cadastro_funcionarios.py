import Cadastro_dinossauros
class Funcionarios():
    def __init__(self,nome,ID,idade,tempo_servico,funcao,partes_perdidas,senha):
        self._nome = nome
        self._ID = ID
        self._senha = senha
        self._idade = idade
        self._tempo_servico = tempo_servico
        self._funcao = funcao
        self._partes_perdidas = partes_perdidas

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome_novo):
        self._nome = nome_novo
    
    @property
    def ID(self):
        return self._ID
    
    @ID.setter
    def ID(self, novo_ID):
        self._ID = novo_ID

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self,nova_senha):
        self._senha = nova_senha

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):  
        if nova_idade < 0:
            print("Idade não pode ser negativa.")   
        else:
            self._idade = nova_idade

    @property
    def tempo_servico(self):
        return self._tempo_servico
    
    @tempo_servico.setter
    def tempo_servico(self, tempo_servico_atual):
        if tempo_servico_atual < 0:
            print('O tempo de serviço não pode ser negativo')
        if tempo_servico_atual == 0:
            print('Novo funcionário')
            self._tempo_servico = tempo_servico_atual
        else:
            print('Tempo de serviço atualizado')
            self._tempo_servico = tempo_servico_atual
    @property
    def funcao(self):
        return self._funcao
    
    @funcao.setter
    def funcao(self,nova_funcao):
        self._funcao = nova_funcao

    @property
    def partes_perdidas(self):
        return self._partes_perdidas
    
    @partes_perdidas.setter
    def partes_perdidas(self,novas_partes_perdidas):
        self._partes_perdidas = novas_partes_perdidas

    def exibir_dados(self):
        print("====== LISTA DE FUNCIONÁRIOS CADASTRADOS ======")
        print(f'Nome: {self._nome}')
        print(f'ID: {self._ID}')
        print(f'Idade: {self._idade}')
        print(f'Tempo de serviço: {self._tempo_servico}')
        print(f'Função: {self._funcao}')
        print(f'Partes perdidas: {self._partes_perdidas}')

    def get_dados_formatados(self):
        return (
            "\n" + "="*40 +
        f"\n FUNCIONÁRIO: {self._nome} (ID: {self._ID})" +
        "\n" + "="*40 +
        f"\n Idade:             {self._idade} anos" +
        f"\n Tempo de serviço:  {self._tempo_servico} meses" +
        f"\n Função:            {self._funcao}" +
        f"\n Partes perdidas:  {self._partes_perdidas if self._partes_perdidas else 'Nenhuma'}" +
        "\n" + "="*40
        )

    def get_dados(self):
        return {
            "Nome": self._nome,
            "ID": self._ID,
            "Idade": f"{self._idade} anos",
            "Tempo de serviço": f"{self._tempo_servico} meses",
            "Função": self._funcao,
            "Partes perdidas": self._partes_perdidas if self._partes_perdidas else "Nenhuma"
        }
funcionarios = []

def cadastrar_funcionario():
    print("\n--- Cadastro de Funcionário ---")
    nome = input("Nome: ")
    ID = input("ID: ")
    idade = int(input("Idade: "))
    tempo_servico = int(input("Tempo de serviço (em meses): "))
    funcao = input("Função: ")
    partes_perdidas = input("Partes perdidas no trabalho (ou deixe vazio): ")
    senha = input("Crie uma senha para esse funcionário: ")

    f = Funcionarios(nome, ID, idade, tempo_servico, funcao, partes_perdidas, senha)
    funcionarios.append(f)
    print(f"\nFuncionário {nome} cadastrado com sucesso!")

def Menu_funcionario():
    while True:
        print('\n=== Menu de Funcionário===')
        print('1 - Cadastrar Dinossauro')
        print('2 - Consultar Dinossauro')
        print('3 - sair')
        opcao = input('Escolha uma opção: ')

        if opcao == "1":
            Cadastro_dinossauros.cadastro_dinossauro()

        elif opcao == "2":
            id_busca = int(input("\nDigite o ID do dinossauro que deseja consultar: "))
            encontrado = False
            for d in Cadastro_dinossauros.dinossauro:
                if d.ID == id_busca:
                    print("\nDinossauro encontrado:")
                    d.exibir_dados()
                    encontrado = True
                    break

            if not encontrado:
                print("\nNenhum dinossauro encontrado com esse ID.")
        elif opcao == "3":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def login():
    print("\n==== Login ====")
    IDL = input("Digite o ID: ")
    senhaL = input("Digite a senha: ")

    for f in funcionarios:
        if f.ID == IDL and f.senha == senhaL:
            print(f"\nLogin bem-sucedido! Bem-vindo, {f.nome}.")
            Menu_funcionario()
            return

    print("\nID ou senha incorretos.")

while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Cadastrar funcionário")
    print("2 - Fazer login")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_funcionario()
    elif opcao == "2":
        login()
    elif opcao == "3":
        print("Encerrando o sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")