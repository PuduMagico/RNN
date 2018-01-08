import numpy as np
import random
import neuron

class layer:
    def __init__(self, n_neurons, alpha):
        self.neurons = []
        for i in range(n_neurons):
            bias = random.uniform(0,1)
            activity = random.uniform(0,1)
            new_neuron = neuron.neuron(bias, activity, alpha)
            self.neurons.append(new_neuron)
        self.n_neurons = n_neurons

        self.is_first = False
        self.previous_layer = False
        self.next_layer = False

        self.last_output = []
        self.avg_activity = 0

    def connect_neurons(self, n_previous_neurons):
        for neuron in self.neurons:
            neuron.set_weights(n_previous_neurons)

    def feed(self, impulse):
        output = []
        for neuron in self.neurons:
            z = neuron.output(impulse)
            output.append(z)
        self.last_output = output

        sum_activity = 0
        for neuron in self.neurons:
            sum_activity += neuron.activity
        self.avg_activity = sum_activity/self.n_neurons

        if self.next_layer.is_first:
            pass
        else:
            self.next_layer.feed(self.last_output)

    def update_weights_layer(self):
        for neuron in self.neurons:
            neuron.update_weights_neuron(self.avg_activity, self.previous_layer.avg_activity, self.previous_layer.last_output)
