use std::collections::HashMap;
use std::fs::read_to_string;

static FIELDS: [&str; 7] = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let raw_passports: Vec<Vec<&str>> = input
        .split("\n\n")
        .map(|x| x.split_whitespace().collect())
        .collect();

    let passports: Vec<HashMap<_, _>> = raw_passports
        .iter()
        .map(|p| {
            p.iter()
                .map(|x| {
                    let mut a = x.split(":");
                    (a.next().unwrap(), a.next().unwrap())
                })
                .collect::<HashMap<_, _>>()
        })
        .collect();

    let part1 = passports.iter().fold(0, |acc, p| {
        if FIELDS.iter().all(|f| p.contains_key(f)) {
            acc + 1
        } else {
            acc
        }
    });

    let part2 = passports.iter().fold(0, |acc, p| {
        if FIELDS.iter().all(|f| {
            p.contains_key(f)
                && match *f {
                    "byr" => (1920..=2002).contains(&p[f].parse::<i32>().unwrap()),
                    "iyr" => (2010..=2020).contains(&p[f].parse::<i32>().unwrap()),
                    "eyr" => (2020..=2030).contains(&p[f].parse::<i32>().unwrap()),
                    "hgt" => match p[f] {
                        v if v.contains("cm") => {
                            (150..=193).contains(&v[0..3].parse::<i32>().unwrap_or(0))
                        }
                        v if v.contains("in") => {
                            (59..=76).contains(&v[0..2].parse::<i32>().unwrap_or(0))
                        }
                        _ => false,
                    },
                    "hcl" => {
                        p[f].starts_with('#')
                            && p[f].len() == 7
                            && p[f].chars().skip(1).all(|c| c.is_ascii_hexdigit())
                    }
                    "ecl" => ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].contains(&p[f]),
                    "pid" => p[f].len() == 9 && p[f].chars().all(|c| c.is_ascii_digit()),
                    _ => false,
                }
        }) {
            acc + 1
        } else {
            acc
        }
    });

    println!("{:?}", part2);
}
