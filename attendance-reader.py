import pandas as pd
import datetime
import os

def convert_col_to_index(roster, date):
    for column in roster.columns[1:]:
        col = datetime.datetime.strptime(str(column), "%Y-%m-%d %H:%M:%S")
        col = datetime.datetime.strftime(col, "%b%d")
        col = col.replace("0", "")
#         print(date, column)
        if date in col:
#             print("yes")
            return int(list(roster.columns).index(column))
#     if column in dates:
#         print(column)


def mark_attendance(sections, dates):
    sections = ["500", "599", "600"]
    dates = ["Jan26", "Jan28", "Feb2"]
    
    for section in sections:
        for date in dates:
            zoom = pd.read_csv("zoom/"+section+"_"+date+".csv")
            zoom = zoom.sort_values(by=[zoom.columns[0]])
            roster = pd.read_excel("roster/"+section+".xlsx")
            for indx in roster.index:
                for present in zoom.iloc[:,0]:
                    if roster.iloc[indx, 0].split()[0].replace(",", "") in present:
                        colindx = convert_col_to_index(roster, date)
                        try:
                            roster.iloc[indx, colindx] = "P"
                        except:
                            print(date, indx, colindx, sep="\n")
            roster.to_excel("roster/"+section+".xlsx", index=False)

# try:
zoom_entries = os.scandir('zoom/')
zoom_files = [(entry.name).split(".")[0] for entry in zoom_entries]

# roster_entries = os.scandir('roster/')
# roster_files = [(entry.name).split(".")[0] for entry in roster_entries]
# sections = roster_files

sections = [file.split("_")[0] for file in zoom_files]
sections = list(set(sections))

dates = [file.split("_")[1] for file in zoom_files]
dates = list(set(dates))

print(sections, dates, sep="\n\n")

mark_attendance(sections, dates)


