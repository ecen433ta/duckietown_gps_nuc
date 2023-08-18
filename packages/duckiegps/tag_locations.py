import numpy as np

def return_fixed_loc(number):
    if number == 116: # visible by the blue camera
        return np.matrix([[1,0,0,2.4384],
                          [0,1,0,0.9144],
                          [0,0,1,0],
                          [0,0,0,1]])
    elif number == 117: # visible by the green camera
        return np.matrix([[1,0,0,0.9144],
                          [0,1,0,2.1336],
                          [0,0,1,0],
                          [0,0,0,1]])
    elif number == 118: # visible by the yellow camera
        return np.matrix([[1,0,0,2.1336],
                          [0,1,0,3.9624],
                          [0,0,1,0],
                          [0,0,0,1]])
    elif number == 119: # visible by the red
        return np.matrix([[1,0,0,3.9624],
                          [0,1,0,3.9624],
                          [0,0,1,0],
                          [0,0,0,1]])
    else:
        return None
        
# Add all the fixed tags here