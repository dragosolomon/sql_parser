import glob, os, datetime, sys,  getopt

argv =sys.argv[1:]

path = "p:"

opt, arg = getopt.getopt(argv, path)

# print(arg)

exit_file = "procedures_list_" +str(datetime.date.today())+".txt"
f = open(exit_file, "a")
os.chdir(arg[0])

for file in glob.glob("*.sql"):
    with open(file, 'r') as file1:
         for line in file1:
            if "ALTER PROCEDURE " in line:
                line_1 = line.replace("ALTER PROCEDURE ", '')
                f.write(line_1)


            if "CREATE PROCEDURE" in line:
                line_2 = line.replace("CREATE PROCEDURE ", '')
                f.write(line_2)