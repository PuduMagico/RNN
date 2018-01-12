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

    rnn.add_layer(10)
    rnn.add_layer(10)
    rnn.add_layer(10)

    rnn.close_cycle()
    rnn.connect_layers()

    # rnn.summarize_info()

    iters = 100
    for i in range(iters):
        rnn.one_cycle()
        rnn.update_weights_net()

    # rnn.summarize_info()

    # rnn.plot_activity_histogram()
    rnn.plot_neuron_activity_summary()
    # rnn.pcolormesh_weights()
    # rnn.plot_neuron_activity_time(iters)

    rnn.add_activity_noise(0.5)

    rnn.plot_neuron_activity_summary()

    iters = 10
    for i in range(iters):
        rnn.one_cycle()
        rnn.update_weights_net()

    rnn.plot_neuron_activity_summary()

    print "the end"

if __name__ == "__main__":
    main()
