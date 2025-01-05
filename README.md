# John's Morning Routine Simulation

This project simulates John's morning routine using Python scripts. Each script represents a different version of the routine, showcasing various aspects of concurrency and sequential execution: 
- subtask1.py executes all tasks sequentially.
- subtask2.py introduces concurrency by allowing John to drink tea and check his phone simultaneously.
- subtask3.py uses multithreading to simulate concurrent activities during John's breakfast cycle.

## Files

### [subtask1.py](subtask1.py)
Simulates John's normal morning routine sequentially:
- Eat a sandwich for 8 seconds
- Drink tea for 3 seconds
- Eat fruits for 2 seconds
- Scroll through social media for 10 seconds

### [subtask2.py](subtask2.py)
Simulates John's new morning routine with some activities happening concurrently:
- Eat a sandwich for 8 seconds
- Drink tea for 6 seconds while checking the phone for 2 seconds
- Eat fruits for 2 seconds
- Scroll through social media for 7 seconds

### [subtask3.py](subtask3.py)
Simulates John's breakfast cycle using multithreading to represent concurrent activities. The simulation runs for 3 cycles, with each representing a portion of the breakfast routine:
- Sandwich bite: 5 seconds
- Tea sip: 2 seconds
- Fruit bite: 3 seconds
- Phone check: 3 seconds

## How to Run

To run any of the scripts, use the following command:

```sh
python <script_name>.py