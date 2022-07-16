import logging
logging.basicConfig(filename='example10_log.log',level=logging.DEBUG,format="%(levelname)s, %(asctime)s, %(message)s")
logging.info("This is an example for using package & module")
from ineuron.ineuron import internship
logging.info("Imported internship from ineuron package")
internshipObj = internship(10,40,'6months')
logging.info("created student class object internshipObj")
class student:
    logging.info("We are inside student class")
    def __init__(self,completedAssignment,completedProjects):
        logging.info("created a constructor and having 2 variables completedAssignment & completedProjects")
        self.completedAssignment = completedAssignment
        self.completedProjects = completedProjects

    def certificate(self):
        logging.info("I got certificate for python course")

logging.info("Created an object of student i.e. stuObj")
stuObj = student(30,7)
try:
    logging.info("Applying condition to check assignment count and project for getting certificate")
    condition = stuObj.completedAssignment < internshipObj.assignmentCount or stuObj.completedProjects < internshipObj._internship__projectCount
    if condition :
        logging.info("Please complete atleast "+str(internshipObj.assignmentCount) + " percent assignments and " + str(internshipObj._internship__projectCount) + " projects")
    else:
        logging.info("Calling Certificate function")
        stuObj.certificate()
except Exception as e:
    logging.exception(e)



