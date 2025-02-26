fn f(n: u64) -> usize {
    let mut r = vec![1];
    for i in 1..n {
        let mut r2 = vec![];
        let mut j = 0;
        while j < r.len() {
            let mut c = 1;
            if j + 1 < r.len() && r[j] == r[j + 1] {
                c += 1;
                if j + 2 < r.len() && r[j] == r[j + 2] {
                    c += 1
                }
            }
            r2.push(c);
            r2.push(r[j]);
            j += c
        }
        r = r2;
    }
    r.len()
}

fn main() {
    println!("{}", f(70));
}
