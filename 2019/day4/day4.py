pwd_range = [206938,679128]

def digitize(n):
    return [int(d) for d in str(n)]

def contains_adjacent(password):
    pairs = zip(password[:-1],password[1:])
    pairs_matching = list(map(lambda x: x[0] == x[1], pairs))
    return any(pairs_matching)

def contains_pairs_only(password):
        for i, v in enumerate(password):
            if i == 0:
                val = v
                run = 1
            else:
                if v == val:
                    run += 1
                else:
                    if run == 2:
                        return True
                    else:
                        val = v
                        run = 1
        if run == 2:
            return True
        return False
def contains_non_descending(password):
    pairs = zip(password[:-1],password[1:])
    return all(map(lambda x: x[0] <= x[1], pairs))


def meet_criteria(password):
    if len(password) != 6:
        return False
    if not contains_adjacent(password):
        return False
    # if not contains_pairs_only(password):
    #     return False
    if not contains_non_descending(password):
        return False
    return True


valid = sum([meet_criteria(str(pwd)) for pwd in range(pwd_range[0], pwd_range[1]+1)])
print(f'# valid: {valid}')
