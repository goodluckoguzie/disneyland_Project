# main.py
# Starts the program, loads data, shows menus and acts on your choices.

import tui
import process
import visual

def main():
    # 2. Read data into a list and tell the user how many rows
    reviews = process.load_data('data/Disneyland_reviews.csv')
    print(f"\nLoaded {len(reviews)} rows.\n")

    while True:
        # 3. Show main menu (A, B, Q) and get choice
        choice = tui.display_main_menu()

        # 4. Echo and check choice
        if choice == 'A':
            handle_view_menu(reviews)
        elif choice == 'B':
            handle_visual_menu(reviews)
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice—please try again.\n")

def handle_view_menu(reviews):
    while True:
        choice = tui.display_view_menu()
        if choice == '1':
            park = input("Which park? ").strip()
            rows = process.filter_by_park(reviews, park)
            tui.print_reviews(rows)

        elif choice == '2':
            park = input("Park name: ").strip()
            loc  = input("Reviewer location: ").strip()
            count = process.count_reviews(reviews, park, loc)
            print(f"\n{count} review(s) for {park} from {loc}.\n")

        elif choice == '3':
            park = input("Park name: ").strip()
            year = input("Year (YYYY): ").strip()
            avg = process.average_for_year(reviews, park, year)
            print(f"\nAverage {park} in {year}: {avg:.2f}/5\n")

        elif choice == '4':
            matrix = process.average_by_location(reviews)
            tui.print_matrix(matrix)

        elif choice == 'Q':
            break
        else:
            print("Invalid choice—please try again.\n")

def handle_visual_menu(reviews):
    while True:
        choice = tui.display_visual_menu()
        if choice == '1':
            visual.pie_reviews(reviews)
        elif choice == '2':
            visual.bar_average_parks(reviews)
        elif choice == '3':
            park = input("Which park? ").strip()
            visual.bar_top_locations(reviews, park)
        elif choice == '4':
            park = input("Which park? ").strip()
            visual.bar_monthly_average(reviews, park)
        elif choice == 'Q':
            break
        else:
            print("Invalid choice—please try again.\n")

if __name__ == '__main__':
    main()
