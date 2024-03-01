# The Railway Inn - Testing

Image

View the live site [here](https://railway-nn-employee-portal-da8a700a2d95.herokuapp.com/)

# Contents
- [Introduction](#introduction)
- [Manual Testing](#manual-testing)
- [Browser Testing](#brower-testing)
- [Google Sheets Testing](#google-sheets-testing)
- [Future Updates](#future-updates)

## Introduction 

Once the portal was up and running with functionality, I began testing it for any potential and obscure errors so that in the event of catching any I was able to fix them.

I went into the Railway Inn to speak with the manager and go through the employee portal with him. We tested it by implementing the current employees into the portal, and we then calculated their gross pay using the relevent options. One issue that we found is that due to the way the code has been written when retrieving the index values from the database, the last employee on the spreadsheet is not calculated. I fixed this within the code through adding +1 to the index values. 

## Manual Testing

The following tests were carried out to ensure that the Employee Portal was working correctly

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Select Option A | Entered 'A' | Displayed Create New Employee | Worked as expected | 
| Select Option B | Entered 'B' | Displayed Display Employee | Worked as expected |
| Select Option C | Entered 'C' | Displayed Calculate Pay | Worked as expected | 
| Select Option | Entered 'D' | Raise Value Error | Worked as expected |
| Select Option | Entered '1' | Raise Value Error | Worked as expected |
| Name Input | Entered 'Cam' | Accepted Input | Worked as expected |
| Name Input | Entered number & special character | Raise Value Error | Worked as expected |
| Hour/Wage Input | Entered number | Accepted Input | Worked as expected |
| Hour/Wage Input | Entered letter & special character | Raise Value Error | Worked as expected |
| Review Input | Entered 'Y'/'N' | Displayed relevent outcome | Worked as expected |
| Review Input | Entered other letter, number, space & special character | Raise Value Error | Worked as Expected |
| Push to Google Sheets | Submitted Employee Details | Appended row in Google Sheets | Worked as expected |
| Return to Main Menu | Entered 'Y'/'N' | Displayed Relevent Outcome | Worked as expected |
| Return to Main Menu | Entered other letter, number, space & special character | Raise Value Error | Worked as Expected |
| Exit Application | Entered 'Y'/'N' | Displayed Relevent Outcome | Worked as expected |
| Ext Application | Entered other letter, number, space & special character | Raise Value Error | Worked as Expected |
| Try Again Input | Entered 'Y'/'N' | Displayed Relevent Outcome | Worked as expected |
| Try Again Input | Entered other letter, number, space & special character | Raise Value Error | Worked as Expected |
| Display Employee Pay Details | Enter relevent info | Displayed employee pay details | Worked as expected |
| Hours Confirmation | Entered 'Y'/'N' | Displayed Relevent Outcome | Worked as expected |
| Hours Confirmation | Entered other letter, number, space & special character | Raise Value Error | Worked as Expected |
| Push Pay Data | Submitted Employee Pay Details | Appended row to Google Sheet | Worked as expected |

## Brower Testing

The Employee Portal was tested in the following browsers:

| Browser | Action | Expected Result | Actual Result | Pass |
| ------- | ------ | --------------- | ------------- | ---- |
| Chrome | Select Option B | Show display Employee | ![A screenshot of the test in Google Chrome browser](assets/images/google-chrome-ss.png) | Y |
| Safari | Select Option A | Show Create Employee | ![A screenshot of the test in Safari browser](assets/images/safari-ss.png) | N - Employee Portal in unresponsive in Safari |
| Firefox | Select Option C | Show Calculate Employee Pay | ![A screenshot of the tes in a Firefox browser](assets/images/firefox-ss.png) | Y |
| Edge | Select Option A | Show Create Employee | ![A screenshot of the test in a Microsoft Edge browser](assets/images/edge-ss.png) | Y |

## Google Sheets Testing

## Future Updates

