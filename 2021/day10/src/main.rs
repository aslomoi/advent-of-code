use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let navs:Vec<Vec<char>> = input.split("\n").map(|l| {
        l.chars().collect::<Vec<_>>()
        }).collect::<Vec<_>>();

    let mut scores:Vec<usize> = vec![];
    let errors = navs.iter().fold(0, |acc, n| {
        let mut stack = vec![];
        let mut error = 0;
        for v in n {
            match v {
                '(' => stack.push(v),
                '[' => stack.push(v),
                '{' => stack.push(v),
                '<' => stack.push(v),
                ')' => {
                    if *stack.iter().last().unwrap() == &'(' {
                        stack.pop();
                    } else {
                        error = 3;
                        break;
                    }
                },
                ']' => {
                    if *stack.iter().last().unwrap() == &'[' {
                        stack.pop();
                    } else {
                        error = 57;
                        break;
                    }
                },
                '}' => {
                    if *stack.iter().last().unwrap() == &'{' {
                        stack.pop();
                    } else {
                        error = 1197;
                        break;
                    }
                },
                '>' => {
                    if *stack.iter().last().unwrap() == &'<' {
                        stack.pop();
                    } else {
                        error = 25137;
                        break;
                    }
                },
                _ => ()
            }
        }
        if error == 0 {
            let amt = stack.iter().rev()
                .fold( 0, |curr, v| {
                        let num = match v {
                            '(' => 1,
                            '[' => 2,
                            '{' => 3,
                            '<' => 4,
                            _ => 0
                        };
                        curr*5 + num
                    }
                );
            scores.push(amt);
        }
        acc + error
    });

    println!("{:?}", errors);

    scores.sort();
    let mid = (scores.len()-1)/2;
    println!("{}", scores[mid]);



}