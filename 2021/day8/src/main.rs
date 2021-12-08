use std::fs::read_to_string;
use std::collections::HashSet;


fn main() {
    let input = read_to_string("input.txt").unwrap();
    let inputs = input.split("\n").map(|l| {
        let mut sp = l.split("|");
        let ins = sp.next().unwrap().split(" ").filter(|x| *x != "").collect::<Vec<_>>();
        let outs = sp.next().unwrap().split(" ").filter(|x| *x != "").collect::<Vec<_>>();
        (ins, outs)
        }).collect::<Vec<_>>();

    // Part 1
    // let cnt = inputs.iter().fold(0, |acc, x| acc + x.1.iter().filter(|x| {
    //     vec![2, 3, 4, 7].contains(&x.chars().count())
    //     }).count());
    // println!("{:?}", cnt);

    // Part 2
    let total = inputs.iter().fold( 0, |acc, x| {
        let mut nums: Vec<HashSet<char>> = vec![HashSet::new(); 10];
        (x.0).iter().for_each(|v|
            match v.chars().count() {
                2 => nums[1] = v.chars().collect(),
                4 => nums[4] = v.chars().collect(),
                3 => nums[7] = v.chars().collect(),
                7 => nums[8] = v.chars().collect(),
                _ => ()
            }
        );
        // Get Nine
        for v in &x.0 {
            if v.chars().count() == 6 {
                let set: HashSet<char> = v.chars().collect();
                if set.is_superset(&nums[4]) {
                    nums[9] = set;
                    break;
                }
            }
        }
        // Get Six
        for v in &x.0 {
            if v.chars().count() == 6 {
                let set: HashSet<char> = v.chars().collect();
                if !set.is_superset(&nums[1]) {
                    nums[6] = set;
                    break;
                }
            }
        }
        // Get Zero
        for v in &x.0 {
            if v.chars().count() == 6 {
                let set: HashSet<char> = v.chars().collect();
                if set != nums[6] && set != nums[9] {
                    nums[0] = set;
                    break;
                }
            }
        }
        // Get Five
        for v in &x.0 {
            if v.chars().count() == 5 {
                let set: HashSet<char> = v.chars().collect();
                if set.is_subset(&nums[6]) {
                    nums[5] = set;
                    break;
                }
            }
        }
        // Get Three
        for v in &x.0 {
            if v.chars().count() == 5 {
                let set: HashSet<char> = v.chars().collect();
                if set.is_superset(&nums[1]) {
                    nums[3] = set;
                    break;
                }
            }
        }
        // Get Two
        for v in &x.0 {
            if v.chars().count() == 5 {
                let set: HashSet<char> = v.chars().collect();
                if set != nums[5] && set != nums[3] {
                    nums[2] = set;
                    break;
                }
            }
        }

        // Determine output
        let v = (x.1).iter().fold( 0, |acc, v| {
            let set = v.chars().collect::<HashSet<_>>();
            let val = nums.iter().position(|r| r == &set).unwrap();
            10*acc + val
        });

        acc + v
    });
    println!("{}", total);
}
