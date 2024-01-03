#include <iostream>

using namespace std;

int main() {
    int x, y;
    
    cin >> x >> y;
    string ans;
    
    if (x>0 && y>0) ans = "1";
    else if (x<0 && y>0) ans = "2";
    else if (x>0 && y<0) ans = "4";
    else if (x<0 && y<0) ans = "3";
    
    cout << ans << endl;
    return 0;
}
