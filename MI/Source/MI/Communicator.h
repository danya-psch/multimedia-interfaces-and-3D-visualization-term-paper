// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "Runtime/Engine/Classes/GameFramework/GameModeBase.h"
#include "mythread.h"
#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Communicator.generated.h"


USTRUCT(BlueprintType)
struct MI_API Fresult_t
{
	GENERATED_USTRUCT_BODY()

		UPROPERTY(EditAnywhere, BlueprintReadWrite)
		int32  tank_num;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
		int32  fuel_type;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
		int32  l_or_m;
	UPROPERTY(EditAnywhere, BlueprintReadWrite)
		int32  amount_l_or_m;
};


UCLASS()
class MI_API ACommunicator : public AActor
{
	GENERATED_BODY()

public:
	UPROPERTY(BlueprintReadWrite, EditAnywhere, Category = "int")
		int destroy_projectiles_on_hit = -10;

	UPROPERTY(BlueprintReadWrite, EditAnywhere)
		AGameModeBase* GameMode;
private:
	mythread *my_worker;

public:
	// Sets default values for this actor's properties
	ACommunicator();

	void notify(int index);
	UFUNCTION(BlueprintCallable, Category = "parser")
		Fresult_t parse_result(FString string);
protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;


public:
	// Called every frame
	virtual void Tick(float DeltaTime) override;
};
