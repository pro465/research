fn first_nonhit(v: &[usize], n: usize) -> usize {
    let mut lim = 0;
    'outer: for i in 0..=n {
        for j in lim..v.len() {
            lim = j;
            if i < v[j] {
                break;
            }
        }
        if lim < v.len() && i >= v[lim] {
            lim = v.len();
        }
        for j in 0..lim {
            for k in &v[j..lim] {
                if i < v[j] + k {
                    break;
                }
                if i == v[j] + k {
                    continue 'outer;
                }
            }
        }
        return i;
    }
    n + 1
}

fn works(v: &[usize], n: usize) -> bool {
    first_nonhit(v, n) == n + 1
}

fn reset(curr: &mut [usize], idx: usize) {
    curr[idx] += 1;
    for j in 1..curr.len() - idx {
        curr[idx + j] = curr[idx] + j;
    }
}

fn next(curr: &mut [usize], n: usize) -> bool {
    let mut lim = n + 1;
    for i in (0..curr.len()).rev() {
        if curr[i] < lim - 1 {
            reset(curr, i);
            return true;
        }
        lim = curr[i]
    }
    false
}

fn skip_obv_invalid(curr: &mut [usize], n: usize) -> bool {
    for i in 0..curr.len() {
        if first_nonhit(&curr[..i], n) < curr[i] {
            if i > 0 {
                reset(curr, i - 1);
            }
            if i == 0 || *curr.last().unwrap() > n {
                return false;
            }
        }
    }
    true
}

fn mss_b(n: usize, last: Vec<usize>) -> Vec<usize> {
    let mut v = last;
    for i in v.len()..=n {
        loop {
            if works(&v, n) {
                return v;
            }
            if !next(&mut v, n) || !skip_obv_invalid(&mut v, n) {
                break;
            }
        }
        v = (0..=i).collect();
    }
    v
}

fn score(v: &[usize], n: usize) -> usize {
    let mut s = 0;
    'outer: for i in 0..=n {
        for j in 0..v.len() {
            for k in &v[j..] {
                if i == v[j] + k {
                    s += 1;
                    continue 'outer;
                }
            }
        }
    }
    s
}

fn mss1(n: usize) -> Vec<usize> {
    let mut res = Vec::new();
    while score(&res, n) < n + 1 {
        let mut bps = 0;
        let mut bpm = 0;
        let mut brs = 0;
        let mut brm = (0, 0);
        for next in 0..=n {
            res.push(next);
            let s = score(&res, n);
            res.pop();

            if s > bps {
                bps = s;
                bpm = next;
            }
            for i in 0..res.len() {
                let t = res[i];
                res[i] = next;
                let s = score(&res, n);
                res[i] = t;
                if s > brs {
                    brs = s;
                    brm = (i, next);
                }
            }
        }
        if bps > brs {
            res.push(bpm);
        } else {
            res[brm.0] = brm.1;
        }
    }
    res.sort();
    res
}

fn main() {
    // for i in 0..10 {
    //     println!("{} {:?}", 3usize.pow(i) - 1, mss1(3usize.pow(i) - 1));
    // }
    // for n in 0..=100 {
    //     let sol = mss1(n);
    //     println!("{} -> {:?}", n, sol);
    //     assert!(works(&sol, n));
    // }
    let mut last = Vec::new();
    for i in 0..=100 {
        last = mss_b(i, last);
        println!("{} -> {:?} {}", i, &last, last.iter().sum::<usize>());
    }
}
