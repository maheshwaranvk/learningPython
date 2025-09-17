#https://drive.google.com/open?id=1o8v0f3PmjWEQLHGH_1SHCVpRT73OsdZQ&usp=drive_fs

class BugTracker:
    def __init__(self):
        self.bugDetails={"bugID":"",
                    "bugValues":{
                        "description":"",
                        "severity":"",
                        "status":""
        }}
    def addBug(self,bugID, description, severity, status):
        self.bugDetails["bugID"]=bugID
        self.bugDetails["bugValues"]["description"]=description
        self.bugDetails["bugValues"]["severity"]=severity
        self.bugDetails["bugValues"]["status"]=status

    def updateStatus(self, newStatus):
        self.bugDetails["bugValues"]["status"]=newStatus
    
    def listAllBugs(self):
        print("Bug ID : ", self.bugDetails["bugID"])
        print("Bug Description : ", self.bugDetails["bugValues"]["description"])
        print("Bug Severity : ", self.bugDetails["bugValues"]["severity"])
        print("Bug Status : ", self.bugDetails["bugValues"]["status"])

if __name__=="__main__":
    bug1=BugTracker()
    bug1.addBug("BUG 1","Login not working","High","Open")
    bug1.listAllBugs()
    bug1.updateStatus("In Progress")
    bug1.listAllBugs()

    bug2=BugTracker()
    bug2.addBug("BUG 2","Logout not working","High","In Progress")
    bug2.listAllBugs()
    bug2.updateStatus("Closed")
    bug2.listAllBugs()