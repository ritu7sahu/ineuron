import logging
logging.basicConfig(filename='list_log.log',level=logging.DEBUG,format="%(levelname)s, %(asctime)s, %(message)s")

class List_c :
    logging.info("created a class List_c and we are inside it")

    def extractAllList(self,l):

        try:
            self.l = l
            logging.info("inside extractAlllist function which is going to extract all lists from a list")
            logging.info("list is %s", self.l)
            logging.info("creating a blank list which will store new list")
            newList = []
            for lst in self.l :
                if type(lst) == list :
                    newList.append(lst)
            logging.info("after finding the lists from a list newlist is %s",newList)
            return newList

        except Exception as e :
            logging.exception(e)

    ''' get all numeric from list '''
    def getAllNumeric(self,l):
        try:
            logging.info("inside getAllNumeric function which is going to extract all numeric data from a list")
            logging.info("list is %s", self.l)
            logging.info("creating a blank list which will store new list")
            self.l = l
            newList = []
            for lst in l:
                list1 = []
                if type(lst) == list or type(lst) == tuple or type(lst) == set:
                    for i in lst:
                        logging.info("checking if data is numeric or not")
                        if str(i).isnumeric():
                            list1.append(i)
                elif type(lst) == dict:
                    for j in lst.values():
                        if str(j).isnumeric():
                            list1.append(j)
                    for j in lst.keys():
                        if str(j).isnumeric():
                            list1.append(j)

                if list1 != []:
                    newList.append(list1)
            logging.info("after finding the lists from a list newlist is %s", newList)
            return newList
        except Exception as e:
            logging.exception(e)


    ''' get all odd numeric from list '''

    def getAllOddNumeric(self, l):
        try:
            logging.info("inside getAllOddNumeric function which is going to extract all odd numeric data from a list")
            logging.info("list is %s", self.l)
            logging.info("creating a blank list which will store new list")
            self.l = l
            newList = []
            for lst in l:
                list1 = []
                if type(lst) == list or type(lst) == tuple or type(lst) == set:
                    for i in lst:
                        logging.info("checking if data is numeric or not")
                        if str(i).isnumeric():
                            if i % 2 != 0:
                                logging.info("getting odd number")
                                list1.append(i)
                elif type(lst) == dict:
                    for j in lst.values():
                        if str(j).isnumeric():
                            if j % 2 != 0:
                                list1.append(j)
                    for j in lst.keys():
                        if str(j).isnumeric():
                            if j % 2 != 0:
                                list1.append(j)

                if list1 != []:
                    newList.append(list1)
            logging.info("after finding the odd no from a list newlist is %s", newList)
            return newList
        except Exception as e:
            logging.exception(e)


    #extract string ineuron from list
    def findString(self, l):
        try:
            logging.info("inside findString function ")
            logging.info("list is %s", self.l)

            self.l = l
            string = ""
            for lst in l:
                if type(lst) == list or type(lst) == tuple or type(lst) == set:
                    for i in lst:
                        if i == "ineuron":
                            string = i + " " + string

                elif type(lst) == dict:
                    for j in lst.values():
                        if (j == 'ineuron'):
                            string += j
            logging.info("got ineuron string %s" ,string)
            return string
        except Exception as e:
            logging.exception(e)

    '''get flat list from collections of list'''
    def getFlatList(self,l):

        try:
            self.l = l
            logging.info("inside extractAlllist function which is going to extract all lists from a list")
            logging.info("list is %s", self.l)
            logging.info("creating a blank list which will store new list")
            newList = []
            for lst in l:
                if type(lst) == list or type(lst) == tuple or type(lst) == set:
                    for i in lst:
                        newList.append(i)

                elif type(lst) == dict:
                    newList.extend(lst.values())
                    newList.extend(lst.keys())
            logging.info("new flatlist is %s", newList)
            return newList

        except Exception as e :
            logging.exception(e)


listObj = List_c()
logging.info("created object of the class named listObj")
l = l = [[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':'sudh',"k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron","data science"]]
logging.info("we have list l = %s",l)
listObj.extractAllList(l)
logging.info("called a function extractAlllist for extracting all lists from list l")

listObj.getAllNumeric(l)
logging.info("called a function getNumericdata for extracting numeric data from list l")

listObj.getAllOddNumeric(l)
logging.info("called a function getAllOddNumeric for extracting odd numeric data from list l")

listObj.findString(l)
logging.info("called a function findString for getting ineuron from list l")

listObj.getFlatList(l)
logging.info("called a function getflatList for getting a single list")
