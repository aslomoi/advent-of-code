use std::fs::read_to_string;
use std::collections::HashSet;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let grid: Vec<Vec<isize>> = input.split('\n')
        .map(|r| r.chars()
                  .map(|c| c.to_digit(10).unwrap() as isize)
                  .collect())
        .collect();
    let start = (0,0);
    let end = (grid[0].len() as isize - 1, grid.len() as isize - 1 );

    let mut dist: Vec<Vec<isize>> = vec![ vec![10000000; end.0+1]; end.1+1];
    let mut prev = vec![ vec![(0,0); end.0+1]; end.1+1];
    let mut queue: Vec<(isize, isize)> = vec![];
    for i in 0..=end.0 {
        for j in 0..=end.1 {
            queue.push((i as isize,j as isize));
        }
    }
    dist[start.1][start.0] = 0;

    while queue.len() > 0 {
        let (x,y) = get_min(queue, &dist);
        queue.remove(0);
        if (x,y) == end {
            println!("{:?}", path);
            break;
        }
        for (x2,y2) in [(x+1, y), (x-1,y), (x, y+1), (x, y-1)] {
            if 0 <= x2 && x2 <= end.0 && 0 <= y2 && y2 <= end.1 && !seen.contains(&(x2,y2)) {
                path.push((x2,y2));
                queue.push(path.clone());
            }
        }
        println!("{:?}", end);
    }

    // println!("{:?}", grid);
}

fn get_min(queue: Vec<(isize, isize)>, dist: &Vec<Vec<usize>>) -> (isize, isize) {
    let mut min = 10000000;
    let mut u = (10000,10000);

    for (x,y) in queue {
        if dist[y as usize][x as usize] <= min {
            min = dist[y as usize][x as usize];
            u = (x,y);
        }
    }
    u
}