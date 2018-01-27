testLabelCopy=testLabel[0:361]
temp2Copy=temp2[0:361]
plt.plot(testLabelCopy, 'r', label='Data',linewidth=2)
#plt.plot(temp1, c='b', label='Linear model')
plt.plot(temp2Copy, 'k*-', label='RBF model')
#plt.plot(temp3, c='m', label='Poly model')
#plt.plot(temp4, c='r', label='Prediction')

plt.ylabel('People',fontsize=60)
plt.xticks(fontsize = 40)
plt.yticks(fontsize = 40)
#plt.title('Support Vector Regression')
plt.legend(fontsize=20)
plt.show()