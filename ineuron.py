#example for package & module
import logging
logging.basicConfig(filename='module_log.log',level=logging.DEBUG,format="%(levelname)s, %(asctime)s, %(message)s")
logging.info("This is an example for using package & module")
class student:
    logging.info("Creating a class student and we are inside it")
    def __init__(self,skill,experience,name):
        logging.info("Created a constructor which is having a variable sSkill,sExperience,name")
        self.sSkill = skill
        self.sExperience = experience
        self.name = name
    def studentDetails(self):
        try:
            logging.info("Name of Student is "+self.name)
        except Exception as e:
            logging.exception(e)
    def skill(self):
        try:
            logging.info("Student knows " + self.sSkill)
        except Exception as e:
            logging.exception(e)
    def experience(self):
        try:
            logging.info("student having " + self.sExperience + " years of experience")
        except Exception as e:
            logging.exception(e)
class internship:
    logging.info("Creating a class internship and we are inside it")
    def __init__(self,projectCount,assignmentCount,projectsDuration):
        logging.info("Created a constructor which is having a variable projectCount,assignmentCount,projectsDuration")
        self.__projectCount = projectCount
        self.assignmentCount = assignmentCount
        self.projectsDuration = projectsDuration
    def realTimePrj(self):
        try:
            logging.info("Real time projects duration is "+self.projectsDuration)
        except Exception as e:
            logging.exception(e)
    def offerLetter(self):
        try:
            logging.info("To get offer letter, the percentage of assignment should be "+self.assignmentCount)
        except Exception as e:
            logging.exception(e)
    def experienceLetter(self):
        try:
            logging.info("To get experience letter, the projects count should be "+self.projectCount)
        except Exception as e:
            logging.exception(e)


