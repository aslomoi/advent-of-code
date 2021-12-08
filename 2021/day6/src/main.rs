use std::fs::read_to_string;
use ndarray::{arr2,Array1};

fn main() {
    let input = read_to_string("input.txt").unwrap();

    let fish: Vec<i32> = input
        .split(",")
        .map(|x| x.parse().unwrap() )
        .collect();

    let mut timers:Vec<i32> = vec![0_i32;9];
    fish.iter().for_each(|x| timers[*x as usize] += 1);

    let x: Array1<usize> = (0..=8_usize).map(|i| timers[i] as usize).collect::<Vec<_>>().into();
    let a = arr2(&[
        [0,1,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,1,0,0],
        [1,0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0]
    ]);

    let count:usize = (0..256).fold(x, |acc, _| a.dot(&acc)).iter().sum();

    println!("{}", count);
}
