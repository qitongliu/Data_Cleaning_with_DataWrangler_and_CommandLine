import csv
with open('2013films_clean.csv') as filmfile:
    films = csv.DictReader(filmfile)
    production = {}
    for film in films:
        film_prods = film[' Production'].split('/')
        for film_prod in film_prods:
            film_prod = film_prod.strip(' ')
            if film_prod in production:
                production[film_prod] += 1
            else:
                production[film_prod] = 1
print sorted(production, key=production.get, reverse=True)[0]