import json

print("Hello World")

# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xfa in position 6225: invalid start byte 
dict_access=[]
f = open('/Users/dhrumilgohil/Desktop/Python/access.log', "r")

for line in f:
    splitline = line.split()
    tempdict = {}
    tempdict["client's IP address"] = splitline[0]
    tempdict["remote user"] = splitline[1] + "  " + splitline[2]
    tempdict["timestamp"] = splitline[3] + " " + splitline[4]
    tempdict["HTTP Method"] = splitline[5][1:]
    tempdict["Requested resource"] = splitline[6]
    tempdict["HTTP version"] = splitline[7][:-1]
    tempdict["Response code"] = splitline[8]
    tempdict["size(bytes)"] = splitline[9]
    tempdict["Referer"] = splitline[10][1:-1]
    tempdict["User Agent"] = str(splitline[11][1:-1]) + " "  + str((splitline[12:]))

    dict_access.append(tempdict)




out_file = open("test-access.json", "w")
jsonfile = json.dump(dict_access, out_file, indent=2)

dict_error = []
f = open('/Users/dhrumilgohil/Desktop/Python/error.log', "r", errors='ignore')

for line in f:
    splitline = line.split(",")
    tempdict = {}

    splitsp1=splitline[0].split()
    tempdict["timestamp"] = splitsp1[0] + " " + splitsp1[1]
    tempdict["Level"] = splitsp1[2] 
    tempdict["identifier"] = splitsp1[3] + " " + splitsp1[4]
    tempdict["Error"] = " ".join(splitsp1[5:])

    if(splitline[0].find("limiting requests") > 0):

        splitsp1=splitline[1].split(":")
        tempdict["excess"] = splitsp1[1]

        splitsp2=splitline[2].split(":")
        tempdict["client"] = splitsp2[1]

        splitsp3=splitline[3].split(":")
        tempdict["server"] = splitsp3[1]

        splitsp4=splitline[4].split(":")
        splitsubsp4=splitsp4[1].split()
        tempdict["Respponse Code"] = splitsubsp4[0]
        tempdict["request"] = splitsubsp4[1]
        tempdict["HTTP Version"] = splitsubsp4[2]

        splitsp5=splitline[5].split(":")
        tempdict["host"] = splitsp5[1]

        if(len(splitline) > 6):
            splitsp6=splitline[6].split(":")
            tempdict["referrer"] = splitsp6[1]

    elif(splitline[0].find("FastCGI sent in stderr") > 0): 

        splitsp1=splitline[1].split(":")
        tempdict["client"] = splitsp1[1]

        splitsp2=splitline[2].split(":")
        tempdict["server"] = splitsp2[1]

        splitsp3=splitline[3].split(":")
        splitsubsp3=splitsp3[1].split()
        tempdict["Respponse Code"] = splitsubsp3[0]
        tempdict["request"] = splitsubsp3[1]
        tempdict["HTTP Version"] = splitsubsp3[2]

        splitsp4=splitline[4].split(": ")
        tempdict["upstream"] = " ".join(splitsp4[1:])

        splitsp5=splitline[5].split(":")
        tempdict["host"] = splitsp5[1]

        if(len(splitline) > 6):
            splitsp6=splitline[6].split(":")
            tempdict["referrer"] = splitsp6[1]
    else:
        splitsp1=splitline[1].split(":")
        tempdict["client"] = splitsp1[1]

        splitsp2=splitline[2].split(":")
        tempdict["server"] = splitsp2[1]

        splitsp3=splitline[3].split(":")
        tempdict["request"] = splitsp3[1]

        splitsp4=splitline[4].split(":")
        tempdict["host"] = splitsp4[1] 
 
    dict_error.append(tempdict)

out_file = open("test-error.json", "w")
jsonfile = json.dump(dict_error, out_file, indent=2)

with open('test-access.json','r') as f:
    data = json.load(f)

#200
SUCCESS=0

#301
MOVED_PERMANENTLY=0

#403
FORBIDDEN=0

#404
NOT_FOUND=0

#302
FOUND=0

TOTAL_GET=0
TOTAL_POST=0

for line in data:
    if(line["Response code"] == "200"):
        SUCCESS=SUCCESS+1
    elif(line["Response code"] == "403"):
        FORBIDDEN=FORBIDDEN+1
    elif(line["Response code"] == "404"):
        NOT_FOUND=NOT_FOUND+1
    elif(line["Response code"] == "302"):
        FOUND=FOUND+1
    elif(line["Response code"] == "301"):
        MOVED_PERMANENTLY=MOVED_PERMANENTLY+1
   
    if(line["HTTP Method"] == "GET"):
        TOTAL_GET = TOTAL_GET + 1
    elif(line["HTTP Method"] == "POST"):
        TOTAL_POST = TOTAL_POST + 1

print("-------- Analysis of Access file -----------")
print("Total Get Request " + str(TOTAL_GET))
print("Total POST Request: " + str(TOTAL_POST))

print("Total Success Request: " + str(SUCCESS))
print("Total Moved Request: " + str(MOVED_PERMANENTLY))
print("Total Forbidden Request: " + str(FORBIDDEN))
print("Total Status not found Request: " + str(NOT_FOUND))
print("Total FOUND Request: " + str(FOUND))
