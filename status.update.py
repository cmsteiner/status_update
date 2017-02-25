#!python3
# status_update.py
import os, subprocess, sys, csv, pprint

scriptPath = 'C:\\Users\\Csteiner\\Documents\\status_update'
scriptTF = 'status.cli'     # CLI script to get updates from TeamForge
inFile = 'artf_list.csv'    # list of artifacts to check in csv format
outFile = 'artf_out.csv'    # output file for the TF CLI script
wikiTab = 'wiki_table.txt'  # reformatted output file into wiki tables
wikiFile = 'Automation_project_wiki.txt'    # text file of project wiki with formatting
colHead = ['||Artifact','||Title','||Status','||Assigned To','||Last Modified By','||Last Modified Date']

# Check if current working directory is correct, and if not go to correct directory
if os.getcwd() != scriptPath:
    os.chdir(scriptPath)

# Check if the TF CLI output file already exists, and if so remove it    
if os.path.exists(outFile):
    try:
        os.remove(outFile)
    except OSError as e:
        print("Error: %s - %s." % (e.filename,e.strerror))

# TODO: Generate the list of artifacts?

# Run the TF CLI script to generate the outFile
subprocess.run(['ctf', '--script', scriptTF, inFile, outFile])

# Open outFile and read into a list of lists
with open(outFile, 'r') as f:
    reader = csv.reader(f)
    tabList = list(reader)

# Set up new list of lists to use for formatted data
tabFormat = []
for i in range(len(tabList)):
    tabFormat.append([])

# Insert pipe character in front of each item in each list
n = 0
for r in tabList:
    for i in r:
        tabFormat[n].append(''.join(['|',i]))
    n += 1

# Update column headers 
tabFormat[0] = colHead
jrList = []
for r in tabFormat:
    jrList.append(''.join(r))
#pprint.pprint(jrList)    

finText = '\n'.join(jrList)
#print(finText)

# TODO: Write out to wikiTab
with open(wikiTab, 'w') as f:
    f.write(finText)

# Possible future enhancements - sort artifact rows by status; divide into different tables based on status or other criteria;
#                                edit actual wiki text file and insert tables