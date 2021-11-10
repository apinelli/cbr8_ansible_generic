import os

curr_dir = os.getcwd()
report_dir = os.path.join(curr_dir, 'REPORTS')

for filename in os.listdir(report_dir):
    with open(os.path.join(report_dir, filename), 'r') as f:
      with open(os.path.join(report_dir, 'results'), 'a') as f2:
        for i in f:
           print('\n', file=f2)
           print(filename, file=f2)
           i2 = i[2:-2]
           l = list(i2.split(','))
           for syslogs in l:
             print(syslogs, file=f2)

