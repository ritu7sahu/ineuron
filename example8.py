import logging
logging.basicConfig(filename='example8_log.log',level=logging.DEBUG,format="%(levelname)s, %(asctime)s, %(message)s")
logging.info("This is an example where 2 classes using one class")
class ineuron:
    logging.info("created a class ineuron and we are inside it")
    def __init__(self,affiliateLink,name,subject,vacancySub):
        logging.info("created constructor having variable name affiliateLink as private,name,subject as protected,vacancySub")
        self.name = name
        self._subject = subject
        self.__affiliateLink = affiliateLink
        self.vacancySub = vacancySub

    def students(self):
        try:
            logging.info("Student name is " +self.name)
        except Exception as e:
            logging.exception(e)
    def affiliates(self):
        try:
            logging.info("Afiliate link for "+self.name+" is "+self.__affiliateLink)
        except Exception as e:
            logging.exception(e)
    def subjects(self):
        try:
            logging.info("Selected subject is "+ self._subject)
        except Exception as e:
            logging.info(e)
    def career(self):
        try:
            logging.info("Ineuron has job requirement of "+self.vacancySub )
        except Exception as e:
            logging.info(e)

class blogs(ineuron):
    logging.info("Created a class blog and inherited class ineuron")
    def writeBlog(self):
        try:
            logging.info("writing a blog for subject "+self._subject)
        except Exception as e:
            logging.exception(e)
    def getTodaysBlog(self):
        logging.info("showing all blogs for today")

class internship(ineuron):
    logging.info("created a class and inherited a class ineuron")
    def offerLetter(self):
        logging.info("Get offer letter after completion of internship")
    def projects(self):
        try:
            logging.info("Complete projects "+self._subject+" to get certificate")
        except Exception as e:
            logging.exception(e)

logging.info("created a object bObj and iObj for blog and internship respectively")
bObj = blogs('abc.affiliate.ineuron.ai','ABC','Python','Python')
iObj = internship('xyz.affiliate.ineuron.ai','XYZ','ML','ML')
logging.info("Calling a function subjects using blog obj")
bObj.subjects()
logging.info("Calling a function writeBlog using blog obj")
bObj.writeBlog()
logging.info("Calling a function getTodaysBlog using blog obj")
bObj.getTodaysBlog()
logging.info("Calling a function students using internship obj")
iObj.students()
logging.info("Calling a function subjects using internship obj")
iObj.subjects()
logging.info("Calling a function affiliates using  internship obj")
iObj.affiliates()
logging.info("Calling a function offerletter using  internship obj")
iObj.offerLetter()
logging.info("Calling a function projects using  internship obj")
iObj.projects()
