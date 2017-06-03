#include <unordered_map>
#include <unordered_set>
#include <stdio.h>
#include <math.h>
#include <iostream>

static std::unordered_map<int, bool> primes({{1, false}});

bool is_prime(int p) {
    auto iterator = primes.find(p);
    if (iterator != primes.end()) { 
        return iterator -> second;
    }

    float sqrt_num = sqrt(p);
    
    for (int i = 2; i <= sqrt_num; ++i) {
        if (p % i == 0) {
            return primes[p] = false;
        }
    }
    
    return primes[p] = true;
}

static std::unordered_map<int, bool> happys;

bool is_happy(int p, std::unordered_set<int> &seen) {
    if (seen.find(p) != seen.end()) {
        return happys[p] = false;
    }
    
    seen.insert(p);
    int sum = 0;
    
    while (p > 0) {
        sum += pow(p % 10, 2);
        p /= 10;
    }
    
    if (sum == 1) {
        return happys[p] = true;
    }
    
    return happys[p] = is_happy(sum, seen);
}

bool is_happy(int p) {
    std::unordered_set<int> seen;
    return is_happy(p, seen);
}

int main() {
    int T;
    std::cin >> T;
    
    for (int t=0; t < T; ++t) {
        int K, m;
        
        std::cin >> K >> m;
        
        if (!is_prime(m)) {
            std::cout << K << " " << m << " NO\n";
        } else if (!is_happy(m)) {
            std::cout << K << " " << m << " NO\n";
        } else {
            std::cout << K << " " << m << " YES\n";
        }
    }

    return 0;
}