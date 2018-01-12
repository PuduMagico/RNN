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

    rnn.add_layer(3)
    # rnn.add_layer(5)
    # rnn.add_layer(5)

    rnn.close_cycle()
    rnn.connect_layers()

    neuron0_weights = []
    neuron1_weights = []
    neuron2_weights = []

    #
    #

    print "Resumen de la red inicial"
    print "numero de capas: " + str(len(rnn.layers))
    print "-------------"
    print rnn.layers[0].last_output
    print rnn.layers[0].show_neuron_weights()
    # for i in range(len(rnn.layers)):
    #     print 'la capa numero ' + str(i) + " " + 'tiene ' + str(rnn.layers[i].n_neurons) + " " + "neuronas"
    #     print "Output inicial de la capa (actividad)"
    #     print rnn.layers[i].last_output
    #     neuron_counter = 0
    #     for j in range(len(rnn.layers[0].neurons)):
    #         if j == 0:
    #             neuron0_weights.append(rnn.layers[0].neurons[0].weights)
    #         elif j == 1:
    #             neuron1_weights.append(rnn.layers[0].neurons[1].weights)
    #         else:
    #             neuron2_weights.append(rnn.layers[0].neurons[2].weights)
    #
    #     for neuron in rnn.layers[i].neurons:
    #          print 'la neurona numero ' + str(neuron_counter) + " de esta capa tiene los siguientes parametros asociados:"
    #          print "Pesos (weights)"
    #          print neuron.weights
    #          # for weight in neuron.weights:
    #          #     print str(weight)
    #          neuron_counter += 1
    print "----------"

    # max_iters = 1
    # for i in range(max_iters):
    #     for j in range(len(rnn.layers[0].neurons)):
    #         if j == 0:
    #             # neuron0_weights.append(rnn.layers[0].neurons[0].weights)
    #             neuron0_activity.append()
    #         elif j == 1:
    #             # neuron1_weights.append(rnn.layers[0].neurons[1].weights)
    #         else:
    #             # neuron2_weights.append(rnn.layers[0].neurons[2].weights)
    #     rnn.one_cycle()
    #     rnn.update_weights_net()
    #
    # layer1_initial_activity = rnn.layers[0].last_output
    # # layer2_initial_activity = rnn.layers[1].last_output
    # # layer3_initial_activity = rnn.layers[2].last_output
    #
    #
    # print " ************************************* "
    #

    # rnn.kickstarter()

    iters = 10

    for i in range(iters):
        rnn.one_cycle()
        rnn.update_weights_net()

    #
    # # print "Resumen de la red actual"
    # # for i in range(len(rnn.layers)):
    # #     print 'Capa numero ' + str(i)
    # #     print "Output final de la capa (actividad)"
    # #     print rnn.layers[i].last_output
    # #
    # #     neuron_counter = 0
    # #     for neuron in rnn.layers[i].neurons:
    # #          print 'la neurona numero ' + str(neuron_counter) + " de esta capa tiene los siguientes parametros asociados:"
    # #          print "Pesos (weights)"
    # #          for weight in neuron.weights:
    # #              print str(weight)
    # #          neuron_counter += 1
    # #     print "----------"
    # #
    # # print " ************************************* "
    #
    # max_iters = 10000
    # for i in range(max_iters):
    #     rnn.one_cycle()
    #     rnn.update_weights_net()
    #
    print "Resumen de la red final"

    print rnn.layers[0].last_output
    print rnn.layers[0].show_neuron_weights()
    #
    # final_weights = []
    # for i in range(len(rnn.layers)):
    #     print 'Capa numero ' + str(i)
    #     print "Output final de la capa (actividad)"
    #     print rnn.layers[i].last_output
    #
    #     neuron_counter = 0
    #     for neuron in rnn.layers[i].neurons:
    #          print 'la neurona numero ' + str(neuron_counter) + " de esta capa tiene los siguientes parametros asociados:"
    #          print "Pesos (weights)"
    #          final_weights.append(neuron.weights)
    #
    #          for weight in neuron.weights:
    #              print str(weight)
    #          neuron_counter += 1
    #     print "----------"
    #
    # print "************************"
    #
    # print "plot section"
    # layer1_final_activity = rnn.layers[0].last_output
    # layer2_final_activity = rnn.layers[1].last_output
    # layer3_final_activity = rnn.layers[2].last_output
    sum_delta_log = []


    for i in range(iters-1):
        sum_delta = 0
        for j in range(3):
            sum_delta += sum(rnn.layers[0].neurons[j].delta_log[i])
        sum_delta_log.append(sum_delta)


    plt.subplot(4, 1, 1)
    x = np.linspace(0,iters,num = iters + 1)
    plt.plot(x,rnn.layers[0].neurons[0].activity_log, '--', label ="activityg")
    # plt.plot(x,layer2_initial_activity, '--', label ="initial activity layer 2")
    # plt.plot(x,layer3_initial_activity, '--', label ="initial activity layer 3")
    # plt.plot(x,layer1_final_activity, '-', label ="final activity layer 1")
    # plt.plot(x,layer2_final_activity, '-', label ="final activity layer 2")
    # plt.plot(x,layer3_final_activity, '-', label ="final activity layer 3")
    plt.xlabel('Iteracion')
    plt.ylabel('Actividad')

    plt.title("Actividad Neurona 1")
    plt.legend()

    plt.subplot(4, 1, 2)
    plt.plot(x,rnn.layers[0].neurons[1].activity_log, '--', label ="activity")
    # plt.plot(x,layer2_initial_activity, '--', label ="initial activity layer 2")
    # plt.plot(x,layer3_initial_activity, '--', label ="initial activity layer 3")
    # plt.plot(x,layer1_final_activity, '-', label ="final activity layer 1")
    # plt.plot(x,layer2_final_activity, '-', label ="final activity layer 2")
    # plt.plot(x,layer3_final_activity, '-', label ="final activity layer 3")
    plt.xlabel('Iteracion')
    plt.ylabel('Actividad')

    plt.title("Actividad Neurona 2")
    plt.legend()

    plt.subplot(4, 1, 3)
    plt.plot(x,rnn.layers[0].neurons[2].activity_log, '--', label ="activity")
    # plt.plot(x,layer2_initial_activity, '--', label ="initial activity layer 2")
    # plt.plot(x,layer3_initial_activity, '--', label ="initial activity layer 3")
    # plt.plot(x,layer1_final_activity, '-', label ="final activity layer 1")
    # plt.plot(x,layer2_final_activity, '-', label ="final activity layer 2")
    # plt.plot(x,layer3_final_activity, '-', label ="final activity layer 3")
    plt.xlabel('Iteracion')
    plt.ylabel('Actividad')

    plt.title("Actividad Neurona 3")
    plt.legend()

    plt.subplot(4, 1, 4)
    x = np.linspace(0,iters,num = iters-1)
    plt.plot(x,sum_delta_log, '--', label ="delta")
    plt.xlabel('Iteracion')
    plt.ylabel('Suma de Deltas')

    plt.title("Deltas")
    plt.legend()


    # plt.subplot(2, 1, 2)

    # plt.pcolormesh(final_weights)
    # plt.axis([1,5,1,5])

    # Plot the EEG

    # numSamples, numRows = 101, 3
    # data = []
    # for i in range(3):
    #     data.append(rnn.layers[0].neurons[i].activity_log)
    # data = np.array(data)
    # data.shape = (numSamples, numRows)
    # # print data
    # t =  100*np.arange(numSamples) / numSamples
    #
    # fig = plt.figure("MRI_with_EEG")
    #
    # ticklocs = []
    # ax2 = fig.add_subplot(2, 1, 2)
    # ax2.set_xlim(0, 100)
    # ax2.set_xticks(np.arange(100))
    # dmin = data.min()
    # dmax = data.max()
    # dr = (dmax - dmin) * 0.7  # Crowd them a bit.
    # y0 = dmin
    # y1 = (numRows - 1) * dr + dmax
    # ax2.set_ylim(y0, y1)
    #
    # segs = []
    # for i in range(numRows):
    #     segs.append(np.hstack((t[:, np.newaxis], data[:, i, np.newaxis])))
    #     ticklocs.append(i * dr)
    #
    # offsets = np.zeros((numRows, 2), dtype=float)
    # offsets[:, 1] = ticklocs
    #
    # lines = LineCollection(segs, offsets=offsets, transOffset=None)
    # ax2.add_collection(lines)
    #
    # # Set the yticks to use axes coordinates on the y axis
    # ax2.set_yticks(ticklocs)
    # ax2.set_yticklabels(['PG3', 'PG5', 'PG7'])
    #
    plt.tight_layout()

    plt.show()
    print "the end"
    #
    # print neuron0_weights
    # print neuron1_weights
    # print neuron2_weights

if __name__ == "__main__":
    main()
