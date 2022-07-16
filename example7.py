'''Multiple Inheritance'''
import logging
logging.basicConfig(filename='example7_log.log',level=logging.DEBUG,format="%(levelname)s, %(asctime)s, %(message)s")
logging.info("This is an example of multiple Inheritance")
class affiliates:
    logging.info("We are inside class affiliates ")
    def __init__(self,affiliate_link,student_name):
        logging.info("Created a constructor having variables affiliate_link,student_name")
        self.__affiliate_link = affiliate_link
        self.student_name = student_name


    def getAffiliateLink(self):
        logging.info("We are inside getAffiliateLink function")
        try:
            logging.info("affliate link is "+self.__affiliate_link)
        except Exception as e:
            logging.exception(e)
    def earnMoney(self):
        logging.info("We are inside earnMoney function")
        try:
            logging.info("student can earn money using " + self.__affiliate_link)
        except Exception as e:
            logging.exception(e)

class courses:
    logging.info("We are inside class courses ")
    courseName = 'DL'
    def getcourseName(self):
        try:
            logging.info("Course name is "+self.courseName)
        except Exception as e:
            logging.exception(e)
    def getcourseDuration(self):
        logging.info("Course duration is 6 months")

class student(affiliates,courses):
    logging.info("Created a class student and inheriting affiliates and courses class")
    def buyCourse(self):
        try:
            logging.info("Buy course " + self.courseName)
        except Exception as e:
            logging.exception(e)
    def sendAffiliateLink(self):
        try:
            logging.info("send link " + self._affiliates__affiliate_link)
        except Exception as e:
            logging.exception(e)
logging.info("Createing object of class student")
sObj = student('abc.affiliate.dl.ac','ABC')
logging.info("Calling getCourseName function of class course")
sObj.getcourseName()
logging.info("Calling getCourseName function of class course")
sObj.getcourseDuration()
logging.info("Calling getCourseName function of class student")
sObj.buyCourse()
logging.info("Calling getCourseName function of class affiliates")
sObj.getAffiliateLink()
logging.info("Calling getCourseName function of class student")
sObj.sendAffiliateLink()
logging.info("Calling earnMoney function of class affiliates")
sObj.earnMoney()