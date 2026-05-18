import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._teams = []

    def creaGrafo(self):
        """Crea il grafo delle squadre"""
        self._grafo.clear()
        self._grafo.add_nodes_from(self._teams) # aggiungo come nodi tutte le squadre dell'anno selezionato
        # Il grafo è COMPLETO, perciò esiste un arco tra ogni coppia di nodi
        for u in self._grafo.nodes(): # doppio ciclo sui nodi
            for v in self._grafo.nodes():
                if u != v: # se i due nodi sono diversi, aggiungo l'arco
                    self._grafo.add_edge(u, v)

    def getTeamsOfYear(self, year):
        """Recupera le squadre che hanno giocato in un certo anno"""
        self._teams = DAO.getTeamsOfYear(year)
        return self._teams

    def getAllYears(self):
        """Restituisce tutti gli anni disponibili"""
        return DAO.getAllYear()

    def getGraphDetails(self):
        """Restituisce il numero di nodi e archi del grafo"""
        return len(self._grafo.nodes()), len(self._grafo.edges())
