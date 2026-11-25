class Pessoa:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf

    def andar(self):
        print(f" {self.nome} começou a andar agora")

    def aniversario(self,nascimento):
        self.nascimento = nascimento
        print(f" O aniversário de {self.nome} é hoje pois nasceu no dia {self.nascimento} ")

    def apresentar(self):
        print(F"Olá sou o(a) {self.nome}")

p1 = Pessoa("Pedro", 9999999999)
p2 = Pessoa("Guilherme", 0000000000)
d1 = input("Digite o nome da pessoa: ")
d2 = int(input("Digite o CPF da pessoa: ")) 

p1.apresentar()
p1.andar()
p2.aniversario("25/11/2000")
print("-"*70)
p3 = Pessoa(d1,d2)
p3.apresentar()