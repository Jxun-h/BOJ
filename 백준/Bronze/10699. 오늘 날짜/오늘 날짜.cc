#include <iostream>
#include <ctime>

int main() {
    struct tm curr_tm;
    time_t curr_time = time(nullptr);
    
    localtime_r(&curr_time, &curr_tm);
    
    int year = curr_tm.tm_year + 1900;
    int month = curr_tm.tm_mon + 1;
    int day = curr_tm.tm_mday;
    
    printf("%04d-%02d-%02d\n", year, month, day);
    return 0;
}
