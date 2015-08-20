import numpy as np
import pandas as pd
import ipdb

hello = "world"
world = "jon"

def print_name():
    #var hello
    print hello + world

def main(input_arr):
    df = pd.read_csv('data/geolocated_rest.csv')
    ipdb.set_trace()
    np_mat = df.as_matrix()
    np.mean(np_mat)
    np.std([1,2,3])
    print "all ok"

print df