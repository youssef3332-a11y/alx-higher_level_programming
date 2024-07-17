#!/usr/bin/python3
"""
this is a module:
for multipling two matrices
"""
def matrix_mul(m_a, m_b):
    """matrix multiplication

    Args: 
    m_a: first matrix
    m_b: second matrix

    Raises:
    TypeError: for some cases
    ValueError: for others
    Returns:
    matrix: the result
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if len(m_a) == 0:
        raise ValueError('m_a can\'t be empty')
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError('m_a must be a list of lists')
        if len(row) == 0:
            raise ValueError('m_a can\'t be empty')
        if len(row) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError('m_a should contain only integers or floats')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if len(m_b) == 0:
        raise ValueError('m_b can\'t be empty')
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError('m_b must be a list of lists')
        if len(row) == 0:
            raise ValueError('m_b can\'t be empty')
        if len(row ) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError('m_b should contain only integers or floats')
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')
    result = [[0]*len(m_b[0]) for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            result[i][j] = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
    return result
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
