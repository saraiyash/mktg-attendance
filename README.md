# mktg-attendance
Automated attendance for Zoom meetings

# Process
1. Create a Roster file (see more info below) and place it in the /roster folder
2. Create a /zoom folder with all the Zoom meeting details extracts in it
3. Check the naming conventions
4. Run attendance-reader.py for these set files
5. This will update the /roster files and VOILA!

# Roster File
Roster files are student-centric XLSX files. For an Excel file, the first column would have the student name (NAME), and the consequent columns will be the days for which attendance is to be marked. Please ensure that the format of the dates are in the right format.
Right now, the date formats are as follows: 1/26/2021  12:00:00 AM

Also, ensure the roster files are included in the code before running it. Right now, only the 3 sections: 500.xlsx, 599.xlsx, 600.xlsx are present in the code as well as in the folders.

# Zoom Extract
The Zoom extracts are to be named as: 

(Section No)_(MonthDate) -- e.g. 500_Feb, 500_Jan28, etc.

The Zoom extracts will have columns such as name, join time, leave time, etc. However, for this sample, we have only used the name column.

For more information, you can get in touch with me at saraiyash@tamu.edu
