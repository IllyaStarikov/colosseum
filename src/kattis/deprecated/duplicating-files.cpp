//  duplicating-files.cpp
//  Desktop
//
//  Created by Illya Starikov on 06/09/17.
//  Copyright 2017. Illya Starikov. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <set>
#include <cstring>
#include <math.h>

int hash(const char to_hash[]) {
    int accumulator = to_hash[0];
    auto length = strlen(to_hash);

    for (auto i = 1; i < length; ++i) {
        accumulator = accumulator ^ (int)to_hash[i];
    }

    std::cout<<accumulator<<"\n";

    return accumulator;
}

int main() {
    std::set<std::string> files;
    std::set<int> hashes;

    unsigned int line = -1, collisions = 0, hash_value;
    char file[51];
    size_t size;

    scanf("%u", &line); // Gotta go fast
    while (line != 0) {
        files.clear();

        for (unsigned int i = 0; i < line; ++i) {
            getchar();
            scanf("%50[^\n]", file);

            hash_value = hash(file);

            if (hashes.find(hash_value) == hashes.end()) {
                ++collisions;
            }

            files.insert(file);
            hashes.insert(hash_value);
        }

        printf("%lu %d\n", files.size(), collisions);
        scanf("%u", &line); // Gotta go fast
    }

    return 0;
}
