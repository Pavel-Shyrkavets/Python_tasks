import matplotlib.pyplot as plt
import numpy as np

def plot():
    #plot 1:
    x1 = np.array([2, 0, 0, 2])
    y1 = np.array([0, 0, 8, 8])
    x2 = np.array([0, 2])
    y2 = np.array([4, 4])
    font1 = {'family': 'serif', 'color': 'blue', 'size': 20}

    plt.subplot(1, 4, 1)
    plt.title('Matplotlib, NumPy &', loc='left', fontdict=font1)
    plt.plot(x1, y1, 'c', x2, y2, 'c', lw='10')

    #plot 2:
    x1 = np.array([0, 0, 2, 2, 0])
    y1 = np.array([0, 8, 8, 4, 4])

    plt.subplot(1, 4, 2)
    plt.plot(x1, y1, 'c', lw='10')

    #plot 3:
    x1 = np.array([0, 1, 2])
    y1 = np.array([0, 8, 0])
    x2 = np.array([0.5, 1.5])
    y2 = np.array([4, 4])

    plt.subplot(1, 4, 3)
    plt.plot(x1, y1, 'c', x2, y2, 'c', lw='10')

    #plot 4:
    x1 = np.array([0, 0, 1, 2, 2])
    y1 = np.array([0, 8, 0, 8, 0])
    font1 = {'family': 'serif', 'color': 'red', 'size': 20}

    plt.subplot(1, 4, 4)
    plt.xlabel('FOREVER', loc='left', fontdict=font1)
    plt.plot(x1, y1, 'c', lw='10')

    #all plots:
    plt.show()
