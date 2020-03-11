import pickle


def load_pkl(pickle_path):
    with open(pickle_path, 'rb') as f:
        py_obj = pickle.load(f)
    return py_obj


def dump_pkl(py_obj, pickle_path):
    with open(pickle_path, 'wb') as f:
        pickle.dump(py_obj, f)
    return True
