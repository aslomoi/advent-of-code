use std::fs::read_to_string;
use std::collections::HashMap;

// Moved to Python until I learn lifetimes :)

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let mut root_map:HashMap<&str, Vec<&str>> = HashMap::new();
    input.split('\n').for_each(|l| {
        let mut vals = l.split('-');
        let a = vals.next().unwrap();
        let b = vals.next().unwrap();
        match root_map.get_mut(&a) {
            Some(v) => {v.push(b);},
            None => {root_map.insert(a, vec![b]);}
        };
        match root_map.get_mut(&b) {
            Some(v) => {v.push(a);},
            None => {root_map.insert(b, vec![a]);}
        };
    });
    println!("Root Map: {:?}", root_map);
    find_paths(&vec![], "start", &root_map);
    }


fn find_paths<'a> (prev_path: &'a Vec<&str>, node: &'a str, root_map: &'a HashMap<&str, Vec<&str>>) -> Vec<Vec<&'a str>> {
    let mut path = prev_path.clone();
    match node.parse::<char>(){
        Ok(c) => {
            if c.is_lowercase() && prev_path.contains(&node) {
                return vec![];
            }
        },
        _ => ()
    }
    if node == "start" && path != vec![] as Vec<&str> {
        return vec![];
    }
    path.push(node.as_ref());
    if node == "end" {
        let mut tmp: Vec<Vec<&str>> = vec![];
        tmp.push(Box::new(path));
        return tmp;
    }
    println!("to check: {:?}", root_map[node]);
    let mut children = vec![];
    for child in &root_map[node] {
        let val = find_paths(&path, child, &root_map);
        if !val.is_empty() {
            println!("{:?}", val);
            children.push(val);
        }
    }
    let out: Vec<Vec<&str>> = children.iter().flatten().map(|v| v.clone()).collect();
    println!("children: {:?}", out);
    out
}