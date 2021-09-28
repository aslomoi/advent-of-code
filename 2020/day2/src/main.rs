use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    if let Ok(lines) = read_lines("input.txt") {
        let mut count = 0;
        for line in lines {
            if let Ok(l) = line {
                let mut splits = l.split(' ');
                let range: Vec<usize> = splits
                    .next()
                    .unwrap()
                    .split('-')
                    .map(|x| x.parse::<usize>().unwrap())
                    .collect();
                let letter = splits.next().unwrap().chars().next().unwrap();
                let password = splits.next().unwrap();

                // Part 1
                /* let occur = password
                    .chars()
                    .fold(0, |acc, x| if x == letter { acc + 1 } else { acc });
                if occur >= range[0] && occur <= range[1] {
                    count += 1
                } */

                // Part 2
                let found: Vec<char> = range
                    .iter()
                    .map(|x| password.chars().nth(x - 1).unwrap())
                    .collect();
                if (letter == found[0]) ^ (letter == found[1]) {
                    count += 1
                }
            }
        }
        println!("{}", count);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
