# Write your solution here, DO NOT START A NEW PROJECT
# ATTENTION: if you create a new project, your exam paper will not be collected
#            and you will be obliged to come in the subsequent exam session
#
# ATTENTION: on Win 10 (Italian keyboard) characters like [ ] { } have to be
#            created using ALTgr+è (e.g. for [ ) and NOT CTRL-ALT-è
#
# ATTENTION: on macOS you have to use CTRL-C and CTRL-V inside the virtual
#            machine and NOT command-C command-V
#
# if your keyboard is broken you can do copy/paste also with mouse
# and you can copy special characters like [ ] { } < > here
#
# print(string.punctuation)
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~

infile = open("timezones.lst","r")

info = list()
for line in infile:
    line = line.rstrip()
    listOfInfo = line.split()
    cleanListOfInfo = list()
    cleanListOfInfo.append(listOfInfo[0].rstrip(":"))
    offset = listOfInfo[1][3:]
    if offset[0]=="+":
        if ":" not in offset:
            offset = int(offset[1:])*60
        else:
            hour = int(offset[1 : offset.index(":") ])
            minute = int(offset[offset.index(":")+1 : ])
            offset = hour*60 + minute
    elif offset[0]=="-":
        if ":" not in offset:
            offset = int(offset[1:])*60
        else:
            hour = int(offset[1 : offset.index(":") ])
            minute = int(offset[offset.index(":")+1 : ])
            offset = hour*60 + minute
        offset *= -1 
    cleanListOfInfo.append(offset)
    info.append(cleanListOfInfo)
infile.close()
#print(info)

infile = open("today.lst","r")
times = list()
for line in infile:
    line = line.rstrip()
    listOfInfo = line.split("\"")
    listOfInfo.pop(2)
    timing = listOfInfo[0].split()
    hour = int(timing[0][:timing[0].index(":")])
    minute = int(timing[0][timing[0].index(":")+1:])
    cleanListOfInfo = list()
    cleanListOfInfo.append(hour*60+minute)
    cleanListOfInfo.append(timing[1])
    cleanListOfInfo.append(listOfInfo[1])
    times.append(cleanListOfInfo)
infile.close()
#print(times)

for message in times:
    flag = False
    for timeInfo in info:
        if message[1] == timeInfo[0]:
            flag = True
            newTime = message[0] - timeInfo[1]
            if newTime < 0:
                print(f"Yesterday {24+(newTime//60):02d}:{newTime%60:02d} {message[2]}")
            elif newTime > 24*60:
                print(f"Tomorrow {(newTime//60)-24:02d}:{newTime%60:02d} {message[2]}")
            else:
                print(f"Today {newTime//60:02d}:{newTime%60:02d} {message[2]}")
    if flag == False:
        print(f"Help: no info about this zone {message[1]}")    
            
