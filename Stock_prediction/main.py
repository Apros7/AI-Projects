import pickle

def read_data():
    with open('data.pickle', 'rb') as f:
        loaded_data = pickle.load(f)
    return loaded_data

