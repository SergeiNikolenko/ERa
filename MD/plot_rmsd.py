
import os
import re
import pandas as pd
import matplotlib.pyplot as plt

def extract_labels(file_name):
    title = None
    xlabel = None
    ylabel = None

    with open(file_name, "r") as file:
        for line in file:
            if re.match(r"@ *title", line):
                title = re.sub(r"@ *title *\"", "", line).strip().strip("\"")
            elif re.match(r"@ *xaxis", line):
                xlabel = re.sub(r"@ *xaxis *label *\"", "", line).strip().strip("\"")
            elif re.match(r"@ *yaxis", line):
                ylabel = re.sub(r"@ *yaxis *label *\"", "", line).strip().strip("\"")
                
    return title, xlabel, ylabel

folder_path = "."  
xvg_files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1] == ".xvg"]

print("Найдены следующие файлы .xvg:")
for i, f in enumerate(xvg_files):
    print(f"{i + 1}. {f}")

file_number = int(input("Введите номер нужного файла: "))
file_name = xvg_files[file_number - 1]

if not os.path.isfile(file_name):
    print("Файл не найден. Пожалуйста, проверьте имя файла и повторите попытку.")
else:
    title, xlabel, ylabel = extract_labels(file_name)
    
    data = pd.read_csv(file_name, skiprows=17, delimiter="\s+", header=None, names=[xlabel, ylabel], comment="@")
    print(data.head())

    plt.figure(figsize=(12, 6))
    
    # Убираем линии и оставляем только точки на графике для файлов с названием clusters_dist.xvg
    if file_name.endswith("_clid.xvg"):
        plt.plot(data[xlabel], data[ylabel], marker="o", markersize=2, linestyle="", color ="black")
    else:
        plt.plot(data[xlabel], data[ylabel], marker="o", markersize=1, linestyle="-", linewidth=0.5)

    #2plt.ylim(0.1, 0.4)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()
