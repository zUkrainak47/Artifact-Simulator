# Add your list of CV values and change sample_size, from_cv, to_cv and set days to the name of your list
# do not touch anything below that :)


import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys


# days_50_old =  [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.01, 1.01, 1.0, 1.0, 1.01, 1.01, 1.0, 1.0, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.02, 1.01, 1.01, 1.02, 1.02, 1.01, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.05, 1.05, 1.05, 1.05, 1.05, 1.06, 1.05, 1.05, 1.09, 1.1, 1.09, 1.1, 1.09, 1.1, 1.09, 1.1, 1.15, 1.15, 1.14, 1.14, 1.15, 1.16, 1.15, 1.15, 1.2, 1.21, 1.2, 1.2, 1.2, 1.2, 1.2, 1.22, 1.24, 1.23, 1.24, 1.23, 1.23, 1.24, 1.24, 1.25, 1.27, 1.26, 1.27, 1.27, 1.25, 1.26, 1.27, 1.29, 1.3, 1.29, 1.29, 1.29, 1.29, 1.3, 1.33, 1.36, 1.37, 1.34, 1.35, 1.34, 1.36, 1.36, 1.45, 1.44, 1.46, 1.45, 1.46, 1.45, 1.46, 1.46, 1.63, 1.59, 1.59, 1.62, 1.61, 1.62, 1.6, 1.62, 1.82, 1.81, 1.83, 1.81, 1.83, 1.81, 1.81, 1.84, 2.05, 2.04, 2.07, 2.05, 2.03, 2.03, 2.04, 2.14, 2.28, 2.24, 2.29, 2.27, 2.29, 2.3, 2.28, 2.32, 2.44, 2.44, 2.42, 2.43, 2.43, 2.43, 2.47, 2.52, 2.62, 2.57, 2.59, 2.63, 2.63, 2.59, 2.72, 2.8, 2.83, 2.84, 2.8, 2.85, 2.82, 2.82, 3.07, 3.13, 3.22, 3.15, 3.14, 3.12, 3.14, 3.15, 3.61, 3.66, 3.68, 3.69, 3.7, 3.68, 3.66, 3.69, 4.37, 4.46, 4.42, 4.38, 4.42, 4.44, 4.41, 4.48, 5.52, 5.52, 5.36, 5.44, 5.47, 5.46, 5.44, 5.61, 6.6, 6.62, 6.55, 6.71, 6.67, 6.82, 6.66, 6.82, 7.97, 7.93, 8.03, 7.9, 8.16, 8.0, 8.05, 8.54, 9.16, 9.07, 9.14, 9.11, 9.12, 9.2, 9.42, 9.91, 10.46, 10.41, 10.51, 10.52, 10.38, 10.38, 11.1, 11.84, 11.91, 12.09, 12.01, 11.95, 12.01, 12.26, 13.46, 14.1, 14.28, 14.43, 14.34, 14.58, 14.52, 14.33, 17.62, 18.12, 18.69, 18.35, 18.38, 18.33, 18.34, 18.39, 24.26, 24.71, 24.73, 24.66, 24.28, 24.63, 24.65, 25.17, 33.74, 34.31, 34.05, 34.41, 34.98, 34.96, 33.94, 37.0, 50.1, 50.85, 50.49, 49.35, 50.38, 50.38, 49.88, 55.26, 72.73, 71.65, 72.18, 72.05, 71.92, 73.4, 71.7, 82.54, 97.43, 99.95, 98.17, 97.5, 97.63, 97.97, 101.52, 114.61, 128.52, 128.27, 129.19, 126.78, 125.42, 128.8, 136.72, 155.67, 164.06, 162.12, 165.35, 161.62, 161.97, 162.86, 190.58, 208.24, 207.5, 209.67, 213.05, 205.49, 207.52, 208.7, 270.59, 283.95, 278.41, 282.72, 281.82, 283.63, 284.88, 292.23, 405.73, 418.63, 412.87, 409.55, 416.36, 416.93, 409.59, 439.13, 645.49, 653.76, 666.08, 664.56, 663.02, 665.17, 666.07, 745.09, 1172.6, 1159.91, 1183.55, 1159.68, 1187.29, 1183.31, 1181.72, 1437.79, 2342.66, 2327.63]
days_52_5_1750 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.12, 1.12, 1.12, 1.12, 1.12, 1.12, 1.12, 1.12, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13, 1.15, 1.15, 1.15, 1.15, 1.15, 1.15, 1.15, 1.16, 1.17, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.2, 1.21, 1.21, 1.21, 1.21, 1.21, 1.21, 1.21, 1.28, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.41, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.58, 1.78, 1.78, 1.78, 1.78, 1.78, 1.78, 1.78, 1.84, 1.95, 1.96, 1.96, 1.96, 1.96, 1.96, 1.97, 2.05, 2.14, 2.14, 2.14, 2.14, 2.14, 2.14, 2.16, 2.24, 2.28, 2.28, 2.28, 2.28, 2.28, 2.28, 2.39, 2.48, 2.52, 2.52, 2.52, 2.52, 2.52, 2.52, 2.75, 2.82, 2.83, 2.83, 2.83, 2.83, 2.83, 2.83, 3.21, 3.27, 3.27, 3.27, 3.27, 3.27, 3.27, 3.28, 3.98, 4.02, 4.02, 4.02, 4.02, 4.02, 4.02, 4.11, 5.04, 5.05, 5.05, 5.05, 5.05, 5.05, 5.05, 5.16, 6.14, 6.18, 6.18, 6.18, 6.18, 6.18, 6.18, 6.49, 7.44, 7.46, 7.46, 7.46, 7.46, 7.46, 7.55, 8.17, 8.88, 8.88, 8.88, 8.88, 8.88, 8.88, 9.17, 9.79, 10.19, 10.19, 10.19, 10.19, 10.19, 10.19, 10.79, 11.58, 11.81, 11.81, 11.81, 11.81, 11.81, 11.81, 13.41, 13.88, 14.02, 14.02, 14.02, 14.02, 14.02, 14.02, 17.01, 17.56, 17.56, 17.56, 17.56, 17.56, 17.56, 17.78, 22.46, 22.9, 22.9, 22.9, 22.9, 22.9, 22.9, 23.49, 32.07, 32.28, 32.28, 32.28, 32.28, 32.28, 32.28, 34.38, 45.75, 46.08, 46.08, 46.08, 46.08, 46.08, 46.08, 52.26, 67.35, 67.48, 67.48, 67.48, 67.48, 67.48, 67.86, 77.27, 91.4, 91.4, 91.4, 91.4, 91.4, 91.4, 94.53, 108.14, 119.42, 119.42, 119.42, 119.42, 119.42, 119.42, 132.09, 149.83, 156.25, 156.25, 156.25, 156.25, 156.25, 156.25, 182.42, 192.73, 197.87, 197.87, 197.87, 197.87, 197.87, 198.88, 259.46, 270.17, 270.17, 270.17, 270.17, 270.17, 270.17, 277.93, 383.05, 392.71, 392.71, 392.71, 392.71, 392.71, 392.71, 416.0, 609.81, 617.48, 617.48, 617.48, 617.48, 617.48, 617.48, 699.25, 1099.82, 1105.49, 1105.49, 1105.49, 1105.49, 1105.49, 1106.48, 1335.37, 2182.52, 2182.6, 2182.6, 2182.6, 2182.6, 2182.6, 2182.6, 3045.84, 5076.96, 5076.96, 5076.96, 5076.96, 5076.96, 5076.96, 5080.58, 8333.89, 13308.91, 13308.91, 13308.91, 13308.91, 13308.91, 13308.91, 13468.8, 29001.69, 46549.06, 46549.06, 46549.06]
days_52_10000 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.12, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13, 1.14, 1.15, 1.15, 1.15, 1.15, 1.15, 1.15, 1.16, 1.17, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.2, 1.22, 1.22, 1.22, 1.22, 1.22, 1.22, 1.22, 1.31, 1.31, 1.31, 1.31, 1.31, 1.31, 1.31, 1.31, 1.43, 1.44, 1.44, 1.44, 1.44, 1.44, 1.44, 1.44, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.61, 1.81, 1.81, 1.81, 1.81, 1.81, 1.81, 1.81, 1.88, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.08, 2.18, 2.18, 2.18, 2.18, 2.18, 2.18, 2.2, 2.28, 2.33, 2.33, 2.33, 2.33, 2.33, 2.33, 2.42, 2.5, 2.54, 2.54, 2.54, 2.54, 2.54, 2.54, 2.74, 2.82, 2.83, 2.83, 2.83, 2.83, 2.83, 2.83, 3.24, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.31, 4.03, 4.07, 4.07, 4.07, 4.07, 4.07, 4.07, 4.12, 5.09, 5.12, 5.12, 5.12, 5.12, 5.12, 5.12, 5.25, 6.22, 6.25, 6.25, 6.25, 6.25, 6.25, 6.25, 6.57, 7.44, 7.45, 7.45, 7.45, 7.45, 7.45, 7.5, 8.03, 8.66, 8.66, 8.66, 8.66, 8.66, 8.66, 8.9, 9.45, 9.82, 9.82, 9.82, 9.82, 9.82, 9.82, 10.55, 11.12, 11.37, 11.37, 11.37, 11.37, 11.37, 11.37, 13.04, 13.63, 13.75, 13.75, 13.75, 13.75, 13.75, 13.78, 16.9, 17.43, 17.43, 17.43, 17.43, 17.43, 17.43, 17.65, 23.02, 23.59, 23.59, 23.59, 23.59, 23.59, 23.59, 24.4, 33.43, 33.74, 33.74, 33.74, 33.74, 33.74, 33.74, 35.71, 48.92, 49.28, 49.28, 49.28, 49.28, 49.28, 49.28, 54.71, 71.01, 71.17, 71.17, 71.17, 71.17, 71.17, 71.62, 81.8, 97.53, 97.53, 97.53, 97.53, 97.53, 97.53, 100.89, 115.19, 126.79, 126.79, 126.79, 126.79, 126.79, 126.79, 138.31, 153.43, 160.14, 160.14, 160.14, 160.14, 160.14, 160.14, 189.3, 205.42, 208.25, 208.25, 208.25, 208.25, 208.25, 209.55, 265.69, 278.97, 278.97, 278.97, 278.97, 278.97, 278.97, 285.79, 393.16, 405.34, 405.34, 405.34, 405.34, 405.34, 405.34, 430.62, 643.54, 651.91, 651.91, 651.91, 651.91, 651.91, 651.91, 728.07, 1137.58, 1143.74, 1143.74, 1143.74, 1143.74, 1143.74, 1144.01, 1395.72, 2274.71, 2279.67, 2279.67, 2279.67, 2279.67, 2279.67, 2280.69, 3132.47, 5129.31, 5129.31, 5129.31, 5129.31, 5129.31, 5129.31, 5149.64, 8627.9, 13906.34, 13906.34, 13906.34, 13906.34, 13906.34, 13906.34]

sample_size = 10000  # this affects file name and plot label. MAKE SURE TO CHANGE IT WHEN SWAPPING BETWEEN ARRAYS
from_cv = 0  # that's for the range you want displayed. setting to 10 and 20 respectively will plot crit values from 10 to 20.
to_cv = 50
days = days_52_10000  # set this to your array of values


def insert_average(arr, num):
    arr = arr[arr >= 0]
    n = arr.shape[0]
    result = np.empty(2 * n - 1)
    result[::2] = arr

    result[1::2] = (arr[:-1] + arr[1:]) / 2
    if num == 12:  # yes this is spaghetti code
        if len(result[result <= 55]) <= num:
            return insert_average(result, num)
    else:
        if len(result) <= num:
            return insert_average(result, num)
    return result[result <= 55] if num == 12 else result

is_log = False

def plot_this(cv_plot, days_plot, cv_range, sample_size, cv_desired):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    if len(cv_plot) == 1:
        ax[0].scatter(cv_plot, days_plot, color='red', label='Single Point')
        ax[1].scatter(cv_plot, days_plot, color='red', label='Single Point')
    else:
        ax[0].plot(cv_plot, days_plot, label='Data')
        ax[1].plot(cv_plot, days_plot, label='Data')

    ax[0].set_title('Regular')
    ax[0].set_xlabel("Crit Value")
    ax[0].set_ylabel("Days to reach CV")
    ax[0].tick_params(axis='x', rotation=60)

    ax[1].set_title('Logarithmic')
    ax[1].set_xlabel("Crit Value")
    ax[1].set_yscale('log')
    ax[1].tick_params(axis='x', rotation=60)

    for a in ax:
        a.grid(True)

    ax[0].set_xticks(insert_average(ax[0].get_xticks(), 12))
    ax[0].set_yticks(insert_average(ax[0].get_yticks(), 10))
    ax[1].set_xticks(insert_average(ax[1].get_xticks(), 12))

    fig.suptitle(f"Average time to reach Crit Value (sample size = {sample_size})")
    plt.tight_layout()
    Path(".\\plots").mkdir(parents=True, exist_ok=True)
    Path(f".\\plots\\sample size = {sample_size}").mkdir(parents=True, exist_ok=True)

    if int(cv_range[0]) == cv_range[0]:
        from_cv = max(int(cv_range[0]), 0)
    else:
        from_cv = max(cv_range[0], 0)

    is_int = int(cv_desired) if int(cv_desired) == cv_desired else cv_desired
    if int(cv_range[1]) == cv_range[1]:
        to_cv = min(int(cv_range[1]), is_int)
    else:
        to_cv = min(cv_range[1], is_int)

    plt.savefig(
        f'.\\plots\\sample size = {sample_size}\\Plot of {from_cv}CV to {to_cv}CV (size = {sample_size}).png',
        dpi=1200)
    plt.show()


cv_desired = len(days) / 10 - 0.1

try:
    cv_range = [from_cv, to_cv]
    if (cv_range[0] > cv_desired or
            cv_range[1] < 0 or
            cv_range[1] < cv_range[0]):
        print('Invalid range\n')
        sys.exit()
except:
    print('Invalid\n')
    sys.exit()

cv = np.arange(len(days))/10

cv_for_plotting = np.arange(len(days)) / 10

days_plot = days[max(int(cv_range[0] * 10), 0):min(int(cv_range[1] * 10 + 1), int(cv_desired * 10 + 1))]
cv_plot = cv_for_plotting[max(int(cv_range[0] * 10), 0):min(int(cv_range[1] * 10 + 1), int(cv_desired * 10 + 1))]
print()
print('Values:', days_plot)
print()

plot_this(cv_plot, days_plot, cv_range, sample_size, cv_desired)
