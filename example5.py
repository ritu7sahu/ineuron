''' data abstraction'''
import logging
logging.basicConfig(filename='example5_log.log',level=logging.DEBUG,format="%(levelname)s, %(asctime)s, %(message)s")
logging.info("This is an example of data abstraction ")
class blog:
    logging.info("created a class blog and we are inside it")

    __BlogSub = 'Blockchain'
    logging.info("Created a variable blogSub and the value is "+__BlogSub)
    def writeBlog(self):
        logging.info("inside a function write blog")
        try:
            logging.info("Write a blog for "+ self.__BlogSub)
        except Exception as e:
            logging.exception(e)


blogObj = blog()
blogObj.writeBlog()
logging.info("created an object blogObj and called a function writeBlog using obj")
logging.info(blogObj._blog__BlogSub+ " is a private variable value of class and we are trying to achieve a concept of data abstraction");
