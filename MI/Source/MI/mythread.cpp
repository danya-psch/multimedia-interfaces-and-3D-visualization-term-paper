
#include "mythread.h"


#include "Misc/Paths.h"
#include "Misc/FileHelper.h"
#include "HAL/PlatformFilemanager.h"
#include "GenericPlatform/GenericPlatformFile.h"
#include <stdio.h>
#include <stdlib.h>
#include "Communicator.h"
// Copyright notice

#pragma region Main Thread Code
// This code will be run on the thread that invoked this thread (i.e. game thread)


#define BUF_LEN (124)
mythread::mythread(/* You can pass in inputs here */)
{
	// Constructs the actual thread object. It will begin execution immediately
	// If you've passed in any inputs, set them up before calling this.
	Thread = FRunnableThread::Create(this, TEXT("Give your thread a good name"));
}


mythread::~mythread()
{
	if (Thread)
	{
		// Kill() is a blocking call, it waits for the thread to finish.
		// Hopefully that doesn't take too long
		Thread->Kill();
		delete Thread;
	}
}


#pragma endregion
// The code below will run on the new thread.



typedef struct {
	int tank_num;
	int fuel_type;
	char l_or_m;
	int amount_l_or_m;
} result_t;

//void parse_result(const wchar_t *str, uint32 size, result_t *res);

void mythread::my_init(ACommunicator *par) {
	UE_LOG(LogTemp, Warning, TEXT("my_init"))
	parent = par;
}

bool mythread::Init()
{
	UE_LOG(LogTemp, Warning, TEXT("My custom thread has been initialized"))

		// Return false if you want to abort the thread
		return true;
}


uint32 mythread::Run()
{
	// Peform your processor intensive task here. In this example, a neverending
	// task is created, which will only end when Stop is called.
	FString file = FPaths::ProjectConfigDir();
	file.Append(TEXT("MyConfig.txt"));

	// We will use this FileManager to deal with the file.
	IPlatformFile& FileManager = FPlatformFileManager::Get().GetPlatformFile();

	FString FileContent;
	// Always first check if the file that you want to manipulate exist.
	if (FileManager.FileExists(*file))
	{
		uint64 last_size = 0;
		while (1) {
			if (FFileHelper::LoadFileToString(FileContent, *file, FFileHelper::EHashOptions::None)) {
				//UE_LOG(LogTemp, Warning, TEXT("FileManipulation: Text From File: %s"), *FileContent);
				//const TCHAR *wavLink = *FileContent;
				int32 i = 0, found = 0;

				for (i = FileContent.Len() - 1; i >= 0; i--) {
					FString currChar = FileContent.Mid(i, 1);
					if (currChar.Equals(TEXT(","))) {
						found = 1;
						break;
					}
				}
				if (found && last_size != FileContent.Len()) {
					last_size = FileContent.Len();
					//const TCHAR *wavLink = *FileContent.Mid(i + 1, FileContent.Len() - i);
					//result_t res = { 0 };
					//char buf[BUF_LEN] = { 0 };
					//memcpy(buf, wavLink, FileContent.Len() - i + 1);
					//parse_result(wavLink, FileContent.Len() - i, &res);
					//UE_LOG(LogTemp, Warning, TEXT("%s tank_num: %i, fuel_type: %i, l_or_m: %i, amount_l_or_m: %i"), wavLink, res.tank_num, res.fuel_type, res.l_or_m, res.amount_l_or_m);
					//if (parent) {
					//	parent->notify(res.tank_num - 1);
					//}
					//parse_result("1|2|3|4", &res);
					
				}
				else {
					UE_LOG(LogTemp, Warning, TEXT("FileManipulation: NONE"));
				}
				/*
					int tank_num;
					int fuel_type;
					char l_or_m;
					int amount_l_or_m;
				*/
				// const TCHAR *wavLink = *FileContent.Mid(i, FileContent.Len() - i);
				//parseResult((char *)wavLink);
				FileContent.Reset();
			}
			FPlatformProcess::Sleep(1.0f);
		}
	}
	else
	{
		UE_LOG(LogTemp, Warning, TEXT("FileManipulation: ERROR: Can not read the file because it was not found."));
		UE_LOG(LogTemp, Warning, TEXT("FileManipulation: Expected file location: %s"), *file);
	}

	return 0;
}


// This function is NOT run on the new thread!
void mythread::Stop()
{
	// Clean up memory usage here, and make sure the Run() function stops soon
	// The main thread will be stopped until this finishes!

	// For this example, we just need to terminate the while loop
	// It will finish in <= 1 sec, due to the Sleep()
	bRunThread = false;
}



typedef enum {
	tank_num = 0,
	fuel_type,
	l_or_m,
	amount_l_or_m,
} field_type;

#define case_field(strct, field, val) case field: {strct->field = val; break;}

void parse_result(FString string, uint32 size, result_t *res) {
	const TCHAR *str = *string;
	char buf[BUF_LEN] = { 0 };
	int buf_i = 0;
	field_type ft = tank_num;
	for (uint32 i = 0; i < size + 1; i++) {
		if (str[i] == '|' || !str[i]) {
			int val = atoi(buf);
			switch (ft) {
				case_field(res, tank_num, val);
				case_field(res, fuel_type, val);
				case_field(res, l_or_m, val);
				case_field(res, amount_l_or_m, val);
			}
			ft = (field_type)((int)ft + 1);
			memset(buf, 0, BUF_LEN);
			buf_i = 0;
		}
		else {
			buf[buf_i++] = str[i];
		}
	}
}