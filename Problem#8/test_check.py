from check import in_order

def test_passed():
    nums = [5, 6, 7, 8, 10]
    result = in_order(nums)
    correct_result = True
    if result == correct_result:
        print('Test passed: in_order() correctly returned True')
        return True
    else:
        print('Test failed: in_order() should have returned True because the numbers are sorted')
        return False

def test_passed2():
    nums = [5, 5, 6, 6, 6, 7, 8, 10, 10, 10, 10]
    result = in_order(nums)
    correct_result = True
    if result == correct_result:
        print('Test passed: in_order() correctly returned True')
        return True
    else:
        print('Test failed: in_order() should have returned True because the numbers are sorted')
        return False

# Run the tests
test_passed()
test_passed2()
