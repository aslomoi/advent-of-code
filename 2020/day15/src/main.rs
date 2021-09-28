use std::collections::HashMap;

fn main() {
    let mut nums = vec![0, 13, 1, 16, 6, 17];
    let mut spoken = HashMap::new();
    nums.iter().enumerate().for_each(|(i, x)| {
        spoken.insert(*x, vec![i, i]);
    });

    while nums.len() < 30000000 {
        let last = nums.last().unwrap();
        let n_idx = nums.len();
        let prev_exists = spoken.contains_key(last);

        match prev_exists {
            false => {
                nums.push(0);
            }
            true => {
                nums.push(spoken[last][0] - spoken[last][1]);
            }
        }

        let newest = nums.last().unwrap();
        if spoken.contains_key(newest) {
            spoken.insert(*newest, vec![n_idx, spoken[newest][0]]);
        } else {
            spoken.insert(*newest, vec![n_idx, n_idx]);
        }
    }

    println!("{:?}", nums.last().unwrap());
}
