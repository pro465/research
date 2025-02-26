use rand::{thread_rng, Rng};

fn main() {
    const w: usize = 10000;
    let h = 10000;
    let mut x = vec![[false; w]; h];
    let mut y = vec![[false; w]; h];
    let mut rng = thread_rng();
    x.iter_mut().for_each(|i| rng.fill(&mut *i as &mut [bool]));
    println!(
        "{}",
        x.iter()
            .map(|x| x.iter().map(|&i| i as u64).sum::<u64>())
            .sum::<u64>() as f64
            / ((w * h) as f64)
    );
    let mut avg = 0.;
    for i in 1..=20 {
        step(&x, &mut y);
        std::mem::swap(&mut x, &mut y);
        step2(&x, &mut y);
        std::mem::swap(&mut x, &mut y);
        println!(
            "{}",
            x.iter()
                .map(|x| x.iter().map(|&i| i as u64).sum::<u64>())
                .sum::<u64>() as f64
                / (w * h) as f64
        );
    }
}

fn step<const N: usize>(x: &[[bool; N]], y: &mut [[bool; N]]) {
    for i in 0..x.len() {
        let c2 = |o| count(x, i, 0, o);
        let (mut s1, mut s2, mut s3) = (c2(0), c2(1), c2(2));
        for j in 0..N {
            let sum = s1 + s2 + s3 - x[i][j] as u8;
            let s4 = count(x, i, j + 1, 2);
            (s1, s2, s3) = (s2, s3, s4);
            y[i][j] = if sum == 3 {
                true
            } else if sum == 2 {
                x[i][j]
            } else {
                false
            }
        }
    }
}
fn step2<const N: usize>(x: &[[bool; N]], y: &mut [[bool; N]]) {
    for i in 0..x.len() {
        let c2 = |o| count(x, i, 0, o);
        let (mut s1, mut s2, mut s3) = (c2(0), c2(1), c2(2));
        for j in 0..N {
            let sum = s1 + s2 + s3 - x[i][j] as u8;
            let s4 = count(x, i, j + 1, 2);
            (s1, s2, s3) = (s2, s3, s4);
            y[i][j] = if sum == 3 { true } else { x[i][j] }
        }
    }
}

fn count<const N: usize>(x: &[[bool; N]], i: usize, j: usize, offset: usize) -> u8 {
    let mut c = 0;
    let l1 = N;
    let l2 = x.len();
    let j = (j + l1 - 1 + offset) % l1;
    for mut i in i + l2 - 1..=i + l2 + 1 {
        i %= l2;
        c += if x[i][j] { 1 } else { 0 }
    }
    c
}
