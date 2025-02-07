# Manage and control the backend of the application.
# Includes the data handling
# Author: Toni Dahlitz
# Date: 2025-02-07
# Version: 0.1

import database

def main():
    database.create_table()
 #Das funktioniert  database.insert_data('2025-02-07', 0.5, 0.00, 'Comment')
    database.show_data()

if __name__ == '__main__':
    main()

