import csv
import pandas
import numpy as np
import matplotlib.pyplot as plt
import pathlib
import json
import os
import time
import random
import sys

current_date = f"{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday}"

try:
    SHUFFLE = sys.argv[1]
except:
    SHUFFLE = "False"

path = pathlib.Path(__file__).parent.absolute()
path_study_file = str(path) + "/study.csv"


def read_csv(path):
    # reads the study csv and returns a list with dict
    collect = []

    with open (path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            collect.append(row)

    return collect


def learning(questions, SHUFFLE, current_date):
    
    if SHUFFLE == "True":
        random.shuffle(questions)
    
    for idx, question in enumerate(questions):
        os.system('cls' if os.name == 'nt' else 'clear') # clears the console
        print(f"Question : {question['question']}")
        result = input("Did you get it right? (t/f) : ")
        question[current_date] = result

    return sorted(questions, key=lambda k: k["id"])

def write_new_file(path, questions):
    with open (path, "w", newline="") as file:
        fieldnames = list(questions[0])
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for question in questions:
            print(question)
            writer.writerow(question)


if __name__ == "__main__":
    questions = read_csv(path_study_file)
    questions = learning(questions, SHUFFLE, current_date)
    write_new_file(path_study_file, questions)






    


