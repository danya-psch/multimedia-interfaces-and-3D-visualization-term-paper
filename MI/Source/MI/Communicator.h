// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "Runtime/Engine/Classes/GameFramework/GameModeBase.h"
#include "mythread.h"
#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Communicator.generated.h"


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
protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;


public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;
};
