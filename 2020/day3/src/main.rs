use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    if let Ok(lines) = read_lines("input.txt") {
        let mut map: Vec<Vec<char>> = vec![];
        for line in lines {
            if let Ok(l) = line {
                map.push(l.chars().collect());
            }
        }
        let width = map[0].len();
        let height = map.len();
        let slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]];
        let mut mult: u128 = 1;
        for slope in &slopes {
            let mut x = 0;
            let mut y = 0;
            let mut count = 0;
            while y < height {
                if map[y][x] == '#' {
                    count += 1
                }
                x = (x + slope[0]) % width;
                y += slope[1];
            }
            println!("{}", count);
            mult *= count;
        }
        println!("{}", mult);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
