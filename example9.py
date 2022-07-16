#example for package & module
import logging
logging.basicConfig(filename='example9_log.log',level=logging.DEBUG,format="%(levelname)s, %(asctime)s, %(message)s")
logging.info("This is an example for using package & module")
from ineuron.ineuron import student
logging.info("Imported student from ineuron package")
stuObj = student('Python','4','Ritu');
logging.info("created student class object stuObj")
class career:
    logging.info("We are inside career class")
    skill = stuObj.sSkill
    experience = stuObj.sExperience
    logging.info("created 2 variables skill and experience which is having values of student class from different module")
    def vacancy(self):
        logging.info("Have vacancy for python")
    def experienceRequired(self):
        try:
            logging.info(self.experience +" years of experience required for "+self.skill)
        except Exception as e:
            logging.exception(e)
    def student(self):
        logging.info("inside student function inside this we are calling a function from imported module student")
        stuObj.studentDetails()

logging.info("Created an object of career class")
careerObj = career()
logging.info("calling vacancy function using obj")
careerObj.vacancy()
logging.info("calling experienceRequired function using obj")
careerObj.experienceRequired()
logging.info("calling student function using obj")
careerObj.student()