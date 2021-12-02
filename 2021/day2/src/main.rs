use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;


fn main() {
    if let Ok(lines) = read_lines("input.txt") {
        let mut aim = 0;
        let mut pos = (0, 0);
        for line in lines {
            if let Ok(l) = line {
                let mut dirs = l.split(' ');
                let dir = dirs.next().unwrap();
                let val = dirs.next().unwrap().parse::<i32>().unwrap();
                // Part 1
                // match dir {
                //     "forward" => pos.0 += val,
                //     "down" => pos.1 += val,
                //     "up" => pos.1 -= val,
                //     _ => ()
                // }
                // Part 2
                match dir {
                    "forward" => {
                        pos.0 += val;
                        pos.1 += aim*val;
                        },
                    "down" => aim += val,
                    "up" => aim -= val,
                    _ => ()
                }
            }
        }
        println!("{}", pos.0*pos.1);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
