use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    if let Ok(lines) = read_lines("input.txt") {
        let mut binaries: Vec<Vec<_>> = vec![];
        for line in lines {
            if let Ok(l) = line {
                binaries.push(
                    l.chars()
                        .map(|x| match x {
                            'B' => 1,
                            'F' => 0,
                            'R' => 1,
                            'L' => 0,
                            _ => 1000,
                        })
                        .collect(),
                );
            }
        }

        let mut seats = binaries
            .iter()
            .map(|b| {
                b.iter().take(7).fold(0, |acc, b| 2 * acc + b) * 8
                    + b.iter().skip(7).fold(0, |acc, b| 2 * acc + b)
            })
            .collect::<Vec<_>>();
        seats.sort();

        let part1 = seats.last().unwrap();

        let mut part2 = -1;
        for i in 0..seats.len() {
            if seats[i + 1] - seats[i] == 2 {
                part2 = seats[i] + 1;
                break;
            }
        }
        println!("{:?}", part2);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
