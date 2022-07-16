'''method overloading'''
import logging
logging.basicConfig(filename='example3_log.log',level=logging.DEBUG,format="%(levelname)s, %(asctime)s, %(message)s")
logging.info("This is another example of method overloading ")
class internship:
    logging.info("Created a class internship and we are inside it")
    def internship1(self,*args):
        logging.info("Created a function internship1 which has multiple parameter and function is trying to achieve string concatenation ")
        try:
            str = ""
            for s in args:
                str = str + " " + s
            logging.info(str)
        except Exception as e:
            logging.exception(e)


logging.info("Creating an object inObj of class internship")
inObj = internship()
logging.info("calling function internship1 with 2 parameters")
inObj.internship1('sub1','sub2')
logging.info("calling function internship1 with 4 parameters")
inObj.internship1('a','b','c','d','e')
