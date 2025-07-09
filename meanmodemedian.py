import random
import statistics
random_num = [random.randint(100,150)for i in range(100)]
print("Mean :")
print(statistics.mean(random_num))
print("Median :")
print(statistics.median(random_num))
print("Mode :")
print(statistics.mode(random_num))