with open(file='data.txt') as file:
    data = sorted([int(num) for num in file.read().split(",")])


def part_one():
    global data
    max_num, min_num = data[-1], data[0]
    lowest_fuel_cost = {'new_pos': 0, 'curr_lowest': float('inf')}
    for new_pos in range(min_num, max_num + 1):
        curr_fuel_cost = 0  # current iter fuel cost
        for crab_pos in data:
            curr_fuel_cost += abs(new_pos - crab_pos)

        if curr_fuel_cost < lowest_fuel_cost['curr_lowest']:
            lowest_fuel_cost['curr_lowest'] = curr_fuel_cost
            lowest_fuel_cost['new_pos'] = new_pos

    return print(lowest_fuel_cost['new_pos'])


def part_two():
    global data
    max_num, min_num = data[-1], data[0]
    lowest_fuel_cost = {'new_pos': 0, 'curr_lowest': float('inf')}
    for new_pos in range(min_num, max_num + 1):
        curr_fuel_cost = 0  # current iter fuel cost
        for crab_pos in data:
            curr_fuel_cost += sum([i for i in range(1, abs(new_pos - crab_pos) + 1)])

        if curr_fuel_cost < lowest_fuel_cost['curr_lowest']:
            lowest_fuel_cost['curr_lowest'] = curr_fuel_cost
            lowest_fuel_cost['new_pos'] = new_pos

    return print(lowest_fuel_cost['new_pos'])


# part one:
part_one()
# part two:
part_two()
