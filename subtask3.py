'''
Subtask 3: Simulating John's breakfast cycle using multithreading to represent concurrent activities.
The simulation runs for 3 cycles, with each representing a portion of the breakfast routine

- Sandwich bite: 5 seconds
- Tea sip: 2 second
- Fruit bite: 3 second
- Phone check: 3 seconds
'''

import time
import threading

def eat_sandwich():
    print ("John takes a bite of his sandwich")
    time.sleep(5) # Simulates the time taken to chew and swallow a bite
    print ("John finishes the bite")

def drink_tea():
    print ("John takes a sip of his tea")
    time.sleep(2) # Time taken to sip tea
    print ("John finishes the sip of tea")

def check_phone():
    print ("John checks a notification on his phone")
    time.sleep(3) # Time taken to read and process a notification
    print ("John finishes checking the notification")

def eat_fruit():
    print ("John takes a bite of his fruits")
    time.sleep(3) # Time taken to eat a piece of fruit
    print ("John finishes the bite")

def breakfast_cycle():
    '''
    Executes one complete breakfast cycle where all activities happen concurrently.
    The cycle repeats 3 times to simulate a complete breakfast
    '''
    for i in range(3): 
        print(f"Cycle {i+1} starts:")

        # Create threads for all concurrent activities 
        threads = [
            threading.Thread(target=eat_sandwich),
            threading.Thread(target=eat_fruit),
            threading.Thread(target=drink_tea),
            threading.Thread(target=check_phone)
        ]

        # Start all threads concurrently
        for thread in threads:
            thread.start()
        
        # Wait for all threads to finish before starting the next cycle
        for thread in threads:
            thread.join()

        print(f"Cycle {i+1} ends")

def breakfast_routine():
    breakfast_cycle()
    print("John finishes his breakfast")

if __name__ == "__main__":
    print("John's breakfast cycle:")
    start_time = time.time()
    breakfast_routine()
    end_time = time.time()
    total_time = end_time - start_time
    print(f"John's breakfast routine tool {total_time:.1f} seconds")