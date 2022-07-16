'''multilevel Inheritance'''
import logging
logging.basicConfig(filename='example6_log.log',level=logging.DEBUG,format="%(levelname)s, %(asctime)s, %(message)s")
logging.info("This is an example of multilevel Inheritance")
class Internship:
    logging.info("Created a class Internship and we are inside it")
    _subjects = 'Python,ML,DL,Java,Blockchain'
    assignments = '40%'
    __projects = '5'
    duration = '6 months'
    logging.info("created variables of class _subjects as protected,assignments as public ,projects as private and duration as public variable")
    def subjects(self):
        try:
            logging.info("Internship covers multiple subjects like "+self._subjects)
        except Exception as e:
            logging.exception(e)
    def offerLetter(self):
        try:
            logging.info("Internship provides offerLetter if you complete "+self.assignments+" And "+str(self.__projects))
        except Exception as e:
            logging.exception(e)
    def experienceLetter(self):

        logging.info("After completion of internship experience letter would be provided")

class python(Internship):
    logging.info("Created a class Python and we are inheriting class Internship in it")
    def studentDetails(self):
        logging.info("Student wants multiple course")
    def course_assignments(self):
        try:
            logging.info("Students need to complete alteast "+self.assignments+ "of assignments")
        except Exception as e:
            logging.exception(e)


class DeepLearning(python):
    logging.info("Created a class DeepLearning and we are inheriting class Python in it")
    def course_duration(self):
        try:
            logging.info("Course duration is " + str(self.duration) + " for this course with " + self._Internship__projects)
        except Exception as e:
            logging.exception(e)

logging.info("creating an Object of class DeepLearning i.e. Dobj")
Dobj = DeepLearning()
logging.info("calling a function subjects")
Dobj.subjects()
logging.info("calling a function course_duration")
Dobj.course_duration()
logging.info("calling a function course_assignments")
Dobj.course_assignments()
logging.info("calling a function offerLetter")
Dobj.offerLetter()
logging.info("calling a function experienceLetter")
Dobj.experienceLetter()

