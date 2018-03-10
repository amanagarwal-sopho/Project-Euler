def solutions(p):
    sol_list = []
    for a in range(2, p):
        for b in range(1, p-a):
            c = p - a - b
            if a**2 + b**2 == c**2 and sorted([a, b, c]) not in sol_list:
                sol_list.append(sorted([a, b, c]))

    return sol_list

print(solutions(120))


def main(limit):
    max_sol = 0
    for p in range(1,limit):
        if len(solutions(p)) > max_sol:
            max_sol = p

        print(solutions(p))

    print(max_sol)


if __name__ == '__main__':
    main(1000)