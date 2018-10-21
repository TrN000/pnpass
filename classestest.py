import MySQLdb


class sqlacces():

    def __init__(self):

        db = MySQLdb.connect(host="localhost", user="demouser", passwd="demopassword", db="demodb")
        cur = db.cursor()


    def acces(self):
        pass

    def createu(self):
        pass
    
    def login(self):
        pass

    def printall(self):
        pass

