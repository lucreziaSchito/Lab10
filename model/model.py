from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """
        # TODO
        self.G.clear()
        filiali = DAO.read_all_filiali()
        for i in filiali :
            self.G.add_node(filiali[i])
        dict_edges = self.get_all_edges()
        self._edges = 0
        for collegamento in dict_edges:
            peso = dict_edges[collegamento][0] / dict_edges[collegamento][1]
            if peso >= float(threshold):
                self.G.add_edge(filiali[collegamento[0]], filiali[collegamento[1]], weight=peso)
                self._edges += 1
        return self.G

    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self._edges

    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        self._nodes = len(DAO.read_all_filiali())
        return self._nodes

    def get_all_edges(self):
        """
        Restituisce tutti i Collegamenti (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        self.dict_bonifici = DAO.read_all_bonifici()
        dict_calcolo_peso = {}
        # creo un dizionario che ha come chiave una tupla formata dalla coppia di filiali tra cui c'è stato un bonifico
        # e come valore una lista contenente il valore dell'importo del bonifico e un contatore per il calcolo del peso
        for i in self.dict_bonifici:
            filiale_partenza = self.dict_bonifici[i].id_filiale_origine
            filiale_arrivo = self.dict_bonifici[i].id_filiale_destinazione

            if filiale_partenza == filiale_arrivo:
                continue
            # in questo modo evito i self-loop

            u = min(filiale_partenza, filiale_arrivo)
            v = max(filiale_partenza, filiale_arrivo)
            coppia = (u, v)
            valore = self.dict_bonifici[i].importo
            if coppia not in dict_calcolo_peso:
                dict_calcolo_peso[coppia] = [valore,1]
                #inizializzo
            else :
                dict_calcolo_peso[coppia][0] += valore
                dict_calcolo_peso[coppia][1] += 1
                #conteggio
        return dict_calcolo_peso
