'''
Task 2: Simulating John's new morning routine: 
- Step 1: Eat a sandwich for 8 seconds (instead of 8 minutes)
- Step 2: Drink tea for 6 seconds (instead of 6 minutes)
          (Tea drinking normally takes 3 minutes but is now extended to 6 minutes
          because John takes longer sips while multitasking with his phone)
- Step 3: Eat fruits for 2 seconds (instead of 2 minutes)
- Step 4: Scroll through social media for 7 seconds (instead of 7 minutes)
          (Reduced from 10 to 7 minutes as some phone time was used during tea)
- Step 5: Total morning routine should be: 8 + 6 + 2 + 7 = 23 seconds
'''

import time
import threading

def eat_sandwich():
    print ("1. He starts by eating his sandwich for 8 seconds")
    time.sleep(8)
    print ("- Sandwich eaten")

def drink_tea():
    print ("- He first starts by taking a sip of tea")
    time.sleep(6) # extended duration to account for multitasking
    print ("- Tea drank")

def check_phone(): 
    # Phone checking happens in short bursts during tea drinking
    print ("- Then he checks a notification on this phone")
    time.sleep(2) # Brief phone checks between sips
    print ("- Finished checking notification")

def drink_tea_while_check_phone():
    print ("2. Then he drinks his tea while checking his phone in total of 6 seconds")

    # Creating a thread for concurrent activities 
    tea_thread = threading.Thread(target=drink_tea)
    phone_thread = threading.Thread(target=check_phone)

    # Both activities start at the same time
    tea_thread.start()
    phone_thread.start()

    # Waiting for both threads to finish before moving on
    tea_thread.join()
    phone_thread.join()

def eat_fruit():
    print ("3. John starts eating his fruits for 2 seconds")
    time.sleep(2)
    print ("- Fruits eaten")

def social_media():
    print ("4. John only needs to check his phone for 7 seconds")
    time.sleep(7) # Reduced duration as some phone time was used during tea
    print ("- Checked phone")

def new_routine():
    eat_sandwich()
    drink_tea_while_check_phone()
    eat_fruit()
    social_media()

if __name__ == "__main__":
    print ("John's new routine:")
    start_time = time.time()
    new_routine()
    end_time = time.time()
    total_time = end_time - start_time
    print (f"John's new morning routine took {total_time:.1f} seconds!")

    