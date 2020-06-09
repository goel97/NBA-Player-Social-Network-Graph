lines_seen = set() # holds lines already seen
outfile = open("out.txt", "w")
for line in open("foo_Out.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()