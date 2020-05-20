from docplex.mp.model import Model


def cplex_example():
    # create one model instance, with a name
    m = Model(name='telephone_production')

    # by default, all variables in Docplex have a lower bound of 0 and infinite upper bound
    desk = m.continuous_var(name='desk')
    cell = m.continuous_var(name='cell')

    # write constraints
    # constraint #1: desk production is greater than 100
    m.add_constraint(desk >= 100)

    # constraint #2: cell production is greater than 100
    m.add_constraint(cell >= 100)

    # constraint #3: assembly time limit
    ct_assembly = m.add_constraint(0.2 * desk + 0.4 * cell <= 400)
    print(ct_assembly)

    # constraint #4: paiting time limit
    ct_painting = m.add_constraint(0.5 * desk + 0.4 * cell <= 490)
    print(ct_painting)

    m.maximize(12 * desk + 20 * cell)

    m.print_information()
    sol = m.solve()
    print(sol)
    m.print_solution()


def main():
    m = Model(name='production_planning')

    Am1 = m.continuous_var(name='A_month_1')
    Am2 = m.continuous_var(name='A_month_2')
    Am3 = m.continuous_var(name='A_month_3')
    Bm1 = m.continuous_var(name='B_month_1')
    Bm2 = m.continuous_var(name='B_month_2')
    Bm3 = m.continuous_var(name='B_month_3')

    # calculated expected values
    R1 = 54.98679995962599
    R2 = 40.0
    R3 = 49.97403331742613
    R4 = 35.24083494467262
    R5 = 44.966804314236484
    R6 = 31.193302160152246

    m.add_constraint(Am1 + Am2 + Am3 == 1100)
    m.add_constraint(Bm1 + Bm2 + Bm3 == 1200)

    # production cost
    prod_costA = Am1 * R1 + Am2 * R2 + Am3 * R3
    prod_costB = Bm1 * R4 + Bm2 * R5 + Bm3 * R6

    # storage cost - consider
    store_A_mon1 = R1 * (1/10 * 100 + 15/100 * (Am1 - 100))
    store_A_mon2 = store_A_mon1 + R2 * (1/10 * 100 + 15/100 * (Am2 - 100))
    store_A_mon3 = store_A_mon1 + store_A_mon2 + R3 * (1/10 * 100 + 15/100 * (Am3 - 100))
    store_costA = store_A_mon1 + store_A_mon2 + store_A_mon3

    store_B_mon1 = R4 * (1/10 * 100 + 15/100 * (Bm1 - 100))
    store_B_mon2 = R5 * (1/10 * 100 + 15/100 * (Bm2 - 100))
    store_B_mon3 = R6 * (1/10 * 100 + 15/100 * (Bm3 - 100))
    store_costB = store_B_mon1 + store_B_mon2 + store_B_mon3

    Z1m1 = m.continuous_var(name='Z1m1')
    Z2m1 = m.continuous_var(name='Z2m1')
    Z1m2 = m.continuous_var(name='Z1m2')
    Z2m2 = m.continuous_var(name='Z2m2')
    Z1m3 = m.continuous_var(name='Z1m3')
    Z2m3 = m.continuous_var(name='Z2m3')

    Z1Am1 = m.continuous_var(name='Z1Am1')
    Z1Am2 = m.continuous_var(name='Z1Am2')
    Z1Am3 = m.continuous_var(name='Z1Am3')
    Z1Bm1 = m.continuous_var(name='Z1Bm1')
    Z1Bm2 = m.continuous_var(name='Z1Bm2')
    Z1Bm3 = m.continuous_var(name='Z1Bm3')

    Z2Am1 = m.continuous_var(name='Z2Am1')
    Z2Am2 = m.continuous_var(name='Z2Am2')
    Z2Am3 = m.continuous_var(name='Z2Am3')
    Z2Bm1 = m.continuous_var(name='Z2Bm1')
    Z2Bm2 = m.continuous_var(name='Z2Bm2')
    Z2Bm3 = m.continuous_var(name='Z2Bm3')

    m.add_constraint(Am1 == (Z1Am1 / 0.2 + Z2Am1 / 0.8) / 2)
    m.add_constraint(Am2 == (Z1Am2 / 0.2 + Z2Am2 / 0.8) / 2)
    m.add_constraint(Am3 == (Z1Am3 / 0.2 + Z2Am3 / 0.8) / 2)
    m.add_constraint(Bm1 == (Z1Bm1 / 0.7 + Z2Bm1 / 0.3) / 2)
    m.add_constraint(Bm2 == (Z1Bm2 / 0.7 + Z2Bm2 / 0.3) / 2)
    m.add_constraint(Bm3 == (Z1Bm3 / 0.7 + Z2Bm3 / 0.3) / 2)

    m.add_constraint(Z1Am1 + Z1Bm1 == Z1m1)
    m.add_constraint(Z2Am1 + Z2Bm1 == Z2m1)
    m.add_constraint(Z1Am2 + Z1Bm2 == Z1m2)
    m.add_constraint(Z2Am2 + Z2Bm2 == Z2m2)
    m.add_constraint(Z1Am3 + Z1Bm3 == Z1m3)
    m.add_constraint(Z2Am3 + Z2Bm3 == Z2m3)

    m.add_constraint(Z1Am1 / 0.2 == Z2Am1 / 0.8)
    m.add_constraint(Z1Am2 / 0.2 == Z2Am2 / 0.8)
    m.add_constraint(Z1Am3 / 0.2 == Z2Am3 / 0.8)
    m.add_constraint(Z1Bm1 / 0.7 == Z2Bm1 / 0.3)
    m.add_constraint(Z1Bm2 / 0.7 == Z2Bm2 / 0.3)
    m.add_constraint(Z1Bm3 / 0.7 == Z2Bm3 / 0.3)

    m.add_constraint(Z1m1 <= 600)
    m.add_constraint(Z1m2 <= 700)
    m.add_constraint(Z1m3 <= 550)
    m.add_constraint(Z2m1 <= 1400)
    m.add_constraint(Z2m2 <= 900)
    m.add_constraint(Z2m3 <= 1200)

    m.minimize(prod_costA + prod_costB + store_costA + store_costB)

    m.print_information()
    sol = m.solve()
    print(sol)
    m.print_solution()


if __name__ == "__main__":
    main()
