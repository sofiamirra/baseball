import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choiceTeam = None

    def handleCreaGrafo(self, e):
        self._model.creaGrafo()
        self._view._txt_result.controls.clear()
        n, m = self._model.getGraphDetails()
        self._view._txt_result.controls.append(ft.Text(f"Grafo correttamente creato! Il grafo è costituito di: {n} nodi e {m} archi", color="green"))
        self._view.update_page()

    def handleDettagli(self, e):
        pass

    def handlePercorso(self, e):
        pass

    def _fillDDYears(self):
        years = self._model.getAllYears()
        yearsDD = []
        for year in years:
            yearsDD.append(ft.dropdown.Option(year))
        self._view._ddAnno.options = yearsDD
        self._view.update_page()

    def handleYearSelection(self, e):
        """Quando l'utente ha selezionato l'anno, recupera tutti i team che
            hanno giocato quell'anno, li stampa e riempie il dropdown"""
        if self._view._ddAnno.options is None:
            self._view._txtOutSquadre.controls.clear()
            self._view._txtOutSquadre.controls.append(ft.Tex("Selezionare un anno dal menù!"))

        teams = self._model.getTeamsOfYear(self._view._ddAnno.value)
        self._view._txtOutSquadre.controls.clear()
        self._view._txtOutSquadre.controls.append(ft.Text(f"Per il {self._view._ddAnno.value} sono iscritte al campionato {len(teams)} squadre."))
        for team in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(team))
            self._view._ddSquadra.options.append(ft.dropdown.Option(data = team,
                                                                    text = team.name,
                                                                    on_click= self.readDDTeams))
        self._view.update_page()

    def readDDTeams(self, e):
        if e.control.data is None:
            self._choiceTeam = None
        else:
            self._choiceTeam = e.control.data





