use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let cmds = input
        .split("\n")
        .map(|l| {
            let mut inst = l.split(" ");
            let cmd = inst.next().unwrap();
            let num = inst.next().unwrap().parse::<i32>().unwrap();
            (cmd, num)
        })
        .collect::<Vec<_>>();

    (0..cmds.len()).for_each(|x| {
        let mut cmds1 = cmds.clone();
        match cmds[x].0 {
            "nop" => cmds1[x].0 = "jmp",
            "jmp" => cmds1[x].0 = "nop",
            _ => (),
        }
        let (fin, acc) = run_program(cmds1);
        if fin {
            println!("Successful Termination: Acc {}", acc);
        };
    });
}

fn run_program(cmds: Vec<(&str, i32)>) -> (bool, i32) {
    let mut done: Vec<usize> = vec![];
    let mut acc: i32 = 0;
    let mut idx: usize = 0;

    loop {
        if done.contains(&idx) {
            return (false, acc);
        } else if idx == cmds.len() {
            return (true, acc);
        } else {
            done.push(idx);
        }

        let (cmd, num) = cmds[idx];

        match cmd {
            "acc" => {
                acc += num;
                idx += 1
            }
            "jmp" => idx = (idx as i32 + num) as usize,
            "nop" => idx += 1,
            _ => println!("ERROR!"),
        }
    }
}
