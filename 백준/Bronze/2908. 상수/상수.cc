#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    string n, m;
    cin >> n >> m;
    
    reverse(n.begin(), n.end());
    reverse(m.begin(), m.end());
    
    cout << (n > m ? n : m) + "\n";

    return 0;
}
