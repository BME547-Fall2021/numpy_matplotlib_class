import numpy as np
import matplotlib.pyplot as plt


def input_data(filename):
    with open(filename, "r") as in_f:
        in_lines = in_f.readlines()
    return in_lines


def parse_data(in_line):
    list_no_return = in_line.strip("\n")
    list_split = list_no_return.split(",")
    list_int = [int(x) for x in list_split]
    return list_int


def plot_single_trace(in_data):
    time = np.arange(0, len(in_data), 1)
    plt.plot(time, in_data)
    plt.show()


def plot_multiple_windows(data_0, data_1, data_2):
    time = np.arange(0, len(data_0), 1)
    plt.figure(1)
    plt.plot(time, data_0)
    plt.ylabel("Pulse Oxymetry")
    plt.figure(2)
    plt.plot(time, data_1)
    plt.ylabel("BP")
    plt.figure(3)
    plt.plot(time, data_2)
    plt.ylabel("ECG")
    plt.show()


def plot_three_in_same_window(data_0, data_1, data_2):
    time = np.arange(0, len(data_0), 1)
    plt.subplot(3, 1, 1)
    plt.plot(time, data_0)
    plt.ylabel("Pulse Oxymetry")
    plt.subplot(3, 1, 2)
    plt.plot(time, data_1)
    plt.ylabel("BP")
    plt.subplot(3, 1, 3)
    plt.plot(time, data_2)
    plt.ylabel("ECG")
    plt.show()


def plot_together(data_0, data_1, data_2):
    time = np.arange(0, len(data_0), 1)
    plt.plot(time, data_0)
    plt.plot(time, data_1)
    plt.plot(time, data_2)
    plt.legend(["O2", "BP", "ECG"])
    plt.show()


def main():
    in_data = input_data("overall_data.dat")
    data_0 = parse_data(in_data[0])
    data_1 = parse_data(in_data[1])
    data_2 = parse_data(in_data[2])
    # plot_single_trace(data_0)
    # plot_single_trace(data_1)
    # plot_single_trace(data_2)
    plot_together(data_0, data_1, data_2)


if __name__ == "__main__":
    main()