import net

def main():
    rnn = net.net(0.01)

    rnn.add_layer(10)
#    rnn.add_layer(3)
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

    max_iters = 1000
    for i in range(max_iters):
        rnn.one_cycle()
        rnn.update_weights_net()
        
    print " ************************************* "

    print "Resumen de la red final"
    for i in range(len(rnn.layers)):
        print 'Capa numero ' + str(i)

        neuron_counter = 0
        for neuron in rnn.layers[i].neurons:
             print 'la neurona numero ' + str(neuron_counter) + " de esta capa tiene los siguientes parametros asociados:"
             print "Pesos (weights)"
             for weight in neuron.weights:
                 print str(weight)
             neuron_counter += 1
        print "----------"

    #Aqui viene lo de graficar resultados and so
    

if __name__ == "__main__":
    main()
