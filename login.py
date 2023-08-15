class Login:
    def __init__(self, base_page):
        self.base_page = base_page;
        
    def Login(self, username, password):
        self.base_page.findAndWrite(username, "LoginDialog_loginText")
        self.base_page.findAndWrite(password, "LoginDialog_passwordText")
        self.base_page.findAndClick("LoginDialog_loginButton")
