import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 1 * (0.5 - np.random.rand(8))

X2 = [[1],[2],[3],[4],[5],[6]]
y2 = [0,0,0,1,1,1]




svr_rbf = SVR(kernel='rbf', C=1e2, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e2)
svr_poly = SVR(kernel='poly', C=1e2, degree=2)
y_rbf = svr_rbf.fit(X, y).predict(X)
y_lin = svr_lin.fit(X, y).predict(X)
y_poly = svr_poly.fit(X, y).predict(X)


plt.scatter(X, y, c='k', label='data')
plt.hold('on')
plt.plot(X, y_rbf, c='g', label='RBF model')
plt.plot(X, y_lin, c='r', label='Linear model')
plt.plot(X, y_poly, c='b', label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()

