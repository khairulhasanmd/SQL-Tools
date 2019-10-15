f = open('export.sql', "r")
lines = f.readlines()

found_some_statement = 0;

fk_file = open("fk_extracted.sql","w+")

for line in lines:
    if "ALTER TABLE" in line:
        found_some_statement = 1
    if found_some_statement == 1:
        #print line
        fk_file.write(line)
    if ";" in line:
        found_some_statement = 0

print "done"
    
