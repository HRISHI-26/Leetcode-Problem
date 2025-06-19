#include<string.h>
int numJewelsInStones(char* jewels, char* stones) {
    int count = 0;
    int jewels_count = strlen(jewels);
    int stones_count = strlen(stones);
    for (int i = 0; i < jewels_count; i++) {
        for (int j = 0; j < stones_count; j++) {
            if (jewels[i] != stones[j])
                continue;
            else
                count++;
        }
    }
    return count;
}