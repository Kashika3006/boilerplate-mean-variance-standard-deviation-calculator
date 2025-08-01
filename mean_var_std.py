import numpy as np

def calculate(glist):
    #If a list containing less than 9 elements is passed into the function,
    # it should raise a ValueError exception with the message: "List must contain nine numbers."
    if len(glist)<9:
        raise ValueError("List must contain nine numbers.")
        
    

    #convert the given list to a 3x3 numpy array
    a = np.array(glist)
    a = a.reshape(3,3)
    # mean along both axes and the flattened matrix
    row_mean = (np.mean(a, axis=1)).tolist()
    column_mean = (np.mean(a, axis=0)).tolist()
    matrix_mean = np.mean(a).item()

    #variance along both axes and the flattened matrix
    row_var = (np.var(a, axis=1)).tolist()
    column_var = (np.var(a, axis=0)).tolist()
    matrix_var = np.var(a).item()

    #standard deviation along both axes and the flattened matrix
    row_std = (np.std(a, axis=1)).tolist()
    column_std = (np.std(a, axis=0)).tolist()
    matrix_std = np.std(a).item()

    #max along both axes and the flattened matrix
    row_max = np.max(a, axis=1).tolist()
    column_max = np.max(a, axis=0).tolist()
    matrix_max = np.max(a).item()

    #min along both axes and the flattened matrix
    row_min = np.min(a, axis=1).tolist()
    column_min = np.min(a, axis=0).tolist()
    matrix_min = np.min(a).item()

    #sum along both axes and the flattened matrix
    row_sum = np.sum(a, axis=1).tolist()
    column_sum = np.sum(a, axis=0).tolist()
    matrix_sum = np.sum(a).item()

    calculations = {'mean': [column_mean, row_mean, matrix_mean],
                    'variance': [column_var, row_var, matrix_var],
                    'standard deviation': [column_std, row_std, matrix_std],
                    'max': [column_max, row_max, matrix_max],
                    'min': [column_min, row_min, matrix_min],
                    'sum': [column_sum, row_sum, matrix_sum]}

    # return a dictionary containing 
    #the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix
    return calculations