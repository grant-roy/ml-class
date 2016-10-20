import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets.samples_generator import make_blobs


centers = [(-5, -5),  (5, 5)]

X, y = make_blobs(n_samples=100, centers=centers, n_features=2,
                   random_state=0)

X = np.array(X)

plt.scatter(X[:,0],X[:,1])
plt.show()

