''' Example for  method overloading'''
import logging
logging.basicConfig(filename='example2_log.log',level=logging.DEBUG,format="%(levelname)s, %(asctime)s, %(message)s")
logging.info("This is an example of method overloading ")
class course :
    logging.info("Creating a class course and we are inside it")
    def courses(self):
        logging.info("created a function course which gives us information about courses")
        logging.info("There are multiple courses for students")

class student :
    logging.info("Creating another class student and we are inside it")
    __name = 'Ritu'
    def studentDetails(self):
        logging.info("created a function studentDetails which gives us information about student")
        try:
            logging.info("Student name is "+self.__name)
        except Exception as e:
            logging.exception(e)
    def courses(self):
        logging.info("Student has taken 2 courses")

logging.info("Now we have created a function showCoursed awhich is having a parameter obj")
def showCourses(obj):
    logging.info("calling a class function using an object")
    obj.courses()
logging.info("Creating objects of classes course and student and the object name are cOBj and sObj respectively ")
cObj = course()
sObj = student()
logging.info("Calling a function showCourses with a parameter course obj i.e. cObj")

showCourses(cObj)
logging.info("Calling again a same function showCourses with a parameter student obj i.e. sObj")
showCourses(sObj)
logging.info("This achieves the concept of method overloading")
