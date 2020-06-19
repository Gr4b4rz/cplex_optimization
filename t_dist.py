import math
from scipy.stats import t
from scipy.special import gamma


class TStudentDist:
    """
    Class responsible for calculating expected values of student-t distribution
    """

    def __init__(self, mu_matrix, sigma_matrix, alpha, beta, v):
        self.mu_matrix = mu_matrix
        self.sigma_matrix = sigma_matrix
        self.alpha = alpha
        self.beta = beta
        self.v = v

    def _calculate_param(self, base, mu, sigma):
        """
        Calculate value of beta or alpha parameter
        """
        return (base - mu) / sigma

    def calculate_expected_value(self, index):
        """
        Calculate expected value using formula from lecture
        """
        result = self.mu_matrix[index]
        sigma = math.sqrt(self.sigma_matrix[index][index])
        a = self._calculate_param(self.alpha, self.mu_matrix[index], sigma)
        b = self._calculate_param(self.beta, self.mu_matrix[index], sigma)
        result += sigma * (gamma((self.v - 1) / 2) * ((self.v + a ** 2) ** ((1 - self.v) / 2) -
                                                      (self.v + b ** 2) ** ((1 - self.v) / 2))
                           * self.v ** (self.v / 2) / (2 * (t.cdf(b, self.v) - t.cdf(a, self.v))
                                                       * gamma(self.v / 2) * gamma(1 / 2)))
        return result

    def generate_scenarios(self):
        """
        """
        return t.rvs(self.v, 40, 5, size=100)


def main():
    mu_matrix = [55, 40, 50, 35, 45, 30]
    sigma_matrix = [
        [1, 1, 0, 2, -1, -1],
        [1, 16, -6, -6, -2, 12],
        [0, -6, 4, 2, -2, -5],
        [2, -6, 2, 25, 0, -17],
        [-1, -2, -2, 0, 9, -5],
        [-1, 12, -5, -17, -5, 36]
    ]
    alpha = 20
    beta = 60
    v = 5

    t_student_dist = TStudentDist(mu_matrix, sigma_matrix, alpha, beta, v)

    e_vector = []
    for mu in range(0, len(mu_matrix)):
        e_vector.append(t_student_dist.calculate_expected_value(mu))

    for exp in e_vector:
        print(exp)

    print(type(t_student_dist.generate_scenarios()))
    print(t_student_dist.generate_scenarios())


if __name__ == '__main__':
    main()
