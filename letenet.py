import numpy as np

def sigmoid(z):
    return 1/(1+np.exp(-z))

def AC(wK, wA, wP, factor):
    wA_aux = np.add(wA.dot(wK),wP)
    wA_new = []
    for activity in wA_aux:
        wA_new.append(sigmoid(activity))
    return np.multiply(wA_new, factor)

def plasticity(wK,wA, alfa):
    averA = sum(wA)/3
    for i in range(3):
        for j in range(3):
            delta = (wA[i]-averA)*(wA[j]-averA)
            wK[i][j]=wK[i][j] -(wK[i][j]- alfa*delta)/100
    return wK

if __name__ == "__main__":
    wA = np.random.uniform(-1/np.sqrt(3),1/np.sqrt(3),3)
    wK = np.random.rand(3,3)
    wP = [0,0,0]

    print "actividad inicial"
    print wA

    for i in range(1000):
        wA = AC(wK, wA, wP, 1)
        wK = plasticity(wK,wA,0.1)

    print "actividad luego de 1000 iteraciones"
    print wA
