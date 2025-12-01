from math import *

# read sample files

#with open('data1.csv') as file1:
def read_csv_to_float_matrix(filename):
    with open(filename) as file:
        lines = file.readlines()
        data = []
        for line in lines:
            row = []
            for n in line.split(','):
                row.append(float(n.strip()))
            data.append(row)
    return data

data1 = read_csv_to_float_matrix('samples1.csv')
data2 = read_csv_to_float_matrix('samples2.csv')
w_matrix = read_csv_to_float_matrix('weights.csv')
w = w_matrix[0]

results = []
for i in range(len(data1)):
    s = 0
    for j in range(len(w)):
        d = data1[i][j] - data2[i][j]
        s += w[j] * abs(d)
    results.append(s)

# critical = 0
# for i in range(len(results)):
#     if results[i] > 5:
#         critical = critical + 1
# if critical == 1:
#     print("criticality: 1 result over 5")
# else:
#     print("criticality:", critical, "results over 5")
dsum =  0
for i in range(len(results)):
    dsum = dsum + results[i]
print("d-index:", dsum/len(results))
