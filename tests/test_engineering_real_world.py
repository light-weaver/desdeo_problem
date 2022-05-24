from desdeo_problem.testproblems.EngineeringRealWorld import *
from desdeo_problem.problem import MOProblem
import pytest
import numpy as np
import numpy.testing as npt

@pytest.mark.re21
def test_number_of_variables_re21():
    p: MOProblem = re21()

    assert p.n_of_variables == 4

# Evaluating problem with some variable values
@pytest.mark.re21
def test_evaluate_re21():
    p: MOProblem = re21()

    # Variable values
    xs = np.array([2, 2, 2, 2])

    objective_vectors = p.evaluate(xs).objectives

    assert objective_vectors.shape[0] == 1

    expected_result = np.array([[2048.528137, 0.02]])

    npt.assert_allclose(objective_vectors, expected_result)

@pytest.mark.re21
def test_variable_bounds_error_re21_1d():
    with pytest.raises(ValueError):
        p: MOProblem = re21(var_iv=np.array([1,2,3,4]))

@pytest.mark.re21
def test_variable_bounds_error_re21_2d():
    with pytest.raises(ValueError):
        p: MOProblem = re21(var_iv=np.array([[1,2,2,2],[4,1,2,0]]))

@pytest.mark.re22
def test_number_of_variables_re22():
    p: MOProblem = re22()

    assert p.n_of_variables == 3

# Evaluating problem with some variable values
@pytest.mark.re22
def test_evaluate_re22():
    p: MOProblem = re22()

    # Variable values
    xs = np.array([[10., 10., 20.], [12., 10., 20.], [11.5, 15, 35]])

    objective_vectors = p.evaluate(xs).objectives

    assert objective_vectors.shape[0] == 3

    expected_result = np.array([[421.938, 2], [472.8, 2], [663.39, 164.0054642]])

    npt.assert_allclose(objective_vectors, expected_result)

@pytest.mark.re22
def test_variable_bounds_error_re22_1d():
    with pytest.raises(ValueError):
        p: MOProblem = re22(var_iv=np.array([1,-2,3]))

@pytest.mark.re22
def test_variable_bounds_error_re22_2d():
    with pytest.raises(ValueError):
        p: MOProblem = re22(var_iv=np.array([[1,2,2],[0,1,2]]))