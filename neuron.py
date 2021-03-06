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
        if new_activity < 0.0001:
            new_activity = 0
        elif new_activity > 0.9999:
            new_activity = 1
        self.activity_log.append(new_activity)
        # new_activity = z
        self.activity = new_activity
        return self.activity

    #Inicializacion de Pesos
    def set_weights(self, n_previous_neurons):
        # self.weights = np.random.uniform(-1/np.sqrt(n_previous_neurons),1/np.sqrt(n_previous_neurons),n_previous_neurons)
        self.weights = np.random.uniform(-1,1,n_previous_neurons)

    #Actualizacion de Pesos
    #Toma como parametros el promedio de actividad en la capa, el promedio de actividad en la capa anterior
    #y la actividad de la capa anterior.
    def update_weights_neuron(self, self_avg_activity, previous_avg_activity, previous_layer_output):
        delta_array = []
        for i in range(len(self.weights)):
            delta = np.multiply((self.activity - self_avg_activity), (previous_layer_output[i] - previous_avg_activity))
            delta_array.append(delta)
            self.weights[i] = self.weights[i] - (self.weights[i] - self.alpha*delta)/100
        self.delta_log.append(delta_array)

    def add_activity_noise(self, noise):
        self.activity += np.random.normal(0,noise)
         
