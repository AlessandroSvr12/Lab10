from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        self.G=nx.Graph()
        hubs=DAO.get_hub()
        for hub in hubs:
            self.G.add_node(hub)
        tratte=DAO.get_tratte()
        for tratta in tratte:
            if tratta.valore>threshold:
                self.G.add_edge(tratta.hub_a, tratta.hub_b,valore=tratta.valore )

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        all_edges = []
        for u, v, data in self.G.edges(data=True):
            edge = (u, v, data.get("valore"))
            all_edges.append(edge)
        return all_edges

