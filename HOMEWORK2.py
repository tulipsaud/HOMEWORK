def shutdown(answer):
    if answer == "yes":
        print("Shutting down...")
    else:
        print("Not shutting down.")
response = input("Shutdown? (yes/no): ")
shutdown(response)

