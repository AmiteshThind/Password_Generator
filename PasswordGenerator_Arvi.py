import random
import string

# Password length must be between 10 and 24


specialCharacters = "-|@.,?/!~#%^&*(){}[]\=*"
specialCharacters = list(specialCharacters)
sizeOfSpecialCharacters = len(specialCharacters)

passwordLength = random.randint(11, 23)

#print("passwordLength :" + str(passwordLength))

numLowercaseCharacters = random.randint(1,
                                        passwordLength - 3)  # subtract 3 because atleast 1 must be lower , atleast 1 must be special atleast 1 must be number

numUppercaseCharacters = (random.randint(1, (passwordLength - numLowercaseCharacters) - 2))
numSpecialCharacters = random.randint(1, (passwordLength - (numUppercaseCharacters + numLowercaseCharacters + 1)))
numRandNumber = passwordLength - (numLowercaseCharacters + numUppercaseCharacters + numSpecialCharacters)

#print ("lowercaseCharacters:" + str(numLowercaseCharacters))
#print ("uppercaseCharacters:" + str(numUppercaseCharacters))
#print("numSpecialCharacters:" + str(numSpecialCharacters))
#print("numRandNumber:" + str(numRandNumber))

password = ""

# generate ranom characters and append to string

for i in range(0, numLowercaseCharacters):
    password += random.choice(string.ascii_lowercase)

for i in range(0, numUppercaseCharacters):
    password += random.choice(string.ascii_uppercase)

for i in range(0, numSpecialCharacters):
    password += specialCharacters[random.randint(0, sizeOfSpecialCharacters)]

for i in range(0, numRandNumber):
    password += str(random.randint(0, 9))

# convert to list to randomize
passwordList = list(password)
# Randomize string
random.shuffle(passwordList)

# join list together into one string

password = "".join(passwordList)



print ("Password:" + password)

# Must contains at least 1 number
# Must contains at least one of these special characters -|@.,?/!~#%^&*(){}[]\=*
