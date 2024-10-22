import webbrowser
import urllib.parse  # To encode the query for the URL
import requests  # For handling HTTP requests to GitHub's API

# Function to check for updates using GitHub API
def check_for_updates(current_version):
    """Check if there's a new version of the program on GitHub releases."""
    url = "https://api.github.com/repos/lPElnagar/GDmaker/releases/latest"
    try:
        response = requests.get(url)
        data = response.json()
        latest_version = data['tag_name']

        if latest_version != current_version:
            print(f"\nNew version available: {latest_version}")
            print("Would you like to update? (1- Yes, 2- No): ")
            choice = get_yes_no_choice("")
            if choice == "yes":
                download_url = data['assets'][0]['browser_download_url']
                print(f"Downloading from {download_url}...")
                webbrowser.open(download_url)
                print("Download started! Please install the latest version.")
            else:
                print("You chose not to update.")
        else:
            print("You already have the latest version.")

    except Exception as e:
        print(f"Error checking for updates: {e}")

# Function to get the user's choice for yes/no type questions
def get_yes_no_choice(prompt):
    """Get the user's choice for yes/no type questions with multiple input options."""
    choice = input(prompt).lower().strip()
    if choice in ["1", "yes", "y"]:
        return "yes"
    elif choice in ["2", "no", "n"]:
        return "no"
    else:
        return choice  # Return what they typed for cases we aren't handling

def google_dorks_search():
    print("GDorks Query Maker")
    print("© 2024 Loai Elnagar. All rights reserved.")
    
    # Current version of the program
    current_version = "v0.1"
    
    # Check for updates before starting the tool
    check_for_updates(current_version)

    while True:
        # User input for the main search query
        query = input("\nsearching about? (e.g., Loai Elnagar): ")

        # User input for the specific website (optional)
        site = input("website? (Enter the website or press Enter to skip): ")

        # User input for the file type (optional)
        filetype = input("filetype? (e.g., pdf, docx, xls) or press Enter to skip: ")

        # Ask if the user wants to see other options
        other_option_choice = get_yes_no_choice("\nWant to see other options? (1- Yes, 2- No): ")

        # Handle the additional input based on the user's choice
        additional_input = ""
        if other_option_choice == "yes":
            print("\nOther Google Dorks options:")
            print("1. intitle: Search for pages with a specific word in the title.")
            print("2. inurl: Search for URLs containing a specific keyword.")
            print("3. allintext: Search for pages containing every word following 'allintext:' in the text.")
            print("4. intext: Search for pages containing a specific word in the text.")
            print("5. link: Find pages that link to a specific URL.")
            print("6. cache: View Google's cached version of a website.")
            other_option = input("Choose an option (or press Enter to skip): ")

            if other_option == "1":
                additional_input = "intitle:" + input("Enter the word to search for in the title: ")
            elif other_option == "2":
                additional_input = "inurl:" + input("Enter the keyword to search for in the URL: ")
            elif other_option == "3":
                additional_input = "allintext:" + input("Enter the words to search for in the text: ")
            elif other_option == "4":
                additional_input = "intext:" + input("Enter the word to search for in the text: ")
            elif other_option == "5":
                additional_input = "link:" + input("Enter the URL to find pages linking to it: ")
            elif other_option == "6":
                additional_input = "cache:" + input("Enter the URL to view its cached version: ")

        # Constructing the Google Dorks query
        dork_query = f'"{query}"'
        if site:
            dork_query += f" site:{site}"
        if filetype:
            dork_query += f" filetype:{filetype}"
        if additional_input:
            dork_query += f" {additional_input}"

        # Output the final query
        print("\nQuery is:")
        print(dork_query)

        # Encode the query for a Google search URL
        encoded_query = urllib.parse.quote(dork_query)
        search_url = f"https://www.google.com/search?q={encoded_query}"

        # Automatically open the default browser and search the query
        webbrowser.open(search_url)

        # Ask the user if they want to perform another search or exit
        continue_choice = get_yes_no_choice("\nAnother query? (1- Yes, 2- No): ")
        if continue_choice != "yes":
            print("EL-Salamo3lekm")
            break

# Run the program
google_dorks_search()
