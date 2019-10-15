f = open('export.sql', "r")
lines = f.readlines()

found_some_statement = 0;

insert_into_file = open("insert_into_extracted.sql","w+")

for line in lines:
    if "INSERT INTO" in line:
        found_some_statement = 1
    if found_some_statement == 1:
        #print line
        insert_into_file.write(line)
    if ");" in line:
        found_some_statement = 0

print "done"
    
