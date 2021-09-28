use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let moves = input
        .split("\n")
        .map(|x| {
            let mut inst = x.chars();
            (
                inst.next().unwrap(),
                inst.collect::<String>().parse::<i128>().unwrap(),
            )
        })
        .collect::<Vec<_>>();
    // println!("{:?}", moves);

    part2(moves);
}

fn manhattan(loc: (i128, i128)) {
    let dist = loc.0.abs() + loc.1.abs();
    println!("Manhattan dist: {}", dist);
}

fn part1(moves: Vec<(char, i128)>) {
    let mut loc = (0, 0);
    let mut dir: f64 = 0.0;

    moves.iter().for_each(|(x, n)| {
        match x {
            'N' => loc.1 += n,
            'S' => loc.1 -= n,
            'E' => loc.0 += n,
            'W' => loc.0 -= n,
            'L' => dir += *n as f64,
            'R' => dir -= *n as f64,
            'F' => {
                loc = (
                    loc.0 + n * (dir.to_radians().cos() as i128),
                    loc.1 + n * (dir.to_radians().sin() as i128),
                );
            }
            _ => println!("Error"),
        };
        // println!("{}, {}", x, n);
        // println!("{:?}, {}deg", loc, dir);
    });
    manhattan(loc);
}

fn part2(moves: Vec<(char, i128)>) {
    let mut loc = (0, 0);
    let mut way = (10, 1);

    moves.iter().for_each(|(x, n)| {
        match x {
            'N' => way.1 += n,
            'S' => way.1 -= n,
            'E' => way.0 += n,
            'W' => way.0 -= n,
            'L' => {
                way = (
                    way.0 * ((*n as f64).to_radians().cos() as i128)
                        - way.1 * ((*n as f64).to_radians().sin() as i128),
                    way.1 * ((*n as f64).to_radians().cos() as i128)
                        + way.0 * ((*n as f64).to_radians().sin() as i128),
                );
            }
            'R' => {
                way = (
                    way.0 * ((*n as f64).to_radians().cos() as i128)
                        + way.1 * ((*n as f64).to_radians().sin() as i128),
                    way.1 * ((*n as f64).to_radians().cos() as i128)
                        - way.0 * ((*n as f64).to_radians().sin() as i128),
                );
            }
            'F' => {
                loc = (n * way.0 + loc.0, n * way.1 + loc.1);
            }
            _ => println!("Error"),
        };
        println!("{}, {}", x, n);
        println!("{:?}, way: {:?}", loc, way);
    });
    manhattan(loc);
}
