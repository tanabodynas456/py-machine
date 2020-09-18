import matplotlib.pyplot as ply
from sklearn import datasets
digit_dataset = datasets.load_digits()
digit_dataset = datasets.load_digits()


print(digit_dataset.target[0])
ply.imshow(digit_dataset.images[0],cmap=ply.get_cmap('gray'))
ply.show()
