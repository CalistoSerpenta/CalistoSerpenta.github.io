class Dinossauros():
    def __init__(self,nome,ID,especie,tamanho,alimentacao,idade,nivel_perigo):
        self._nome = nome
        self._ID = ID
        self._especie = especie
        self._tamanho = tamanho
        self._alimentacao = alimentacao
        self._idade = idade
        self._nivel_perigo = nivel_perigo

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,novo_nome):
        self._nome = novo_nome

    @property
    def ID(self):
        return self._ID   

    @ID.setter
    def ID(self,novo_ID):
        self._ID = novo_ID

    @property
    def especie(self):
        return self._especie
    
    @especie.setter
    def especie(self,nova_especie):
        self._especie = nova_especie
    
    @property
    def tamanho(self):
        return self._tamanho
    
    @tamanho.setter
    def tamanho(self,novo_tamanho):
        if novo_tamanho < 0:
            print('O tamanho não pode ser negativo')
        else:
            self._tamanho = novo_tamanho

    @property
    def alimentacao(self):
        return self._alimentacao
    
    @alimentacao.setter
    def alimentacao(self,nova_alimentacao):
        self._alimentacao = nova_alimentacao
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self,nova_idade):
        if nova_idade < 0:
            print('A idade não pode ser negativa')
        else:
            self._idade = nova_idade
    
    @property
    def nivel_perigo(self):
        return self._nivel_perigo
    
    @nivel_perigo.setter
    def nivel_perigo(self,novo_nivel_perigo):
        if novo_nivel_perigo < 0:
            print('O nível de perigo não pode ser negativo')
        else:
            self._nivel_perigo = novo_nivel_perigo

    def exibir_dados(self):
        print("Exibindo dados do dinossauro:")
        print(f'Nome: {self._nome}')
        print(f'ID: {self._ID}')
        print(f'Espécie: {self._especie}')
        print(f'Idade: {self._idade}')
        print(f'Tamanho: {self._tamanho} CM')
        print(f'Tipo de alimentação: {self._alimentacao}')
        print(f'Nível de perigo: {self._nivel_perigo}')

dinossauros = []

def cadastro_dinossauro():
        nome = input('Insira o nome do Dinossauro: ')
        ID = int(input('Insira o ID do animal: '))
        especie = input('Insira a espécie dele: ')
        idade = int(input('Insira a idade: '))
        tamanho = float(input('Insira o tamanho em centímetros: '))
        alimentacao = input('Insira o tipo de alimentação: ')
        nivel_perigo = int(input('Insira o nível de perigo na escala de 0 a 10: '))

        dinossauro = Dinossauros(nome,ID,especie,tamanho,alimentacao,idade,nivel_perigo)
        dinossauros.append(dinossauro)


if __name__ == "__main__":
    qtd = int(input('Digite quantos dinossauros deseja cadastrar: '))

    for i in range(qtd):
        print(f"\n--- Cadastro do dinossauro {i+1} ---")
        cadastro_dinossauro()