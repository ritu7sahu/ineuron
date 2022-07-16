''' Example of method overriding'''
import logging
logging.basicConfig(filename='example1.log',level=logging.DEBUG,format="%(levelname)s, %(asctime)s, %(message)s")
logging.info("This is an example of method overriding ")
class students:
    logging.info("Created a class student and we are inside it")
    def __init__(self,name,course):
        try:
            self.name = name
            self.courseName = course
            self.__cmode = "Offline"
            logging.info('Created a constructor which is having variable name,courseName,classMode and a self keyword which is a pointer')
        except Exception as e:
            logging.exception(e)
    def studentDetails(self):
        logging.info("This is StudentDetails function which is taking name of student")
        try:
            logging.info("Student name is "+self.name)
        except Exception as e:
            logging.exception(e)
    def classMode(self):
        print(self.courseName+" class would be "+self.__cmode+" for student")

class ClassType(students):
    logging.info("Created another class class type and we are inside it")
    def classMode(self,clMode):
        logging.info("inside a function class mode for knowing class mode")
        try:
            self.mode = clMode
            logging.info(self.name+" class would be "+ self.mode +" due to covid " )
        except:
            logging.exception(e)

logging.info("Creating an object stuObj")
stuObj = students('Ritu','Python')
logging.info("Changing private variable cmode from offline to online and saving it a variable clMode")
stuObj.__cmode = 'Online'
clMode = stuObj.__cmode
logging.info("Now the value of cmode is "+clMode)
logging.info("Created an object of 2nd class and the name is classObj")
classObj = ClassType('Ritu','Python')
logging.info("calling a function classMode")
classObj.classMode(clMode)
