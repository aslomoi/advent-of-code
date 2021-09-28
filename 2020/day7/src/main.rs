use std::collections::{HashMap, HashSet};
use std::fs::read_to_string;

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let rules = input
        .split("\n")
        .map(|l| {
            let mut rule = l.split(" bags contain");
            let colour = rule.next().unwrap();
            let contents = rule
                .next()
                .unwrap()
                .split(", ")
                .filter(|&x| !x.contains(&"no other"))
                .map(|x| {
                    let mut content = x.split_whitespace();
                    (
                        content.next().unwrap().parse::<u64>().unwrap(),
                        content.next().unwrap().to_owned() + " " + content.next().unwrap(),
                    )
                })
                .collect::<Vec<_>>();
            (colour, contents)
        })
        .collect::<HashMap<_, _>>();

    part1("shiny gold", rules.clone());
    // Subtract 1 as problem asks for bags within, not total bags
    println!("{}", part2("shiny gold", rules.clone()) - 1);
}
fn part1(colour: &str, rules: HashMap<&str, Vec<(u64, String)>>) {
    let mut colours: HashSet<String> = HashSet::new();
    colours.insert(String::from(colour));

    loop {
        let new_colours: HashSet<String> = rules
            .clone()
            .into_iter()
            .filter(|(_, v)| v.iter().any(|(_, c)| colours.contains(c)))
            .map(|(k, _)| String::from(k))
            .collect::<HashSet<_>>();

        if new_colours
            .difference(&colours)
            .collect::<HashSet<_>>()
            .is_empty()
        {
            break;
        } else {
            colours = new_colours.union(&colours).map(|x| x.to_owned()).collect();
        }
    }
    println!("Final Colours: {:?}", colours);
    println!("Final Length: {:?}", colours.len() - 1);
}

fn part2(colour: &str, rules: HashMap<&str, Vec<(u64, String)>>) -> u64 {
    let sum: u64 = rules[colour]
        .iter()
        .map(|(num, c)| num * part2(c, rules.clone()))
        .sum();
    1 + sum
}
