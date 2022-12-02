import re
import os
import sys
import time
import math          # For getting ceil of number only.
import numpy as np   # For storing data only.
import pandas as pd  # For showing data only. 

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

# -----------------------------------------------------------------------------
# ERROR HANDLING
# ----------------------------------------------------------------------------- 

# Constants for error messages.
SOMETHING_WENT_WRONG = '[WARNING]: Something wen wrong with'

# Checks for non numeric digit. Used in main menu to check if user input is 
# numeric.
def inputChecker(user_input):
    if not user_input.isdigit():
        print(f'[WARNING]: {user_input} is not valid!')
        return False
    return True

# Checks if column name is available.
def columnChecker(column, columns_with_value):
    if column not in columns_with_value:
        print(f'[WARNING]: {column} not valid!')
        return False
    return True

# -----------------------------------------------------------------------------
# DATA PROCESSOR
# -----------------------------------------------------------------------------

# Indexes indexes checks if the value is already in the idx, if not it will
# create an np array where it can store them.
def data_indexer(idx, column, value, columns_with_value_index):
    if value not in columns_with_value_index[column]:
        columns_with_value_index[column][value] = []

    # line_index - 1 since we do not include the header and 
    # array, starts at idx 0. 
    columns_with_value_index[column][value].append(idx - 1)

# Process csv and store data with or without indexing to a dictionary. 
def data_processor(columns_with_value, columns_with_value_index):
    print('Load data set:\n**************')
    
    inp_str = f'[{time.time()}]: Please type the name of the file to load: '
    file_name = input(inp_str)

    print(f'[{time.time()}]: {file_name}')

    if file_name != 'data.csv':
        print(f'Please enter valid csv file')
        return

    print('\nProcessing data...')   # Indicate that data is loading.

    start = time.time()

    print(f'File Size is {os.stat(file_name).st_size / (1024 * 1024)} MB')

    with open (file_name) as f:
        columns = f.readline()
        columns = columns.replace('\n', '')
        columns = columns.split(',')

        for col in columns:
            columns_with_value[col] = []
            columns_with_value_index[col] = {}
        
        # Skip header in for loop.
        next(f)
        line_index = 1
        for line in f:
            # Clean out each row.
            line = line.replace('\n', '')
            line = re.sub(f'[^a-zA-Z0-9\s\.\-,_]', '', line)
            cols = line.split(',')

            try:
                [v1, v2, v3, v4, v5, v6, v7, v8, v9, v10] = cols[:10]
                [v11, v12, v13, v14, v15, v16, v17, v18, v19, v20] = cols[10:20]
                [v21, v22, v23, v24, v25, v26, v27, v28, v29, v30] = cols[20:]
            except:
                continue
            
            # Converts numeric columns to float values.
            v1 = float(v1)
            v2 = float(v2)
            v3 = float(v3)

            v5 = float(v5)
            v6 = float(v6)
            v7 = float(v7)
            v8 = float(v8)
            v10 =float(v10)

            v11 = float(v11)
            v12 = float(v12)
            v13 = float(v13)
            v14 = float(v14)
            v15 = float(v15)
            v16 = float(v16)
            v17 = float(v17)
            v19 = float(v19)
            v20 = float(v20)

            v22 = float(v22)
            v23 = float(v23)
            v24 = float(v24)
            v25 = float(v25)
            v26 = float(v26)
            v27 = float(v27)
            v28 = float(v28)
            v29 = float(v29)
            v30 = float(v30) 

            # Get start time and end time for 'DEP_TIME_BLK' and subtract
            # end and start to get time duration. 
            duration = v4.split('-')
            v4 = float(duration[1]) - float(duration[0])

            # Start storing values per column. Hardcoded since looping would
            # significantly increase time complexity.
            columns_with_value['MONTH'].append(v1)
            columns_with_value['DAY_OF_WEEK'].append(v2)
            columns_with_value['DEP_DEL15'].append(v3)
            columns_with_value['DEP_TIME_BLK'].append(v4)

            columns_with_value['DISTANCE_GROUP'].append(v5)
            columns_with_value['SEGMENT_NUMBER'].append(v6)
            columns_with_value['CONCURRENT_FLIGHTS'].append(v7)
            columns_with_value['NUMBER_OF_SEATS'].append(v8)
            columns_with_value['CARRIER_NAME'].append(v9)

            columns_with_value['AIRPORT_FLIGHTS_MONTH'].append(v10)
            columns_with_value['AIRLINE_FLIGHTS_MONTH'].append(v11)
            columns_with_value['AIRLINE_AIRPORT_FLIGHTS_MONTH'].append(v12)
            columns_with_value['AVG_MONTHLY_PASS_AIRPORT'].append(v13)
            columns_with_value['AVG_MONTHLY_PASS_AIRLINE'].append(v14)

            columns_with_value['FLT_ATTENDANTS_PER_PASS'].append(v15)
            columns_with_value['GROUND_SERV_PER_PASS'].append(v16)
            columns_with_value['PLANE_AGE'].append(v17)
            columns_with_value['DEPARTING_AIRPORT'].append(v18)
            columns_with_value['LATITUDE'].append(v19)

            columns_with_value['LONGITUDE'].append(v20)
            columns_with_value['PREVIOUS_AIRPORT'].append(v21)
            columns_with_value['PRCP'].append(v22)
            columns_with_value['SNOW'].append(v23)
            columns_with_value['SNWD'].append(v24)

            columns_with_value['TMAX'].append(v25)
            columns_with_value['AWND'].append(v26)
            columns_with_value['CARRIER_HISTORICAL'].append(v27)
            columns_with_value['DEP_AIRPORT_HIST'].append(v28)
            columns_with_value['DAY_HISTORICAL'].append(v29)
            columns_with_value['DEP_BLOCK_HIST'].append(v30)

            # Start indexing indexes for fast search. Looks ugly but is
            # an essential part of making program efficient.
            data_indexer(line_index, 'MONTH', v1, columns_with_value_index)
            data_indexer(line_index, 'DAY_OF_WEEK', v2, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'DEP_DEL15', v3, columns_with_value_index)
            data_indexer(line_index, 'DEP_TIME_BLK', v4, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'DISTANCE_GROUP', v5, 
                                                    columns_with_value_index)

            data_indexer(line_index, 'SEGMENT_NUMBER', v6, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'CONCURRENT_FLIGHTS', v7, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'NUMBER_OF_SEATS', v8, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'CARRIER_NAME', v9, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'AIRPORT_FLIGHTS_MONTH', 
                                                v10, columns_with_value_index)

            data_indexer(line_index, 'AIRLINE_FLIGHTS_MONTH', v11, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'AIRLINE_AIRPORT_FLIGHTS_MONTH', 
                                        v12, columns_with_value_index)
            data_indexer(line_index, 'AVG_MONTHLY_PASS_AIRPORT', v13, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'AVG_MONTHLY_PASS_AIRLINE', v14, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'FLT_ATTENDANTS_PER_PASS', v15, 
                                                    columns_with_value_index)

            data_indexer(line_index, 'GROUND_SERV_PER_PASS', v16, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'PLANE_AGE', v17, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'DEPARTING_AIRPORT', v18, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'LATITUDE', v19, columns_with_value_index)
            data_indexer(line_index, 'LONGITUDE', v20, columns_with_value_index)

            data_indexer(line_index, 'PREVIOUS_AIRPORT', v21, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'PRCP', v22, columns_with_value_index)
            data_indexer(line_index, 'SNOW', v23, columns_with_value_index)
            data_indexer(line_index, 'SNWD', v24, columns_with_value_index)
            data_indexer(line_index, 'TMAX', v25, columns_with_value_index)

            data_indexer(line_index, 'AWND', v26, columns_with_value_index)
            data_indexer(line_index, 'CARRIER_HISTORICAL', v27, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'DEP_AIRPORT_HIST', v28, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'DAY_HISTORICAL', v29, 
                                                    columns_with_value_index)
            data_indexer(line_index, 'DEP_BLOCK_HIST', v30, 
                                                    columns_with_value_index)

            line_index += 1
    f.close()

    elapse = time.time() - start
    total_columns = len(list(columns_with_value.keys()))
    print(f'[{time.time()}] Total Columns Read: {total_columns}')
    print(f'[{time.time()}] Total Rows Read: {line_index - 1}')

    print(f'\nFile loaded successfully! Time to load {elapse} sec.')

# Maps column names to their ids.
# Example: 
#   Columns 'MONTH' is mapped to 1.
def map_col_to_ids(columns_with_value, columns_to_id_mapping):
    for col in columns_with_value:
        col_id = list(columns_with_value).index(col) + 1
        columns_to_id_mapping[col_id] = col

# Parses condtion query and returns an array of entries.
def parse_condition(condition_logic):
    entries = []

    if not condition_logic:
        return entries

    entries = condition_logic.split(' AND ')

    for i, entry in enumerate(entries):
        entries[i] = entry.split(' OR ')

    for i in range(len(entries)):
        for j in range(len(entries[i])):
            # TODO(etagaca): Handle when it is not only '=' operation.
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
    print('\n(21) List all columns:\n**********************')
    for col_id in columns_to_id_mapping:
        print(col_id, ':', columns_to_id_mapping[col_id])

# Show query results by idx.
# @deprecated
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
            res += columns_with_value[col.strip()][int(i)] + ' ' 
        print(res)

# Shows results by idx or object/dicts.
def show(columns_to_show, columns_with_value, result):
    # Process object/dict results.
    if isinstance(result, dict):
        # Use DataFrame when dict has list of values,
        if isinstance(result[list(result.keys())[0]], list):
            print(pd.DataFrame(result))

        # Use Series for normal dict.
        else:
            print(pd.Series(result))

    else:
        # Show all columns when query is missing columns to show.
        if len(columns_to_show) and columns_to_show[0] == '':
            columns_to_show = list(columns_with_value.keys())

        try:
            df = pd.DataFrame(columns_with_value)
            print(df.loc[result, columns_to_show])
        except:
            print(f'\nSomething went wrong with showing results -_-')

# Project results by values.
def project(columns_to_show, columns_with_value, values = []):
    data = {}
    for column in columns_to_show:
        # Project values when there are values passed.
        data[column] = columns_with_value[column] if (not values) else values
    print(pd.DataFrame(data))

# -----------------------------------------------------------------------------
# DATABASE OPERATIONS
# -----------------------------------------------------------------------------

# Count distinct values in a column selected by the user.
def distinct(columns_with_value, column):
    return len(set(columns_with_value[column]))

# Drops any column from data.
def drop_column(columns_with_value, columns_to_id_mapping):
    print('\n(22) Drop Columns:\n******************')

    # Get column to drop based on id.
    column_id_to_drop = int(input('Name column to Drop: '))

    try:
        col = columns_to_id_mapping[column_id_to_drop]

        print(f'{time.time()}: {col}')

        # Remove selected column.
        columns_with_value.pop(col)
        columns_to_id_mapping.pop(column_id_to_drop)

        print(f'{time.time()}: Column dropped!')
    except:
        print(f'\nDropping column failed!')
        print(f'Usage: <column-id>')

# Select rows from data where condtion is met. cols_with_value is main data to 
# be used to display rows and cols_with_val_idx is used to search for rows by 
# conditions to enable fast query.
def select(query_str, cols_with_value, cols_with_val_idx):
    try:
        [column, condition] = query_str.split('where')
        column = column.strip()
    except:
        print(f'Select query cannot be parsed')

    # Error handling: Checks for column validity.
    if not columnChecker(column, cols_with_value):
        return

    condition = condition.strip()

    conditions = {'AND': [], 'OR': []}

    # Starting time for search.
    start = time.time()

    # Parse condition from input.
    entries = parse_condition(condition)

    try:
        for entry in entries:
            # Check for 'AND' condition entries.
            if len(entry) < 2:
                col = entry[0][0]
                value = entry[0][1]

                # Error handling: Checks for column validity.
                if not columnChecker(col, cols_with_value):
                    return

                # Convert string to float for columns that contains 
                # int or float values.
                try:
                    value = float(value)
                except ValueError:
                    value = value

                # TODO(etagaca): Support greater than and less than operations.
                conditions['AND'].append(cols_with_val_idx[col][value])
            
            # Check for 'OR' condtition entries.
            else:
                for sub_entry in entry:
                    col = sub_entry[0]
                    value = sub_entry[1]

                    # Error handling: Checks for column validity.
                    if not columnChecker(col, cols_with_value):
                        return

                    # Convert string to float for columns that contains 
                    # int or float values.
                    try:
                        value = float(value)
                    except ValueError:
                        value = value

                    conditions['OR'].append(cols_with_val_idx[col][value])
        
        d = conditions['AND']

        # Get query results that meets all 'AND' conditions
        and_results = []

        if len(d):
            and_results = set.intersection(*map(set, d))

        # Return early if no 'OR' conditions.
        if not conditions['OR']:
            elapse = time.time() - start
            return list(and_results)

        final_result = set()
        
        for or_condition in conditions['OR']:
            # Check if there are any 'AND' condtions to add to final result.
            if len(and_results):
                final_result.update(set.intersection(set(or_condition), 
                                                                and_results))
            else:
                final_result.update(or_condition)

        elapse = time.time() - start
        return list(final_result)
    except:
        print('\nSomething wrong with query search :(')

# Counts how many values are in a given set/data. If 
def count(data, columns_with_value, column = ''):
    if column:
        return len(columns_with_value[column])

    return len(data)

# Returns unique values of a column.
def unique(column, columns_with_value):
    return list(set(columns_with_value[column]))

# Sorts given set/data.
def sort(data):
    # Sort dictonaries by values.
    if isinstance(data, dict):
        return dict(sorted(data.items(), key=lambda item: item[1]))
    else:
        try:
            return sorted(data)
        except:
            # Convert every value to a string to be sorted.
            data = [str(x) for x in data]
            return sorted(data)

# Reverse sorts given set/data.
def sort_reverse(data):
    # Sort dictonaries by values.
    if isinstance(data, dict):
        return dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    else:
        try:
            return sorted(data, key=None, reverse=True)
        except:
            # Convert every value to a string to be sorted.
            data = [str(x) for x in data]
            return sorted(data, key=None, reverse=True)

# Returns first N numbers within result list.
# NOTE: Can be a list of idxs or values.
def first(number, data):
    n = int(number)

    # Show top results for dictionaries.
    if isinstance(data, dict):
        return dict(list(data.items())[:n])
    else:
        return data[0:n]

# Returns last N numbers within result list.
# NOTE: Can be a list of idxs or values.
def last(number, data):
    n = int(number)

    # Show top results for dictionaries.
    if isinstance(data, dict):
        return dict(list(data.items())[:n])
    else:
        return data[-n:]

# Returns idx of max value within a column.
def maximum(column_name, result, columns_with_value):
    # Process object/dict results.
    if isinstance(result, dict) and len(result.keys()):

        max_value = max(result, key=result.get)
        return { max_value: result[max_value] }
    
    # Process idxs results.
    else:
        max_value = np.max(columns_with_value[column_name])
        result = np.where(columns_with_value[column_name] == max_value)

        # Return only one max value in case there are multiple ones.
        return result[0][0]

# Returns idx of min value within a column.
def minimum(column_name, result, columns_with_value):
    # Process object/dict results.
    if isinstance(result, dict) and len(result.keys()):
        min_value = min(result, key=result.get)
        return  { min_value: result[min_value] }

    else:
        min_value = np.amin(columns_with_value[column_name])
        result = np.where(columns_with_value[column_name] == min_value)

        # Return only one max value in case there are multiple ones.
        return result[0][0]

# Gets average of values within a list.
def average(data):
    return sum(data)/len(data)

# Gets median of values within a list.
def get_median(data):
    ls_sorted = data.sort() # sort the list

    # find the median
    if len(data) % 2 != 0:
        # total number of values are odd
        # subtract 1 since indexing starts at 0
        m = int((len(data)+1)/2 - 1)
        return data[m]
    else:
        m1 = int(len(data)/2 - 1)
        m2 = int(len(data)/2)
        return (data[m1] + data[m2])/2

# Gets mode of values within a list.
def get_mode(data):
    if not data:
        return None
    else:
        return max(set(data), key = data.count)

# Gets percentile within values of list.
def get_percentile(data, percentile):
    n = len(data)
    p = n * percentile / 100
    if p.is_integer():
        return sorted(data)[int(p)]
    else:
        return sorted(data)[int(math.ceil(p)) - 1]

# Receives idxs and group it by the column specified. Also accepts aggregate
# functions, and only returns values if there is no aggregate function defined.
def group_by(column, aggregate, result_idxs, columns_with_value, 
                                                    columns_with_value_index):
    value_groups = {} # Store to a dict for data frame.

    # Name of aggregate function.
    aggregate_func = ''

    # Actual value to compare to when it comes to converting idxs to values for
    # aggregation.
    values = []
    column_to_aggregate = ''

    # Check for aggregates.
    if len(aggregate):
        # Clean aggregate query.
        [query_func, col_to_aggregate] = aggregate.split('(')
        col_to_aggregate = col_to_aggregate.replace(')', '')

        cols_to_aggregate = col_to_aggregate.split('+')

        column_to_aggregate = col_to_aggregate
        col_values1 = columns_with_value[cols_to_aggregate[0].strip()]

        col_values2 = []
        if len(cols_to_aggregate) == 2:
            col_values2 = columns_with_value[cols_to_aggregate[1].strip()]

        aggregate_func = query_func

    # Group values and by result idxs.
    for group in columns_with_value_index[column]:
        idxs = set(columns_with_value_index[column][group])
        
        # Set column value idx when there are no results.
        group_idxs = set(result_idxs).intersection(idxs) if result_idxs else idxs

        if len(aggregate):
            # Get values of selected column.
            col_aggregate_values = np.take(col_values1, list(group_idxs))

            # Dynamic variable
            result_group_value = []

            if aggregate_func == 'count':
                result_group_value = count(col_aggregate_values, 
                                                        columns_with_value)
            elif aggregate_func == 'avg':
                if len(col_aggregate_values):
                    result_group_value = average(col_aggregate_values)

                    if len(cols_to_aggregate) == 2:
                        col_val2 = np.take(col_values2, list(group_idxs))
                        param_avg = result_group_value + average(col_val2)
                        result_group_value = param_avg / 2
                else:
                    result_group_value = 0

            elif aggregate_func == 'max':
                if len(col_aggregate_values):
                    result_group_value = max(col_aggregate_values)

            value_groups[group] = result_group_value

        # Return values when there is no aggregation.
        else:
            value_groups[group] = columns_with_value[column]

    return value_groups

def chained_query(query_str, columns_with_value, columns_with_value_index):
    # Store queries that are parsed from the input.
    queries = query_str.split('<')

    # Store query functions with parameter values.
    # Example:
    #   [[count, data], [unique, column_name]]
    query_entries = []

    for query in queries:
        try:
            [query_func, value] = query.split(':')
            query_entries.append([query_func.strip(), value.strip()])
        except:
            print(f'\nUSAGE: <query-operation>: <value>')

    result = []

    start = time.time()

    for i in reversed(range(len(query_entries))):
        [query_func, value] = query_entries[i]

        if query_func == 'count':
            result = count(result, columns_with_value)
            print(f'Count: {result}')

        elif query_func == 'unique':
            result = unique(value, columns_with_value)

        elif query_func == 'max':
            result = maximum(value, result, columns_with_value)

        elif query_func == 'min':
            result = minimum(value, result, columns_with_value)
        
        elif query_func == 'show':
            columns_to_show = [x.strip() for x in value.split(',')]
            show(columns_to_show, columns_with_value, result)

        elif query_func == 'project':
            columns_to_show = [x.strip() for x in value.split(',')]
            project(columns_to_show, columns_with_value, result)

        elif query_func == 'group by':
            group_by_query = value.split(',')
            column = group_by_query[0].strip()
            aggregate = ''

            # Catch when there is no aggregate function defined.
            if 2 == len(group_by_query):
                aggregate = group_by_query[1].strip()

            # Turn result to an object/dictionary.
            result = group_by(column, aggregate, result, 
                                columns_with_value , columns_with_value_index)

        elif query_func == 'sort':
            result = sort(result)

        elif query_func == 'sort reverse':
            result = sort_reverse(result)

        elif query_func == 'first':
            result = first(value, result)

        elif query_func == 'last':
            result = last(value, result)

        elif query_func == 'search':
            result = select(value, columns_with_value, columns_with_value_index)

        # Error handling: Check for query operation validity.
        else:
            print(f'[WARNING]: Operation {query_func} is not valid!')

    elapse = time.time() - start
    print(f'\nTime to analyze: {elapse} sec.')

def describe_data(columns_with_value, columns_with_value_idx):
    print('\n(23) Describe Columns:\n**********************')
    
    # Show only describable data (numeric columns).
    print('Available Columns:\n=================')
    for col in columns_with_value:
        if type(columns_with_value[col][0]) is float:
            print(col)

    print(f'\n[{time.time()}]: Name column to Describe:')

    column = input(f'[{time.time()}]: ')

    try:
        start = time.time()
        print('\nColumn stats:\n============')
        print(f'Count: {count([], columns_with_value, column)}')
        print(f'Unique: {len(unique(column, columns_with_value))}')

        data = columns_with_value[column]

        mean = average(columns_with_value[column])
        print(f'Mean: {mean}')

        median = get_median(columns_with_value[column])
        print(f'Median: {median}')

        mode = get_mode(columns_with_value[column])
        print(f'Mode: {mode}')

        variance = sum([((x - mean) ** 2) for x in columns_with_value[column]])
        variance = variance / len(columns_with_value[column])

        standard_deviation = variance ** 0.5

        print(f'Standard Deviation (SD): {standard_deviation}')
        print(f'Variance: {variance}')

        # Get idx of min value in a column.
        min_idx = minimum(column, {}, columns_with_value)
        print(f'Minimum: {columns_with_value[column][min_idx]}')

        # Get idx of max value in a column.
        max_idx = maximum(column, {}, columns_with_value)
        print(f'Maximum: {columns_with_value[column][max_idx]}')

        percentile20 = get_percentile(data, 20)
        print(f'20 Percentile (P20): {percentile20}')

        percentile40 = get_percentile(data, 40)
        print(f'40 Percentile (P40): {percentile40}')

        percentile50 = get_percentile(data, 50)
        print(f'50 Percentile (P50): {percentile50}')

        percentile60 = get_percentile(data, 60)
        print(f'60 Percentile (P60): {percentile60}')

        percentile80 = get_percentile(data, 80)
        print(f'80 Percentile (P80): {percentile80}')

        elapse = time.time() - start
        print(f'\nStats printed succesfully! time to process is {elapse} sec.')
    except:
        print(f'[WARNING]: Something went wrong with describing column')

def data_analysis(columns_with_value, columns_with_value_index, 
                                                        columns_to_id_mapping):
    print('\nData Analysis:\n**************')
    inp = input(f'{time.time()}: ')
    chained_query(inp, columns_with_value, columns_with_value_index)
    return

def explore_data_menu(columns_with_value, columns_with_value_index, 
                                                        columns_to_id_mapping):
    while 1:
        print('\nExploring Data:\n**************')
        print('(21) List All Columns:')
        print('(22) Drop Columns:')
        print('(23) Describe Columns:')
        print('(24) Search Element in Column:')
        print('(25) Back to Main Menu:')

        user_input = input('-> ')

        # Check for valid input.
        if not inputChecker(user_input):
            continue

        selected = int(user_input)

        if selected == 21:
            try:
                show_columns(columns_to_id_mapping)
            except:
                print(f'{SOMETHING_WENT_WRONG} with show function')

        elif selected == 22:
            try:
                drop_column(columns_with_value, columns_to_id_mapping)
            except:
                print(f'{SOMETHING_WENT_WRONG} with drop function')

        elif selected == 23:
            try:
                describe_data(columns_with_value, columns_with_value_index)
            except:
                print(f'{SOMETHING_WENT_WRONG} with describe function')

        elif selected == 24:
            try:
                print('\nSearch Element in Column:\n*************************')

                # Get column to search from.
                column = input(f'{time.time()} Enter Column Name: ')
                print(f'{time.time()}: {column}')

                # Get condition for result.
                condition = input(f'{time.time()}: Enter Element to Search: ')
                print(f'{time.time()}: {condition}')
                
                # Combine column name and search query.
                query_str = f'{column} where {column} = {condition}'

                start = time.time()
                result = select(query_str, columns_with_value, 
                                                    columns_with_value_index)

                elapse = time.time() - start
                print(f'\nGot the index results! {elapse} sec.\n')

                start = time.time()
                show(list(columns_with_value.keys()), columns_with_value, 
                                                                        result)
                elapse = time.time() - start
                print(f'\nTime to show values: {elapse} sec.\n')
            except:
                print(f'{SOMETHING_WENT_WRONG} with search function')

        elif selected == 25:
            main_menu(columns_with_value, columns_with_value_index, 
                                                        columns_to_id_mapping)

        # Error handling: Check for valid selection.
        else:
            print(f'[WARNING]: {selected} is not from 21 - 25!')

def main_menu(columns_with_value, columns_with_value_index, 
                                                        columns_to_id_mapping):
    # Menu selection.
    print('\nMain Menu:\n**********')
    print('(1) Load Data')
    print('(2) Exploring Data')
    print('(3) Data Analysis')
    print('(4) Quit')

    user_input = input('-> ')

    # Check for valid input.
    if not inputChecker(user_input):
        return

    selected = int(user_input)

    # Load data.
    if selected == 1:
        data_processor(columns_with_value, columns_with_value_index)
        map_col_to_ids(columns_with_value, columns_to_id_mapping)

    # Exploring data.
    elif selected == 2:
        explore_data_menu(columns_with_value, columns_with_value_index, 
                                                        columns_to_id_mapping)

    # Data analysis.
    elif selected == 3:
        data_analysis(columns_with_value, columns_with_value_index, 
                                                    columns_to_id_mapping)
    # Quit.
    elif selected == 4:
        print('Bye')
        quit()

    # Error handling: Check for valid selection.
    else:
        print(f'[WARING]: {selected} is not from 1 - 4!')
        main_menu()

def main():
    columns_with_value = {} 
    columns_with_value_index = {}
    columns_to_id_mapping = {}

    while 1:
        main_menu(columns_with_value, columns_with_value_index, 
                                                        columns_to_id_mapping)
main() # Driver code.