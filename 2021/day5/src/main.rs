use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let inputs = input
        .split("\n");
    let mut lines = vec![];
    for l in inputs {
        let mut pts = vec![];
        for pt in l.split(" -> ") {
            let v = pt.split(',').map(|x| x.parse::<usize>().unwrap() ).collect::<Vec<_>>();
            pts.push(v)
        }
        lines.push(pts)
    }
    let size = 1000;
    let mut grid = vec![vec![0; size]; size];
    for line in &lines {
        let pt1 = &line[0];
        let pt2 = &line[1];
        if pt1[0] == pt2[0] {
            let x = pt1[0];
            for y in pt1[1]..=pt2[1] {
                grid[y][x] +=1
                }
            for y in pt2[1]..=pt1[1] {
                grid[y][x] +=1
                }
        }
        else if pt1[1] == pt2[1] {
            let y = pt1[1];
            for x in pt1[0]..=pt2[0] {
                grid[y][x] +=1
                }
            for x in pt2[0]..=pt1[0] {
                grid[y][x] +=1
                }
        }
        else if pt1[0] < pt2[0] && pt1[1] > pt2[1] {
            for (x,y) in (pt1[0]..=pt2[0]).zip((pt2[1]..=pt1[1]).rev()) {
                grid[y][x] +=1
                }
        }
        else if pt1[0] > pt2[0] && pt1[1] > pt2[1] {
            for (x,y) in (pt2[0]..=pt1[0]).rev().zip((pt2[1]..=pt1[1]).rev()) {
                grid[y][x] +=1
                }
        }
        else if pt1[0] > pt2[0] && pt1[1] < pt2[1] {
            for (x,y) in (pt2[0]..=pt1[0]).rev().zip(pt1[1]..=pt2[1]) {
                grid[y][x] +=1
                }
        }
        else if pt1[0] < pt2[0] && pt1[1] < pt2[1] {
            for (x,y) in (pt1[0]..=pt2[0]).zip(pt1[1]..=pt2[1]) {
                grid[y][x] +=1
                }
        }
    }
    print_grid(&grid);
    println!("{}", grid.iter().flatten().filter(|&x| *x > 1).count());

}

fn print_grid(grid: &Vec<Vec<usize>>) -> () {
    for g in grid {
        for x in g {
            match x {
                0 => print!("."),
                x => print!("{}", x)
            }
        }
        println!();
    }
}