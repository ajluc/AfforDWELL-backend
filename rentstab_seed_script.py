import csv
from application import db
from application import application
from models.rent_stab import RentStab

def import_csv(csv_file):
    with application.app_context(): # Need to create application context to be able to run database operations
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            # row_counter = 0  # Initialize a counter for rows
            for row in reader:
                # if row_counter < 10:  # Process only the first 10 rows
                processed_row = []
                for item in row:
                    processed_row.append(None if item == "NA" else item)

                # Convert bbl columns to integer
                if processed_row[0] is not None:
                    processed_row[0] = int(processed_row[0])

                # Create a new RentStab object with processed row data
                rent_stab_entry = RentStab(*processed_row)
                db.session.add(rent_stab_entry)

                #     row_counter += 1  # Increment the row counter
                # else:
                #     break  # Stop processing after 5 rows

            db.session.commit()

import_csv('seeds/rentstab_counts_from_doffer_2021.csv')
