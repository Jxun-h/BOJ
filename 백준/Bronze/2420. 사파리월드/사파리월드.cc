#include <iostream>

using namespace std;

int main() {
    long n, m;
    
    cin >> n >> m;
    
    cout << ((n - m) < 0 ? (n - m) * -1 : (n - m)) << endl;
    
    return 0;
}
