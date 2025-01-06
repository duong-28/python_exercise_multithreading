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
    print ("First he takes a bite of his sandwich")
    time.sleep(5) # Assuming the time it takes for John to chew and swallow a it is 5 seconds
    print ("sandwich's swallowed")

def drink_tea():
    print ("And takes a sip of his tea")
    time.sleep(2) # Time taken to sip tea
    print ("tea's sipped")

def check_phone():
    print ("He also checks a notification on his phone")
    time.sleep(3) # Time taken to read and process a notification
    print ("phone's checked")

def eat_fruit():
    print ("And even takes yet another bite of his fruits")
    time.sleep(3) # Time taken to eat a piece of fruit
    print ("fruit's eaten")

def breakfast_cycle():
    '''
    Executes one complete breakfast cycle where all activities happen concurrently.
    The cycle repeats 3 times to simulate a complete breakfast
    (this is assuming John is a fast eater and multitasker and can complete his breakfast in 3 cycles)
    '''
    for i in range(3): 
        print(f"Cycle {i+1} starts:")

        # Create threads for all concurrent activities 
        threads = [
            threading.Thread(target=eat_sandwich),
            threading.Thread(target=drink_tea),
            threading.Thread(target=check_phone),
            threading.Thread(target=eat_fruit)
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
    print("John's breakfast cycles (this time he's multitasking):")
    start_time = time.time()
    breakfast_routine()
    end_time = time.time()
    total_time = end_time - start_time
    print(f"John's breakfast routine tool {total_time:.1f} seconds")