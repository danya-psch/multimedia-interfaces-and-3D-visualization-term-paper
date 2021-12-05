#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#define STR_LEN (80)

int main()
{
    int fd, res = 0;
    const char *myfifo = "mypipe";
    mkfifo(myfifo, 0666);
    fd = open(myfifo, O_RDONLY);
    char str[STR_LEN] = {0};
    while(1)
    {
        if (read(fd, str, STR_LEN - 1)) {
            printf("User1: %s\n", str);
            memset(str, 0, STR_LEN);
        }
    }
    close(fd);
    return 0;
}