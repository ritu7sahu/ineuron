'''Example of data Encapsulation'''
import logging
logging.basicConfig(filename='example4_log.log',level=logging.DEBUG,format="%(levelname)s, %(asctime)s, %(message)s")
logging.info("This is an example of data encapsulation ")

class career:
    logging.info("Creating a class career and we are inside it")
    def __init__(self,currentSal):
        logging.info("Creating a constructor. It is having a variable currentSal")
        self.currentSal = currentSal

    __maxSalaryFor2YExp = 30000
    logging.info("created a private variable __maxSalaryFor2YExp having value is "+str(__maxSalaryFor2YExp))
    def candidate(self):
        logging.info("Created a function candidate")
        try:
            logging.info("candidate having current salary " + str(self.currentSal) + " with 2 years of experience")
        except Exception as e:
            logging.exception(e)
    def maxSalary(self):
        logging.info("created a function maxSalary")
        try:
            logging.info("Candidate should get maximum salary of " + str(self.__maxSalaryFor2YExp) + " for this experience")
        except Exception as e:
            logging.exception(e)
    def change_sal_canditate(self):
        logging.info("created a function change_sal_candidate which get max salary according to current salary")
        try:
            if (self.currentSal >= 40000):
                self.__maxSalaryFor2YExp = 45000
            else:
                self.__maxSalaryFor2YExp = self.currentSal + 10000
        except Exception as e:
            logging.exception(e)


logging.info("taking input from user for current salary")
salary = int(input("Enter current salary"))
logging.info("user entered current salary "+str(salary))
logging.info("creating onject of career class i.e cObj")
cObj = career(salary)
logging.info("calling function candidate")
cObj.candidate()
logging.info("calling function change_sal_canditate")
cObj.change_sal_canditate()
logging.info("calling function maxSalary")
cObj.maxSalary()