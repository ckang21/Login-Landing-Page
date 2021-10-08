from tkinter import Tk, ttk, StringVar, messagebox
#Currently importing LandingPage from my folder, will need to adjust to import from proper location later
from CS2450LandingPage import LandingPage



#This class will call up the login GUI and prompt for username and password
class LoginPage():
    def __init__(self, parent):
        #username and password text boxes plus labels, save inputs to variables for future use
        #Set up the frame and create all buttons
        self.frame = ttk.Frame(parent)
        usernameLabel = ttk.Label(parent, text = "User Name").grid(row=3, column = 3)
        username = StringVar()
        usernameInput = ttk.Entry(parent, textvariable = username).grid(row = 3, column = 4)
        passwordLabel = ttk.Label(parent, text = "Password").grid(row = 3, column = 7)
        password = StringVar()
        passwordInput = ttk.Entry(parent, textvariable = password, show = '*').grid(row = 3, column = 8)
        
        #add login button, calls checkLogin
        loginButton = ttk.Button(parent, text = "Login", command = self.checkLogin(username, password)).grid(row = 8, column = 5)
        
    #Will call up a warning box if the credentials are invalid
    def failLogin(self):
         messagebox.showwarning(title="Failed Login", message="Incorrect Username or Password")
         
    #Will call to remove the Frame
    def removeLogin(self):
        self.frame.grid_forget()
        
    #Inputs will be passed in here to verify validity
    #Will finish implementation when username and password csv are completed
    def checkLogin(self, username, password):
        #placeholder for veryifying the user and password
        #results = checkCredential(username, password)
        #if results is true:
        #LandingPage.makePage(self)
        #loginPage.removeLogin()
        #else:
         
        #self.failLogin()
        return
         
        
def main():
    #Setting up the window and dimensions
    tkWindow = Tk()
    tkWindow.geometry('650x100')
    tkWindow.title('Login Page')
    loginPage = LoginPage(tkWindow)
    
    #Automatically start off by calling Login in a main loop
    def showLogin():
        loginPage.render()
        #landingPage = LandingPage(tkWindow, user, showLogin)
    
    
    
    
            
    tkWindow.mainloop()

if __name__ == "__main__":
    main()
