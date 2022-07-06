import logging
logging.basicConfig(filename='dict_log.log',level=logging.DEBUG,format="%(levelname)s, %(asctime)s, %(message)s")

class Dict_c :
    logging.info("created a class Dict_c")

    def getDictFromList(self,l):
        try:
            logging.info("inside function to get dictionary from list")
            self.l = l
            for dic in l :
                if type(dic) == dict :
                    logging.info("getting dictionary from list %s",dic)
                    return dic
        except Exception as e:
            logging.exception(e)

    ''' getting number of keys from dictionary'''

    def getKeysCount(self,l):
        try:
            logging.info("inside function to get keys count from dictionary")
            self.l = l
            for dic in l:
                if type(dic) == dict:
                    count = 0
                    for key in dic.keys():
                        count += 1
                    logging.info("count of keys are %s",count)
                    return count
        except Exception as e:
            logging.exception(e)
dictObj = Dict_c()
l = l = [[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':'sudh',"k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron","data science"]]
logging.info("we have list l = %s",l)
dictObj.getDictFromList(l)
logging.info("called a function getDictFromList for extracting all dictionary from list l")
dictObj.getKeysCount(l)
logging.info("called a function getKeysCount")
