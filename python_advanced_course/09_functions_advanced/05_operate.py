def operate(sign, *args):
    mapper = {
        "+": lambda nums: sum(nums),
        "-": lambda nums: nums[0] - sum(nums[1:]),
        "*": lambda nums: multiply(nums),
        "/": lambda nums: divide(nums)
    }
    return mapper[sign](args)


def multiply(nums):
    result = 1
    for n in nums:
        result *= n
    return result


def divide(nums):
    result = nums[0]
    for n in nums[1:]:
        result /= n
    return result
