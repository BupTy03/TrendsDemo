import matplotlib.pyplot as plt


def plot_example():
    x_axis = list(range(0, 5))
    y1_axis = [22, 17, 81, 41, 25]
    y2_axis = [62, 37, 39, 36, 49]

    plt.title('Salary Graph')
    plt.xlabel('days')
    plt.ylabel('salary, $')
    plt.plot(x_axis, y1_axis, label='Mark', marker='o')
    plt.plot(x_axis, y2_axis, label='Steven', marker='^')
    plt.legend()
    plt.show()


def main():
    plot_example()


if __name__ == "__main__":
    main()
