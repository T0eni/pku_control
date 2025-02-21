# Manage and control the backend of the application.
# Includes the data handling
# Author: Toni Dahlitz
# Date: 2025-02-21
# Version: 0.1

import backend.database as database

def main():
    database.create_table()
    database.insert_data()
    database.show_data()

if __name__ == '__main__':
    main()

