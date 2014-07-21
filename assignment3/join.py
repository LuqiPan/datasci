import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    mr.emit_intermediate(record[1], record)

def reducer(key, list_of_records):
    line_items = [r for r in list_of_records if r[0] == "line_item"]
    orders = [r for r in list_of_records if r[0] == "order"]
    results = ([(o + li) for li in line_items for o in orders])
    for r in results:
        mr.emit(r)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
