"""Analysis of the Rhine-water level data from https://pegel.bonn.de/php/rheinpegel.php ."""

from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas

from regularization import set_up_point_matrix

if __name__ == "__main__":
    rhein = pandas.read_csv("./data/pegel.tab", sep=" 	")
    levels = np.array([int(pegel.split(" ")[0]) for pegel in rhein["Pegel"]])

    timestamps = [ts[:-4] for ts in rhein["Zeit"]]
    datetime_list = []
    keep_indices = []
    for idx, ts in enumerate(timestamps):
        ts_date, ts_time = ts.split(",")
        day, month, year = ts_date.split(".")
        hour, minute = ts_time.split(":")
        datetime_list.append(datetime(int(year), int(month), int(day)))
        if hour == " 04" or hour == " 05":
            keep_indices.append(idx)

    # 2.3.0
    # uncomment to start in the year 2000.
    # levels = levels[:-30_000:4]
    # datetime_list = datetime_list[:-30_000:4]

    datetime_stamps = np.array([dt.timestamp() for dt in datetime_list])
    levels = np.array(levels)

    levels = levels[::-1]
    datetime_stamps = datetime_stamps[::-1]
    datetime_list = datetime_list[::-1]

    plt.plot(datetime_list, levels)
    plt.xlabel("Year")
    plt.ylabel("Water level [cm]")
    plt.title("Rhine water level in Bonn")
    plt.show()

    # 2.1 Regression

    # 2.1.1 Set up the point matrix for n=2
    #       The corresponding function that you have implemented in Part 1 has already been imported and is ready to use!

    # 2.1.2 Estimate the coefficients

    # 2.1.3 Evaluate the straight line and plot your result

    # 2.1.4 Calculate the data where the Rhine will be dried out



    # 2.2 Fitting a higher-order Polynomial

    # 2.2.1 Take a look at the datetime_stamps and scale the axis

    # 2.2.2 Set up the point matrix with n=20

    # 2.2.3 Compute the coefficients for the polynomial

    # 2.2.4 Evaluate the polyomial

    # 2.2.5 Plot the results



    # 2.3 Regularization

    # 2.3.0 Uncomment the lines of code above

    # 2.3.1 Compute the SVD of the point-matrix for n=20

    # 2.3.2 Compute the filter matrix

    # 2.3.3 Estimate the coefficients by applying regularization

    # 2.3.4 Plot the evaluated, regularized polynomial
