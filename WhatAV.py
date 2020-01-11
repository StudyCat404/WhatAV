# coding : utf-8

import json
import re
import argparse

def logo():
    print("""
  _____ _             _        _____      _   
 / ____| |           | |      / ____|    | |  
| (___ | |_ _   _  __| |_   _| |     __ _| |_ 
 \___ \| __| | | |/ _` | | | | |    / _` | __|
 ____) | |_| |_| | (_| | |_| | |___| (_| | |_ 
|_____/ \__|\__,_|\__,_|\__, |\_____\__,_|\__|
                         __/ |                
                        |___/     
                        
             https://www.cnblogs.com/StudyCat/  
             
    """)

def loadApps(file):
    try:
        with open(file,"r",encoding='utf-8') as f:
            contents = f.read()
            return json.loads(contents)
    except Exception as e:
        print(e)
        return
        
def parseTasklist(file):
    with open(file,"r") as f:
        output = f.read()
    if output:
        result = pattern.findall(output)
        if result:
            return result
    return         
        
def whatAV(task):
    for av in apps.keys():
        for process in apps[av]["processes"]:
            if process.lower() == task.lower():
                return (av,process,apps[av]["url"])
    return
    
def get_args():
    global args
    
    parser = argparse.ArgumentParser('sameIP.py', formatter_class=lambda prog:argparse.HelpFormatter(prog,max_help_position=40))
    parser.add_argument('-f', '--file', help='File containing tasklist output', dest='file', required=False)
    parser.add_argument('-p', '--process', help='Process name', dest='process', required=False)
    args = parser.parse_args()       
        
def main():
    global apps,pattern 
    detected = False
    apps = loadApps("av.json")

    if args.file:
        pattern = re.compile(".+\.exe",re.I)
        tasklist = parseTasklist(args.file)
        
        if tasklist:
            tasklist = list(set(tasklist))
            for task in tasklist:
                res = whatAV(task)
                if res:
                    detected = True
                    print("Antivirus: %s\tProcess: %s\tURL: %s" % (res[0],res[1],res[2]))
                    
    if args.process: 
        res = whatAV(args.process)
        if res:
            detected = True
            print("Antivirus: %s\tProcess: %s\tURL: %s" % (res[0],res[1],res[2]))        
                    
    if not detected:
        print("No Antivirus found")
        
if __name__ == "__main__":
    logo()
    get_args()
    main()        