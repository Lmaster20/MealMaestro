# Meal Maestro V1.0
# Simplifies group meal selection

str_emojiBirb = "🐥"
str_emojiYes = "👍"
str_emojiNo = "👎"

import gspread
from oauth2client.service_account import ServiceAccountCredentials


def testOpen(fileName):
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
    print(list_of_hashes)

testOpen("test_data")