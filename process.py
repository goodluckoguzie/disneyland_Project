# process.py
# All data work: load CSV, filter, count, average, etc.

import csv
from collections import defaultdict

def load_data(path):
    with open(path, encoding='utf-8') as f:
        return list(csv.DictReader(f))

def filter_by_park(rows, park_name):
    return [r for r in rows if r['Branch'] == park_name]

def count_reviews(rows, park_name, location):
    count = 0
    for r in rows:
        if r['Branch'] == park_name and r['Reviewer_Location'] == location:
            count += 1
    return count

def average_for_year(rows, park_name, year):
    total = 0
    count = 0
    for r in rows:
        if r['Branch'] == park_name and r['Year_Month'].startswith(year):
            total += int(r['Rating'])
            count += 1
    return total / count if count else 0

def average_by_location(rows):
    # { park: { location: avg_rating } }
    data = defaultdict(lambda: defaultdict(list))
    for r in rows:
        data[r['Branch']][r['Reviewer_Location']].append(int(r['Rating']))
    result = {}
    for park, locs in data.items():
        result[park] = {}
        for loc, ratings in locs.items():
            result[park][loc] = sum(ratings) / len(ratings)
    return result

# Helpers for visual.py
def reviews_per_park(rows):
    counts = defaultdict(int)
    for r in rows:
        counts[r['Branch']] += 1
    return counts

def average_score_per_park(rows):
    sums = defaultdict(int)
    counts = defaultdict(int)
    for r in rows:
        sums[r['Branch']] += int(r['Rating'])
        counts[r['Branch']] += 1
    return {park: sums[park] / counts[park] for park in sums}

def top_locations(rows, park_name):
    sums = defaultdict(int)
    counts = defaultdict(int)
    for r in rows:
        if r['Branch'] == park_name:
            loc = r['Reviewer_Location']
            sums[loc] += int(r['Rating'])
            counts[loc] += 1
    avgs = [(loc, sums[loc]/counts[loc]) for loc in sums]
    return sorted(avgs, key=lambda x: x[1], reverse=True)[:10]

def monthly_average(rows, park_name):
    sums = defaultdict(int)
    counts = defaultdict(int)
    for r in rows:
        if r['Branch'] == park_name:
            month = int(r['Year_Month'].split('-')[1])
            sums[month] += int(r['Rating'])
            counts[month] += 1
    return {m: (sums[m]/counts[m] if counts[m] else 0) for m in range(1,13)}
