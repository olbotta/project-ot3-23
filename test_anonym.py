import pandas as pd
import numpy as np
# Quantize the latitude and longitude
def quantize (df, square_size):
    df['lat_q'] = np.floor(df['lat'] / square_size) * square_size
    df['long_q'] = np.floor(df['long'] / square_size) * square_size
    return df

data = pd.DataFrame({
        'id':   [  1,   1,   1,   1,   1,   2,   2,   2,   2],
        'lat':  [ 12,  10,  20,  11,  33,  10,  40,  22,  33],
        'long': [122, 100, 200, 111, 333, 100, 400, 222, 333]
    })

def obfuscate_traces(data: pd.DataFrame, id1, id2, square_size):
    """
    Obfuscates the traces in the given DataFrame by swapping the paths 
    of the two given IDs if they cross each other.

    note: assumes data is ordered temporally
    Args:
        data (pd.DataFrame): The DataFrame containing the traces.
        id1: The first ID to swap.
        id2: The second ID to swap.
        square_size: The size of the square used for quantization.

    Returns:
        pd.DataFrame: The obfuscated DataFrame.
    """
    # Get the rows for the given IDs
    data = quantize(data, square_size)
    rows_id1 = data[data['id'] == id1]
    rows_id2 = data[data['id'] == id2]
    
    # Check if there are any common quantized coordinates
    common_coords = pd.merge(rows_id1, rows_id2, on=['lat_q', 'long_q'])
    print(common_coords)
    # if not common_coords.empty:
    #     # Swap the IDs
    #     data.loc[data['id'].isin([id1, id2]), 'id'] = [id2, id1]
    #     data.sort_values(by=['id'], inplace=True)
    
    data.drop(['lat_q', 'long_q'], axis=1, inplace=True)
    return data
obfuscate_traces(data, 1, 2, 10)