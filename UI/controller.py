import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choiceTeam = None # variabile in cui si salva la squadra del menù a tendina

    def handleCreaGrafo(self, e):
        """Gestisce il click sul bottone Crea Grafo"""
        self._model.creaGrafo() # la costruzione del grafo è delegata al Model
        self._view._txt_result.controls.clear()
        n, m = self._model.getGraphDetails() # recupero dal Model archi e nodi
        self._view._txt_result.controls.append(ft.Text(f"Grafo correttamente creato! Il grafo è costituito di: {n} nodi e {m} archi", color="green"))
        self._view.update_page()

    def handleDettagli(self, e):
        pass

    def handlePercorso(self, e):
        pass

    def _fillDDYears(self):
        """Riempie il menù a tendina degli anni (dati semplici, disponibili subito)"""
        years = self._model.getAllYears() # chiede al Model gli anni disponibili (dal DAO)
        yearsDD = [] # lista di opzioni per il DropDown
        for year in years: # ogni anno diventa un'opzione selezionabile
            yearsDD.append(ft.dropdown.Option(year))
        self._view._ddAnno.options = yearsDD # assegno la lista di opzioni al menù a tendina
        self._view.update_page()

    def handleYearSelection(self, e):
        """Quando l'utente ha selezionato l'anno, recupera tutti i team che
            hanno giocato in quell'anno, li stampa e riempie il dropdown"""
        if self._view._ddAnno.options is None:
            self._view._txtOutSquadre.controls.clear()
            self._view._txtOutSquadre.controls.append(ft.Tex("Selezionare un anno dal menù!"))

        teams = self._model.getTeamsOfYear(self._view._ddAnno.value) # recupera dal Model le squadre che hanno giocato in quell'anno
        self._view._txtOutSquadre.controls.clear()
        self._view._txtOutSquadre.controls.append(ft.Text(f"Per il {self._view._ddAnno.value} sono iscritte al campionato {len(teams)} squadre."))
        for team in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(team)) # stampa nell'area di testo
            # Riempimento del DropDown squadre (si salvano oggetti dipendenti dall'anno)
            self._view._ddSquadra.options.append(ft.dropdown.Option(data = team,
                                                                    text = team.name,
                                                                    on_click= self.readDDTeams))
        self._view.update_page()

    def readDDTeams(self, e):
        """Legge la squadra selezionata dal DropDown"""
        if e.control.data is None: # se l'opzione selezionata non ha dati associati, la resetto
            self._choiceTeam = None
        else: # altrimenti salvo nel Controller l'oggetto Team selezionato
            self._choiceTeam = e.control.data





