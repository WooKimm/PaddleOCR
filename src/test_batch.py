import pickle

def load(filename):
    with open(filename, 'rb') as fo:
        data = pickle.load(fo, encoding='latin1')
    return data

d = "./test_batch"
dataset_path_1 = load(d)
print(dataset_path_1.keys())
# print(dataset_path_1)
print(dataset_path_1[b'labels'])
print("---------------")
print(dataset_path_1[b'batch_label'])
print("---------------")
print(dataset_path_1[b'data'])
print("---------------")
print(dataset_path_1[b'filenames'])