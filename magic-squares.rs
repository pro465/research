fn is_square(a: u128) -> bool {
    if a == 0 {
        return true;
    }
    let mut x = 1 << (129 - a.leading_zeros()) / 2;

    loop {
        let y = (x + a / x) / 2;
        if y >= x {
            return x * x == a;
        }
        x = y;
    }
}

fn works(n: u128, d: u128) -> bool {
    n >= d && is_square(n - d) && is_square(n + d)
}

fn find_magic_square(n: u128, v: &mut Vec<u128>) -> Option<(u128, u128)> {
    let ns = n * n;
    for i in 0..n {
        let is = i * i;
        let d1 = ns - is;
        let js = ns + d1;
        if is_square(js) {
            for d2 in v.iter().copied() {
                if works(is, d2) && works(js, d2) {
                    return Some((d1, d2));
                }
            }
            v.push(d1);
        }
    }
    v.clear();
    None
}

fn main() {
    let mut v = Vec::new();
    for n in 0.. {
        if let Some((d1, d2)) = find_magic_square(n, &mut v) {
            println!("{n} {d1} {d2}");
            break;
        }
        if n % 5000 == 0 {
            println!("{n}");
        }
    }
}
