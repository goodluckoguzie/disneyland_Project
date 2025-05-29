# tui.py
# All the print()/input() helpers live here.

def display_main_menu():
    print("Main Menu:")
    print("A. View Data")
    print("B. Visualise Data")
    print("Q. Quit")
    choice = input("Your choice: ").strip().upper()
    print(f"You chose: {choice}\n")
    return choice

def display_view_menu():
    print("View Data Menu:")
    print("1. All reviews for a park")
    print("2. Count reviews by park & location")
    print("3. Average rating for park in a year")
    print("4. Average score per park by reviewer location")
    print("Q. Back")
    choice = input("Your choice: ").strip().upper()
    print(f"You chose: {choice}\n")
    return choice

def display_visual_menu():
    print("Visualise Data Menu:")
    print("1. Pie: reviews per park")
    print("2. Bar: average score per park")
    print("3. Bar: top-10 locations for a park")
    print("4. Bar: monthly average for a park")
    print("Q. Back")
    choice = input("Your choice: ").strip().upper()
    print(f"You chose: {choice}\n")
    return choice

def print_reviews(rows):
    if not rows:
        print("No reviews found.\n")
    for r in rows:
        print(f"{r['Year_Month']} | {r['Reviewer_Location']} | {r['Rating']}/5")
        print(" ", r['Review'], "\n")

def print_matrix(matrix):
    for park, locs in matrix.items():
        print(park + ":")
        for loc, avg in locs.items():
            print(f"  {loc}: {avg:.2f}")
    print()
