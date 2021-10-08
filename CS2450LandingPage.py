from tkinter import Tk, ttk, StringVar


#This class will create the Landing page
class LandingPage():
    
    #Constructor class
    def __init__(self, parent, user, login, permission):
        self.parent = parent
        self.userID = user
        self.frame = ttk.Frame(parent)
        self.loginCommand = login
        
        #Set the format of the buttons and all of their locations
        logoutButton = ttk.Button(self.frame, text = "Logout", command = self.onLogoutClicked)
        logoutButton.grid(row = 5, column = 3)
        profileButton = ttk.Button(self.frame, text = "Go to Profile", command = self.onProfileClicked)
        profileButton.grid(row = 2, column = 0)
        employeeButton = ttk.Button(self.frame, text ="Go to Employee Page", command = self.onEmployeeClicked)
        employeeButton.grid(row = 2, column = 5)
    
    #Once implemented this command will take the user to his personal profile
    #Currently unavailable
    def onProfileClicked(self):
        return
    
    #Once implemented this command will take a user with higher permission to a list of Employees page
    #Currently unavailable
    def onEmployeeClicked(self):
        return
    
    #Construct the frame
    def makePage(self):
        self.frame.grid()
    
    #This command will return the user to the login page and remove the current frame
    def onLogoutClicked(self):
        self.removePage()
        self.loginCommand()
        
    #Command to remove frame
    def removePage(self):
        self.frame.grid_forget()
        