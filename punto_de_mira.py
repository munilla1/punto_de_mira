import matplotlib.pyplot as plt

def punto_mira():
    plt.plot([3], [3], 'k+')
    plt.plot([-2], [5], 'k+')
    plt.plot([-3], [3], 'k+')
    plt.plot([-1], [0], 'k+')
    plt.ylabel('Y')
    plt.ylabel('X')
    plt.show()
punto_mira()