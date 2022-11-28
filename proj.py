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
    with open('sample2.csv') as fp:
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

# -----------------------------------------------------------------------------
# SHOW OPERATIONS
# -----------------------------------------------------------------------------

# Shows all available columns.
def show_columns(columns_to_id_mapping):
    for col_id in columns_to_id_mapping:
        print(col_id, ':', columns_to_id_mapping[col_id])

# -----------------------------------------------------------------------------
# DATABASE OPERATIONS
# -----------------------------------------------------------------------------

# Drops any column from data.
def drop_column(columns_with_value, columns_to_id_mapping, column_id_to_drop):
    col = columns_to_id_mapping[column_id_to_drop]
    columns_with_value.pop(col)
    columns_to_id_mapping.pop(column_id_to_drop)

    # Show available columns after deletion.
    show_columns(columns_to_id_mapping)

    
def mean(columns_with_value, columns_to_id_mapping, column_id_to_mean):
    col = columns_to_id_mapping[column_id_to_mean]
    numbers_int = [int(x) for x in columns_with_value[col]]
    res = sum(numbers_int) / len(numbers_int)
    return res

def mode(columns_with_value, columns_to_id_mapping, column_id_to_mode):
    col = columns_to_id_mapping[column_id_to_mode]
    numbers_int = [int(x) for x in columns_with_value[col]]
    res = max(set(numbers_int), key=numbers_int.count)
    return res

def median(columns_with_value, columns_to_id_mapping, column_id_to_mode):
    col = columns_to_id_mapping[column_id_to_mode]
    numbers_int = [int(x) for x in columns_with_value[col]]
    columns_with_value[col].sort()
    mid = len(columns_with_value[col]) // 2
    res = (numbers_int[mid] + numbers_int[~mid]) / 2
    return res


# def variance(columns_with_value):

#     meanval = mean(columns_with_value)
#     return mean([(i-meanval) ** 2 for i in columns_with_value])


# def std(columns_with_value):

#     return (variance(columns_with_value)) ** (1/2)


# def analysis(columns_with_value, column):
#     pass

# -----------------------------------------------------------------------------
# STATISTICAL OPERATIONS
# -----------------------------------------------------------------------------
# Asks users to select column to calculate values for
def stat_analysis(columns_with_value, columns_to_id_mapping):
    print('Choose number to describe column: \n')
    stat_col = input('Enter a number: ')
    get_mean = ('Mean : {fmean}').format(fmean = mean(columns_with_value, columns_to_id_mapping, int(stat_col)))
    get_median = ('Median : {fmedian}').format(fmedian = median(columns_with_value, columns_to_id_mapping, int(stat_col)))
    get_mode = ('Mode : {fmode}').format(fmode = mode(columns_with_value, columns_to_id_mapping, int(stat_col)))
    return (get_mode + '\n' + get_mean +  '\n' + get_median)

        


        
def show_stats(columns_with_value, columns_to_id_mapping, column_id_to_drop):

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

    return stat_analysis(columns_with_value, columns_to_id_mapping)



    


   
result = main()
print(result)

#main()
