#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <deque>

std::vector<std::pair<int,int>> nodes;

int distance(std::pair<int,int> point_A, std::pair<int,int> point_B) {
    return abs(point_A.first - point_B.first) + abs(point_A.second - point_B.second);
}

bool solve() {
    int num_nodes = nodes.size();
    std::map<int, std::vector<int>> adj;
    
    for (int i = 0; i < num_nodes; i++) {
        adj[i] = std::vector<int>();
    }

    // initializing graph with valid edges only
    for (int i = 0; i < num_nodes; i++) {
        for (int j = 0; j < i; j++) {
            if (distance(nodes[i], nodes[j]) <= 20 * 50) {
                adj[i].push_back(j);
                adj[j].push_back(i);
            }
        }
    }

    // doing the BFS
    int src = 0, dst = num_nodes - 1;
    std::set<int> visited = std::set<int>();
    std::deque<int> to_visit = std::deque<int>();
    
    to_visit.push_back(src);

    while (!to_visit.empty()) {
        int current = to_visit.front();
        to_visit.pop_front();
        visited.insert(current);

        if (current == dst) {
            return true;
        }

        for (auto i : adj[current]) {
            if (visited.count(i) == 0) {
                to_visit.push_back(i);
            }
        }
    }

    return false;
}

int main()
{
    int T, N;
    int x, y;
    
    std::cin >> T;
    
    while (T--) {
        std::cin >> N;
        nodes.resize( N + 2);
        
        for (int i = 0; i < N + 2; i++) {
            std::cin >> x >> y;
            nodes[i] = std::make_pair(x, y);
        }

        bool path_exists = solve();
        
        if (path_exists) {
            std::cout << "happy" << std::endl;
        } else {
            std::cout << "sad" << std::endl;
        }
    }
}