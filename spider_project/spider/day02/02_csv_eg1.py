import csv

with open('test.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows([('步惊云','30'),('聂风','29'),('楚楚','28')])

with open('test.csv','a',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['步惊云','30'])
    writer.writerow(['聂风','29'])
    writer.writerow(['楚楚','28'])
