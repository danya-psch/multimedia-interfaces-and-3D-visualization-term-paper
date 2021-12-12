#pragma once

#include "CoreMinimal.h"
#include "HAL/Runnable.h"


class ACommunicator;
/**
 *
 */
class MI_API mythread : public FRunnable
{
public:

	// Constructor, create the thread by calling this
	mythread();

	// Destructor
	virtual ~mythread() override;


	// Overriden from FRunnable
	// Do not call these functions youself, that will happen automatically
	bool Init() override; // Do your setup here, allocate memory, ect.
	uint32 Run() override; // Main data processing happens here
	void Stop() override; // Clean up any memory you allocated here

	void my_init(ACommunicator *par);


private:

	// Thread handle. Control the thread using this, with operators like Kill and Suspend
	FRunnableThread* Thread;
	ACommunicator *parent = nullptr;

	// Used to know when the thread should exit, changed in Stop(), read in Run()
	bool bRunThread;
};