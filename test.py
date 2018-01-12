import numpy as np

if __name__ == "__main__":
    n_neurons = 2
    matrix = np.random.rand(n_neurons,n_neurons)
    vector = np.random.rand(n_neurons)

    print matrix
    print vector
    print matrix.dot(vector)
