import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """

        if self._view.guadagno_medio_minimo.value.isdigit():

            self._view.lista_visualizzazione.clean()
            self._model.costruisci_grafo(int(self._view.guadagno_medio_minimo.value))
            num_nodi = self._model.get_num_nodes()
            num_archi = self._model.get_num_edges()
            num_archi_pesati=self._model.get_all_edges()
            self._view.lista_visualizzazione.controls.append(
                ft.Text(f"numero di hubs: {num_nodi}")
            )
            self._view.lista_visualizzazione.controls.append(
                ft.Text(f"numero di tratte: {num_archi}")
            )

            for i, (u, v, valore) in enumerate(num_archi_pesati, start=1):
                self._view.lista_visualizzazione.controls.append(
                    ft.Text(f"{i}. Hub {u} ↔ Hub {v} | valore medio: {valore}")
                )
            self._view.page.update()
            #print("debug")
            #print("Nodi nel grafo:", self._model.get_num_nodes())
            #print("Archi nel grafo:", self._model.get_num_edges())
            #print("Edges dettagliati:", self._model.get_all_edges())
            return
        else:
            self._view.alert.show_alert("input non valido")
            return


