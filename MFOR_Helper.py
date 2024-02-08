import json, sys
revealBosses = 2
revealDataRooms = 1
revealSectors = 1
bossesDict = {
    "Arachnus":"S0",
    "Yakuza":"S0",
    "Charge Core-X":"S1",
    "Ridley":"S1",
    "Zazabi":"S2",
    "Nettori":"S2",
    "Wide Core-X":"S3",
    "Serris":"S4",
    "Nightmare":"S5",
    "Mega Core-X":"S6",
    "Box-2":"S6"
}
def main():
    requiredItems = [
        [
            "Missile Data",
            "Super Missile Data",
            "Ice Missile Data"
        ],
        "Morph Ball",
        "Charge Beam",
        "Gravity Suit",
        "Speed Booster",
        "Plasma Beam"
    ]
    filename = "C:\YOUR\SPOILER\LOG\LOCATION\HERE.json"
    file = open(filename)
    data = json.load(file)
    itemNumber = 1
    missilesFound = False
    for i in data["Item order"]:
        tempItem = data["Item order"][i]
        if "Missile" in tempItem and missilesFound == False:
            requiredItems.pop(0)
            missilesFound = True
            print(getPrintString(i, data["Item order"][i], itemNumber) + " | Required")
        else:
            try:
                requiredItems.pop(requiredItems.index(tempItem))
                if len(requiredItems) == 0:
                    print(getPrintString(i, data["Item order"][i], itemNumber) + " | Go mode!")
                else:
                    print(getPrintString(i, data["Item order"][i], itemNumber) + " | Required")
            except:
                print(getPrintString(i, data["Item order"][i], itemNumber))
        itemNumber = itemNumber + 1
    file.close()

def getPrintString(tempKey, tempItem, itemNumber):
    bossString = ""
    dataString = ""
    sectorString = ""
    if revealSectors == 1:
        if "Item" not in tempKey and "Data" not in tempKey:
            sectorString = bossesDict[tempKey] + " "
        else:
            sectorString = tempKey[5:7] + " "
    if revealBosses > 0 or revealDataRooms == 1:
        if "Item" not in tempKey:
            if "Data" not in tempKey:
                if revealBosses > 0:
                    bossString = "(Locked Behind " + (tempKey + ") " if revealBosses == 2 else "Boss) ")
            else:
                if revealDataRooms == 1:
                    dataString = "(In a Data Room) "
    return "#" + str(itemNumber) + " " + sectorString + bossString + dataString + tempItem

if __name__ == "__main__":
    main()
