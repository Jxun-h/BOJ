#include <iostream>

using namespace std;

long factorial_(long num, long res) {
    if (num <= 1) return res;
    else {
        res = factorial_(num - 1, res * num);
        
    }
    return res;
}

int main() {
    long n;
    
    cin >> n;
    
    cout << factorial_(n, 1) << "\n";
    
    return 0;
}
