import numpy as np
from pylab import *
from numpy import array
import matplotlib.pyplot as plt

def main():
    #impl
    xlist = np.linspace(-10, 10, 1001)
    print(xlist)
    print(type(xlist))
    mean = 0
    sigma = 1
    ylist = np.subtract(xlist, mean)
    print('ylist ', type(ylist))
    ylist = np.square(ylist)
    print(ylist)
    ylist = ylist/(2*square(sigma))
    ylist = ylist*(-1)
    print(ylist)
    ylist = np.exp(ylist)
    print(ylist)
    ylist = ylist*(1/(sqrt(2*np.pi*square(sigma))))
    plt.plot(xlist, ylist, 'g-')

    #ref answer
    mu = 0
    sigma = 2
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    plt.plot(x,mlab.normpdf(x, mu, sigma), 'r-')
    plt.show()

if __name__ == "__main__":
    main()