fn cost(cm: &[(usize, u64)], n: usize, prev_record: u64, costs: &mut [u64]) -> u64 {
    costs.fill(0);
    let mut partial_sum = 0;

    for i in 1..=n {
        let c = cm.iter().filter(|(d, _)| i>=*d).map(|(d, c)| costs[i-d]+c).min().unwrap_or(100000);
        costs[i] = c;
        partial_sum += c;
        if partial_sum > prev_record {
            break
        }
    }

    partial_sum
}

fn check(curr: &[(usize, u64)]) -> bool {
     curr.iter().any(|x| x.0 == 1) && (curr[0].0 == 1 || curr[1..].iter().all(|x| x.0 != curr[0].0))
}

fn inc(curr: &mut [(usize, u64)], n: usize) -> bool {
    for (d, _) in curr.iter_mut() {
        if *d < n {
            *d+=1;
            return true
        }
        *d=1;
    }
    false
}

fn find(costs: &[u64], n: usize) -> Vec<(usize, u64)> {
    let mut cm: Vec<_> = costs.iter().map(|&x| (1, x)).collect();
    let mut costs = vec![0; n+1];
    let mut curr_best = cm.clone();
    let mut cost_best = cost(&cm, n, u64::MAX, &mut costs);

    while inc(&mut cm, n) {
        if !check(&cm) {
            continue
        }
        let curr_cost = cost(&cm, n, cost_best, &mut costs);
        if curr_cost < cost_best {
            use std::iter::FromIterator;
            println!("{:?} score={}", Vec::from_iter(cm.iter().map(|x| x.0)), (curr_cost as f64)/(n as f64));
            cost_best = curr_cost;
            curr_best = cm.clone();
        }
    }

    curr_best
}

fn main() {
    let n=4;
    println!("n={:?}\n============", n);
    
    for up in 2.. {
        let cm: Vec<_> = (2..=up).collect();
        println!("weights=2..{up:?}");
        let cm = &cm;
        let sol: Vec<_> = find(cm, n).iter().map(|x| x.0).collect();

        println!("sol={:?}", sol);
    }
}
