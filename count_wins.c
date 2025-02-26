#include <stdio.h>
#include <stdlib.h>
int main(int argc, char * argv[]) {
    int max = atoi(argv[1]);
    int aw = 0, bw = 0;
    for (int i = 0; i < 1<<max; i++) {
        int a = 0, b = 0;
        for (int j = 0; j < max - 1; j++) {
            int bits = (i & (3 << j)) >> j;
            if(bits == 0) a++; else if(bits == 1) b++;
        }
        a > b && aw++; a < b && bw++;
    }
    printf("A: %d, B: %d, N: %d\n", aw, bw, max);
}
