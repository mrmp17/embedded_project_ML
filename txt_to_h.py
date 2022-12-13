import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time

class hls_weights:
    def txt_to_cpp(self):

        file1 = open("layer_1_weights.txt", "r")
        #print(file1.read())
        file2 = open("layer_2_weights.txt", "r")
        file3= open("layer_3_weights.txt", "r")

        outputfile = open("all_weights.h","w").close()
        outputfile = open("all_weights.h","w")
        outputfile.write('namespace weights{')
        outputfile.write('\n')
        outputfile.write('\tconst ap_fixed<32,24> layer3_weights[n_layer2][n_layer3] =')
        outputfile.write(file3.read(),)
        outputfile.write(';')

        outputfile.write('\n')
        outputfile.write('\tconst ap_fixed<32,24> layer2_weights[n_layer1][n_layer2] =')
        outputfile.write(file2.read(),)
        outputfile.write(';')

        outputfile.write('\n')
        outputfile.write('\tconst ap_fixed<32,24> layer1_weights[n_inputs][n_layer1] = ')
        outputfile.write(file1.read(),)
        outputfile.write(';')
        outputfile.write('\n')
        outputfile.write('}')

        outputfile.close()
        return "done"
        

