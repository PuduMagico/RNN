import layer
import numpy as np

class net:
    def __init__(self, alpha):
        self.layers = []
        self.initialized = False
        self.alpha = alpha

    def add_layer(self, n_neurons):
        new_layer = layer.layer(n_neurons, self.alpha)
        if len(self.layers) == 0:
            new_layer.is_first = True
        else:
            #conectar layers
            new_layer.previous_layer = self.layers[-1]
            self.layers[-1].next_layer = new_layer
        self.layers.append(new_layer)

    def close_cycle(self):
        self.layers[-1].next_layer = self.layers[0]
        self.layers[0].previous_layer = self.layers[-1]

    #Funcion que conecta todas las capas de manera consecutiva.
    #La capa final se conecta con la primera
    def connect_layers(self):

        for layer in self.layers:
            n_previous_neurons = layer.previous_layer.n_neurons
            layer.connect_neurons(n_previous_neurons)

    def first_impulse(self):
        random_impulse = np.random.uniform(0,1,self.layers[-1].n_neurons)
        self.layers[0].feed(random_impulse)

    def one_cycle(self):
        if not self.initialized:
            self.first_impulse()
            self.initialized = True
        else:
            self.layers[0].feed(self.layers[-1].last_output)

    def update_weights_net(self):
        for layer in self.layers:
            layer.update_weights_layer()
