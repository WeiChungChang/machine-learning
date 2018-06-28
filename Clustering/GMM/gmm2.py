#coding:utf-8
import numpy as np
from pylab import *

K = 3

def scale(X):
    col = X.shape[1]
    mu = np.mean(X, axis=0)
    #print(type(mu)) # <class 'numpy.ndarray'>
    #print(mu) # [3.48778309  70.89705882]
    #print("shape ", shape(mu)) # shape(2,)
    #print("shape ", shape([[1, 2],[3, 4]])) # shape(2, 2)
    sigma = np.std(X, axis=0)
    #print("sigma = " ,sigma) # sigma = [  1.13927121  13.56996002]
    for i in range(col):
        X[:,i] = (X[:,i] - mu[i]) / sigma[i]

    #print(X)
    #print("mu = ", np.mean(X, axis=0)) # [  4.48579082e-16   4.27048103e-16]
    #print("sigma = ", np.std(X, axis=0)) # [ 1.  1.]
    return X

def gaussian(x, mean, cov):
    temp1 = 1 / ((2 * np.pi) ** (x.size/2.0))
    temp2 = 1 / (np.linalg.det(cov) ** 0.5)
    temp3 = - 0.5 * np.dot(np.dot(x - mean, np.linalg.inv(cov)), x - mean)
    return temp1 * temp2 * np.exp(temp3)

def likelihood(X, mean, cov, pi):
    summation = 0.0
    for n in range(len(X)):
        temp = 0.0
        for k in range(K):
            temp += pi[k] * gaussian(X[n], mean[k], cov[k])
        summation += np.log(temp)
    return summation

if __name__ == "__main__":
    data = np.genfromtxt("faithful.txt") #<class 'numpy.ndarray'>
    X = data[:, 0:2] #<class 'numpy.ndarray'>
    # print(type(data)) #<class 'numpy.ndarray'>
    # print(type(X))
    X = scale(X) 
    # print("scale", type(X)) #<class 'numpy.ndarray'>
    N = len(X)

    mean = np.random.rand(K, 2)
    #print("mean = ", mean)
    '''
    [[ 0.57562132  0.54919238]
     [ 0.60123221  0.31792234]
     [ 0.51873718  0.28652638]] 
    '''
    #print(shape(mean)) # (3, 2)
    cov = zeros( (K, 2, 2) )

    for k in range(K):
        cov[k] = [[1.0, 0.0], [0.0, 1.0]]
    #print(cov)
    #print(shape(cov)) # (3, 2, 2)
    '''
    [
     [[ 1.  0.]
      [ 0.  1.]]
     [[ 1.  0.]
      [ 0.  1.]]
     [[ 1.  0.]
      [ 0.  1.]]
    ]
    '''

    pi = np.random.rand(K)
    #print(pi)
    #print(shape(pi))
    gamma = zeros( (N, K) )

    like = likelihood(X, mean, cov, pi)
    print(like)
    print("like", shape(like))    

    turn = 0
    while True:
        print(turn) 
        print(like)

        for n in range(N):
            denominator = 0.0
            for j in range(K):
                denominator += pi[j] * gaussian(X[n], mean[j], cov[j])
            for k in range(K):
                gamma[n][k] = pi[k] * gaussian(X[n], mean[k], cov[k]) / denominator

        for k in range(K):
            Nk = 0.0
            for n in range(N):
                Nk += gamma[n][k]

            mean[k] = array([0.0, 0.0])
            for n in range(N):
                mean[k] += gamma[n][k] * X[n]
            mean[k] /= Nk

            cov[k] = array([[0.0,0.0], [0.0,0.0]])
            for n in range(N):
                temp = X[n] - mean[k]
                cov[k] += gamma[n][k] * matrix(temp).reshape(2, 1) * matrix(temp).reshape(1, 2)  # ?????x?????
            cov[k] /= Nk

            pi[k] = Nk / N

        new_like = likelihood(X, mean, cov, pi)
        diff = new_like - like
        if diff < 0.01:
            break
        like = new_like
        turn += 1

    for k in range(K):
        scatter(mean[k, 0], mean[k, 1], c='r', marker='o')

    xlist = np.linspace(-2.5, 2.5, 50)
    ylist = np.linspace(-2.5, 2.5, 50)
    x, y = np.meshgrid(xlist, ylist)
    for k in range(K):
        z = bivariate_normal(x, y, np.sqrt(cov[k,0,0]), np.sqrt(cov[k,1,1]), mean[k,0], mean[k,1], cov[k,0,1])
        cs = contour(x, y, z, 3, colors='k', linewidths=1)

    plot(X[:,0], X[:,1], 'gx')

    xlim(-2.5, 2.5)
    ylim(-2.5, 2.5)
    show()