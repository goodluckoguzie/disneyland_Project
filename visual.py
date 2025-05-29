# visual.py
# Draws charts with matplotlib

import matplotlib.pyplot as plt
from calendar import month_abbr
import process

def pie_reviews(rows):
    data = process.reviews_per_park(rows)
    labels = list(data.keys())
    sizes  = list(data.values())
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Reviews per park')
    plt.show()

def bar_average_parks(rows):
    data = process.average_score_per_park(rows)
    labels = list(data.keys())
    values = list(data.values())
    plt.bar(labels, values)
    plt.title('Average score per park')
    plt.ylabel('Rating')
    plt.show()

def bar_top_locations(rows, park):
    data = process.top_locations(rows, park)
    labels = [x[0] for x in data]
    values = [x[1] for x in data]
    plt.bar(labels, values)
    plt.title(f'Top-10 locations for {park}')
    plt.xticks(rotation=45, ha='right')
    plt.show()

def bar_monthly_average(rows, park):
    data = process.monthly_average(rows, park)
    months = [month_abbr[m] for m in range(1,13)]
    values = [data[m] for m in range(1,13)]
    plt.bar(months, values)
    plt.title(f'Monthly average for {park}')
    plt.ylabel('Rating')
    plt.show()
