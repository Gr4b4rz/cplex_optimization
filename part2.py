from docplex.mp.model import Model


def main():
    objectives_from_scenarios = []
    with open('objectives_from_scenarios.txt', 'r') as f:
        lines = f.readlines()
        for item in lines:
            objectives_from_scenarios.append(float(item))
            #  count += count + 1
            #  if count == 2:
            #  break

    # 2. Rozszerzenie
    R1_list = []
    R2_list = []
    R3_list = []
    R4_list = []
    R5_list = []
    R6_list = []
    with open("scenarios.txt") as f:
        lines = f.readlines()
        for line in lines:
            values = line.split("\t")
            R1_list.append(float(values[0]))
            R2_list.append(float(values[1]))
            R3_list.append(float(values[2]))
            R4_list.append(float(values[3]))
            R5_list.append(float(values[4]))
            R6_list.append(float(values[5]))
        #  risk = m.sum(m.abs(initial[i] - final[i]) for i in range(n))

    results = []
    for scen in range(1000):
        R1 = R1_list[scen]
        R2 = R2_list[scen]
        R3 = R3_list[scen]
        R4 = R4_list[scen]
        R5 = R5_list[scen]
        R6 = R6_list[scen]

        m = Model(name='production_planning')

        ############################
        ### Continuous Variables ###
        ############################

        # Ilość wyprodukowanego produktu A i B w każdym z miesięcy
        Am1 = m.continuous_var(name='A_month_1')
        Am2 = m.continuous_var(name='A_month_2')
        Am3 = m.continuous_var(name='A_month_3')
        Bm1 = m.continuous_var(name='B_month_1')
        Bm2 = m.continuous_var(name='B_month_2')
        Bm3 = m.continuous_var(name='B_month_3')

        # Ilość zasobu Z1 przeznaczonego na produkt A i B w każdym z miesięcy
        Z1Am1 = m.continuous_var(name='Z1Am1')
        Z1Am2 = m.continuous_var(name='Z1Am2')
        Z1Am3 = m.continuous_var(name='Z1Am3')
        Z1Bm1 = m.continuous_var(name='Z1Bm1')
        Z1Bm2 = m.continuous_var(name='Z1Bm2')
        Z1Bm3 = m.continuous_var(name='Z1Bm3')

        # Ilość zasobu Z2 przeznaczonego na produkt A i B w każdym z miesięcy
        Z2Am1 = m.continuous_var(name='Z2Am1')
        Z2Am2 = m.continuous_var(name='Z2Am2')
        Z2Am3 = m.continuous_var(name='Z2Am3')
        Z2Bm1 = m.continuous_var(name='Z2Bm1')
        Z2Bm2 = m.continuous_var(name='Z2Bm2')
        Z2Bm3 = m.continuous_var(name='Z2Bm3')

        ###################
        ### Constraints ###
        ###################

        # Ograniczenia liczby sztuk wymaganych do dostawy
        m.add_constraint(Am1 + Am2 + Am3 == 1100)
        m.add_constraint(Bm1 + Bm2 + Bm3 == 1200)

        # Ograniczenia, określające ile komponentu A i B można wyprodukować w każdym miesiącu
        # zależnie od wielkości dostaw komponentu Z1 i Z2
        m.add_constraint(Am1 == (Z1Am1 / 0.2 + Z2Am1 / 0.8) / 2)
        m.add_constraint(Am2 == (Z1Am2 / 0.2 + Z2Am2 / 0.8) / 2)
        m.add_constraint(Am3 == (Z1Am3 / 0.2 + Z2Am3 / 0.8) / 2)
        m.add_constraint(Bm1 == (Z1Bm1 / 0.7 + Z2Bm1 / 0.3) / 2)
        m.add_constraint(Bm2 == (Z1Bm2 / 0.7 + Z2Bm2 / 0.3) / 2)
        m.add_constraint(Bm3 == (Z1Bm3 / 0.7 + Z2Bm3 / 0.3) / 2)

        # Ograniczenia wymuszające produkowanie komponentów A i B w każdym miesiacu w całości
        m.add_constraint(Z1Am1 / 0.2 == Z2Am1 / 0.8)
        m.add_constraint(Z1Am2 / 0.2 == Z2Am2 / 0.8)
        m.add_constraint(Z1Am3 / 0.2 == Z2Am3 / 0.8)
        m.add_constraint(Z1Bm1 / 0.7 == Z2Bm1 / 0.3)
        m.add_constraint(Z1Bm2 / 0.7 == Z2Bm2 / 0.3)
        m.add_constraint(Z1Bm3 / 0.7 == Z2Bm3 / 0.3)

        # Ograniczenia możliwych dostaw komponentów A i B w każdym miesiącu
        m.add_constraint(Z1Am1 + Z1Bm1 <= 600)
        m.add_constraint(Z2Am1 + Z2Bm1 <= 700)
        m.add_constraint(Z1Am2 + Z1Bm2 <= 550)
        m.add_constraint(Z2Am2 + Z2Bm2 <= 1400)
        m.add_constraint(Z1Am3 + Z1Bm3 <= 900)
        m.add_constraint(Z2Am3 + Z2Bm3 <= 1200)

        ##########################
        ### Objective function ###
        ##########################

        # Koszt produkcji
        prod_costA = Am1 * R1 + Am2 * R2 + Am3 * R3
        prod_costB = Bm1 * R4 + Bm2 * R5 + Bm3 * R6

        # Koszt składowania komponentu A
        store_A_mon1 = R1 * (1/10 * Am1 + (5/100 * (Am1 - 100) + m.abs(5/100 * (Am1 - 100)) / 2))
        store_A_mon2 = store_A_mon1 + R2 * \
            (1/10 * Am2 + (5/100 * (Am2 - 100) + m.abs(5/100 * (Am2 - 100)) / 2))
        store_A_mon3 = store_A_mon1 + store_A_mon2 + R3 * \
            (1/10 * Am3 + (5/100 * (Am3 - 100) + m.abs(5/100 * (Am3 - 100)) / 2))
        store_costA = store_A_mon1 + store_A_mon2 + store_A_mon3

        # Koszt składowania komponentu B
        store_B_mon1 = R4 * (1/10 * Bm1 + (5/100 * (Bm1 - 100) + m.abs(5/100 * (Bm1 - 100)) / 2))
        store_B_mon2 = store_B_mon1 + R5 * \
            (1/10 * Bm2 + (5/100 * (Bm2 - 100) + m.abs(5/100 * (Bm2 - 100)) / 2))
        store_B_mon3 = store_B_mon1 + store_B_mon2 + R6 * \
            (1/10 * Bm3 + (5/100 * (Bm3 - 100) + m.abs(5/100 * (Bm3 - 100)) / 2))
        store_costB = store_B_mon1 + store_B_mon2 + store_B_mon3

        cost = prod_costA + prod_costB + store_costA + store_costB
        risk = m.abs(101296.561 - cost)

        m.minimize_static_lex([cost, risk])

        result = m.solve()  # .get_objective_value()
        results.append(result.get_objective_value())

    with open('risk.txt', 'w') as f:
        for item in results:
            f.write("%s\n" % item)


if __name__ == "__main__":
    main()
