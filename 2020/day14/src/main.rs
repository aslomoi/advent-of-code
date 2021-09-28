use std::collections::HashMap;
use std::fmt;
use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let blocks = input.split("mask = ").skip(1);

    let mut mem: HashMap<u64, u64> = HashMap::new();
    for block in blocks {
        let mask = block.split("\n").next().unwrap();

        for line in block.split("\n").skip(1) {
            if line == "" {
                continue;
            }
            let mem_loc = line[4..].split(']').next().unwrap().parse::<u64>().unwrap();
            let num = line.split(" ").last().unwrap().parse::<u64>().unwrap();

            part2(&mut mem, mask, mem_loc, num);
        }
    }

    // println!("Hashmap: {:?}", mem);
    let mem_sum = mem.iter().fold(0, |acc, (_, x)| acc + x);
    println!("Sum: {}", mem_sum);
}

fn part1(mem: &mut HashMap<u64, u64>, mask: &str, mem_loc: u64, num: u64) {
    let (or_mask, and_mask) = get_masks(mask);
    mem.insert(mem_loc, num & and_mask | or_mask);
}

fn part2(mem: &mut HashMap<u64, u64>, mask: &str, mem_loc: u64, num: u64) {
    let xs = mask
        .chars()
        .fold(0, |acc, x| if x == 'X' { acc + 1 } else { acc });
    let xs_bin = to_bin_vec(xs);

    let rev_idx = mask.len() - 1;
    let pre_mask = mask
        .chars()
        .enumerate()
        .map(|(i, x)| match x {
            '0' => mem_loc.rotate_right((rev_idx - i) as u32) & 1,
            '1' => 1,
            'X' => 2,
            _ => panic!("Wrong value!"),
        })
        .collect::<Vec<_>>();

    let post_masks = xs_bin
        .iter()
        .map(|x_bin| {
            let mut x_rep = x_bin.clone();
            pre_mask
                .iter()
                .map(|x| match x {
                    2 => x_rep.pop().unwrap(),
                    x => *x,
                })
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();

    let mem_locs = post_masks
        .iter()
        .rev()
        .map(|m| m.iter().fold(0u64, |acc, x| acc.rotate_left(1) + x))
        .collect::<Vec<_>>();

    mem_locs.iter().for_each(|new_m| {
        mem.insert(*new_m, num);
    });
}

fn to_bin_vec(x: u64) -> Vec<Vec<u64>> {
    let mut out: Vec<Vec<u64>> = vec![];
    for n in 0..u64::pow(2, x as u32) {
        let mut num: Vec<u64> = vec![];
        for i in 0..x {
            num.insert(0, (n >> i) & 1)
        }
        out.insert(0, num);
    }
    out
}

fn merge_vecs(a: Vec<Vec<u64>>, b: Vec<u64>) -> Vec<u64> {
    let mut c = vec![];
    a.iter().enumerate().for_each(|(i, x)| {
        x.iter().for_each(|a| c.push(*a));
        if i < b.len() {
            c.push(b[i]);
        }
    });
    c
}

fn get_masks(mask: &str) -> (u64, u64) {
    let or_mask: u64 = mask
        .chars()
        .map(|x| match x {
            '0' => 0,
            '1' => 1,
            'X' => 0,
            x => panic!("Error on OR-mask: found {}", x),
        })
        .fold(0, |acc, x| acc * 2 + x);

    let and_mask: u64 = mask
        .chars()
        .map(|x| match x {
            '0' => 0,
            '1' => 1,
            'X' => 1,
            x => panic!("Error on OR-mask: found {}", x),
        })
        .fold(0, |acc, x| acc * 2 + x);
    // println!("mask: {}", mask);
    // println!("or: {}, and: {}", or_mask, and_mask);
    (or_mask, and_mask)
}
