use std::fs::read_to_string;

static QUESTIONS: [char; 26] = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z',
];

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let groups = input
        .split("\n\n")
        .map(|x| x.split_whitespace().collect::<Vec<_>>())
        .collect::<Vec<Vec<_>>>();

    let part1 = groups
        .iter()
        .map(|g| {
            QUESTIONS
                .iter()
                .filter(|&x| g.iter().any(|u| u.contains(*x)))
                .collect::<Vec<_>>()
                .len()
        })
        .fold(0, |acc, x| acc + x);

    let part2 = groups
        .iter()
        .map(|g| {
            QUESTIONS
                .iter()
                .filter(|&x| g.iter().all(|u| u.contains(*x)))
                .collect::<Vec<_>>()
                .len()
        })
        .fold(0, |acc, x| acc + x);

    println!("{:?}", part1);
    println!("{:?}", part2);
}
