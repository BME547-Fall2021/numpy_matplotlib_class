from plot_data import input_data, parse_data, plot_together
from math import sin, cos


def make_wave(a1: int, a2: int, f1: int, f2: int, time: list):
    curve1 = [a1 * sin(x * f1) for x in time]
    curve2 = [a2 * cos(x * f2) for x in time]
    one_and_two = []
    for i, val in enumerate(curve1):
        one_and_two.append(val + curve2[i])
    return one_and_two


def main():
    dat = input_data("curve_to_match.dat")
    my_data = parse_data(dat[1])
    time = parse_data(dat[0])
    my_wave = make_wave(1, 2, 2, 3, time)
    plot_together(time=time, data=my_data, waves=my_wave)


if __name__ == "__main__":
    main()
