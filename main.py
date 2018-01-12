import net
import matplotlib.pyplot as plt
import numpy as np

# from __future__ import division, print_function

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.cm as cm

from matplotlib.collections import LineCollection
from matplotlib.ticker import MultipleLocator

def main():
    rnn = net.net(100)

    rnn.add_layer(40)
    rnn.add_layer(40)
    rnn.add_layer(40)

    rnn.close_cycle()
    rnn.connect_layers()

    print "Resumen de la red inicial"
    print "numero de capas: " + str(len(rnn.layers))
    print "-------------"
    print rnn.layers[0].last_output
    print rnn.layers[0].show_neuron_weights()

    print "----------"

    iters = 100
    for i in range(iters):
        rnn.one_cycle()
        rnn.update_weights_net()

    print "----------"

    print "Resumen de la red final"
    print rnn.layers[0].last_output
    print rnn.layers[0].show_neuron_weights()

    rnn.plot_activity_histogram()
    rnn.plot_neuron_activity_summary()
    rnn.pcolormesh_weights()


    print "the end"

if __name__ == "__main__":
    main()
