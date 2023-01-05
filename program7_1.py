import numpy as np
from sklearn import datasets
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score as acs
import matplotlib.pyplot as plt

dataset = datasets.load_iris()
X = dataset.data
y = dataset.target

colormap = np.array(['red', 'green', 'blue'])

kmeans = KMeans(n_clusters=3)
k_pred = kmeans.fit_predict(X)

gmm = GaussianMixture( n_components=3)
gmm_pred = gmm.fit_predict(X)

kmeansAccuracy = acs(y, k_pred)*100
gmmAccuracy = acs(y, gmm_pred)*100

print(f'Accuracy of KMeans is {kmeansAccuracy}%\nAccuracy of GMM is {gmmAccuracy}%')
print(f'''Therefore {'KMeans' if kmeansAccuracy>gmmAccuracy else 'GMM' } is better''')

plt.figure(figsize=(20, 20))

plt.subplot(3, 3, 1)
plt.scatter(X[:, 2], X[:, 3], s=40, c=colormap[y])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Original Data')

plt.subplot(3, 3, 2)
plt.scatter(X[:, 2], X[:, 3], s=40, c=colormap[k_pred])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Original Data')

plt.subplot(3, 3, 3)
plt.scatter(X[:, 2], X[:, 3], s=40, c=colormap[gmm_pred])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Original Data')

plt.plot()