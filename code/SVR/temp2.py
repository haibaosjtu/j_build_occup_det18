import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16], 'r',linewidth=3,label='1')
plt.plot([6,7,8,9], [1,4,9,16], 'b',linewidth=3,label='2')
plt.axis([0, 10, 0, 20])
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.xlabel('data',fontsize=40)
plt.ylabel('target',fontsize=40)
plt.title('Support Vector Regression',fontsize=40)
plt.legend(fontsize=40)
plt.show()
plt.show()


