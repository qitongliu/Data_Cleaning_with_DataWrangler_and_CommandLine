import csv
with open('worldcup_clean.csv') as cupfile:
    records = csv.DictReader(cupfile)
    won = {}
    for record in records:
        if record[' position'] == ' 1':
            country = record['country']
            if country in won:
                won[country] += 1
            else:
                won[country] = 1
for w in sorted(won, key=won.get, reverse=True):
    print w, won[w]