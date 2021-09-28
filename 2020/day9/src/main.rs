use queue::Queue;
use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let nums = input
        .split("\n")
        .map(|x| x.parse::<u64>().unwrap())
        .collect::<Vec<_>>();

    let preamble: usize = 25;
    let mut pre: Queue<u64> = Queue::with_capacity(preamble);
    for i in nums.iter().take(preamble) {
        pre.queue(*i).unwrap();
    }

    let mut invalid: u64 = 0;
    nums.iter().skip(preamble).for_each(|x| {
        match possible(&pre, *x) {
            true => (),
            false => {
                invalid = *x;
            }
        };
        pre.force_queue(*x);
    });

    println!("Invalid num: {}", invalid);

    for i in 0..nums.len() - 1 {
        let mut j = 2;
        loop {
            let sum = nums.iter().skip(i).take(j).fold(0, |acc, x| acc + x);

            if sum == invalid {
                let mut contig = nums.iter().skip(i).take(j).collect::<Vec<_>>();
                contig.sort();
                println!(
                    "Contiguous outer sum: {:?}",
                    *contig.first().unwrap() + *contig.last().unwrap()
                );
                break;
            } else if sum > invalid {
                break;
            } else {
                j += 1;
            }
        }
    }
}

fn possible(pre: &Queue<u64>, x: u64) -> bool {
    let v = pre.vec();
    for i in 0..pre.len() - 1 {
        for j in i + 1..pre.len() {
            if v[i] + v[j] == x {
                return true;
            }
        }
    }
    false
}
