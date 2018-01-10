import numpy as np

class neuron:
    def __init__(self, bias, activity, alpha):
        self.weights = []
        self.bias = bias
        self.activity = activity
        self.alpha = alpha
        self.activity_log = []
        self.activity_log.append(self.activity)
        self.delta_log = []

    def output(self, previous_layer_activity):
        z = np.add(sum(np.multiply(self.weights, previous_layer_activity)), self.bias)
        new_activity = 1/(1+np.exp(-z))
        self.activity_log.append(new_activity)
        # new_activity = z
        self.activity = new_activity
        return self.activity

    #Inicializacion de Pesos
    #https://isaacchanghau.github.io/2017/05/24/Weight-Initialization-in-Artificial-Neural-Networks/
    def set_weights(self, n_previous_neurons):
        self.weights = np.random.uniform(-1/np.sqrt(n_previous_neurons),1/np.sqrt(n_previous_neurons),n_previous_neurons)

    #Actualizacion de Pesos
    #Toma como parametros el promedio de actividad en la capa, el promedio de actividad en la capa anterior
    #y la actividad de la capa anterior.
    def update_weights_neuron(self, self_avg_activity, previous_avg_activity, previous_layer_output):
        delta_array = []
        for i in range(len(self.weights)):
            delta = np.multiply((self.activity - 0), (previous_layer_output[i] - 0))
            delta_array.append(delta)
            self.weights[i] = self.weights[i] - (self.weights[i] - self.alpha*delta)/100
        self.delta_log.append(delta_array)
