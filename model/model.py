import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._teams = []

    def creaGrafo(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._teams)
        # Il grafo è COMPLETO, perciò esiste un arco tra ogni coppia di nodi
        for u in self._grafo.nodes(): # doppio ciclo sui nodi
            for v in self._grafo.nodes():
                if u != v: # se i due nodi sono diversi, aggiungo l'arco
                    self._grafo.add_edge(u, v)

    def getTeamsOfYear(self, year):
        self._teams = DAO.getTeamsOfYear(year)
        return self._teams

    def getAllYears(self):
        return DAO.getAllYear()

    def getGraphDetails(self):
        return len(self._grafo.nodes()), len(self._grafo.edges())
