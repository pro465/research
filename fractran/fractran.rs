fn idx(n: &[u64], max: &[u64]) -> usize {
    let mut res=0;
    for (i,j) in n.iter().zip(max.iter()) {
        res*=j;
        res+=i.min(j);
    }
    res as _
}

fn calculate_lookup(prog: &[Vec<i64>]) -> Vec<usize> {
    let mut m=vec![0;prog[0].len()];
    for i in prog {
        for (j, x) in i.iter().enumerate() {
            m[j]=m[j].min(*x);
        }
    }
    let mut res=Vec::with_capacity(m.iter().map(|x| *x+1).product::<i64>() as usize);
    for i in prog {

    }
    res
}

struct State {
    lookup: Vec<usize>,
    prog: Vec<Vec<u64>>,
    curr: Vec<u64>,
}

impl State {
    fn new(prog: Vec<Vec<i64>>, inp: Vec<u64>) -> Self {
        Self {
            lookup: calculate_lookup(&prog),
            curr: inp,
            prog: prog.into_iter().map(|x| x.into_iter().map(|x| x as u64).collect()).collect(),
        }
    }
}

fn main(){}
