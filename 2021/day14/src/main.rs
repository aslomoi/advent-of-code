use std::fs::read_to_string;
use std::collections::HashMap;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let mut inputs = input
        .split("\n\n");
    let mut poly: Vec<char> = inputs.next().unwrap().chars().collect();
    let pairs = inputs.next().unwrap().split('\n')
        .fold(HashMap::new(), |mut hash, x| {
            let mut vals = x.split(" -> ");
            let pairs: Vec<char> = vals.next().unwrap().chars().collect();
            let pair = (pairs[0], pairs[1]);
            let val: char = vals.next().unwrap().parse().unwrap();

            hash.insert(pair,val);
            hash
            });

    let mut counter: HashMap<_,u128> = poly.iter().zip(poly.iter().skip(1)).fold(
    HashMap::new(), |mut hash, x| {
        *hash.entry(x).or_insert(0) += 1;
        hash
    }
    );

    for _ in 0..40 {
        counter = counter.keys().fold(
            HashMap::new() as HashMap<_,u128>, |mut hash, &(a,c)| {
                let num = counter[&(a,c)];
                let b = &pairs[&(*a,*c)];
                *hash.entry((a,b)).or_insert(0) += num;
                *hash.entry((b,c)).or_insert(0) += num;
            hash
        });
    }

    let mut char_count = counter.keys().fold(
        HashMap::new(), |mut hash, &(a,b)| {
            let num = counter[&(a,b)];
            *hash.entry(a).or_insert(0) += num;
            hash
        }
    );
    // add in the last value
    *char_count.entry(poly.iter().last().unwrap()).or_insert(0) += 1;

    let max = char_count.values().max().unwrap();
    let min = char_count.values().min().unwrap();
    println!("{}", max - min);
}