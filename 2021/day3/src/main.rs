use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let cmds = input
        .split("\n")
        .map(|l| {
            l.chars().collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();

    let n_cols = cmds[0].len();

    let gamma = sum_cols(&cmds);
    let mut gamma_rate:i32 = 0;
    let mut epsilon_rate:i32 = 0;
        for (i, &val) in gamma.iter().rev().enumerate() {
        match(val) {
            val if val > 0 => {
                gamma_rate += i32::pow(2, i as u32)
            },
            val if val < 0 => {
                epsilon_rate += i32::pow(2, i as u32)
            },
            _ => ()
        }
    }

    let result = gamma_rate * epsilon_rate;
    println!("Part 1: {}", result);

    let mut oxy = cmds.clone();
    for i in 0..n_cols {
        let val = sum_cols(&oxy)[i];
        let mut new_oxy: Vec<Vec<char>> = vec![];
        match val {
            val if val > 0 => {
                for r in 0..oxy.len() {
                    if oxy[r][i] == '1' {
                        new_oxy.push(oxy[r].clone())
                    }
                }
            },
            val if val < 0 => {
                for r in 0..oxy.len() {
                    if oxy[r][i] == '0' {
                        new_oxy.push(oxy[r].clone())
                    }
                }
            },
            val if val == 0 => {
                for r in 0..oxy.len() {
                    if oxy[r][i] == '1' {
                        new_oxy.push(oxy[r].clone())
                    }
                }
            },
            _ => ()
        }
        oxy = new_oxy;
        if oxy.len() == 1 {
            break;
        }
    }

    let mut co2 = cmds.clone();
    for i in 0..n_cols {
        let val = sum_cols(&co2)[i];
        let mut new_co2: Vec<Vec<char>> = vec![];
        match val {
            val if val > 0 => {
                for r in 0..co2.len() {
                    if co2[r][i] == '0' {
                        new_co2.push(co2[r].clone())
                    }
                }
            },
            val if val < 0 => {
                for r in 0..co2.len() {
                    if co2[r][i] == '1' {
                        new_co2.push(co2[r].clone())
                    }
                }
            },
            val if val == 0 => {
                for r in 0..co2.len() {
                    if co2[r][i] == '0' {
                        new_co2.push(co2[r].clone())
                    }
                }
            },
            _ => ()
        }
        co2 = new_co2;
        if co2.len() == 1 {
            break;
        }
    }

    let co = bin_to_digit(co2[0].clone());
    let ox = bin_to_digit(oxy[0].clone());

    println!("Part 2: {}", ox*co);
}

fn sum_cols(cmds: &Vec<Vec<char>>) -> Vec<i32> {
    let mut cols = vec![0; cmds[0].len()];
    for cmd in cmds {
        for (i, val) in cmd.iter().enumerate() {
            match val {
                '1' => cols[i] += 1,
                '0' => cols[i] -= 1,
                _ => ()
            }

        }
    }
    cols
}

fn bin_to_digit(bin: Vec<char>) -> i32 {
    let mut num: i32 = 0;
    for (i, &val) in bin.iter().rev().enumerate() {
        if val == '1' {
            num += i32::pow(2, i as u32);
        }
    }
    num
}