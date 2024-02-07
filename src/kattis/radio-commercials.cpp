#include <iostream>
#include <string>
#include <set>

void send_cookie(std::multiset<unsigned int>& diameters, std::multiset<unsigned int>::iterator& median) {
    auto new_median = median;

    if (diameters.size() % 2) {
        ++new_median;
    } else {
        --new_median;
    }

    diameters.erase(median);
    median = new_median;
}

void add_cookie(std::multiset<unsigned int>& diameters, std::multiset<unsigned int>::iterator& median, unsigned int diameter) {
    diameters.insert(diameter);

    if (diameters.size() == 1) {
        median = diameters.begin();
    } else if (diameters.size() % 2) {
        if (diameter < *median) {
            --median;
        }
    } else {
        if (diameter >= *median) {
            ++median;
        }
    }
}

int main(int argc, char *argv[]) {
    std::multiset<unsigned int> diameters;
    std::multiset<unsigned int>::iterator median;

    for (std::string operation; std::cin >> operation;) {
        if (operation == "#") {
            std::cout << *median << '\n';
            send_cookie(diameters, median);
        } else {
            add_cookie(diameters, median, stoi(operation));
        }
    }

    return 0;
}   