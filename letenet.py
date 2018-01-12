import numpy as np

def sigmoid(z):
    return 1/(1+np.exp(-z))

def AC(wK, wA, wP, factor):
    wA_aux = np.add(wA.dot(wK),wP)
    wA_new = []
    for activity in wA_aux:
        wA_new.append(sigmoid(activity))
    return np.multiply(wA_new, factor)

def plasticity(wK,wA, alfa, n_neurons):
    averA = sum(wA)/n_neurons
    for i in range(n_neurons):
        for j in range(n_neurons):
            delta = (wA[i]-averA)*(wA[j]-averA)
            wK[i][j]=wK[i][j] -(wK[i][j]- alfa*delta)/100
    return wK

if __name__ == "__main__":

    n_neurons = 3

    wA = np.divide(np.add(np.random.uniform(-1,1,n_neurons),1),10)

    wK = np.subtract(np.random.rand(n_neurons,n_neurons),0.5)
    wP = np.zeros(n_neurons)

    print "actividad inicial"
    print wA
    print "pesos iniciales"
    print wK

    for i in range(100):
        wA = AC(wK, wA, wP, 1)
        wK = plasticity(wK,wA,100,n_neurons)
    # print "actividad de patada inicial"
    # wA = AC(wK, wA, wP, 0.01)
    #
    # print wA
    #
    # wA = AC(wK, wA, wP, 1)
    # wK = plasticity(wK,wA,0.1,n_neurons)
    #
    # print "actividad 2"
    # print wA
    # print "pesos 2"
    # print wK
    #
    # wA = AC(wK, wA, wP, 1)
    # wK = plasticity(wK,wA,0.1,n_neurons)
    #
    # print "actividad 3"
    # print wA
    # print "pesos 3"
    # print wK
    #
    # wA = AC(wK, wA, wP, 1)
    # wK = plasticity(wK,wA,0.1,n_neurons)
    #
    # print "actividad 4"
    # print wA
    # print "pesos 4"
    # print wK
    #
    # wA = AC(wK, wA, wP, 1)
    # wK = plasticity(wK,wA,0.1,n_neurons)

    print "actividad final"
    print wA
    print "pesos finales"
    print wK
