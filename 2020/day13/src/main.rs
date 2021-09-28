use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let time = input.split("\n").next().unwrap().parse::<u128>().unwrap();

    // Part 1
    // let ids = input
    //     .split("\n")
    //     .skip(1)
    //     .next()
    //     .unwrap()
    //     .split(",")
    //     .filter(|x| *x != "x")
    //     .map(|x| x.parse::<u128>().unwrap())
    //     .collect::<Vec<_>>();

    // let id = ids
    //     .iter()
    //     .reduce(|a, b| {
    //         if extra(*a, time) <= extra(*b, time) {
    //             a
    //         } else {
    //             b
    //         }
    //     })
    //     .unwrap();
    // println!("{}", time);
    // println!("{:?}", ids);
    // println!("Best is ID {}, with {}", id, id * extra(*id, time));

    let ids = input
        .split("\n")
        .skip(1)
        .next()
        .unwrap()
        .split(",")
        .enumerate()
        .filter(|(_, x)| *x != "x")
        .map(|(i, x)| (i as u128, x.parse::<u128>().unwrap()))
        .collect::<Vec<(_, _)>>();

    println!("{:?}", ids);

    // let mut t: u128 = 1;
    // while !ids.iter().all(|(i, x)| ((t + i) % x == 0)) {
    //     t += 1
    // }
    // println!("t={}", t);

    let n_max = ids
        .iter()
        .map(|(_, x)| x)
        .reduce(|a, b| if *a > *b { a } else { b })
        .unwrap();

    let (offset, max) = ids.iter().filter(|(_, x)| x == n_max).next().unwrap();
    println!("offset={} max={}", offset, max);
    let mut t: u128 = *max;
    while !ids.iter().all(|(i, x)| ((t + i - offset) % x == 0)) {
        t += max;
    }

    println!("t={}", t - offset);
}

fn extra(x: u128, time: u128) -> u128 {
    x * ((time as f32 / x as f32).ceil() as u128) - time
}
