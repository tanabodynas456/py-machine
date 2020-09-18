from sklearn import datasets
digit_dataset = datasets.load_digits()
print(digit_dataset['DESCR'])
print(digit_dataset['data'])
print(digit_dataset['images'].shape)