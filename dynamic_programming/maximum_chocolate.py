import sys

#Problem
#
#Bharat is chocoholic. He found a chocolate factory of N floors ,but the factory has N*N rooms where in each room specific number of chocolate is present. Now, Bharat starts collecting chocolate from ground floor. He can only collect chocolate from one room in a floor. Bharat can only move to upper room or upper-right room or upper-left room .
#
#He want to collect maximum number of chocolate possible. Help him in finding maximum number of chocolate.
#
#Input:
#
#First line contains a value of N. Next N lines contains N space separated integer.
#
#Output:
#
#Output a single integer denoting the maximum number of chocolate Bharat can collect.
#
#Constraints
#
#1 <= N <= 1000
#
#1 <= Number chocolate in 1 room <= 10^5
max_chocolates = 0

with open("input_maximum_chocolate.txt", "r") as file_p:
    file_content = file_p.readlines()

factory = []
for floor_id, floor in enumerate(file_content):
    if floor_id > 0:
        factory.append([])
        for room in floor.split(" "):
            factory[floor_id - 1].append(int(room))

def pick(factory, floor_number, room_number, total):
    if floor_number == len(factory):
        global max_chocolates
        if total > max_chocolates:
            max_chocolates = total
        return

    num_chocolates = factory[floor_number][room_number]
    if room_number == 0:
        pick(factory, floor_number + 1, room_number, num_chocolates + total)
        pick(factory, floor_number + 1, room_number + 1, num_chocolates + total)
    elif room_number == len(factory) - 1:
        pick(factory, floor_number + 1, room_number, num_chocolates + total)
        pick(factory, floor_number + 1, room_number - 1, num_chocolates + total)
    else:
        pick(factory, floor_number + 1, room_number, num_chocolates + total)
        pick(factory, floor_number + 1, room_number + 1, num_chocolates + total)
        pick(factory, floor_number + 1, room_number - 1, num_chocolates + total)

def pick_memoize(factory, floor, table = []):
    if floor == len(factory):
        max_chocolates = max(table[len(factory) - 1])
        print(f'maximum number of chocolate is {max_chocolates}');
        return

    if floor == 0:
        table.append(list(factory[0]))
    else:
        table.append([None] * len(factory))
        for room_id in range(0, len(factory)):
            num_chocolates_room = factory[floor][room_id]
            if room_id == 0:
                table[floor][room_id] = max(table[floor - 1][room_id], table[floor - 1][room_id + 1]) + num_chocolates_room
            elif room_id == len(factory) - 1:
                table[floor][room_id] = max(table[floor - 1][room_id - 1], table[floor - 1][room_id]) + num_chocolates_room
            else:
                table[floor][room_id] = max(table[floor - 1][room_id - 1], table[floor - 1][room_id], table[floor - 1][room_id + 1]) + num_chocolates_room
    pick_memoize(factory, floor + 1, table)

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print(f'Usage: python {sys.argv[0]}')
        print(f'option: -dp -> launch the solution that implements dynamic programming')
        sys.exit()
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-dp":
            pick_memoize(factory, 0, [])
    else:
        for room_number in range(0, len(factory)):
            pick(factory, 0, room_number, 0);
        print(f'maximum number of chocolate is {max_chocolates}');
