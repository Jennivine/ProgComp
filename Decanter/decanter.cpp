#include <bits/stdc++.h>
using namespace std;

int A, B, W;
int N;
map<int, string> op;

queue<pair<int, int> > q;
int visited[1000][1000];
pair< pair<int, int>, int> path[1000][1000];

void printRoute(int left, int right); 
void BFS();
pair<int, int> generateState(int A, int B, int i);

int main() {
    op[0] = "AF";
    op[1] = "AE";
    op[2] = "AB";
    op[3] = "BF";
    op[4] = "BE";
    op[5] = "BA";

    freopen("task5.txt", "r", stdin);
    scanf("%d", &N);

    for (int i=0; i<N; i++) {
        scanf("%d %d %d", &A, &B, &W);
        BFS();
        printf("\n");
        
        // clear the cache
        for (int j=0; j<1000; j++) {
            for (int k=0; k<1000; k++) {
                visited[j][k] = 0;
            }
        }

        // clear the queue
        while (q.size()) {
            q.pop();
        }
    }
}

void BFS() {
    int found = 0;
    pair<int, int> start = make_pair(0, 0);
    
    q.push(start);
    visited[0][0] = 1;
    path[0][0] = make_pair(start, -1);
 
    int left, right;
    while (!q.empty()) {
        pair<int, int> top = q.front();
        q.pop();

        left = top.first;
        right = top.second;

        if (left == W) {
            // found the path to target!
            found = 1;
            break;
        }

        for (int i=0; i<6; i++) {
            // generate new states
            int newL, newR;
            pair<int, int> nextState;
            nextState = generateState(left, right, i);
            newL = nextState.first;
            newR = nextState.second;

            if (visited[newL][newR]) {
                continue;
            }
            path[newL][newR] = make_pair(top, i);
            q.push(nextState);
            visited[newL][newR] = 1;
        }
    }

    // print path
    if (!found) {
        printf("no solution");
    } else {
        //printf("found solution");
        printRoute(left,right);
    }
}

void printRoute(int left, int right) {
    int prevL = path[left][right].first.first;
    int prevR = path[left][right].first.second;

    if (path[left][right].first == make_pair(left, right)) { 
        return;
    }

    printRoute(prevL, prevR);
    printf("%s ", op[path[left][right].second].c_str());
}
    
pair<int, int> generateState (int left, int right, int i) {
   switch (i) {
       case 0: return make_pair(A, right);
       case 1: return make_pair(0, right);
       case 2: while (left != 0 and right < B) {
                   left--;
                   right++;
               }
               return make_pair(left, right);
       case 3: return make_pair(left, B);
       case 4: return make_pair(left, 0);
       case 5: while (right != 0 and left < A) {
                   right--;
                   left++;
               }
               return make_pair(left, right);
   }
}

