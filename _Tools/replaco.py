files = ["News", "Pictures", "Videos"]
for name in files:
    #input file
    fin = open(f"../{name}/index.html", "rt")
    #output file to write the result to
    fout = open(f"../home/{name}/index.html", "wt")
    #for each line in the input file
    for line in fin:
        #read replace the string and write to output file
        fout.write(line)
    #close input and output files
    fin.close()
    fout.close()
