use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


fn main() {
    if let Ok(lines) = read_lines("input.txt") {
        let mut vals: Vec<i32> = vec![];
        for line in lines {
            if let Ok(l) = line {
                vals.push(l.parse::<i32>().unwrap());
            }
        }

        { // Part 1
            let mut prev: i32 = 10000000;
            let mut count: i32 = 0;
            for &num in vals.iter() {
                if num > prev {
                    count+= 1;
                }
                prev = num;
            }
            println!("{}", count);
        }

        { // Part 2
            let mut count = 0;
            let mut prev: i32 = 100000000;
            for i in 0..vals.len()-2 {
                let slice = &vals[i..=i+2];
                let num: i32 = slice.iter().sum();
                if num > prev { count += 1};
                prev = num;
            }
            println!("{}", count);
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
