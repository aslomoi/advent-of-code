use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let mut inputs = input
        .split("\n\n");
    let pts: Vec<Vec<usize>> = inputs.next().unwrap().split('\n')
        .map(|st| {
            let mut x = st.split(',');
            vec![x.next().unwrap().parse().unwrap(), x.next().unwrap().parse().unwrap()]
            })
        .collect();
    let folds: Vec<Vec<usize>> = inputs.next().unwrap().split('\n')
        .map(|st| {
            let mut x = st[11..].split('=');
            let dir = match x.next().unwrap() {
                "y" => 1,
                "x" => 0,
                _ => panic!()
            };
            vec![dir, x.next().unwrap().parse().unwrap()]
        })
        .collect();
    let x_max = pts.iter().fold(0, |mut max, pt| {
        if pt[0] > max {
            max = pt[0]
        }
        max
    });
    let y_max = pts.iter().fold(0, |mut max, pt| {
        if pt[1] > max {
            max = pt[1]
        }
        max
    });
    let mut grid = vec![ vec![false; x_max+1] ; y_max+1];
    pts.iter().for_each(|pt| grid[pt[1]][pt[0]] = true);

    for f in &folds {
        if f[0] == 1 {
            grid = grid.iter().zip(grid.iter().skip(f[1]+1).rev())
            .map(|(r1,r2)| {
                r1.iter().zip(r2.iter())
                .map(|(c1, c2)| c1 | c2).collect()
            }).collect();
        } else {
            grid = grid.iter().map(|r| {
                r.iter().zip(r.iter().skip(f[1]+1).rev())
                .map(|(c1, c2)| c1 | c2).collect()
            }).collect();
        }
    }
    let sum = grid.iter().fold(0, |acc, r| {
        let r_sum = r.iter().filter(|&c| *c).count();
        acc + r_sum
        });
    println!("{}", sum);
    print_grid(&grid);
}
fn print_grid(grid: &Vec<Vec<bool>>) {
    for r in grid {
        for c in r {
            if *c {
                print!("█")
            } else { print!(" ")}
        }
        println!("");
    }
    println!("");
}