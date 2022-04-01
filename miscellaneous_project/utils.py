def find_max (numbers):
    max_ = numbers [0]
    for number in numbers:
        if number > max_:
            max_ = number
    return max_
     
