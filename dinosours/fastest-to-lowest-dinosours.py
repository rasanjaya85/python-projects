#! /usr/bin/python

import math
import csv

bipedal_dinosaurs = {}
g = 9.8


def fastestToSlowDinosours(filePathDinoInfo, filePathAddInfo, stance):
    try:
        with open(filePathAddInfo, 'r') as file:
            dataset2 = csv.reader(file)
            for line in dataset2:
                NAME, STRIDE_LENGTH, STANCE = line
                if STANCE == stance:
                    bipedal_dinosaurs[NAME] = float(STRIDE_LENGTH)

        with open(filePathDinoInfo, 'r') as file:
            dataset1 = csv.reader(file)
            for line in dataset1:
                NAME, LEG_LENGTH, DIET = line
                if NAME in bipedal_dinosaurs:
                    STRIDE_LENGTH = bipedal_dinosaurs[NAME]
                    LEG_LENGTH = float(LEG_LENGTH)
                    bipedal_dinosaurs[NAME] = abs((STRIDE_LENGTH / LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * g)

        for name, speed in (sorted(bipedal_dinosaurs.items(), key=lambda x: x[1], reverse=True)):
            print(name)
    finally:
        file.close()


fastestToSlowDinosours('dataset1.csv', 'dataset2.csv', "bipedal")
