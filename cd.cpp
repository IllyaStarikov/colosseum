#include <unordered_set>
#include <stdio.h>

int main() {
    int jack_size, jill_size;
    scanf("%d %d\n", &jack_size, &jill_size);

    while (jack_size != 0 or jill_size != 0) {
        std::unordered_set<int> jack;
        jack.reserve(jack_size);
        
        int value;
        
        for (int i = 0; i < jack_size; ++i) {
            scanf("%d\n", &value);
            jack.insert(value);
        }
        
        int in_common = 0;
        for (int i = 0; i < jill_size; ++i) {
            scanf("%d\n", &value);
            if (jack.find(value) != jack.end()) ++in_common;
        }
        
        printf("%d\n", in_common);
        scanf("%d %d", &jack_size, &jill_size);
    }


    return 0;
}
