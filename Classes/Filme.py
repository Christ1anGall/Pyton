class Filme:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao
        self.numero_de_exibicoes = 0

    def __str__(self):
        return f"<Filme: {self.titulo}>"
    
    def __len__(self):
        return self.duracao
    
    def __call__(self):
        self.numero_de_exibicoes += 1
        return self.numero_de_exibicoes

john_wick = Filme('John Wick', 113)

# 2
print(john_wick)

# 3
print(len(john_wick))

# 4
print(john_wick.numero_de_exibicoes)

# 5
print(vars(john_wick))

# 6
john_wick()
print(john_wick.numero_de_exibicoes)

# 7
print(vars(john_wick))