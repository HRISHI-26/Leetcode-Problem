int maxDepth(char* s) {
    int count = 0, max = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] == '(') {
            count++;
            if (count > max)
                max = count;
        } else if (s[i] == ')') {
            count--;
        }
    }
    return max;
}