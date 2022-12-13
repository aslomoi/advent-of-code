use std::fs::read_to_string;


fn main() {
    let input = read_to_string("input.txt").unwrap();
    let mut grid:Vec<Vec<i32>> = input.split("\n").map(|l| {
        l.split("").filter(|x| *x != "").map(|x| x.parse().unwrap()).collect::<Vec<_>>()
        }).collect::<Vec<_>>();

    let n_row = grid.iter().len();
    let n_col = grid[0].iter().len();

    let mut flashes = 0;
    for step in 0..1000 {
        if grid.iter().flatten().filter(|&x| *x == 0).count() == grid.iter().flatten().count() {
            println!("Aligned: {}", step);
            break;
        }

        for x in 0..n_col {
            for y in 0..n_row {
                grid[y][x] += 1;
            }
        }

        let neighbours: Vec<(i32,i32)> = vec![(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)];

        while grid.iter().flatten().filter(|&x| *x > 9).count() > 0 {
            for x in 0..n_col {
                for y in 0..n_row {
                    if grid[y][x] > 9 {
                        grid[y][x] = 0;
                        flashes +=1;
                        neighbours.iter().for_each(|p|
                        if 0 <= y as i32 + p.1 && y as i32 + p.1 < n_row as i32 &&
                        0 <= x as i32 +p.0  && x as i32 +p.0 < n_col as i32 &&
                        grid[(y as i32 + p.1) as usize][(x as i32 +p.0) as usize] != 0
                        {
                            grid[(y as i32 + p.1) as usize][(x as i32 +p.0) as usize] += 1;
                        });
                    }
                }
            }
        }
    }

    println!("Total Flashes: {}", flashes)
}
