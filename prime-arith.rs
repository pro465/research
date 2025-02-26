fn main() {
    let lim = 100000;
    let primes = gen_primes_upto(lim);
    let n = 1;
    let mut v = Vec::new();
    for i in 0..n {
        v.push(working(i, lim, &primes, &v));
    }
    for (i, c) in working(n, lim, &primes, &v).iter().enumerate() {
        println!("{i}");
        if !c && v.iter().all(|c| !c[i]) {
            println!("^^^^^^^^ FOUND (maybe)");
            break;
        }
    }
}

fn gen_primes_upto(n: usize) -> Vec<usize> {
    let mut res = Vec::new();
    for i in 2..n {
        if res.iter().all(|p| i%p > 0) {
            res.push(i)
        }
    }
    res
}

fn working(n: usize, upto: usize, primes: &[usize], prev: &[Vec<bool>]) -> Vec<bool> {
    if n == 0 {
        let mut v = vec![false; upto];
        for &i in primes {
            v[i] = true;
        }
        return v
    }
    let mut res = vec![false; upto];
    for part1 in 0..=(n-1)/2 {
        let part2 = n-1-part1;
        for (a, c) in prev[part1].iter().enumerate() {
            if !c { continue }
            let lim = if part1 == part2 { a+1 } else { upto };
            for (b, c) in prev[part2][..lim].iter().enumerate() {
                if !c { continue }
                if a*b < upto {
                    res[a*b]=true;
                }
                if a+b < upto {
                    res[a+b]=true;
                }
                if a-b < upto {
                    res[a-b]=true;
                }
                if b > 0 && a/b < upto && a%b == 0 {
                    res[a/b]=true;
                }
            }
        }
    }
    res
}
