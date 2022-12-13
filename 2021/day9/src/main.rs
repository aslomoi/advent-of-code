use std::fs::read_to_string;


fn main() {
    let input = read_to_string("input.txt").unwrap();
    let grid:Vec<Vec<i32>> = input.split("\n").map(|l| {
        l.split("").filter(|x| *x != "").map(|x| x.parse().unwrap()).collect::<Vec<_>>()
        }).collect::<Vec<_>>();

    let max_col = grid[0].iter().count() -1;
    let max_row = grid.iter().count() -1;

    println!("{}, {}", max_col, max_row);
    let mut risks = vec![];
    for (j,r) in grid.iter().enumerate() {
        for (i,c) in r.iter().enumerate() {
            // Left
            if i > 0 {
                if grid[j][i-1] <= grid[j][i] {
                    continue
                }
            }
            // Right
            if i+1 <= max_col {
                if grid[j][i+1] <= grid[j][i] {
                    continue
                }
            }
            // Up
            if j > 0 {
                if grid[j-1][i] <= grid[j][i] {
                    continue
                }
            }
            // Down
            if j+1 <= max_row {
                if grid[j+1][i] <= grid[j][i] {
                    continue
                }
            }
            risks.push(((j,i),c+1))
        }
    }

    let mut basins: Vec<usize> = risks.iter().map(|(loc, _)| basin(*loc, &grid).iter().count()).collect();
    basins.sort();
    println!("{:?}", basins);
    let mult = basins.iter().rev().take(3).fold(1, |acc, x| x*acc);
    println!("{:?}", mult);
}

fn basin(loc: (usize, usize), grid: &Vec<Vec<i32>>) -> Vec<(usize, usize)> {
    let max_col = grid[0].iter().count() -1;
    let max_row = grid.iter().count() -1;

    let mut count = vec![loc];

    if loc.1 > 0 && grid[loc.0][loc.1 -1] > grid[loc.0][loc.1] && grid[loc.0][loc.1 -1] != 9{
        count.extend(basin((loc.0, loc.1 -1), grid));
    };
    if loc.1 < max_col && grid[loc.0][loc.1 +1] > grid[loc.0][loc.1]  && grid[loc.0][loc.1 + 1] != 9 {
        count.extend(basin((loc.0, loc.1 + 1), grid));
    };
    if loc.0 > 0 && grid[loc.0 -1][loc.1] > grid[loc.0][loc.1]   && grid[loc.0 -1][loc.1] != 9{
        count.extend(basin((loc.0 -1, loc.1), grid));
    };
    if loc.0 < max_row && grid[loc.0 + 1][loc.1] > grid[loc.0][loc.1]  && grid[loc.0 +1][loc.1] != 9 {
        count.extend(basin((loc.0 + 1, loc.1), grid));
    };
    count.sort();
    count.dedup();
    count
}