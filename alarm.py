import time
import winsound
def start_timer():
    return time.time()
def stop_timer(start_time):
    elapsed_time = time.time() - start_time
    return elapsed_time
#beep
def beep_alarm():
    frequency = 1000
    duration = 2000
    winsound.Beep(frequency, duration)
#main program
if __name__ == "__main__":
    input("Press Enter to start the timer...")
    start_time = start_timer()
    input("Press Enter to stop the timer...")
    end_time = stop_timer(start_time)
    print(f"Elapsed time: {end_time} seconds")
    if end_time > 0:
        print("Hurrah!")
        beep_alarm()
