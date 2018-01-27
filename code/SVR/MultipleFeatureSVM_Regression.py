import matplotlib.pyplot as plt
#from sklearn.svm import SVR
#import numpy as np
#n_samples, n_features = 10, 5
#np.random.seed(0)
#y = np.random.randn(n_samples)
#X = np.random.randn(n_samples, n_features)
#clf = SVR(C=1.0, epsilon=0.2)
#clf.fit(X, y) 
#SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.2, gamma='auto',
#    kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)






from sklearn.svm import SVR
import numpy as np
n_samples, n_features = 10, 5
#np.random.seed(0)
y = np.random.randn(n_samples)
X = np.random.randn(n_samples, n_features)

clf = SVR(C=1.0, epsilon=0.2)
temp1=clf.fit(X, y).predict(X)
clf2 = SVR(kernel='rbf', C=1e3, gamma=0.1)
temp2=clf2.fit(X, y).predict(X)
clf3 = SVR(kernel='poly', C=1e3, degree=2)
temp3=clf3.fit(X, y).predict(X)

#clf2=SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.2, gamma='auto',
#    kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
#temp2=clf2.fit(X,y).predict(X)
plt.hold('on')
plt.plot(y, c='b', label='Data')
plt.plot(temp1, c='r', label='Linear model')
plt.plot(temp2, c='g', label='RBF model')
plt.plot(temp3, c='y', label='Poly model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()


