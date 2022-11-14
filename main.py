import time

"""Exploring The Data:
 - Load the csv file and stored into an array or data frame [done]
 - list all columns in the dataset and offer the user the possibility of drop 
   any of them. [done]
 - Count distinct values of any column selected by the user.
 - Search any value in any column as input by the user.
 - Sort any columns (Ascending or descending) as selected by the user.
 - Print the first 100, 1000 or 5000 rows of the dataset as selected by the 
   user.
"""

"""Data Representation:

 columns_with_value: {
   MONTH: [val1, val2, val3, val4],
   DAY_OF_WEEK: [val1, val2, val3, val4],
 }

 columns_with_value_index: {
   CARRIER_NAME: {
     'American Airlines': [1, 5, 14, 23],
     'Delta': [0, 2, 6, 21]
   }
   MONTH: {
     '1': [1, 5, 14, 23],
     '2': [0, 2, 6, 21]
   }
 }
"""

# Process data to be stored in dictionary.
def data_processor(columns_with_value, columns_with_value_index):
    print('Processing data...')   # Indicate that data is loading.
    with open('..//data/sample_data.csv') as fp:
        line = fp.readline()
        line_index = 0

        while line:
            line = line.replace('\n', '')
            cols = line.split(',')

            # Get header and break them to column names.
            if line_index == 0:
                for col in cols:
                    columns_with_value[col] = []
                    columns_with_value_index[col] = {}

            else: 
                idx = 0
                # Append each value to their columns.
                for key in columns_with_value:
                    value = cols[idx]

                    columns_with_value[key].append(value) 

                    if value not in columns_with_value_index[key]:
                        columns_with_value_index[key][value] = []
                    
                    # line_index - 1 since we do not include the header and 
                    # array, starts at idx 0.
                    columns_with_value_index[key][value].append(line_index - 1)
                    idx += 1

            line = fp.readline()
            line_index += 1

# Maps column names to their ids.
# Example: 
#   Columns 'MONTH' is mapped to 1.
def map_col_to_ids(columns_with_value, columns_to_id_mapping):
    print('Columns available:')

    for col in columns_with_value:
        col_id = list(columns_with_value).index(col) + 1
        columns_to_id_mapping[col_id] = col
        print(col_id, ':', col)

# Asks users to drop any column.
def drop_inquiry(columns_with_value, columns_to_id_mapping):
    # TODO(eidmonetagaca): Implement error handling for any input errors.
    while 1:
        print('Choose number to drop column: \n')
        drop_col = input('Enter a number: ')

        drop_column(columns_with_value, columns_to_id_mapping, int(drop_col))

# Parses condtion query and returns an array of entries.
def parse_condition(condition_logic):
    entries = []

    if not condition_logic:
        return entries

    entries = condition_logic.split(' AND ')

    for i, entry in enumerate(entries):
        entries[i] = entry.split(' OR ')

    print('entries', entries)
    for i in range(len(entries)):
        for j in range(len(entries[i])):
            entries[i][j] = entries[i][j].split('=')

            entry = entries[i][j]

            entry[0] = entry[0].strip()
            entry[1] = entry[1].strip()  

    return entries

# -----------------------------------------------------------------------------
# SHOW OPERATIONS
# -----------------------------------------------------------------------------

# Shows all available columns.
def show_columns(columns_to_id_mapping):
    for col_id in columns_to_id_mapping:
        print(col_id, ':', columns_to_id_mapping[col_id])

# Show query results by idx.
def show_rows(columns_with_value, cols_to_read, idxs):
    column_view = cols_to_read

    # All column view.
    if cols_to_read == '*':
        column_view = columns_with_value.keys()

    # Get all columns that users wants to view.
    else:
        column_view = cols_to_read.split(',')

    # Print query results with columns.
    for i in list(idxs):
        res = ''
        for col in column_view:
            res += columns_with_value[col.strip()][i] + ' ' 
        print(res)

# -----------------------------------------------------------------------------
# DATABASE OPERATIONS
# -----------------------------------------------------------------------------

# Select rows from data where condtion is met. cols_with_value is main data to 
# be used to display rows and cols_with_val_idx is used to search for rows by 
# conditions to enable fast query.
def select(cols_with_value, cols_with_val_idx, column, condition):
    conditions = {'AND': [], 'OR': []}

    # Parse query from input.
    entries = parse_condition(condition)

    # TODO(eidmonetagaca): Implemenet a column name checker for error handling.
    for entry in entries:
        # Check for 'AND' condition entries.
        if len(entry) < 2:
            col = entry[0][0]
            value = entry[0][1]
            conditions['AND'].append(cols_with_val_idx[col][value])
        
        # Check fro 'OR' condtition entries.
        else:
            for sub_entry in entry:
                col = sub_entry[0]
                value = sub_entry[1]
                conditions['OR'].append(cols_with_val_idx[col][value])
    
    d = conditions['AND']
    # Get query results that meets all 'AND' conditions
    and_results = set.intersection(*map(set, d))

    if not conditions['OR']:
        return show_rows(cols_with_value, column, and_results)

    final_result = set()
    for or_condition in conditions['OR']:
        final_result.update(set.intersection(set(or_condition), and_results))

    show_rows(cols_with_value, column, final_result)

# Count distinct values in a column selected by the user.
def distinct(columns_with_value, column):
    return len(set(columns_with_value[column]))

# Drops any column from data.
def drop_column(columns_with_value, columns_to_id_mapping, column_id_to_drop):
    col = columns_to_id_mapping[column_id_to_drop]
    columns_with_value.pop(col)
    columns_to_id_mapping.pop(column_id_to_drop)

    # Show available columns after deletion.
    show_columns(columns_to_id_mapping)

def main():
    columns_with_value = {} 
    columns_with_value_index = {}
    columns_to_id_mapping = {}

    # Process csv and store data with or without indexing to a dictionary. 
    data_processor(columns_with_value, columns_with_value_index)

    map_col_to_ids(columns_with_value, columns_to_id_mapping)
    show_columns(columns_to_id_mapping)

    while 1:
        print('\nQuery syntax: <columns to view> WHERE <condition>')
        user_query = input('Type a Query:\n')
        function_query = user_query.split('WHERE')
        
        print(function_query)
        start = time.time()
        select(columns_with_value, columns_with_value_index, 
                        function_query[0].strip(), function_query[1].strip())
        elapse = time.time() - start
        
        print('Search time:', elapse)

main()
