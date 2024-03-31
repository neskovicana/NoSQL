import csv
import json
import re

def extract_title_and_year(title):
    pattern = r'^(.*?) \((\d{4})\)$'
    match = re.match(pattern, title)
    if match:
        return match.group(1), int(match.group(2))
    else:
        return None, None

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title, year = extract_title_and_year(row['Title'])
            data.append({
                'Rank': int(row['Rank']),
                'Title': {
                    'name': title,
                    'year': year
                },
                'RatingTomatometer': int(row['RatingTomatometer']),
                'No. of Reviews': int(row['No. of Reviews']),
                'Genres': row['Genres'].split('|')
            })

    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

csv_to_json('rotten_tomatoes_top_movies_2019-01-15.csv', 'movies.json')
