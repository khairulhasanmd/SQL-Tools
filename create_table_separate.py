f = open('export.sql', "r")
lines = f.readlines()

found_some_statement = 0;

create_table_file = open("create_table_extracted.sql","w+")

for line in lines:
    if "CREATE TABLE" in line:
        found_some_statement = 1
    if found_some_statement == 1:
        #print line
        create_table_file.write(line)
    if ";" in line:
        found_some_statement = 0

print "done"
    
