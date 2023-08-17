#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
using namespace std;

int main() {
    cin.sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int now = 0;
    vector<int> notes;
    int n, q;
    cin >> n >> q;

    for (int i = 1; i <= n; i++) {
        int count;
        cin >> count;
        notes.push_back(now + count - 1);
        now += count;
    }

    for (int i = 1; i <= q; i++) {
        int question;
        cin >> question;
        auto it = lower_bound(notes.begin(), notes.end(), question);
        cout << it - notes.begin() + 1 << '\n';
    }
    
    return 0;
}