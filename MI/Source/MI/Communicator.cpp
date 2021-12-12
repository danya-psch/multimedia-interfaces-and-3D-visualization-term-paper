// Fill out your copyright notice in the Description page of Project Settings.


#include "Communicator.h"

#include <stdlib.h>

#include "Runtime/Core/Public/Misc/OutputDevice.h"
#include "Runtime/Core/Public/Misc/OutputDeviceNull.h"


#define STR_LEN (80)

// Sets default values
ACommunicator::ACommunicator()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

	/*
	int fd, res = 0;
	const char *myfifo = "mypipe";
	mkfifo(myfifo, 0666);
	fd = open(myfifo, O_RDONLY);
	char str[STR_LEN] = { 0 };
	while (1)
	{
		if (read(fd, str, STR_LEN - 1)) {
			printf("User1: %s\n", str);
			memset(str, 0, STR_LEN);
		}
	}
	close(fd);
	*/
	/*
	FOutputDeviceNull ar;
	GameMode = GetWorld()->GetAuthGameMode();
	const FString command = FString::Printf(TEXT("ShowAchievement %d"), 11);
	GameMode->CallFunctionByNameWithArguments(*command, ar, NULL, true);
	*/
}

typedef struct Result Result;
struct Result {
	int tank_num;
	int fuel_type;
	char l_or_m;
	int amount_l_or_m;
};

Result parseResult(char * str);

// Called when the game starts or when spawned
void ACommunicator::BeginPlay()
{
	Super::BeginPlay();

	GameMode = GetWorld()->GetAuthGameMode();
	//my_worker = new mythread();
	//my_worker->my_init(this);


	/*HANDLE hPipe;
	char buffer[STR_LEN];
	DWORD dwRead;

	hPipe = CreateNamedPipe(TEXT("\\\\.\\pipe\\Pipe"),
		PIPE_ACCESS_DUPLEX,
		PIPE_TYPE_BYTE | PIPE_READMODE_BYTE | PIPE_WAIT,   // FILE_FLAG_FIRST_PIPE_INSTANCE is not needed but forces CreateNamedPipe(..) to fail if the pipe already exists...
		1,
		1024 * 16,
		1024 * 16,
		NMPWAIT_USE_DEFAULT_WAIT,
		NULL);
	while (hPipe != INVALID_HANDLE_VALUE)
	{
		if (ConnectNamedPipe(hPipe, NULL) != FALSE)   // wait for someone to connect to the pipe
		{
			while (1)
			{

				if (ReadFile(hPipe, buffer, STR_LEN - 1, &dwRead, NULL)) {
				
					memset(buffer, 0, STR_LEN);
				}
			}
		}

		DisconnectNamedPipe(hPipe);
	}*/
}

void ACommunicator::notify(int index) {
	FOutputDeviceNull ar;
	const FString command = FString::Printf(TEXT("Move_bunny %d"), index);
	GameMode->CallFunctionByNameWithArguments(*command, ar, NULL, true);
}

// Called every frame
void ACommunicator::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);
}

typedef enum {
	tank_num = 0,
	fuel_type,
	l_or_m,
	amount_l_or_m,
} field_type;


#define BUF_LEN (124)
#define case_field(strct, field, val) case field: {(strct)->field = (val); break;}
Fresult_t ACommunicator::parse_result(FString string) {
	const TCHAR *str = *string;
	int32 size = string.Len();
	Fresult_t res;
	char buf[BUF_LEN] = { 0 };
	int buf_i = 0;
	field_type ft = tank_num;
	for (int32 i = 0; i < size + 1; i++) {
		if (str[i] == '|' || !str[i]) {
			int val = atoi(buf);
			switch (ft) {
				case_field(&res, tank_num, val);
				case_field(&res, fuel_type, val);
				case_field(&res, l_or_m, val);
				case_field(&res, amount_l_or_m, val);
			}
			ft = (field_type)((int)ft + 1);
			memset(buf, 0, BUF_LEN);
			buf_i = 0;
		}
		else {
			buf[buf_i++] = str[i];
		}
	}
	return res;
}