use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let mut layout = input
        .split("\n")
        .map(|x| x.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let rows = layout.len();
    let cols = layout[0].len();

    // render(&layout);

    loop {
        let mut next = layout.clone();
        for r in 0..rows {
            for c in 0..cols {
                next[r][c] = iter(r as isize, c as isize, &layout);
            }
        }
        if layout == next {
            let n_final = next.iter().fold(0, |acc, r| {
                acc + r
                    .iter()
                    .fold(0, |acc, c| if *c == '#' { acc + 1 } else { acc })
            });
            println!("\nNo. occupied seats: {}", n_final);
            // render(&next);
            break;
        } else {
            layout = next;
        }
    }
}

fn render(layout: &Vec<Vec<char>>) {
    for row in layout {
        for seat in row {
            print!("{} ", seat);
        }
        println!("");
    }
}

fn iter(r: isize, c: isize, layout: &Vec<Vec<char>>) -> char {
    let rows = layout.len() as isize;
    let cols = layout[0].len() as isize;
    let neighbours: Vec<(isize, isize)> = vec![
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ];
    let n_occupied = neighbours.iter().fold(0, |acc, (r_n, c_n)| {
        // Part 2
        let mut ray = 1..;
        let mut ret_val: i32 = acc;
        let mut x;

        loop {
            x = ray.next().unwrap();

            if (0..rows).contains(&(r + *r_n * x)) && (0..cols).contains(&(c + *c_n * x)) {
                match layout[(r + *r_n * x) as usize][(c + *c_n * x) as usize] {
                    '#' => {
                        ret_val += 1;
                        break;
                    }
                    'L' => break,
                    _ => (),
                }
            } else {
                break;
            }
        }
        ret_val

        // Part 1
        // if (0..rows).contains(&(r + *r_n))
        //     && (0..cols).contains(&(c + *c_n))
        //     && layout[(r + *r_n) as usize][(c + *c_n) as usize] == '#'
        // {
        //     acc + 1
        // } else {
        //     acc
        // }
    });

    let next: char;
    match layout[r as usize][c as usize] {
        'L' if n_occupied == 0 => next = '#',
        '#' if n_occupied >= 5 => next = 'L',
        x => next = x,
    }
    next
}
