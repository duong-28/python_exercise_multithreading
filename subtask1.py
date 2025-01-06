'''
Subtask 1: Simulating John's normal morning routine: 
- Step 1: Eat a sandwich for 8 seconds (instead of 8 minutes for simplicity)
- Step 2: Drink tea for 3 seconds (instead of 3 minutes)
- Step 3: Eat fruits for 2 seconds (instead of 2 minutes)
- Step 4: Scroll through social media for 10 seconds (instead of 10 minutes)
- Step 5: Total morning routine should be: 8 + 3 + 2 + 10 = 23 seconds (instead of 23 minutes)
'''

import time

def eat_sandwich():
    # Step 1: Eat a sandwich
    print ("1. He starts by eating his sandwich for 8 seconds")
    time.sleep(8) # Each second represents 1 minute in real time
    print ("- Sandwich eaten")

def drink_tea():
    # Step 2: Drink tea 
    print ("2. Then he starts drinking his tea for 3 seconds")
    time.sleep(3) # Each second represents 1 minute in real time
    print ("- Tea drank")

def eat_fruit():
    # Step 3: Eat fruits
    print ("3. John starts eating his fruits for 2 seconds")
    time.sleep(2) # Each second represents 1 minute in real time
    print ("- Fruits eaten")

def social_media():
    # Step 4: Scroll through social media
    print ("4. John checks his phone for 10 seconds")
    time.sleep(10) # Each second represents 1 minute in real time
    print ("- Checked phone")

def routine():
    # Execute all morning routine in sequence
    eat_sandwich()
    drink_tea()
    eat_fruit()
    social_media()

if __name__ == "__main__":
    print ("This is John's normal morning routine:")
    # Track total execution time
    start_time = time.time()
    routine()
    end_time = time.time()
    total_time = end_time - start_time
    print (f"John's morning routine took {total_time:.1f} seconds!")

    