graf=[]
A = {'Node': 'A', 'C': 1, 'D': 2}
B = {'Node': 'B', 'C': 2, 'F': 3}
C = {'Node': 'C', 'A': 1, 'B': 2, 'D': 1, 'E': 3}
D = {'Node': 'D', 'A': 2, 'C': 1, 'G': 1}
E = {'Node': 'E', 'C': 3, 'F': 2}
F = {'Node': 'F', 'B': 3, 'E': 2, 'G': 1}
G = {'Node': 'G', 'D': 1, 'F': 1}
graf.append(A)
graf.append(B)
graf.append(C)
graf.append(D)
graf.append(E)
graf.append(F)
graf.append(G)




class Alg_dikstry(object):
    def __init__(self, graf):
        self.lista_otwartych = []
        self.lista_zamknietych = []
        self.poprzedni = []
        self.graf = graf
        self.obecny = None
        self.dystans = 0
        self.step = 0


    def sciezka(self, poczatek, koniec):
        self.obecny = {poczatek: self.dystans}
        self.lista_otwartych.append(self.obecny)
        self.poprzedni.append({poczatek: poczatek})

        while list(self.obecny.keys())[0] != koniec:
            self.lista_zamknietych.append(list(self.obecny.keys())[0])
            self.lista_otwartych.pop(self.lista_otwartych.index(self.obecny))
            for node in self.graf:
                if node['Node'] in list(self.obecny.keys()):
                    for element in node:
                        if element != 'Node':
                            if element not in self.lista_zamknietych:
                                if any(element in d for d in
                                       self.lista_otwartych):
                                    for e in self.lista_otwartych:
                                        if list(e.keys())[0] == element:
                                            if node.get(element) + self.dystans < list(e.values())[0]:
                                                e[list(e.keys())[0]] = node.get(element) + self.dystans
                                                for p in self.poprzedni:
                                                    if list(p.keys())[0] == element:
                                                        p[list(e.keys())[0]] = list(self.obecny.keys())[0]
                                else:
                                    self.lista_otwartych.append({element: node.get(element) + self.dystans})
                                    self.poprzedni.append({element: list(self.obecny.keys())[0]})

            values = []
            for element in self.lista_otwartych:
                for node in element:
                    values.append(element.get(node))
            self.obecny = self.lista_otwartych[(values.index(min(values)))]
            self.dystans = list(self.obecny.values())[0]


        a = koniec
        string = str(koniec)
        while a != poczatek:
            for element in self.poprzedni:
                for node in element:
                    if node == a:
                        a = element.get(node)
                        string = str(a) + " ; " + string
        print("\nNajkrótsza odległość pomiądzy " + str(poczatek) + " i " + str(koniec) + " to:")
        print(string)
        print("Wartość odległości: ", self.dystans)

d = Alg_dikstry(graf)
d.sciezka('A', 'F')