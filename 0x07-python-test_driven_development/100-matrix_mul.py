#!/usr/bin/python3
"""
this module contains two functions for multiplication of two matrices.
"""


def get_matrix_sizes(matrix1, matrix2, name1, name2):
    """
    Computes the size of the two passed matrices and
    performs some matrices validation.

    Args:
        matrix1 (list): the first matrice which is list of lists.
        matrix2 (list): the second matricewhich is list of lists.

    Returns:
        list: The (size) number of rows and columns of each matrices.

    Raises:
        TypeError: if a matrice is not a list.
                   if a matrice is not a list of lists.
                   if a matice doesnot contain integer or float.
                   if each row size of matrices is not equal.
        ValueError: if a matrices is empty.
    """

    funcs = (
            lambda txt: '{} must be a list'.format(txt),
            lambda txt: '{} can\'t be empty'.format(txt),
            lambda txt: '{} must be a list of lists'.format(txt),
            lambda txt: '{} should contain only integers or \
floats'.format(txt),
            lambda txt: 'each row of {} must be of the same size'.format(txt),
            lambda _list: all(map(lambda n: isinstance(n, (int, float)), _list))
            )
    size0 = [0, 0]     # number of rows and columns for matrix1
    size1 = [0, 0]     # number of rows and columns for matrix2

    if not isinstance(matrix1, list):
        raise TypeError(funcs[0](name1))
    elif not isinstance(matrix2, list):
        raise TypeError(funcs[0](name2))

    size0[0] = len(matrix1)    # obtain the number of rows from matrix 1
    size1[0] = len(matrix2)    # obtain the number of rows from matrix 2

    if size0[0] == 0:
        raise ValueError(funcs[1](name1))
    elif size1[0] == 0:
        raise ValueError(funcs[1](name2))
    elif not all(map(lambda x: isinstance(x, list), matrix1)):
        raise TypeError(funcs[2](name1))
    elif not all(map(lambda x: isinstance(x, list), matrix2)):
        raise TypeError(funcs[2](name2))
    elif all(map(lambda x: len(x) == 0, matrix1)):
        raise ValueError(funcs[1](name1))
    elif all(map(lambda x: len(x) == 0, matrix2)):
        raise ValueError(funcs[1](name2))
    elif not all(map(lambda x: funcs[5](x), matrix1)):
        raise TypeError(funcs[3](name1))
    elif not all(map(lambda x: funcs[5](x), matrix2)):
        raise TypeError(funcs[3](name2))

    size0[1] = len(matrix1[0])     # obtain the number of columns from matrix 1
    size1[1] = len(matrix2[0])     # obtain the number of columns from matrix 2

    if not all(map(lambda x: len(x) == size0[1], matrix1)):
        raise TypeError(funcs[4](name1))
    elif not all(map(lambda x: len(x) == size1[1], matrix2)):
        raise TypeError(funcs[4](name2))

    return size0, size1


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices.

    Args:
        m_a (list): the first matrix.
        m_b (list): the second matrix.

    Returns:
        list: a list of lists that is result of the product
              of the two given matrices.

    Raises:
        ValueError: if m_a's column count isnot equal to m_b's row count.
    """

    m_a_size, m_b_size = get_matrix_sizes(m_a, m_b, 'm_a', 'm_b')

    if m_a_size[1] != m_b_size[0]:
        """
         For matrix multiplication, the number of columns in the
         first matrix must be equal to the number of rows in the second matrix.
         if they are not equal raise an error.
        """
        raise ValueError('m_a and m_b can\'t be multiplied')
    else:
        result = []
        for row in m_a:
            row_result = []
            for i in range(m_b_size[1]):
                cells = zip(range(m_a_size[1]), row)
                value = map(lambda x: x[1] * m_b[x[0]][i], cells)
                row_result.append(sum(list(value)))
            result.append(row_result)
        return result
