from AdvancedFernetDataEncryption import *
import json

# Generates the Token and stores the random token into the Token.json file 
def writeJson():
    with open("Token.json", "w") as outfile:
        outfile.write(json.dumps({"GenerateToken":passwordToken()}))

# Reads all information from Token.json file and stores in the dictionary data
def useJson():
    with open("Token.json") as Token:
        data = json.load(Token)
    return data

