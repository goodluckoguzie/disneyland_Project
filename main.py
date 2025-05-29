# main.py
# This is the main entry point of the Disneyland Reviews program.
# It starts the program, loads data, displays menus, and acts based on user choices.

import tui      # Module for Text-based User Interface (menus and display functions)
import process  # Module for processing and analyzing data
import visual   # Module for generating visualizations

def main():
    # 2. Read data from a CSV file into a list of dictionaries (one per review)
    # and tell the user how many rows were loaded.
    reviews = process.load_data('data/Disneyland_reviews.csv')
    print(f"\nLoaded {len(reviews)} rows.\n")  # Feedback to user

    while True:
        # 3. Display the main menu and get user's choice (A: view, B: visuals, Q: quit)
        choice = tui.display_main_menu()

        # 4. Check user's menu choice and act accordingly
        if choice == 'A':
            handle_view_menu(reviews)  # Go to submenu for viewing/filtering data
        elif choice == 'B':
            handle_visual_menu(reviews)  # Go to submenu for data visualizations
        elif choice == 'Q':
            print("Goodbye!")  # Exit the program
            break
        else:
            print("Invalid choice—please try again.\n")  # Handle invalid input

# Function to handle the view menu (text-based analysis options)
def handle_view_menu(reviews):
    while True:
        # Display the view menu and get user's choice
        choice = tui.display_view_menu()

        if choice == '1':
            # Filter reviews by park name entered by user
            park = input("Which park? ").strip()
            rows = process.filter_by_park(reviews, park)
            tui.print_reviews(rows)  # Display the filtered reviews

        elif choice == '2':
            # Count how many reviews are from a specific location for a given park
            park = input("Park name: ").strip()
            loc  = input("Reviewer location: ").strip()
            count = process.count_reviews(reviews, park, loc)
            print(f"\n{count} review(s) for {park} from {loc}.\n")  # Display count

        elif choice == '3':
            # Calculate average review score for a park in a specific year
            park = input("Park name: ").strip()
            year = input("Year (YYYY): ").strip()
            avg = process.average_for_year(reviews, park, year)
            print(f"\nAverage {park} in {year}: {avg:.2f}/5\n")  # Display average rating

        elif choice == '4':
            # Show average ratings by reviewer location in a matrix format
            matrix = process.average_by_location(reviews)
            tui.print_matrix(matrix)

        elif choice == 'Q':
            break  # Return to main menu
        else:
            print("Invalid choice—please try again.\n")  # Handle invalid input

# Function to handle the visual menu (graph-based visualizations)
def handle_visual_menu(reviews):
    while True:
        # Display the visualization menu and get user's choice
        choice = tui.display_visual_menu()

        if choice == '1':
            # Show a pie chart of review counts by park
            visual.pie_reviews(reviews)
        elif choice == '2':
            # Show a bar chart of average ratings for each park
            visual.bar_average_parks(reviews)
        elif choice == '3':
            # Show top locations (most reviews) for a specific park
            park = input("Which park? ").strip()
            visual.bar_top_locations(reviews, park)
        elif choice == '4':
            # Show a bar chart of average monthly ratings for a specific park
            park = input("Which park? ").strip()
            visual.bar_monthly_average(reviews, park)
        elif choice == 'Q':
            break  # Return to main menu
        else:
            print("Invalid choice—please try again.\n")  # Handle invalid input

# Entry point of the program
if __name__ == '__main__':
    main()
