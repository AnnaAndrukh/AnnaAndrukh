import json
from tovar import nounlist2
from price import nounlist1

def  convertTojson():
 with open("price_json.jsonc", "w") as f:
    json.dump(nounlist1, f)
def convertInjson():
 with open("tovar_json.json", "w") as f:
    json.dump(nounlist2, f)

