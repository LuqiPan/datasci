import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    if record[0] == "a":
        for i in range(5):
            mr.emit_intermediate((record[1], i), record)

    if record[0] == "b":
        for i in range(5):
            mr.emit_intermediate((i, record[2]), record)

def reducer(key, list_of_records):
    a_s = [r for r in list_of_records if r[0] == "a"]
    b_s = [r for r in list_of_records if r[0] == "b"]
    i = key[0]
    j = key[1]
    results = [a[3] * b[3] for a in a_s for b in b_s if a[2] == b[1]]
    mr.emit((i, j, sum(results)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
