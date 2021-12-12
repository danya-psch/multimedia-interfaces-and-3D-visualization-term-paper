#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#define STR_LEN (80)

typedef struct Result Result;
struct Result {
    int tank_num;
    int fuel_type;
    char l_or_m;
    int amount_l_or_m;
};

Result parseResult(char * str);

int main()
{
    int fd, res = 0;
    const char *myfifo = "mypipe";
    mkfifo(myfifo, 0666);
    fd = open(myfifo, O_RDONLY);
    char str[STR_LEN] = "12|2|0|20";
    while(1)
    {
        if (read(fd, str, STR_LEN - 1)) {
            printf("User1: %s\n", str);
            Result res = parseResult(str);
            printf("User1: %d\n", res.l_or_m);
            memset(str, 0, STR_LEN);
        }
    }
    
    close(fd);
    return 0;
}

Result parseResult(char * str) {
    Result res;
    char * temp = malloc(sizeof(int));
    int temp_count = 0;
    int num_count = 0;
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] != '|') {
            temp[temp_count] = str[i];
            temp_count++;
        }
        else {
            int parsed = atoi(temp);
            switch (num_count) {
                case 0:
                    res.tank_num = parsed;
                    break;
                case 1:
                    res.fuel_type = parsed;
                    break;
                case 2:
                    res.l_or_m = parsed;
                    break;
                default:
                    break;
            }
            memset(temp, 0, sizeof(int));
            temp_count = 0;
            num_count++;
        }
    }
    res.amount_l_or_m = atoi(temp);
    free(temp);
    return res;
}