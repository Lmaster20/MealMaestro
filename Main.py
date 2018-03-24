# Meal Maestro V1.0
# Simplifies group meal selection

str_emojiBirb = "🐥"
str_emojiYes = "👍"
str_emojiNo = "👎"

import gspread
from oauth2client.service_account import ServiceAccountCredentials


def openSheet(fileName):
    """Opens the passed Google Sheet and returns a list of dictionaries of the contents
    """
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    testSheet = client.open(fileName).sheet1

    # Extract and print all of the values
    list_of_hashes = testSheet.get_all_records()
    return(list_of_hashes)

testList = openSheet("test_data")
print(testList)
print(testList[0])
print(testList[0]['Restaurant Name'])

num = 0
name = "RJ"
team = ["RJ", "DN", "DK", "PS"]
bigTeam = ["AA", "ACD", "AL", "AR", "CP", "CS", "DK", "DN", "JJ", "JM", "KB", "MB", "NB", "PS", "RJ", "SC", "SM"]

for person in bigTeam:
    num = 0
    while num < len(testList):
        if testList[num][person] == str_emojiYes:
            print(person, " likes ", testList[num]['Restaurant Name'])
        num = num + 1
for person in bigTeam:
    num = 0
    while num < len(testList):
        if testList[num][person] == str_emojiNo:
            print(person, " dislikes ", testList[num]['Restaurant Name'])
        num = num + 1

print("\n\nGo to fucking bed")

