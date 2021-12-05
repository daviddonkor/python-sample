import random
import string

class RandomPasswordGeneratorAPI:

    def __init__(self,minlength=8):
        self.minlength=int(minlength)
        self.passwordlength=self.minlength
        self.maxlength=80
        self.lengthset=False
        self.stringcombination=""
        self.specailcharacters='/?[]|{)}(*&^%$#@!~;_-=+'
        
    #getting Lower, upper, numbers and special characters from String Object
    def setStringCombinations(self):
        lower=string.ascii_lowercase
        uppercase=string.ascii_uppercase
        numbers=string.digits
        self.stringcombination=lower+numbers+self.specailcharacters+uppercase
        #print(self.stringcombination)


    def getPassword(self):
        self.setStringCombinations()
       # print(self.passwordlength)
        return "".join(random.sample(self.stringcombination, self.passwordlength))

    def getPasswordLen(self):
       
        try:
            ans=int(input("\nYou can type 0 to end this application. \nWhat is the length of your password today? "))
            if(ans==0):
                exit()
            if(ans<self.minlength or ans > 80):
                self.getPasswordLen()
            self.passwordlength=ans
            self.lengthset=True
        except ValueError:
            print("You need to enter a valid number! Try again.")



#execution point of the API
print("Welcome to the strong password generator")
test=RandomPasswordGeneratorAPI()

while(not test.lengthset):
    test.getPasswordLen()

print(test.getPassword())