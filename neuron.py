import numpy as np

class neuron:
    def __init__(self, bias, activity, alpha):
        self.weights = []
        self.bias = bias
        self.activity = activity
        self.alpha = alpha

    def output(self, impulse):
        z = np.add(sum(np.multiply(self.weights, impulse)), self.bias)
        new_activity = 1/(1+np.exp(z))
        self.activity = new_activity
        return self.activity

    def set_weights(self, n_previous_neurons):
        self.weights = np.random.uniform(0,1,n_previous_neurons)

    def update_weights_neuron(self, self_avg_activity, previous_avg_activity, previous_layer_output):
        for i in range(len(self.weights)):
            delta = (self.activity - self_avg_activity) * (previous_layer_output[i] - previous_avg_activity)
            self.weights[i] = self.weights[i] - (self.weights[i] - self.alpha*delta)/100
