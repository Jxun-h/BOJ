#include <iostream>

using namespace std;

int main() {
    long x;
    
    cin >> x;
    string ans;
    
    for (int i=1; i< x + 1; i++) {
        ans += "*";
        
        cout << ans << "\n";
    }
    return 0;
}
