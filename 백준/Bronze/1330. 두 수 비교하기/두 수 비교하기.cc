#include <iostream>

using namespace std;

int main() {
    long n, m;
    cin >> n >> m;

    cout << fixed;
    cout.precision(13);
    
    string ans;
    
    if (n > m) ans = ">";
    else if (n < m) ans = "<";
    else ans = "==";
    
    cout << ans << endl;
    return 0;
}
