use std::fs::read_to_string;
use std::collections::{HashMap,HashSet};

fn main() {
    let input = read_to_string("input.txt").unwrap();
    let mut sections = input.split("\n\n");
    let mut rules = HashMap::new();
    sections.next().unwrap().split('\n').for_each(|l| {
        let key = l.split(": ").next().unwrap();
        let val = l.split(": ").skip(1).next().unwrap().split(" or ");

        let range = val.map(|x| {
            let mut y = x.split('-');
            (y.next().unwrap().parse::<u64>().unwrap(),y.next().unwrap().parse::<u64>().unwrap())
        } 
        )
        .collect::<Vec<_>>();

        rules.insert(key, range);
    });

    let my_tkt = parse_tik(sections.next().unwrap().split("\n").skip(1).next().unwrap());
    let tkts = sections.next().unwrap().split('\n').skip(1).map(|x| parse_tik(x)).collect::<Vec<_>>();

    let errors = tkts.iter().fold(0,|acc,tkt| acc + sum_errors(tkt.to_vec(), &rules));
    println!("Error sum: {}", errors);

    let valid_tkts = tkts.iter().filter(|tkt| sum_errors(tkt.to_vec(), &rules) == 0).collect::<Vec<_>>();

    // let v_errors = valid_tkts.iter().fold(0,|acc,tkt| acc + sum_errors(tkt.to_vec(), &rules));
    // println!("Valid: {}", v_errors);


    let keys = rules.keys().into_iter().collect::<HashSet<_>>();
    let mut options = vec![keys; my_tkt.len()];

    for tkt in valid_tkts {
        for (i,v) in tkt.iter().enumerate() {
            let del = options[i].clone().into_iter().filter( |&key| 
                !((rules[*key][0].0..=rules[*key][0].1).contains(v) ||  (rules[*key][1].0..=rules[*key][1].1).contains(v) )
            ).collect::<HashSet<_>>();
            if i == 10 {println!("{}: from {} {:?}",i, v,del)};

            options[i] = options[i].clone().into_iter().filter( |&key| 
                (rules[*key][0].0..=rules[*key][0].1).contains(v) ||  (rules[*key][1].0..=rules[*key][1].1).contains(v) 
            ).collect::<HashSet<_>>();
        }
    }

    let mut mappings: HashMap<&str, usize> = HashMap::new();
    'outer: while options.len() > 0 {
        'index: for (i, idx) in options.clone().iter().enumerate() {
            if idx.len() == 1 {
                let key = idx.iter().next().unwrap();
                mappings.insert(key,i);
                for mut each in &options {
                    each.remove(key);
                }
                println!("{:?}", &options);
                break 'outer;
            }
        }
    }
    // for (i,vs) in options.iter().enumerate() {
    //     println!("{}: {:?}", i, vs);
    // }

    
}

fn parse_tik(line: &str) -> Vec<u64> {
    line.split(',').map(|x| x.parse::<u64>().unwrap()).collect::<Vec<_>>()
}

fn sum_errors(tkt: Vec<u64>, rules: &HashMap<&str, Vec<(u64,u64)>>) -> u64 {
    let mut error = 0u64;
    for v in tkt {
        let mut found = false;
        for (_,r) in rules {

            if (r[0].0..=r[0].1).contains(&v) ||  (r[1].0..=r[1].1).contains(&v) {
                found = true;
                break;
            }
        }
        if !found {
            error += v;
        }
    }
    error
}