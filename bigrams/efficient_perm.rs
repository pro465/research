use std::{io, fs::read_to_string};
use std::time::{UNIX_EPOCH, SystemTime as S};
use std::collections::HashSet;

const ROWS: usize = 8;
const COLS: usize = 8;

fn ru64() -> u64 {
    let s = S::now().duration_since(UNIX_EPOCH).unwrap().as_nanos();
    s as u64
}

struct Random {
    state: u64,
}

impl Random {
    fn new() -> Self {
        let state = ru64();
        Self { state }
    }
    fn generate(&mut self) -> u64 {
        self.state *= 3935559000370003845;
        self.state += 1;
        let idx = self.state&63;
        self.state = (self.state << idx) | (self.state >> 63-idx);
        self.state ^= self.state << 13;
        self.state ^= self.state << 7;
        self.state ^= self.state << 17;
        //if self.state % 500 == 0 { println!("{}", self.state) }
        self.state
    }
    fn generate_perm(&mut self) -> Vec<usize> {
        let mut rem: Vec<_> = (0..COLS*ROWS).collect();
        let mut res = vec![27; COLS*ROWS];
        for i in 0..26 {
            let d = self.generate() as usize % rem.len();
            res[rem.remove(d)] = i;
        }
        res
    }
}

fn process(inp: String) -> Vec<Vec<f64>> {
    let mut v = Vec::new();
    let mut curr = Vec::new();
    for i in inp.split_whitespace() {
        curr.push(i.parse().unwrap());
        if curr.len() == 26 {
            v.push(curr);
            curr = Vec::new();
        }
    }
    v
}

fn main() {
    let mat = process(read_to_string("bigrams-data.txt").unwrap());
    // let perm = vec![16, 22, 4, 17, 19, 24, 20, 8, 14, 15, 0, 18, 3, 5, 6, 7, 9, 10, 11, 27, 25, 23, 2, 21, 1, 13, 12, 27, 27, 27];
    // println!("{}", cost(&perm, &mat));
    let mut c = 0;
    let mut rng = Random::new();
    let mut perm: Vec<_> = rng.generate_perm();
    let mut best_cost = dbg!(cost(&perm, &mat));
    let mut valleys = HashSet::new();
    let mut times = 0;
    loop {
        while minimize(&mut rng, &mut perm, &mat) {
            times += 1;
        }
        c+=1;
        let cost = cost(&perm, &mat);
        if cost < best_cost {
            println!("{cost}: {:?}", &perm);
            best_cost = cost;
        }
        if valleys.insert(perm.clone()) {
            println!("{}: {c}, avgtimes: {}", valleys.len(), times as f64/c as f64);
        }
        scramble(&mut rng, &mut perm);
    }
}

fn scramble(rng: &mut Random, perm: &mut [usize]) {
    for i in 1..perm.len() {
        for j in 0..i {
            if rng.generate()>>57 < 13 {
                perm.swap(i, j);
            }
        }
    }
}

fn dist(a: usize, b: usize) -> f64 {
    let y = (a/COLS).abs_diff(b/COLS) as f64;
    let x = (a%COLS).abs_diff(b%COLS) as f64;
    (x*x+y*y).sqrt()
}

fn cost(perm: &[usize], mat: &[Vec<f64>]) -> f64 {
    let mut s = 0.;
    for i in 0..perm.len() {
        if perm[i] == 27 { continue; }
        for j in 0..perm.len() {
            if perm[j] == 27 { continue; }
            s += dist(i, j) * mat[perm[i]][perm[j]];
        }
    }
    s
}

#[inline(always)]
fn minimize(rng: &mut Random, perm: &mut [usize], mat: &[Vec<f64>]) -> bool {
    let (mut best_swap, mut best_cost) = ((0, 0), cost(perm, mat));
    let curr_cost = best_cost;
    for i in 1..perm.len() {
        for j in 0..i {
            if (perm[i], perm[j]) == (27, 27) { continue }
            perm.swap(i, j);
            let c = cost(perm, mat);
            if c < best_cost {
                (best_swap, best_cost) = ((i, j), c);
            }
            if c < curr_cost && rng.generate()%100 < 10 {
                return true;
            }
            perm.swap(i, j);
        }
    }
    let (i, j) = best_swap;
    perm.swap(i, j);
    i != j
}
