use num::{BigInt as R, FromPrimitive, One, ToPrimitive};

type C = (R, R);
type Cf = (f64, f64);

const LIM: usize = 1000;
const TERM_LIM: usize = 150;

fn addc(a: &mut C, b: &C) {
    a.0 += &b.0;
    a.1 += &b.1;
}

fn mulc((w, x): &C, (y, z): &C) -> C {
    ((w * y - x * z), (w * z + x * y))
}

fn mulcf((w, x): &Cf, (y, z): &Cf) -> Cf {
    (w * y - x * z, w * z + x * y)
}

fn mul(a: &[C], b: &[C], prec: u64, lim: usize) -> Vec<C> {
    let lim = lim.min(a.len() + b.len() - 1);
    let mut res = Vec::with_capacity(lim);
    for i in 0..lim {
        let mut coeff = (R::ZERO, R::ZERO);
        for j in 0..a.len().min(i + 1) {
            let k = i - j;
            if k >= b.len() {
                continue;
            }
            addc(&mut coeff, &mulc(&a[j], &b[k]));
        }
        coeff.0 >>= prec;
        coeff.1 >>= prec;
        res.push(coeff)
    }
    res
}

fn calculate_mid((x0, y0): C, prec: u64, times: usize) -> Vec<C> {
    let mut x1 = R::from_u8(0).unwrap();
    let mut y1 = x1.clone();
    let mut res = Vec::with_capacity(times + 1);
    res.push((x1.clone(), y1.clone()));
    for _ in 0..times {
        let xt = (x1.pow(2) - y1.pow(2)) >> prec;
        y1 *= x1 << 1;
        y1 >>= prec;
        y1 += &y0;
        x1 = xt + &x0;
        res.push((x0.clone(), y0.clone()));
    }
    res
}

fn calculate_poly(mid: &[C], prec: u64, lim: usize) -> Vec<Vec<C>> {
    let mut res = Vec::with_capacity(mid.len());
    let one = R::one() << prec;
    res.push(Vec::new());
    for i in 0..mid.len() - 1 {
        // d_n = d + d_{n-1}*(d_{n-1}+2*z_{n-1})
        let z = mid[i].clone();
        let z2 = (z.0 << 1, z.1 << 1);
        let mut inner = res[i].clone();
        if !inner.is_empty() {
            inner[0] = z2;
        } else {
            inner.push(z2);
        }
        let mut outer = mul(&res[i], &inner, prec, lim);
        if outer.len() > 1 {
            outer[1].0 += one.clone();
        } else {
            outer.push((R::ZERO, R::ZERO));
            outer.push((one.clone(), R::ZERO));
        }
        res.push(outer);
    }
    res
}

fn calc_for_diff(poly: &[C], prec: u64, d_pows: &[Cf]) -> Cf {
    let (mut r, mut i) = (0., 0.);
    let sc = 2f64.powi(-(prec as i32));
    for (p, q) in poly.iter().zip(d_pows.iter()) {
        let p = ((&p.0).to_f64().unwrap() * sc, (&p.1).to_f64().unwrap() * sc);
        r += p.0 * q.0 - p.1 * q.1;
        i += p.0 * q.1 + p.1 * q.0;
    }
    (r, i)
}

fn score(polys: &[Vec<C>], prec: u64, d: &Cf, lim: usize) -> usize {
    let mut d_pows = Vec::with_capacity(lim);
    let mut curr_p = (1., 0.);
    for _ in 0..lim {
        d_pows.push(curr_p);
        curr_p = mulcf(&curr_p, d);
    }
    for (i, p) in polys.iter().enumerate() {
        let (c, d) = calc_for_diff(p, prec, &d_pows);
        if c * c + d * d > 4. {
            return i;
        }
    }
    LIM
}

fn print_pix(sc: usize) {
    if sc == LIM {
        print!("%");
    } else {
        print!(" ");
    }
}

fn plot(dim: (u64, u64), mid: (R, R), prec: u64, scale: f64) {
    let (w, h): (i64, i64) = (dim.0.try_into().unwrap(), dim.1.try_into().unwrap());
    let polys = calculate_poly(&calculate_mid(mid, prec, LIM), prec, TERM_LIM);
    for j in -h..=h {
        let y = j as f64 * scale;
        for i in -w..=w {
            let x = i as f64 * scale;

            print_pix(score(&polys, prec, &(x, y), TERM_LIM));
        }
        println!();
    }
}

fn main() {
    let prec = 70;
    let scale = 0.03;
    let midx = -R::from(0);
    let midy = R::from(0);
    plot((20, 20), (midx, midy), prec, scale)
}
