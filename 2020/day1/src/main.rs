use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut entries: Vec<u32> = vec![];
    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            if let Ok(entry) = line {
                entries.push(entry.parse::<u32>().unwrap());
            }
        }
    }
    entries.sort();
    part_two(entries);
}

fn part_one(entries: Vec<u32>) {
    let mut backwards = entries.clone();
    'outer: for entry in entries {
        println!("Trying {}...", entry);
        loop {
            let largest = backwards.pop().unwrap();
            match entry + largest {
                sum if sum < 2020 => break,
                sum if sum == 2020 => {
                    println!("FOUND {} and {}", entry, largest);
                    println!("Product: {}", entry * largest);
                    break 'outer;
                }
                _ => println!("{}", largest),
            }
        }
    }
}

fn part_two(entries: Vec<u32>) {
    let mut forwards = entries.clone();
    let mut backwards: Vec<u32>;
    'outer: for entry in entries {
        println!("Trying {}...", entry);
        forwards.remove(0);
        backwards = forwards.clone();
        'inner: for forward in &forwards {
            println!("with {}...", forward);
            loop {
                let largest = backwards.last().unwrap().clone();
                if *forward == largest {
                    break 'inner;
                }
                match entry + forward + largest {
                    sum if sum < 2020 => {
                        println!("{}: {}, {}, {} too small!!", sum, entry, forward, largest);
                        break;
                    }
                    sum if sum == 2020 => {
                        println!("FOUND {}, {} and {}", entry, forward, largest);
                        println!("Product: {}", entry * forward * largest);
                        break 'outer;
                    }
                    sum => {
                        backwards.pop();
                        println!("{}: {}, {}, {}", sum, entry, forward, largest);
                    }
                }
            }
        }
    }
}
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
