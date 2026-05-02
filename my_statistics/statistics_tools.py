def mean(data):
    total = 0
    for number in data:
        total += number
    return total / len(data)

def median(data):
    data.sort()
    n = len(data)
    if n % 2 != 0:
        index = int(((n / 2) + 0.5) - 1)
        return data[index]
    else:
        mid = n // 2
        return (data[mid] + data[mid - 1]) / 2

def mode(data):
    counts = {}
    for number in data:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
            
    max_count = 0
    common_number = None
    for number, count in counts.items():
        if count > max_count:
            max_count = count
            common_number = number
    return common_number

def variance(data):
    avg = mean(data)
    total_squares = 0
    for number in data:
        total_squares += (number - avg) ** 2
    return total_squares / len(data)

def std_dev(data):
    return variance(data) ** 0.5

def summarize(data):
    return {
        "mean": mean(data),
        "median": median(data),
        "mode": mode(data),
        "variance": variance(data),
        "std_dev": std_dev(data)
    }