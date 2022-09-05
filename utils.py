from random import sample

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import random

data = pd.read_csv(r"C:\Users\admin\Downloads\Clt-data.csv")
print(data)

population_mean = data.mean()
# print(population_mean)   # here Population mean is 12.802049
plt.hist(data["Wall Thickness"])
plt.xlabel("Wall thickness")
plt.ylabel("Frequency")
plt.title("histogram of wall thickness")
plt.savefig(r"D:\code\Central_limit_theorem_application\histogram_of_wall_thickness")

sample_size = 100
# no_of_samples = 10
# no_of_samples = np.arange(100,2100,100)
no_of_samples=np.arange(10,110,10)
random_sample = []
mean_of_random_sample = []

for i in no_of_samples:
    for j in range(1, i):
        numbers = (random.choice(data["Wall Thickness"], sample_size,replace=True))
        mean = numbers.mean()
        random_sample.append(numbers)
        mean_of_random_sample.append(mean)
    #
    # print(random_sample)
    plt.clf()
    print(mean_of_random_sample)
    plt.hist(mean_of_random_sample)
    plt.xlabel("sample_mean_of_Wall thickness")
    plt.ylabel("Frequency")
    plt.title("histogram of mean_of_random_sample" +str(i))
    plt.savefig(r"D:\code\Central_limit_theorem_application\histogram_of_mean_of random_sample"+str(i)+".png")





#     plt.xlabel("sample_mean_of_Wall thickness")
#     plt.ylabel("Frequency")
#     plt.title("histogram of mean_of_random_sample")
# plt.savefig(r"D:\code\Central_limit_theorem_application\histogram_of_mean_of random_sample")


