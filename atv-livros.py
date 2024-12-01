
class Pessoa:
    
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

class Usuario(Pessoa):
    

    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.emprestimos = []

    def _pegar_livro(self, livro):
        if livro.acesso == "Sim":
            if len(self.emprestimos) < 3:
                self.emprestimos.append(livro.titulo)
                print(f"\n{livro.titulo} foi emprestado para {self.nome}")
                livro._acesso_nao()
            else:
                print(f"\nO usuário {self.nome} já tem três livros emprestados")
        else:
            print(f"{livro.titulo} não está disponível para empréstimo")

    def _devolver_livro(self, livro):
        for i in (0,len(self.emprestimos)):
            if self.emprestimos[i] == livro.titulo:
                self.emprestimos.remove(livro.titulo)
                livro._acesso_sim()
                print(f"\n{livro.titulo} foi devolvido")
                break
            else:
                print(f"\n{livro.titulo} não foi emprestado para {self.nome}")
                break

class Administrador(Pessoa):
    

    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.relatorio = []

    def _relatorio(self, item):
        self.relatorio.append(item)

    def _cadastrar_usuario(self, usuario, ida, mt):
        usuario = Usuario(f"{usuario}",f"{ida}",f"{mt}")
        print(f"\nUsuário {usuario.nome} foi cadastrado com sucesso!\n")
        self._relatorio(usuario)
        return usuario

    def _cadastrar_livro(self, livro, au, an, ac):
        livro = Livro(f"{livro}",f"{au}",f"{an}",f"{ac}")
        print(f"{livro.titulo} cadastrado")
        self._relatorio(livro)
        return livro

    def _mostrar_relatorio(self):
        print("\nMostrando Relatório")
        for i in (self.relatorio):
            if i .__class__.__name__ == "Usuario" and len(i.emprestimos) > 0:
                print(f"Usuário: {i.nome}")
                print(f"{i.emprestimos}\n")
            elif i.__class__.__name__ == "Livro" and i.acesso == "Sim":
                print(f"Livro: {i.titulo} está disponível")
        print()

class ItemBiblioteca:
    
    def __init__(self, titulo, autor, ano, acesso):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.acesso = acesso

class Livro(ItemBiblioteca):
    
    def __init__(self, titulo, autor, ano, acesso):
        super().__init__(titulo, autor, ano, acesso)

    def _acesso_nao(self):
        self.acesso = "Não"

    def _acesso_sim(self):
        self.acesso = "Sim"

karol = Administrador("karolayne",20,210)

levi = karol._cadastrar_usuario("Levih",15,601)
ravi = karol._cadastrar_usuario("Ravih",18,601)

novembro = karol._cadastrar_livro("9 de Novembro.","Collen Hoover","2015","Sim")
terminar = karol._cadastrar_livro("Até o verão terminar.","Collen Hoover","2021","Sim")
acaba = karol._cadastrar_livro("É assim que acaba.","Collen Hoover","2016","Sim")
cinderela = karol._cadastrar_livro("Em busca de cinderela/ Em busca da perfeição.","Collen Hoover","2022","Sim")

levi._pegar_livro(novembro)
levi._pegar_livro(terminar)
levi._pegar_livro(acaba)
levi._pegar_livro(cinderela)

levi._devolver_livro(novembro)
levi._devolver_livro(novembro)

karol._mostrar_relatorio()