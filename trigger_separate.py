f = open('export.sql', "r")
lines = f.readlines()

found_some_statement = 0;

trigger_file = open("trigger_extracted.sql","w+")

for line in lines:
    if "DROP TRIGGER IF EXISTS" in line:
        found_some_statement = 1
    if found_some_statement == 1:
        #print line
        trigger_file.write(line)
    if ";" in line:
        found_some_statement = 0

print "done"
    
