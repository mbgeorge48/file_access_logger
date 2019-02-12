import os
import sys
import time
import csv


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()

    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def getKey(item):
    return item[2]


if len(sys.argv) == 1:
    print("You need to provide a path to scan")
    sys.exit()
else:
    path = sys.argv[1]

allFiles = getListOfFiles(path)

all_file_details = []

for file in allFiles:
    file_stats = []
    file_stats.append(file)
    file_stats.append(time.ctime(os.stat(file).st_atime))
    file_stats.append(os.stat(file).st_atime)
    all_file_details.append(file_stats)

sorted_file_list = sorted(all_file_details, key=getKey)

with open("file_use.csv", "w+") as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerows(sorted_file_list)
