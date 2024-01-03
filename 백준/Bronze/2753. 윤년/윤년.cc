#include <iostream>

using namespace std;

int main() {
    int year;
    cin >> year;
    
    string ans;
    
    if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) ans = "1";
    else ans = "0";
    
    cout << ans << endl;
    return 0;
}
