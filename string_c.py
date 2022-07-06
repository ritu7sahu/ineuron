import logging
logging.basicConfig(filename="String_log.log", level=logging.DEBUG, format="%(levelname)s %(asctime)s %(message)s")

class String_C :
    logging.info("created a class string")

    # extract index from 1 to 300 with 3 jumps
    def extractStr(self,s):
        try:
            self.s = s
            logging.info("String is %s", self.s)
            logging.info("we are inside extractStr function to get string from index 1 to 300 with jump 3")
            extractedStr = self.s[1:300:3];
            logging.info("extracted string is %s",extractedStr)
            return extractedStr
        except Exception as e :
            logging.exception(e)

    #reverse a string
    def reverseStr(self, s):
        try:
            self.s = s
            logging.info("String is %s", self.s)
            logging.info("we are inside reverseStr function to get reversed string ")
            reversedStr = self.s[: :-1];
            logging.info("extracted string is %s", reversedStr)
            return reversedStr
        except Exception as e:
            logging.exception(e)

     #split a string after conversion of entire string in uppercase
    def splitStr(self, s):
        try:
            self.s = s
            logging.info("String is %s", self.s)
            logging.info("we are inside splitStr function to get string in uppercase and split it ")
            Str = self.s.upper().split(" ");
            logging.info(" string is %s", Str)
            return Str
        except Exception as e:
            logging.exception(e)

    # convert string in lowercase
    def strInLowerCase(self, s):
        try:
            self.s = s
            logging.info("String is %s", self.s)
            logging.info("we are inside strInLowerCase function to get string in lowercase")
            Str = self.s.lower();
            logging.info(" string is %s", Str)
            return Str
        except Exception as e:
            logging.exception(e)

    # Capitalize whole string
    def capitalizeStr(self, s):
        try:
            self.s = s
            logging.info("String is %s", self.s)
            logging.info("we are inside capitalize function")
            Str = self.s.capitalize()
            logging.info(" string is %s", Str)
            return Str
        except Exception as e:
            logging.exception(e)

    # expandTab
    def expandTabStr(self):
        try:
            s = 'this\tis\tmy\tfirst\tpython\tprogramming\tclass\tand\ti\tam\tlearning\tpython\tlearning\tand\tits\tfunction'
            logging.info("String is %s", s)
            logging.info("we are inside expandTabStr function ")
            Str = s.expandtabs()
            logging.info(" string is %s", Str)
            return Str
        except Exception as e:
            logging.exception(e)

    # replace a string character with new character
    def replaceStr(self, s):
        try:
            self.s = s
            logging.info("String is %s", self.s)
            logging.info("we are inside replaceStr function ")
            Str = self.s.replace('t','z')
            logging.info(" string is %s", Str)
            return Str
        except Exception as e:
            logging.exception(e)

    #difference between isalnum and isalpha
    ''' isalpha returns true if given string contains alphabets only and isalnum returns true if given 
        string containing alphabets and numeric values both.'''

    #defination of string Center function with an example
    ''' String center() function accept 2 parameters. First parameter added a width or padding and second can be
    any character or blank space.
    example: if "Ritu" is a string it has 4 characters now if I add width of 10 then it will add padding of 6 characters
    3 before the str and ext 3 after the str
   
    example:    str = 'Ritu'
                str.center(10 ,'*')
    output :    ***Ritu***            
    '''


    # defination of compiler and interpreter
    '''compiler scans the entire code and translates in single line and if code having any syntax error it returns that
    errors . Interpreter read one statement at a time.Compiler is faster than interpreter'''

    #pyhton is compiled or interpreted language
    '''
    Python can be called as compiled and interpreted both language.In python, when source code executes,
    compile translates source code into binary code and this binary code can not be understood by any of OS.
    So this binary code needs to be converted in machine code and for this interpreter is used.Interpreter 
    translates this binary code into machine code on Python virtual machine which can be understandable code
    by any OS. 
    '''

    #usecases of python
    '''
        1. Python is used for Data science in machine learning.Python has multiple libraries that can be used in ML.
        2. Python is used for web application and software development.We can use its framework like  flask and django etc.
        3. Python is used in AI.
        4. Python is used for game applications.
        
    '''


strObj = String_C()
string = 'this is My First Python programming class and i am learNING python learning and its function'
logging.info("calling function extractStr() using strObj")
strObj.extractStr(string)
logging.info("calling function reverseStr() using strObj")
strObj.reverseStr(string)
logging.info("calling function splitStr() using strObj")
strObj.splitStr(string)
logging.info("calling function strInLowerCase() using strObj")
strObj.splitStr(string)
logging.info("calling function capitalizeStr() using strObj")
strObj.capitalizeStr(string)
logging.info("calling function expandTabStr() using strObj")
strObj.expandTabStr()
logging.info("calling function replaceStr() using strObj")
strObj.replaceStr(string)
