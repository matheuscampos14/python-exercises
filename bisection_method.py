def square_root_bisection(square_target, tolerance = 0.0001, maximum_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1 or square_target == 0:
        print(f'The square root of {square_target} is {square_target}')
        return square_target
    low = 0
    high = max(1, square_target)
    iterations = 0
    while high - low > tolerance:
        iterations += 1
        if iterations >= maximum_iterations:
            print(f"Failed to converge within {maximum_iterations} iterations")
            return None
        root = (low + high) / 2
        if root * root > square_target:
            high = root
        else:
            low = root
        iterations += 1
    root = (low + high) / 2
    print(f"The square root of {square_target} is approximately {root}")
    return root
square_root_bisection(0.001, 1e-7, 50)