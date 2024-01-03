#include <iostream>

using namespace std;

int main() {
    int grade;
    
    cin >> grade;
    
    string ans;
    
    if (90 <= grade && grade <= 100) ans = "A";
    else if (80 <= grade && grade <= 89) ans = "B";
    else if (70 <= grade && grade <= 79) ans = "C";
    else if (60 <= grade && grade <= 69) ans = "D";
    else ans = "F";
    
    cout << ans << endl;
    return 0;
}
