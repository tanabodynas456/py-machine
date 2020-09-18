from sklearn import datasets
digit_dataset = datasets.load_digits()
print(digit_dataset.images[0])
print(digit_dataset.images[0].shape)

