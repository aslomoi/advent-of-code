from collections import Counter
from copy import deepcopy
from functools import cmp_to_key
from pathlib import Path

PATH = Path(__file__).parent
INPUT_PATH = PATH / "input.txt"
SAMPLE_PATH = PATH / "sample.txt"


def parse_input(path: Path) -> list:
    with open(path, "r") as f:
        lines = [l.strip() for l in f.read().split("\n")]
        return lines


def cmp(l, r):
    if isinstance(l, tuple):
        l_card = l[1]
        r_card = r[1]
        l_tiebreaker = l[0]
        r_tiebreaker = r[0]
        strengths = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    else:
        l_tiebreaker = l_card = l
        r_tiebreaker = r_card = r
        strengths = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    count_l = list(Counter(l_card).values())
    count_r = list(Counter(r_card).values())

    ls = sorted(count_l, reverse=True)
    rs = sorted(count_r, reverse=True)

    if ls[0] > rs[0]:
        return 1
    elif ls[0] < rs[0]:
        return -1
    else:
        if ls[0] == rs[0] == 3:
            if ls[1] == 2 and rs[1] < 2:
                return 1
            elif ls[1] < 2 and rs[1] == 2:
                return -1
        if ls[0] == rs[0] == 2:
            if ls[1] == 2 and rs[1] < 2:
                return 1
            elif ls[1] < 2 and rs[1] == 2:
                return -1
        for lv, rv in zip(l_tiebreaker, r_tiebreaker):
            if strengths.index(lv) < strengths.index(rv):
                return 1
            elif strengths.index(lv) > strengths.index(rv):
                return -1
        assert False


def part_1(data: list):
    cards = {line.split()[0]: int(line.split()[1]) for line in data}
    card_vals = list(cards.keys())
    card_vals.sort(key=cmp_to_key(cmp))
    return sum((i + 1) * cards[card] for i, card in enumerate(card_vals))


def best(card):
    if "J" not in (vals := set(card)):
        return card
    if len(options := vals - {"J"}) == 0:
        return "A" * len(card)
    cards = [card]
    for i in range(len(card)):
        new_cards = []
        for c in cards:
            if c[i] == "J":
                for opt in options:
                    cards.append(c[:i] + opt + c[i + 1 :])
            else:
                new_cards.append(c)
        cards = new_cards
    cards.sort(key=cmp_to_key(cmp))
    return cards[-1]


def part_2(data: list):
    cards = {line.split()[0]: int(line.split()[1]) for line in data}
    pairs = [(card, best(card)) for card in cards]
    pairs.sort(key=cmp_to_key(cmp))
    return sum((i + 1) * cards[card] for i, (card, _) in enumerate(pairs))


def run():
    sample = parse_input(SAMPLE_PATH)
    data = parse_input(INPUT_PATH)

    print("\n** Part 1 **")
    print(f"sample: {part_1(deepcopy(sample))}")
    print(f"data: {part_1(deepcopy(data))}")

    print("\n** Part 2 **")
    print(f"sample: {part_2(sample)}")
    print(f"data: {part_2(data)}")


if __name__ == "__main__":
    run()
