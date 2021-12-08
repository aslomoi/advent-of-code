use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let mut inputs = input
        .split("\n\n");
    let vals: Vec<_> = inputs.next().unwrap().split(",").map(|x| x.parse::<i32>().unwrap()).collect();
    let mut boards = vec![];
    for board in inputs {
        let mut b = vec![];
        for row in board.split("\n")
        {
            let mut r = vec![];
            for val in row.split(" ") {
                if val != "" {
                    r.push(val.parse::<i32>().unwrap())
                }
            }
            b.push(r)
        }
        boards.push(b);
    }

    let mut pos: Option<usize>;
    let mut winner = 100;
    let mut last_val = 101;

    // // Part 1
    // 'outer: for num in vals {
    //     for i in 0..boards.len() {
    //         pos = find_val(boards[i].clone(), num as i32);
    //         match pos {
    //             Some(x) => {
    //                 boards[i][x / 5][x % 5] = -1;
    //                 if  won(&boards[i]) {
    //                     winner = i;
    //                     last_val = num;
    //                     break 'outer;
    //                 }
    //             },
    //             None => ()
    //         }
    //     }
    // }

    // Part 2
    let mut won_already = vec![];
    'outer: for num in vals {
        for i in 0..boards.len() {
            if won_already.contains(&i) {
                continue;
            }
            pos = find_val(boards[i].clone(), num as i32);
            match pos {
                Some(x) => {
                    boards[i][x / 5][x % 5] = -1;
                    if won(&boards[i]) {
                        if won_already.len() == boards.len() -1 {
                            winner = i;
                            last_val = num;
                            break 'outer;
                        } else {
                        won_already.push(i);
                        }
                    }
                },
                None => ()
            }
        }
    }

    let unmarked = boards[winner].iter().flatten().filter(|&x| *x != -1).sum::<i32>();
    println!("{}", unmarked * last_val);
}

fn won(board: &Vec<Vec<i32>>) -> bool {
    for row in board {
        let sum = (*row).iter().sum::<i32>();
        if sum == -5 {
            return true;
        }
    };
    for row in transpose((&board).to_vec()) {
        let sum = (*row).iter().sum::<i32>();
        if sum == -5 {
            return true;
        }
    }
    false
}

fn find_val(board: Vec<Vec<i32>>, val: i32) -> Option<usize> {
    let list = board.into_iter().flatten().collect::<Vec<i32>>();
    list.iter().position(|&v| v == val)
}

fn transpose<T>(v: Vec<Vec<T>>) -> Vec<Vec<T>>
where
    T: Clone,
{
    assert!(!v.is_empty());
    (0..v[0].len())
        .map(|i| v.iter().map(|inner| inner[i].clone()).collect::<Vec<T>>())
        .collect()
}