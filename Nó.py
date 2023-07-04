class No:
    def __init__(self, nome, distancia_objetivo):
        self.adjacentes = []
        self.nome = nome
        self.distancia_objetivo = distancia_objetivo
        self.visitado = False
    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.No.nome, i.custo)

class Adjacente:
    def __init__(self, No,custo):
        self.custo = custo
        self.No = No

        self.distancia_aestrela = No.distancia_objetivo + self.custo
'''
class Arvore:
    arad = No('Arad', 366)
    zerind = No('Zerind', 374)
    oradea = No('Oradea', 380)
    sibiu = No('Sibiu', 253)
    timisoara = No('Timisoara', 329)
    lugoj = No('Lugoj', 244)
    mehadia = No('Mehadia', 241)
    dobreta = No('Dobreta', 242)
    craiova = No('Craiova', 160)
    rimnicu = No('Rimnicu', 193)
    fagaras = No('Fagaras', 178)
    pitesti = No('Pitesti', 98)
    bucharest = No('Bucharest', 0)
    giurgiu = No('Giurgiu', 77)

    arad.adiciona_adjacente(Adjacente(zerind, 75))
    arad.adiciona_adjacente(Adjacente(sibiu, 140))
    arad.adiciona_adjacente(Adjacente(timisoara, 118))

    zerind.adiciona_adjacente(Adjacente(arad, 75))
    zerind.adiciona_adjacente(Adjacente(oradea, 71))

    oradea.adiciona_adjacente(Adjacente(zerind, 71))
    oradea.adiciona_adjacente(Adjacente(sibiu, 151))

    sibiu.adiciona_adjacente(Adjacente(oradea, 151))
    sibiu.adiciona_adjacente(Adjacente(arad, 140))
    sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
    sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

    timisoara.adiciona_adjacente(Adjacente(arad, 118))
    timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

    lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
    lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

    mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
    mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

    dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
    dobreta.adiciona_adjacente(Adjacente(craiova, 120))

    craiova.adiciona_adjacente(Adjacente(dobreta, 120))
    craiova.adiciona_adjacente(Adjacente(pitesti, 138))
    craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

    rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
    rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
    rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

    fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
    fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

    pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
    pitesti.adiciona_adjacente(Adjacente(craiova, 138))
    pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

    bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
    bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
    bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))
'''
class Arvore:
    portoUniao = No('porto Uniao', 203)
    pauloFrontin = No('paulo Frontin', 172)
    canoinhas = No('canoinhas', 141)
    tresBarras = No('tres Barras', 131)
    saoMateusDoSul = No('são mateus do sul', 123)
    irati = No('irati', 139)
    curitiba = No('curitiba', 0)
    palmeira = No('palmeira', 59)
    mafra = No('mafra', 94)
    campoLargo = No('Campo Largo', 27)
    balsaNova = No('balsa nova', 41)
    lapa = No('Lapa', 74)
    tijucaDoSul = No('Tijuca do sul', 56)
    araucaria = No('Araucária', 23)
    saoJose = No('são josé dos pinhais', 13)
    contenda = No('Contenda', 39)

    portoUniao.adiciona_adjacente(Adjacente(pauloFrontin,46))
    portoUniao.adiciona_adjacente(Adjacente(saoMateusDoSul,87))
    portoUniao.adiciona_adjacente(Adjacente(canoinhas,78))

    canoinhas.adiciona_adjacente(Adjacente(portoUniao,78))
    canoinhas.adiciona_adjacente(Adjacente(tresBarras,12))
    canoinhas.adiciona_adjacente(Adjacente(mafra,66))

    tresBarras.adiciona_adjacente(Adjacente(canoinhas,12))
    tresBarras.adiciona_adjacente(Adjacente(saoMateusDoSul,43))

    saoMateusDoSul.adiciona_adjacente(Adjacente(portoUniao,87))
    saoMateusDoSul.adiciona_adjacente(Adjacente(irati,57))
    saoMateusDoSul.adiciona_adjacente(Adjacente(tresBarras,43))
    saoMateusDoSul.adiciona_adjacente(Adjacente(lapa,60))
    saoMateusDoSul.adiciona_adjacente(Adjacente(palmeira,77))

    irati.adiciona_adjacente(Adjacente(pauloFrontin,75))
    irati.adiciona_adjacente(Adjacente(saoMateusDoSul,57))
    irati.adiciona_adjacente(Adjacente(palmeira,75))
    
    curitiba.adiciona_adjacente(Adjacente(campoLargo,29))
    curitiba.adiciona_adjacente(Adjacente(balsaNova,51))
    curitiba.adiciona_adjacente(Adjacente(araucaria,37))
    curitiba.adiciona_adjacente(Adjacente(saoJose,15))

    palmeira.adiciona_adjacente(Adjacente(saoMateusDoSul,77))
    palmeira.adiciona_adjacente(Adjacente(irati,75))
    palmeira.adiciona_adjacente(Adjacente(campoLargo,55))

    mafra.adiciona_adjacente(Adjacente(lapa,57))
    mafra.adiciona_adjacente(Adjacente(canoinhas,66))    
    mafra.adiciona_adjacente(Adjacente(tijucaDoSul,99))

    campoLargo.adiciona_adjacente(Adjacente(palmeira,55))
    campoLargo.adiciona_adjacente(Adjacente(balsaNova,22))  
    campoLargo.adiciona_adjacente(Adjacente(curitiba,29))

    balsaNova.adiciona_adjacente(Adjacente(campoLargo,22))
    balsaNova.adiciona_adjacente(Adjacente(contenda,19))
    balsaNova.adiciona_adjacente(Adjacente(curitiba,51))

    lapa.adiciona_adjacente(Adjacente(mafra,26))
    lapa.adiciona_adjacente(Adjacente(saoMateusDoSul,60))
    lapa.adiciona_adjacente(Adjacente(contenda,26))

    tijucaDoSul.adiciona_adjacente(Adjacente(mafra,99))
    tijucaDoSul.adiciona_adjacente(Adjacente(saoJose,49))

    araucaria.adiciona_adjacente(Adjacente(curitiba,37))
    araucaria.adiciona_adjacente(Adjacente(contenda,18))

    saoJose.adiciona_adjacente(Adjacente(curitiba,15))
    saoJose.adiciona_adjacente(Adjacente(tijucaDoSul,49))

    contenda.adiciona_adjacente(Adjacente(balsaNova,22))
    contenda.adiciona_adjacente(Adjacente(araucaria,18))
    contenda.adiciona_adjacente(Adjacente(lapa,26))