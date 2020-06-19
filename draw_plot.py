import matplotlib.pyplot as plt


def main():
    cost = []
    risk = []
    with open("risk.txt") as f:
        lines = f.readlines()
        for line in lines:
            values = line.split(", ")
            if float(values[0]) < 101296.561:
                cost.append(float(values[0]))
                risk.append(float(values[1]))

    plt.scatter(cost, risk)
    plt.ylabel('ryzyko')
    plt.xlabel('koszt')
    plt.show()


if __name__ == "__main__":
    main()
