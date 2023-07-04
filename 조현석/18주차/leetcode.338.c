// Counting Bits

int popcount1(int x){
    int count = 0;
    while(x) {
        count += x & 1;
        x >>= 1;
    }
    return count;
}

int popcount2(int x){
    x = x - ((x >> 1) & 0x55555555);
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333);
    x = (x + (x >> 4)) & 0x0F0F0F0F;
    x = x + (x >> 8);
    x = x + (x >> 16);
    return x & 0x0000003F;
}


int* countBits(int n, int* returnSize){
    int* result = (int*)malloc(sizeof(int) * (n+1));
    *returnSize = n+1;
    result[0] = 0;
    for(int i = 1; i <= n; i++){
        // result[i] = result[i/2] + i%2;
        result[i] = popcount2(i);
    }
    return result;
}