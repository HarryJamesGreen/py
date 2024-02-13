import sys, sqlite3

def usage():
    print("[-] Incorrect arguments...")
    print("Usage: ", sys.argv[0], "<database> <table>")
    sys.exit()

if len(sys.argv) != 3:
    usage()

tgtBase = sys.argv[1]
tgtTbl = sys.argv[2]

conn = sqlite3.connect(tgtBase)
c = conn.cursor()
result = c.execute("SELECT * FROM " + tgtTbl + ";")

for row in result:
    print(', '.join(map(str, row)))

conn.close()
