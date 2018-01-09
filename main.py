import net
import matplotlib.pyplot as plt
import numpy as np

def main():
    rnn = net.net(0.01)

    rnn.add_layer(20)
#   rnn.add_layer(3)
#    rnn.add_layer(1)

    rnn.close_cycle()
    rnn.connect_layers()

    print "Resumen de la red inicial"
    print "numero de capas: " + str(len(rnn.layers))
    print "-------------"
    for i in range(len(rnn.layers)):
        print 'la capa numero ' + str(i) + " " + 'tiene ' + str(rnn.layers[i].n_neurons) + " " + "neuronas"

        neuron_counter = 0
        for neuron in rnn.layers[i].neurons:
             print 'la neurona numero ' + str(neuron_counter) + " de esta capa tiene los siguientes parametros asociados:"
             print "Pesos (weights)"
             for weight in neuron.weights:
                 print str(weight)
             neuron_counter += 1
        print "----------"



    max_iters = 5
    for i in range(max_iters):
        rnn.one_cycle()
        rnn.update_weights_net()

    layer1_initial_activity = rnn.layers[0].last_output
    # layer2_activity = rnn.layers[1].last_output


    print " ************************************* "

    # print "Resumen de la red actual"
    # for i in range(len(rnn.layers)):
    #     print 'Capa numero ' + str(i)
    #     print "Output final de la capa (actividad)"
    #     print rnn.layers[i].last_output
    #
    #     neuron_counter = 0
    #     for neuron in rnn.layers[i].neurons:
    #          print 'la neurona numero ' + str(neuron_counter) + " de esta capa tiene los siguientes parametros asociados:"
    #          print "Pesos (weights)"
    #          for weight in neuron.weights:
    #              print str(weight)
    #          neuron_counter += 1
    #     print "----------"
    #
    # print " ************************************* "

    max_iters = 10000
    for i in range(max_iters):
        rnn.one_cycle()
        rnn.update_weights_net()

    print "Resumen de la red final"

    final_weights = []
    for i in range(len(rnn.layers)):
        print 'Capa numero ' + str(i)
        print "Output final de la capa (actividad)"
        print rnn.layers[i].last_output

        neuron_counter = 0
        for neuron in rnn.layers[i].neurons:
             print 'la neurona numero ' + str(neuron_counter) + " de esta capa tiene los siguientes parametros asociados:"
             print "Pesos (weights)"
             final_weights.append(neuron.weights)

             for weight in neuron.weights:
                 print str(weight)
             neuron_counter += 1
        print "----------"

    print "************************"

    print "plot section"
    layer1_final_activity = rnn.layers[0].last_output


    plt.subplot(2, 1, 1)
    x = np.linspace(0,1,20)
    plt.plot(x,layer1_initial_activity, label ="initial activity")
    plt.plot(x,layer1_final_activity, label ="final activity")
    plt.xlabel('Neuronas')
    plt.ylabel('Actividad')

    plt.title("test")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.pcolormesh(final_weights)

    plt.show()
    print "the end"

if __name__ == "__main__":
    main()
