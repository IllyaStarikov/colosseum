#include <iostream>

#include <iostream>
#include <string.h>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

vector<int> adjacencyMatrix[1000];
vector<bool> visited(1000, false);
vector<int> order;

void topologicalSort(int u) {
    if (visited[u]) {
        return;
    }
    visited[u] = true;
    for (int i = 0; i < adjacencyMatrix[u].size(); i++) {
        int v = adjacencyMatrix[u][i];
        topologicalSort(v);
    }
    order.push_back(u);
}

bool contains(int x, int y){
    for(int i = 0; i < adjacencyMatrix[x].size(); i++){
        if(adjacencyMatrix[x][i] == y){
            return true;
        }
    }
    return false;
}

bool checkSeries(){
    for(int i = order.size() - 1; i > 0; i--){
        if(!contains(order[i], order[i - 1])){
            return false;
        }
    }
    return true;
}


int main(int argc, char *argv[]) {
    int n, k;
    scanf("%d %d\n", &n, &k);

    int a, b;
    for(int i = 0; i < k; i++){
        scanf("%d %d", &a, &b);
        adjacencyMatrix[a].push_back(b);
    }

    for (int u = 0; u < n; u++) {
        topologicalSort(u);
    }

    if (checkSeries()) {
        for (vector<int>::reverse_iterator it = order.rbegin(); it != order.rend(); it++) {
            cout << *it << " ";
        }
    } else {
        cout << "back to the lab";
    }
    
    return 0;
}