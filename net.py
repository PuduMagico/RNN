import layer
import numpy as np
import matplotlib.pyplot as plt

class net:
    def __init__(self, alpha):
        self.layers = []
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

    #Funcion deprecada
    # def first_impulse(self):
    #     random_impulse = np.random.uniform(0,1,self.layers[-1].n_neurons)
    #     self.layers[0].feed(random_impulse)

    def one_cycle(self):
        # if not self.initialized:
        #     self.first_impulse()
        #     self.initialized = True
        # else:
        self.layers[0].feed(self.layers[-1].last_output)

    def update_weights_net(self):
        for layer in self.layers:
            layer.update_weights_layer()

    def add_activity_noise(self, noise):
        for layer in self.layers:
            layer.add_activity_noise(noise)

    def plot_activity_histogram(self):
        num_layers = len(self.layers)
        for i in range(num_layers):
            plt.subplot(1,num_layers,i+1)
            categories = ['0s', '1s']
            zeros = self.layers[i].last_output.count(0)
            ones =  self.layers[i].last_output.count(1)
            values = [zeros , ones]
            plt.bar(categories, values)
            plt.ylabel('Frecuencia')
            title = 'Layer ' + str(i)
            plt.title(title)
        plt.tight_layout()
        plt.show()

    # Aun no
    # def plot_weights_histogram(self):
    #     pass

    def pcolormesh_weights(self):
        num_layers = len(self.layers)
        for i in range(num_layers):
            plt.subplot(1,num_layers,i+1)
            final_weights = []
            for neuron in self.layers[i].neurons:
                final_weights.append(neuron.weights)
            plt.pcolormesh(final_weights)
            plt.colorbar()
            title = "Pesos Cruzados Layer " + str(i)
            plt.title(title)
        plt.tight_layout()
        plt.show()

    # Se puso dificil
    # def plot_neuron_activity_time(self, iters):
    #     num_layers = len(self.layers)
    #     max_num_neurons = 0
    #     for i in range(num_layers):
    #         if max_num_neurons < len(self.layers[i].neurons):
    #             max_num_neurons = len(self.layers[i].neurons)
    #
    #     x = np.linspace(0,iters,num = iters + 1)
    #     for i in range(num_layers*max_num_neurons):
    #         plt.subplot(num_layers, max_num_neurons, i+1)
    #         for j in range(len(self.layers[j].neurons)):
    #

    def plot_neuron_activity_summary(self):
        num_layers = len(self.layers)
        for i in range(num_layers):
            plt.subplot(num_layers,1,i+1)
            num_neurons = len(self.layers[i].neurons)
            x = np.linspace(1,num_neurons, num = num_neurons)
            activities = []
            for neuron in self.layers[i].neurons:
                activities.append(neuron.activity)
            plt.plot(x,activities)
            plt.ylabel('Actividad')
            plt.xlabel('Neuronas')
            title = "Actividad Layer " + str(i)
            plt.title(title)
        plt.tight_layout()
        plt.show()


    def summarize_info(self):
        pass
