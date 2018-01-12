import numpy as np
import random
import neuron

class layer:
    def __init__(self, n_neurons, alpha):
        self.neurons = []
        self.last_output = []
        for i in range(n_neurons):
            bias = 0
            activity = np.divide(np.add(np.random.uniform(-1,1),1),10)
            self.last_output.append(activity)
            new_neuron = neuron.neuron(bias, activity, alpha)
            self.neurons.append(new_neuron)
        self.n_neurons = n_neurons

        self.is_first = False
        self.previous_layer = False
        self.next_layer = False
        self.avg_activity = 0

    def connect_neurons(self, n_previous_neurons):
        for neuron in self.neurons:
            neuron.set_weights(n_previous_neurons)

    def feed(self, activity):
        output = []
        for neuron in self.neurons:
            z = neuron.output(activity)
            output.append(z)
        self.last_output = output

        sum_activity = 0
        for neuron in self.neurons:
            sum_activity += neuron.activity
        self.avg_activity = sum_activity/(self.n_neurons*1.0)

        if self.next_layer.is_first:
            pass
        else:
            self.next_layer.feed(self.last_output)

    def update_weights_layer(self):
        for neuron in self.neurons:
            neuron.update_weights_neuron(self.avg_activity, self.previous_layer.avg_activity, self.previous_layer.last_output)

    def show_neuron_weights(self):
        for neuron in self.neurons:
            print neuron.weights

    def add_activity_noise(self, noise):
        for neuron in self.neurons:
            neuron.add_activity_noise(noise)
