import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    docid = record[0]
    words = record[1].split()
    for w in words:
      mr.emit_intermediate(w, docid)

def reducer(key, list_of_values):
    # key: word
    # value: list of document ids
    mr.emit((key, list(set(list_of_values))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
