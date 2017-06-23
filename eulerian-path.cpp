#include <iostream>
#include <vector>
#include <cstring>
#include <stack>

struct edge {
    int to, id;
    edge(int _to, int _id){
        to = _to;
        id = _id;
    }
};


int main(int argc, char *argv[]) {
    int n,m,u,v;
    
    while (std::cin >> n >> m && n) {
        std::vector<edge> g[n];
        std::vector<int> in_deg(n, 0), out_deg(n, 0);
        
        for (int i = 0; i < m; i++) {
            std::cin >> u >> v;
            g[u].push_back(edge(v, i));
            out_deg[u]++;
            in_deg[v]++;
        }
        
        int start = u, total = 0;
        for (int i = 0;i < n; i++) {
            if (out_deg[i] != in_deg[i]) {
                total++;
            }
            if (out_deg[i] - in_deg[i] == 1) {
                start = i;
            }
        }
        
        std::stack<int> s;
        std::vector<int> path;
        bool marked[m]; 
        memset(marked,false,sizeof(marked));
        int cur = start;
        
        while(!s.empty() || out_deg[cur]) {
            if (!out_deg[cur]) {
                path.push_back(cur);
                cur = s.top(); s.pop();
                continue;
            } else {
                for (int i=0; i < g[cur].size(); i++) {
                    edge e = g[cur][i];
                    int to = e.to, id = e.id;

                    if (!marked[id]) {
                        out_deg[cur]--;
                        marked[id] = true;
                        
                        s.push(cur);
                        cur = to;
                        
                        break;
                    }
                }
            }
        }
        
        path.push_back(cur);
        if (path.size() == m + 1 && (total==0 || total==2)) {
            for (int i = m; i >= 0; i--) {
                std::cout << (i !=m ? " " : "") << path[i];
            }
            std::cout << std::endl;
        }
        else {
            std::cout << "Impossible" << std::endl;
        } 
    }
    return 0;
}