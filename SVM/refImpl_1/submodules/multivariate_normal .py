import numpy as np
import matplotlib.pyplot as plt

'''
1: Understand multivariate_normal
2:  
'''
def gen_lin_separable_overlap_data():
    # generate training data in the 2-d case
    mean1 = np.array([0, 2])
    mean2 = np.array([2, 0])
    print('mean1 = ', mean1)
    print('mean1 = ', type(mean1), " ", np.shape(mean1))
    print(mean2)
    cov = np.array([[1.5, 1.0], [1.0, 1.5]])
    X1 = np.random.multivariate_normal(mean1, cov, 100)
    print(X1)
    print('X1 = ', type(X1), " ", np.shape(X1))
    print(X1[:,0])
    print(X1[:,1])
    plt.scatter(X1[:,0], X1[:,1])
    y1 = np.ones(len(X1))
    #print(y1)
    X2 = np.random.multivariate_normal(mean2, cov, 100)
    plt.scatter(X2[:,0], X2[:,1])

    y2 = np.ones(len(X2)) * -1
    #print(y2)
    plt.show()

    return X1, y1, X2, y2

gen_lin_separable_overlap_data()
