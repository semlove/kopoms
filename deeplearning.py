import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
X_dataset, y_dataset = make_blobs(centers=[[-0.3, 0.3], [0.3, -0.3]],
                                  cluster_std=0.2,
                                  n_samples=20,
                                  center_box=(-1.0, 1.0),
                                  random_state=42)
dataset = pd.DataFrame(X_dataset, columns=['x0', 'x1'])
dataset['y'] = y_dataset
fig, ax = plt.subplots()
for key, g in dataset.groupby('y'):
  color = 'k' if key == 1 else 'w'
  g.plot(ax=ax, kind='scatter', x='x0', y='x1', label=key, color=color, edgecolor='black', linewidth='1')

fig, ax = plt.subplots()
for key, g in dataset.groupby('y'):
  color = 'k' if key == 1 else 'w'
  g.plot(ax=ax, kind='scatter', x='x0', y='x1', label=key, color=color, edgecolor='black', linewidth='1')

a = 0
x = np.arange(-1.0, 1.0, 0.1)
y = a * x
plt.plot(x, y)

