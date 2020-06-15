import sys, getopt
import numpy as np

from Models import model_one_NN
from Models import model_two_NN
from Algos import random_search
from Algos import genetic_search
from Algos import algo_tools
import random

def benchmark_random(model):
    algo = random_search.Random_search(model, 48)
    f = open("result_random.txt", "a")
    nb_seconds = 660
    while nb_seconds <= 1200 :
        #time = random.randint(2,60)
        time = nb_seconds
        algo.search(time)
        result = algo.get_best_configs(5)
        algo.clean_memory()
        f.write(str(time) + " " + str(result[0][2]) + str(result[0][0]) + "\n")
        nb_seconds += 60
    f.close()

def benchmark_genetic(model):
    f = open("result_genetic.txt", "a")
    nb_seconds = 2
    while nb_seconds <= 90:
        algo = genetic_search.Algo(model)
        algo.search(nb_seconds)
        result = algo.get_best_configs(1)
        f.write(str(nb_seconds) + " " + str(result[0].fitness_val) + " " + str(result[0].config) + "\n")
        nb_seconds += 2
    f.close()

def genetic_algorithm(model, nb_seconds):
        algo = genetic_search.Algo(model)
        algo.search(nb_seconds)
        result = algo.get_best_configs(1)
        print(str(result[0].fitness_val) + " " + str(result[0].config))
    

def main(argv):
    model = None
    try:
        opts, args = getopt.getopt(argv,"htu",["help", "train", "use", "experiment"])
    except getopt.GetoptError:
      print("Erreur d'arguments. Lancez script.py -h pour plus d'information.")
      sys.exit()
    for opt, arg in opts:
        if opt in ('-h', "-help"):
            print("Bienvenue dans l'aide de notre script")
            print("Si vous souhaitez entrainer un modele : main.py -train")
            print("Si vous souhaitez utiliser un modèle déjà entrainé : main.py -use")
            sys.exit()
        elif opt in ("-t", "-train"):
            #model = model_two_NN.Model_two_NN()
            model = model_one_NN.Model_one_NN()
            model.save()
    
    if model == None:
        #If we dont train it, then we load it from a file
        model = model_one_NN.Model_one_NN("model.h5")


    genetic_algorithm(model, 90)


if __name__ == "__main__":
    main(sys.argv[1:]) 