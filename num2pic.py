# try:
# 960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719

def num2pic(h, n):
    n//=h
    w=(n.bit_length()+h-1)//h
    for row in range(h):
        for col in range(w):
            loc = h-row+col*h
            bit = (n>>loc)&1
            print(" @"[bit], end="")
        print()

num2pic(17, int(input("Enter the number: ")))
