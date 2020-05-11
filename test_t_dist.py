from . import TStudentDist
import pytest


def test_student_t_dist():
    """
    Test student-t distribution expected value calculation, using example from lecture
    """
    mu_matrix = [45, 35, 40]
    sigma_matrix = [
        [1, -2, -1],
        [-2, 36, -8],
        [-1, -8, 9]
    ]
    alpha = 20
    beta = 50
    v = 4

    t_student_dist = TStudentDist(mu_matrix, sigma_matrix, alpha, beta, v)

    e_vector = []
    for mu in range(0, len(mu_matrix)):
        e_vector.append(t_student_dist.calculate_expected_value(mu))

    assert e_vector[0] == pytest.approx(44.97, 1e-2)
    assert e_vector[1] == 35
    assert e_vector[2] == pytest.approx(39.83, 1e-2)
