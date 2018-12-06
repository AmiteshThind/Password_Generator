import random
import string

password = ""
specialCharacters = "-|@.,?/!~#%^&*(){}[]\=*"
specialCharacters = list(specialCharacters)
sizeOfSpecialCharacters = len(specialCharacters)

passwordLength = random.randint(11, 23)

numLowercaseCharacters = random.randint(1,passwordLength - 3) 
numUppercaseCharacters = (random.randint(1, (passwordLength - numLowercaseCharacters) - 2))
numSpecialCharacters = random.randint(1, (passwordLength - (numUppercaseCharacters + numLowercaseCharacters + 1)))
numRandNumber = passwordLength - (numLowercaseCharacters + numUppercaseCharacters + numSpecialCharacters)

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
