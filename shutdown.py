import os

def shutdown_system(minutes):
    command = "shutdown /s /t " + str(minutes * 60)
    os.system(command)

def cancel_shutdown():
    os.system("shutdown /a")
    print("Shutdown canceled.")

print("Enter Number of Minutes to Shutdown System: ")
minutes = int(input())

shutdown_system(minutes)

print("Do you want to cancel the shutdown? (y/n): ")
cancel_choice = input().lower()

if cancel_choice == "y":
    cancel_shutdown()