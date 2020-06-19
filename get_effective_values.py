def main():
    cost = []
    risk = []
    with open("risk.txt") as f:
        lines = f.readlines()
        for line in lines:
            values = line.split(", ")
            cost.append(float(values[0]))
            risk.append(float(values[1]))

    max_sum = 10000000
    effective = []
    for i in range(len(cost)):
        if cost[i] + risk[i] <= max_sum:
            max_sum = cost[i] + risk[i]
            effective.append(i)
        if risk[i] == 9.0:
            print("koszt: {}, ryzyko: {}, suma: {}".format(cost[i], risk[i], cost[i] + risk[i]))
        if cost[i] == 67620.0:
            print("koszt: {}, ryzyko: {}, suma: {}".format(cost[i], risk[i], cost[i] + risk[i]))
        if risk[i] == 33676.0:
            print("koszt: {}, ryzyko: {}, suma: {}".format(cost[i], risk[i], cost[i] + risk[i]))
        if cost[i] == 124681.0:
            print("koszt: {}, ryzyko: {}, suma: {}".format(cost[i], risk[i], cost[i] + risk[i]))

    print(max_sum)
    print(effective)
    print(min(cost))
    print(min(risk))
    print(max(cost))
    print(max(risk))
    #  for x in effective:
    #  print("koszt: {}, ryzyko: {}, suma: {}".format(cost[x], risk[x], cost[x] + risk[x]))


if __name__ == "__main__":
    main()
