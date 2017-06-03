#include <iostream>
#include <cmath>
double answers[1000000] = {0};

int main(){
    int number;
    for(int i = 1;i <= 1000000; i++) {
            answers[i] += answers[i - 1] + log10(i);
    }
    
    while(std::cin >> number) {
        std::cout << int(answers[number] + 1) << std::endl; 
    }
}