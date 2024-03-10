import csv
from application import db
from application import application
from models.pluto import PLUTO

def import_csv(csv_file):
    with application.app_context(): # Need to create application context to be able to run database operations
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file) # Using DictReader for column names
            # next(reader)  # Skip the header row

            # row_counter = 0  # Initialize a counter for rows
            for row in reader:
                # if row_counter < 10:  # Process only the first 10 rows
                try:
                    processed_row = [
                        row['postcode'],
                        row['address'],
                        row['unitsres'],
                        row['unitstotal'],
                        row['yearbuilt'],
                        int(row['bbl']),
                        row['latitude'],
                        row['longitude'],
                        row['version'],
                    ]

                    # Create a new PLUTO object with processed row data
                    pluto_entry = PLUTO(*processed_row)
                    db.session.add(pluto_entry)

                # Error handling for conversion failure
                except ValueError:
                    print(f"Error converting row {row_counter}")

                #     row_counter += 1  # Increment the row counter
                # else:
                #     break  # Stop processing after 5 rows

            db.session.commit()

import_csv('seeds/Primary_Land_Use_Tax_Lot_Output__PLUTO__20240308.csv')
