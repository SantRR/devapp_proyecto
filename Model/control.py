class ControladorVentanas:
    def __init__(self):
        self.login_window = None
        self.main_window = None

    def show_login(self):
        from Model.load_login import LoadLogin
        self.login_window = LoadLogin(self)
        self.login_window.show()
        if self.main_window:
            self.main_window.close()

    def show_main(self):
        from Model.load_main import LoadMain
        self.main_window = LoadMain(self)
        self.main_window.show()
        if self.login_window:
            self.login_window.close()
