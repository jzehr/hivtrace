


'''
-- will it be useful to add keyword-only args to pass to functions?
    - as in set them to false and then from the config depending 
    on what the user wants to run set them to true? using some 
    logic switches?



this file will be used as a place to make face 
functions and then test them in the snakefile 
'''

def tester(input, output):
    print(input)
    print(output)
    infile = str(input)
    outfile = str(output)
    with open(outfile, 'w') as out_f:
        with open(infile,'r') as fh:
            for line in fh:
                out_f.write(line)



'''
the tn93 stuff all has stdout and stderr going to the same folder
- do we want it to break at this point if there is nothing in 
    the file?? 
'''