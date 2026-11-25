import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_collegamenti(self, e):
        """
        Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
        poi popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Filiali presenti
        * Numero di Collegamenti
        * Lista di Collegamenti che superano l'importo indicato come soglia
        """
        # TODO
        count = 0
        if self._view.importo_medio_minimo.value.isdigit():
            grafo = self._model.costruisci_grafo(self._view.importo_medio_minimo.value)
            self._view.lista_visualizzazione.controls.clear()
            self._view.lista_visualizzazione.controls.append(
                ft.Text(f"Numero di Filiali {self._model.get_num_nodes()}"))
            self._view.lista_visualizzazione.controls.append(
                ft.Text(f"Numero di Collegamenti {self._model.get_num_edges()}"))

            for collegamento in grafo.edges(data=True):
                # Ogni elemento restituito da questo metodo è una tupla composta da (nodo_u, nodo_v, attributi = {})
                count = count + 1
                self._view.lista_visualizzazione.controls.append(
                    ft.Text(
                        f"{count}) {collegamento[0].nome} ({collegamento[0].provincia}) -> {collegamento[1].nome} ({collegamento[1].provincia}) "
                        f"-- Importo medio per bonifico: € {collegamento[2]["weight"]:.2f}"))
            self._view.update()

        else :
            self._view.show_alert("Deve inserire una soglia adeguata prima di proseguire")
            return

