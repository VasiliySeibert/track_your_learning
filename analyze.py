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
path = pathlib.Path(__file__).parent.absolute() # works only with python skript
# path = "/Users/vs21/track_your_learning" # for notebook

def read_csv(path):
    # reads the study csv and returns a list with dict
    collect = []

    with open (path, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            collect.append(row)

    return collect


def write_new_file(path, questions):
    with open (path, "w", newline="") as file:
        fieldnames = list(questions[0])
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for question in questions:
            print(question)
            writer.writerow(question)


def find_directories(path):
    collect = []
    for dirs in os.walk(path):
        dir_ = dirs[0]
        if "." not in dir_:
            collect.append(dir_)  

    return collect


def check_for_studyFile(path):
    # check in for loop if there is a study.csv 
    for element in os.listdir(path):
        if element == "study.csv": return True

def find_all_studyFiles(path):
    collect = []
    for dir in find_directories("/Users/vs21/track_your_learning/data"):
        if check_for_studyFile(dir) == True:
            collect.append(dir + "/study.csv")
            
    return collect

def analyze_studyFiles(all_studyFiles):
    collect = []

    for studyFile in find_all_studyFiles(path):
        all_questions = read_csv(studyFile)
        x = list(all_questions[0])[3:]
        collect_ = []
        for _ in x:
            y = [] 
            for element in all_questions:
                y.append(element[_])
            all_f = y.count('f')
            all_t = y.count('t')
            collect_.append(all_t / (all_t + all_f))
        collect.append({"file":studyFile, "x":x, "y":collect_})
            
    return collect


def plot_learningProgress(study_file):

    title = study_file["file"].replace(str(path), "").replace("study.csv", "")

    x = study_file["x"]
    y = study_file["y"]

    plt.title(title) 
    plt.ylim(-0.1,1.1)
    plt.plot(x, y)
    plt.xticks(rotation=90)

    plt.savefig(study_file["file"].replace("study.csv", "learning_progress.pdf"))
    plt.close()


if __name__ == "__main__":
    all_dir = find_directories(path)
    study_files = analyze_studyFiles(all_dir)
    for study_file in study_files:
        plot_learningProgress(study_file)
