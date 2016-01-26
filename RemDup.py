import 


def monitor_file:
    cmd = "tail -f -n 0 /var/log/syslog"
    
    pipe = os.popen(cmd)
    while True:
        line = pipe.readline().strip()
        m = i.search(line) 





lines_seen = set() # holds lines already seen
outfile = open(outfilename, "w")
for line in open(infilename, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()



