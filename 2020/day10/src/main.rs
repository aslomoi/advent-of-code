use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let mut adapters = input
        .split("\n")
        .map(|x| x.parse::<u64>().unwrap())
        .collect::<Vec<_>>();

    adapters.sort();
    adapters.insert(0, 0);
    adapters.push(adapters.last().unwrap() + 3);

    let mut ones = 0;
    let mut threes = 0;
    let mut diffs = vec![];
    for i in 1..adapters.len() {
        let diff = adapters[i] - adapters[i - 1];
        diffs.push(diff);
        match diff {
            1 => ones += 1,
            3 => threes += 1,
            _ => println!("ERROR"),
        }
    }

    println!("{:3.?}", adapters);
    println!("..{:3.?}", diffs);
    let mut i: usize = 0;
    let mut run: i64 = 0;
    let mut sum: u64 = 1;
    while i < diffs.len() {
        match diffs[i] {
            1 => run += 1,
            3 if run > 1 => {
                match run {
                    1 => (),
                    2 => sum *= 2,
                    3 => sum *= 4,
                    4 => sum *= 7,
                    5 => sum *= 13,
                    _ => println!("Uh, oh: {}", run),
                }
                run = 0;
            }
            3 => run = 0,
            _ => println!("ERROR"),
        }
        i += 1;
    }
    println!("Part 2: {}", sum);

    println!("1's: {}\n3's: {}", ones, threes);
    println!("{}", ones * threes);
}
