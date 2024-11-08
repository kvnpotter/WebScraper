# Imports

from WebScraperPackage import (get_cookie, get_first_paragraph, get_leaders)
from WebScraperPackage import save

# Main program

def main() :
    leader_dict = get_leaders()
    save(leader_dict)

if __name__ == '__main__':
    print("Running program, getting leaders, scraping Wikipedia.")
    main()