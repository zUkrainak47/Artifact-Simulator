# Add your list of CV values and change sample_size, from_cv, to_cv and set days to the name of your list
# do not touch anything below that :)


import numpy as np
from pathlib import Path
import sys
from simulator_for_plotting import plot_this


# days_50_old =  [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.01, 1.01, 1.0, 1.0, 1.01, 1.01, 1.0, 1.0, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.02, 1.01, 1.01, 1.02, 1.02, 1.01, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.05, 1.05, 1.05, 1.05, 1.05, 1.06, 1.05, 1.05, 1.09, 1.1, 1.09, 1.1, 1.09, 1.1, 1.09, 1.1, 1.15, 1.15, 1.14, 1.14, 1.15, 1.16, 1.15, 1.15, 1.2, 1.21, 1.2, 1.2, 1.2, 1.2, 1.2, 1.22, 1.24, 1.23, 1.24, 1.23, 1.23, 1.24, 1.24, 1.25, 1.27, 1.26, 1.27, 1.27, 1.25, 1.26, 1.27, 1.29, 1.3, 1.29, 1.29, 1.29, 1.29, 1.3, 1.33, 1.36, 1.37, 1.34, 1.35, 1.34, 1.36, 1.36, 1.45, 1.44, 1.46, 1.45, 1.46, 1.45, 1.46, 1.46, 1.63, 1.59, 1.59, 1.62, 1.61, 1.62, 1.6, 1.62, 1.82, 1.81, 1.83, 1.81, 1.83, 1.81, 1.81, 1.84, 2.05, 2.04, 2.07, 2.05, 2.03, 2.03, 2.04, 2.14, 2.28, 2.24, 2.29, 2.27, 2.29, 2.3, 2.28, 2.32, 2.44, 2.44, 2.42, 2.43, 2.43, 2.43, 2.47, 2.52, 2.62, 2.57, 2.59, 2.63, 2.63, 2.59, 2.72, 2.8, 2.83, 2.84, 2.8, 2.85, 2.82, 2.82, 3.07, 3.13, 3.22, 3.15, 3.14, 3.12, 3.14, 3.15, 3.61, 3.66, 3.68, 3.69, 3.7, 3.68, 3.66, 3.69, 4.37, 4.46, 4.42, 4.38, 4.42, 4.44, 4.41, 4.48, 5.52, 5.52, 5.36, 5.44, 5.47, 5.46, 5.44, 5.61, 6.6, 6.62, 6.55, 6.71, 6.67, 6.82, 6.66, 6.82, 7.97, 7.93, 8.03, 7.9, 8.16, 8.0, 8.05, 8.54, 9.16, 9.07, 9.14, 9.11, 9.12, 9.2, 9.42, 9.91, 10.46, 10.41, 10.51, 10.52, 10.38, 10.38, 11.1, 11.84, 11.91, 12.09, 12.01, 11.95, 12.01, 12.26, 13.46, 14.1, 14.28, 14.43, 14.34, 14.58, 14.52, 14.33, 17.62, 18.12, 18.69, 18.35, 18.38, 18.33, 18.34, 18.39, 24.26, 24.71, 24.73, 24.66, 24.28, 24.63, 24.65, 25.17, 33.74, 34.31, 34.05, 34.41, 34.98, 34.96, 33.94, 37.0, 50.1, 50.85, 50.49, 49.35, 50.38, 50.38, 49.88, 55.26, 72.73, 71.65, 72.18, 72.05, 71.92, 73.4, 71.7, 82.54, 97.43, 99.95, 98.17, 97.5, 97.63, 97.97, 101.52, 114.61, 128.52, 128.27, 129.19, 126.78, 125.42, 128.8, 136.72, 155.67, 164.06, 162.12, 165.35, 161.62, 161.97, 162.86, 190.58, 208.24, 207.5, 209.67, 213.05, 205.49, 207.52, 208.7, 270.59, 283.95, 278.41, 282.72, 281.82, 283.63, 284.88, 292.23, 405.73, 418.63, 412.87, 409.55, 416.36, 416.93, 409.59, 439.13, 645.49, 653.76, 666.08, 664.56, 663.02, 665.17, 666.07, 745.09, 1172.6, 1159.91, 1183.55, 1159.68, 1187.29, 1183.31, 1181.72, 1437.79, 2342.66, 2327.63]
# days_52_5_1750 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.12, 1.12, 1.12, 1.12, 1.12, 1.12, 1.12, 1.12, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13, 1.15, 1.15, 1.15, 1.15, 1.15, 1.15, 1.15, 1.16, 1.17, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.2, 1.21, 1.21, 1.21, 1.21, 1.21, 1.21, 1.21, 1.28, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.41, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.57, 1.58, 1.78, 1.78, 1.78, 1.78, 1.78, 1.78, 1.78, 1.84, 1.95, 1.96, 1.96, 1.96, 1.96, 1.96, 1.97, 2.05, 2.14, 2.14, 2.14, 2.14, 2.14, 2.14, 2.16, 2.24, 2.28, 2.28, 2.28, 2.28, 2.28, 2.28, 2.39, 2.48, 2.52, 2.52, 2.52, 2.52, 2.52, 2.52, 2.75, 2.82, 2.83, 2.83, 2.83, 2.83, 2.83, 2.83, 3.21, 3.27, 3.27, 3.27, 3.27, 3.27, 3.27, 3.28, 3.98, 4.02, 4.02, 4.02, 4.02, 4.02, 4.02, 4.11, 5.04, 5.05, 5.05, 5.05, 5.05, 5.05, 5.05, 5.16, 6.14, 6.18, 6.18, 6.18, 6.18, 6.18, 6.18, 6.49, 7.44, 7.46, 7.46, 7.46, 7.46, 7.46, 7.55, 8.17, 8.88, 8.88, 8.88, 8.88, 8.88, 8.88, 9.17, 9.79, 10.19, 10.19, 10.19, 10.19, 10.19, 10.19, 10.79, 11.58, 11.81, 11.81, 11.81, 11.81, 11.81, 11.81, 13.41, 13.88, 14.02, 14.02, 14.02, 14.02, 14.02, 14.02, 17.01, 17.56, 17.56, 17.56, 17.56, 17.56, 17.56, 17.78, 22.46, 22.9, 22.9, 22.9, 22.9, 22.9, 22.9, 23.49, 32.07, 32.28, 32.28, 32.28, 32.28, 32.28, 32.28, 34.38, 45.75, 46.08, 46.08, 46.08, 46.08, 46.08, 46.08, 52.26, 67.35, 67.48, 67.48, 67.48, 67.48, 67.48, 67.86, 77.27, 91.4, 91.4, 91.4, 91.4, 91.4, 91.4, 94.53, 108.14, 119.42, 119.42, 119.42, 119.42, 119.42, 119.42, 132.09, 149.83, 156.25, 156.25, 156.25, 156.25, 156.25, 156.25, 182.42, 192.73, 197.87, 197.87, 197.87, 197.87, 197.87, 198.88, 259.46, 270.17, 270.17, 270.17, 270.17, 270.17, 270.17, 277.93, 383.05, 392.71, 392.71, 392.71, 392.71, 392.71, 392.71, 416.0, 609.81, 617.48, 617.48, 617.48, 617.48, 617.48, 617.48, 699.25, 1099.82, 1105.49, 1105.49, 1105.49, 1105.49, 1105.49, 1106.48, 1335.37, 2182.52, 2182.6, 2182.6, 2182.6, 2182.6, 2182.6, 2182.6, 3045.84, 5076.96, 5076.96, 5076.96, 5076.96, 5076.96, 5076.96, 5080.58, 8333.89, 13308.91, 13308.91, 13308.91, 13308.91, 13308.91, 13308.91, 13468.8, 29001.69, 46549.06, 46549.06, 46549.06]
# days_52_5_2500 = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.11, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13, 1.14, 1.14, 1.14, 1.14, 1.14, 1.14, 1.14, 1.15, 1.16, 1.17, 1.17, 1.17, 1.17, 1.17, 1.17, 1.19, 1.21, 1.21, 1.21, 1.21, 1.21, 1.21, 1.21, 1.27, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.28, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.41, 1.58, 1.58, 1.58, 1.58, 1.58, 1.58, 1.58, 1.59, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.79, 1.85, 1.99, 1.99, 1.99, 1.99, 1.99, 1.99, 1.99, 2.07, 2.15, 2.15, 2.15, 2.15, 2.15, 2.15, 2.19, 2.26, 2.31, 2.31, 2.31, 2.31, 2.31, 2.31, 2.39, 2.46, 2.51, 2.51, 2.51, 2.51, 2.51, 2.51, 2.72, 2.84, 2.85, 2.85, 2.85, 2.85, 2.85, 2.85, 3.22, 3.26, 3.26, 3.26, 3.26, 3.26, 3.26, 3.28, 3.91, 3.95, 3.95, 3.95, 3.95, 3.95, 3.95, 4.0, 4.96, 4.97, 4.97, 4.97, 4.97, 4.97, 4.97, 5.09, 6.16, 6.18, 6.18, 6.18, 6.18, 6.18, 6.18, 6.53, 7.34, 7.35, 7.35, 7.35, 7.35, 7.35, 7.43, 7.94, 8.53, 8.53, 8.53, 8.53, 8.53, 8.53, 8.84, 9.43, 9.84, 9.84, 9.84, 9.84, 9.84, 9.84, 10.6, 11.22, 11.44, 11.44, 11.44, 11.44, 11.44, 11.44, 13.13, 13.75, 13.9, 13.9, 13.9, 13.9, 13.9, 13.94, 16.8, 17.39, 17.39, 17.39, 17.39, 17.39, 17.39, 17.67, 23.22, 23.67, 23.67, 23.67, 23.67, 23.67, 23.67, 24.39, 33.06, 33.61, 33.61, 33.61, 33.61, 33.61, 33.61, 35.41, 47.87, 48.03, 48.03, 48.03, 48.03, 48.03, 48.03, 53.99, 69.78, 69.87, 69.87, 69.87, 69.87, 69.87, 70.53, 80.84, 95.15, 95.15, 95.15, 95.15, 95.15, 95.15, 97.76, 111.82, 122.03, 122.03, 122.03, 122.03, 122.03, 122.03, 134.41, 149.45, 156.86, 156.86, 156.86, 156.86, 156.86, 156.86, 183.06, 197.14, 199.9, 199.9, 199.9, 199.9, 199.9, 201.44, 258.2, 269.57, 269.57, 269.57, 269.57, 269.57, 269.57, 277.28, 384.39, 394.87, 394.87, 394.87, 394.87, 394.87, 394.87, 420.93, 621.03, 628.47, 628.47, 628.47, 628.47, 628.47, 628.47, 706.34, 1112.28, 1115.62, 1115.62, 1115.62, 1115.62, 1115.62, 1116.32, 1410.95, 2242.22, 2247.87, 2247.87, 2247.87, 2247.87, 2247.87, 2255.4, 3143.9, 5258.02, 5258.02, 5258.02, 5258.02, 5258.02, 5258.02, 5272.08, 8734.29, 13784.4, 13784.4, 13784.4, 13784.4, 13784.4, 13784.4, 13867.72, 29822.8, 46533.3, 46533.3, 46533.3])
# days_52_5_5000_1 = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.12, 1.12, 1.12, 1.12, 1.12, 1.12, 1.12, 1.13, 1.14, 1.14, 1.14, 1.14, 1.14, 1.14, 1.14, 1.15, 1.16, 1.16, 1.16, 1.16, 1.16, 1.16, 1.17, 1.18, 1.19, 1.19, 1.19, 1.19, 1.19, 1.19, 1.21, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.29, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42, 1.43, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.59, 1.6, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.86, 2.0, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.05, 2.16, 2.16, 2.16, 2.16, 2.16, 2.16, 2.19, 2.27, 2.32, 2.32, 2.32, 2.32, 2.32, 2.32, 2.42, 2.51, 2.54, 2.54, 2.54, 2.54, 2.54, 2.54, 2.76, 2.84, 2.85, 2.85, 2.85, 2.85, 2.85, 2.85, 3.28, 3.35, 3.35, 3.35, 3.35, 3.35, 3.35, 3.36, 4.07, 4.1, 4.1, 4.1, 4.1, 4.1, 4.1, 4.13, 5.04, 5.07, 5.07, 5.07, 5.07, 5.07, 5.07, 5.21, 6.28, 6.3, 6.3, 6.3, 6.3, 6.3, 6.3, 6.6, 7.5, 7.51, 7.51, 7.51, 7.51, 7.51, 7.54, 7.99, 8.67, 8.67, 8.67, 8.67, 8.67, 8.67, 8.91, 9.42, 9.89, 9.89, 9.89, 9.89, 9.89, 9.89, 10.55, 11.11, 11.36, 11.36, 11.36, 11.36, 11.36, 11.36, 12.9, 13.41, 13.54, 13.54, 13.54, 13.54, 13.54, 13.57, 16.61, 17.23, 17.23, 17.23, 17.23, 17.23, 17.23, 17.48, 22.95, 23.38, 23.38, 23.38, 23.38, 23.38, 23.38, 24.27, 33.11, 33.42, 33.42, 33.42, 33.42, 33.42, 33.42, 35.45, 47.81, 47.98, 47.98, 47.98, 47.98, 47.98, 47.98, 53.12, 69.69, 69.87, 69.87, 69.87, 69.87, 69.87, 70.33, 80.59, 94.74, 94.74, 94.74, 94.74, 94.74, 94.74, 98.65, 111.85, 123.42, 123.42, 123.42, 123.42, 123.42, 123.42, 133.56, 149.09, 156.28, 156.28, 156.28, 156.28, 156.28, 156.28, 182.67, 197.45, 201.35, 201.35, 201.35, 201.35, 201.35, 202.49, 255.13, 270.62, 270.62, 270.62, 270.62, 270.62, 270.62, 277.12, 380.89, 390.99, 390.99, 390.99, 390.99, 390.99, 390.99, 418.44, 622.22, 628.6, 628.6, 628.6, 628.6, 628.6, 628.6, 702.3, 1116.62, 1120.51, 1120.51, 1120.51, 1120.51, 1120.51, 1120.51, 1367.67, 2215.86, 2221.09, 2221.09, 2221.09, 2221.09, 2221.09, 2221.09, 3102.6, 5110.23, 5110.23, 5110.23, 5110.23, 5110.23, 5110.23, 5126.55, 8608.16, 13775.34, 13775.34, 13775.34, 13775.34, 13775.34, 13775.34, 13960.16, 28725.9, 44949.28, 44949.28, 44949.28])
# days_52_5_5000_2 = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.08, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13, 1.14, 1.15, 1.15, 1.15, 1.15, 1.15, 1.15, 1.15, 1.16, 1.17, 1.17, 1.17, 1.17, 1.17, 1.17, 1.2, 1.21, 1.21, 1.21, 1.21, 1.21, 1.21, 1.21, 1.28, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.43, 1.61, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.62, 1.81, 1.81, 1.81, 1.81, 1.81, 1.81, 1.81, 1.87, 2.0, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.07, 2.18, 2.18, 2.18, 2.18, 2.18, 2.18, 2.2, 2.29, 2.34, 2.34, 2.34, 2.34, 2.34, 2.34, 2.43, 2.51, 2.54, 2.54, 2.54, 2.54, 2.54, 2.54, 2.74, 2.82, 2.83, 2.83, 2.83, 2.83, 2.83, 2.83, 3.24, 3.32, 3.32, 3.32, 3.32, 3.32, 3.32, 3.33, 4.05, 4.11, 4.11, 4.11, 4.11, 4.11, 4.11, 4.14, 5.01, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.15, 6.16, 6.19, 6.19, 6.19, 6.19, 6.19, 6.19, 6.5, 7.32, 7.34, 7.34, 7.34, 7.34, 7.34, 7.37, 7.95, 8.55, 8.55, 8.55, 8.55, 8.55, 8.55, 8.79, 9.35, 9.76, 9.76, 9.76, 9.76, 9.76, 9.76, 10.46, 11.01, 11.25, 11.25, 11.25, 11.25, 11.25, 11.25, 12.96, 13.48, 13.57, 13.57, 13.57, 13.57, 13.57, 13.61, 16.9, 17.52, 17.52, 17.52, 17.52, 17.52, 17.52, 17.82, 23.02, 23.48, 23.48, 23.48, 23.48, 23.48, 23.48, 24.38, 33.24, 33.51, 33.51, 33.51, 33.51, 33.51, 33.51, 35.77, 47.93, 48.35, 48.35, 48.35, 48.35, 48.35, 48.35, 53.29, 68.27, 68.4, 68.4, 68.4, 68.4, 68.4, 69.08, 79.56, 93.62, 93.62, 93.62, 93.62, 93.62, 93.62, 96.93, 110.53, 122.15, 122.15, 122.15, 122.15, 122.15, 122.15, 133.55, 147.43, 155.59, 155.59, 155.59, 155.59, 155.59, 155.59, 183.77, 200.93, 204.16, 204.16, 204.16, 204.16, 204.16, 205.56, 264.04, 279.96, 279.96, 279.96, 279.96, 279.96, 279.96, 285.69, 395.28, 406.52, 406.52, 406.52, 406.52, 406.52, 406.52, 428.8, 627.77, 634.59, 634.59, 634.59, 634.59, 634.59, 634.59, 711.43, 1122.7, 1127.26, 1127.26, 1127.26, 1127.26, 1127.26, 1127.26, 1358.79, 2197.87, 2200.61, 2200.61, 2200.61, 2200.61, 2200.61, 2202.69, 3112.56, 5050.77, 5050.77, 5050.77, 5050.77, 5050.77, 5050.77, 5073.18, 8579.69, 14131.71, 14131.71, 14131.71, 14131.71, 14131.71, 14131.71, 14278.2, 29606.26, 46274.98, 46274.98, 46274.98])

days_52_5_12500 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.08, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.12, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13, 1.14, 1.15, 1.15, 1.15, 1.15, 1.15, 1.15, 1.16, 1.17, 1.18, 1.18, 1.18, 1.18, 1.18, 1.18, 1.2, 1.22, 1.22, 1.22, 1.22, 1.22, 1.22, 1.22, 1.28, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42, 1.43, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.61, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.8, 1.86, 2.0, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.06, 2.17, 2.17, 2.17, 2.17, 2.17, 2.17, 2.19, 2.28, 2.33, 2.33, 2.33, 2.33, 2.33, 2.33, 2.42, 2.5, 2.53, 2.53, 2.53, 2.53, 2.53, 2.53, 2.74, 2.83, 2.84, 2.84, 2.84, 2.84, 2.84, 2.84, 3.25, 3.32, 3.32, 3.32, 3.32, 3.32, 3.32, 3.33, 4.03, 4.07, 4.07, 4.07, 4.07, 4.07, 4.07, 4.11, 5.01, 5.03, 5.03, 5.03, 5.03, 5.03, 5.03, 5.16, 6.21, 6.23, 6.23, 6.23, 6.23, 6.23, 6.23, 6.55, 7.4, 7.41, 7.41, 7.41, 7.41, 7.41, 7.45, 7.96, 8.59, 8.59, 8.59, 8.59, 8.59, 8.59, 8.85, 9.39, 9.83, 9.83, 9.83, 9.83, 9.83, 9.83, 10.52, 11.09, 11.33, 11.33, 11.33, 11.33, 11.33, 11.33, 12.97, 13.51, 13.62, 13.62, 13.62, 13.62, 13.62, 13.66, 16.76, 17.38, 17.38, 17.38, 17.38, 17.38, 17.38, 17.65, 23.03, 23.48, 23.48, 23.48, 23.48, 23.48, 23.48, 24.34, 33.15, 33.49, 33.49, 33.49, 33.49, 33.49, 33.49, 35.57, 47.87, 48.14, 48.14, 48.14, 48.14, 48.14, 48.14, 53.36, 69.14, 69.28, 69.28, 69.28, 69.28, 69.28, 69.87, 80.23, 94.37, 94.37, 94.37, 94.37, 94.37, 94.37, 97.78, 111.32, 122.63, 122.63, 122.63, 122.63, 122.63, 122.63, 133.73, 148.5, 156.12, 156.12, 156.12, 156.12, 156.12, 156.12, 183.19, 198.78, 202.18, 202.18, 202.18, 202.18, 202.18, 203.51, 259.31, 274.15, 274.15, 274.15, 274.15, 274.15, 274.15, 280.58, 387.35, 397.98, 397.98, 397.98, 397.98, 397.98, 397.98, 423.08, 624.2, 630.97, 630.97, 630.97, 630.97, 630.97, 630.97, 706.76, 1118.18, 1122.23, 1122.23, 1122.23, 1122.23, 1122.23, 1122.37, 1372.77, 2213.94, 2218.25, 2218.25, 2218.25, 2218.25, 2218.25, 2220.59, 3114.84, 5116.0, 5116.0, 5116.0, 5116.0, 5116.0, 5116.0, 5134.31, 8622.0, 13919.7, 13919.7, 13919.7, 13919.7, 13919.7, 13919.7, 14068.89, 29297.42, 45796.36, 45796.36, 45796.36]
days_50_100000 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.11, 1.12, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13, 1.14, 1.15, 1.15, 1.15, 1.15, 1.15, 1.15, 1.16, 1.17, 1.17, 1.17, 1.17, 1.17, 1.17, 1.17, 1.2, 1.22, 1.22, 1.22, 1.22, 1.22, 1.22, 1.22, 1.29, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.3, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42, 1.42, 1.43, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.61, 1.81, 1.81, 1.81, 1.81, 1.81, 1.81, 1.81, 1.87, 2.01, 2.01, 2.01, 2.01, 2.01, 2.01, 2.02, 2.08, 2.17, 2.17, 2.17, 2.17, 2.17, 2.17, 2.2, 2.27, 2.33, 2.33, 2.33, 2.33, 2.33, 2.33, 2.41, 2.49, 2.52, 2.52, 2.52, 2.52, 2.52, 2.52, 2.74, 2.83, 2.84, 2.84, 2.84, 2.84, 2.84, 2.84, 3.26, 3.33, 3.33, 3.33, 3.33, 3.33, 3.33, 3.34, 4.03, 4.07, 4.07, 4.07, 4.07, 4.07, 4.07, 4.11, 5.02, 5.05, 5.05, 5.05, 5.05, 5.05, 5.05, 5.16, 6.21, 6.24, 6.24, 6.24, 6.24, 6.24, 6.24, 6.56, 7.45, 7.47, 7.47, 7.47, 7.47, 7.47, 7.52, 8.02, 8.67, 8.67, 8.67, 8.67, 8.67, 8.67, 8.91, 9.48, 9.89, 9.89, 9.89, 9.89, 9.89, 9.89, 10.63, 11.23, 11.46, 11.46, 11.46, 11.46, 11.46, 11.46, 13.11, 13.7, 13.82, 13.82, 13.82, 13.82, 13.82, 13.85, 17.0, 17.57, 17.57, 17.57, 17.57, 17.57, 17.57, 17.81, 23.18, 23.61, 23.61, 23.61, 23.61, 23.61, 23.61, 24.36, 33.05, 33.34, 33.34, 33.34, 33.34, 33.34, 33.34, 35.5, 47.93, 48.23, 48.23, 48.23, 48.23, 48.23, 48.23, 53.38, 68.89, 69.05, 69.05, 69.05, 69.05, 69.05, 69.66, 79.65, 94.56, 94.56, 94.56, 94.56, 94.56, 94.56, 98.14, 112.12, 123.15, 123.15, 123.15, 123.15, 123.15, 123.15, 134.67, 149.29, 155.82, 155.82, 155.82, 155.82, 155.82, 155.82, 183.78, 198.29, 201.41, 201.41, 201.41, 201.41, 201.41, 202.61, 260.41, 273.65, 273.65, 273.65, 273.65, 273.65, 273.65, 280.84, 390.1, 400.99, 400.99, 400.99, 400.99, 400.99, 400.99, 425.23, 632.84, 640.46, 640.46, 640.46, 640.46, 640.46, 640.46, 718.34, 1123.86, 1129.32, 1129.32, 1129.32, 1129.32, 1129.32, 1129.43, 1377.03, 2245.87, 2250.55]

days = days_50_100000  # set this to your array of values
sample_size = 100000  # this affects file name and plot label. MAKE SURE TO CHANGE IT WHEN SWAPPING BETWEEN ARRAYS
start_cv = 0  # that's for the range you want displayed. setting to 10 and 20 respectively will plot crit values from 10
end_cv = 50   # to 20.

cv_desired = len(days) / 10 - 0.1

try:
    cv_range = [start_cv, end_cv]
    if (cv_range[0] > cv_desired or
            cv_range[1] < 0 or
            cv_range[1] < cv_range[0]):
        print('Invalid range\n')
        sys.exit()
except:
    print('Invalid\n')
    sys.exit()

Path(".\\plots").mkdir(parents=True, exist_ok=True)
Path(f".\\plots\\sample size = {sample_size}").mkdir(parents=True, exist_ok=True)

cv_for_plotting = np.arange(len(days)) / 10

days_plot = days[max(int(cv_range[0] * 10), 0):min(int(cv_range[1] * 10 + 1), int(cv_desired * 10 + 1))]
cv_plot = cv_for_plotting[max(int(cv_range[0] * 10), 0):min(int(cv_range[1] * 10 + 1), int(cv_desired * 10 + 1))]
print()
print('Values:', days_plot)
print()

plot_this(cv_plot, days_plot, cv_range, sample_size, cv_desired, False)
