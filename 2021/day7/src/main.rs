use std::fs::read_to_string;


fn main() {
    let input = read_to_string("input.txt").unwrap();
    let mut crabs = input
    .split(",")
    .map(|x| x.parse::<i32>().unwrap() )
    .collect::<Vec<_>>();
    crabs.sort();


    let min = crabs.first().unwrap();
    let max = crabs.last().unwrap();

    let mut best: (i32, i32) = (0, -1);
    for i in *min..=*max {
        let sum = crabs.iter().map(|c|  {
            let n =  (c-i).abs();

            // Part 1
            // n
            // Part 2
            n * (n+1)/2
        }).sum();

        if best.1 < 0 || sum < best.1 {
            best = (i, sum);
        }
    }
    println!("{:?}", best);
}
