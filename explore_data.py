"""
 Exploring The Data:
 - Load the csv file and stored into an array or data frame
 - list all columns in the dataset and offer the user the possibility of drop 
   any of them.
 - Count distinct values of any column selected by the user.
 - Search any value in any column as input by the user.
 - Sort any columns (Ascending or descending) as selected by the user.
 - Print the first 100, 1000 or 5000 rows of the dataset as selected by the 
   user.
"""

data = {}                   # Dictionary that stores cols with values.
column_to_id_mapping = {}   # Column ids mapped to their 'actual' names.

# Pre process's csv data to be stored in a global dictionary.
def pre_processor():
    print('Processing data...')   # Indicate that data is loading.
    with open('data.csv') as fp:
        line = fp.readline()

        flag = 0
        # Only process 500000 rows.
        while line and flag < 500000:
            line = line.replace('\n', '')
            cols = line.split(',')

            # Get header and break them to column names.
            if flag == 0:
                for col in cols:
                    data[col] = []

            else: 
                idx = 0
                # Append each value to their columns.
                for key in data:
                    data[key].append(cols[idx]) 
                    idx += 1

            line = fp.readline()
            flag += 1

pre_processor()

# Maps column names to their ids.
# Example: 
#   columns 'MONTH' is mapped to 1.
def map_col_to_ids():
    print('Columns available:')

    for col in data:
        col_id = list(data).index(col) + 1
        column_to_id_mapping[col_id] = col
        print(col_id, ':', col)

map_col_to_ids()

# Shows all available columns.
def show_columns():
    for col_id in column_to_id_mapping:
        print(col_id, ':', column_to_id_mapping[col_id])

# Drops any column from data dictionary.
def drop_column(col_id_to_drop):
    col = column_to_id_mapping[col_id_to_drop]
    data.pop(col)
    column_to_id_mapping.pop(col_id_to_drop)

    # Show available columns after deletion.
    show_columns()

# Asks users to drop any column.
def drop_inquiry():
    # TODO(eidmonetagaca): Implement error handling for any input errors.
    while 1:
        print('Choose number to drop column: \n')
        drop_col = input('Enter a number: ')

        drop_column(int(drop_col))

drop_inquiry()

# TODO(eidmonetagaca): Implement count, search, sort, and selection of top N 
# values.