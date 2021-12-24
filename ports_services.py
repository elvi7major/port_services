import csv
import sys

if len(sys.argv) <=1 :
    print("Usage: python",sys.argv[0],"port number")
    print("Ex: python",sys.argv[0],"80")
else:
    reader = csv.reader(open('service-names-port-numbers.csv','r'))
    headers = []
    headers = next(reader)
    rows = [x for x in reader]
    lis = [x for x in rows if x[1] == str(sys.argv[1])]
    print(headers[1],headers[0],headers[2],headers[3])
    for i in lis:
        print(i[1],'\t   ',i[0],'\t',i[2],'\t  ',i[3])