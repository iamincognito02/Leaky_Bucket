# Leaky Bucket Congestion Control Simulation

## Project Statement
The Leaky Bucket algorithm simulates congestion control in computer networks by regulating data flow to prevent network congestion. It models the network as a bucket with finite capacity, allowing data to be added at a constant rate while controlling the overflow to ensure a consistent data transfer rate.

## Project Modules
1. **Setup and Initialization**: 
   - Choose a programming language (e.g., Python).
   - Set up the environment with essential libraries/tools.
   - Define leaky bucket parameters: Bucket size (B), Leak rate (R), and Arrival rate (A).
   - Create data structures to simulate the leaky bucket algorithm.

2. **Simulation**:
   - Initialize the bucket and track time.
   - Simulate incoming traffic and manage packet arrivals.
   - Process packets by allowing them if there is room or dropping them if the bucket overflows.
   - Track and visualize statistics on dropped and transmitted packets using tools like Matplotlib.

3. **Testing and Analysis**:
   - Test the simulation under varying conditions (input traffic rates, bucket sizes, and leak rates).
   - Analyze how the leaky bucket algorithm controls congestion and regulates outgoing traffic.
   - Summarize findings in a report or presentation.
   - Explore enhancements like parameter adjustments during runtime or simulating multiple leaky buckets.

## Theory

### Introduction
The leaky bucket algorithm is a traffic-shaping mechanism used to control the rate of data transmission, preventing network congestion by allowing packets to be added at a constant rate and leaking them out at a specified rate.

### Components
- **Bucket**: Virtual container with a fixed capacity.
- **Arriving Packets**: Packets added to the bucket over time.
- **Leak Rate**: Rate at which the bucket releases packets.
- **Bucket Overflow**: Situation when the bucket's capacity is exceeded.

### Operation
1. Packets arrive and are added to the bucket.
2. At regular intervals, packets are leaked from the bucket.
3. The bucket's content decreases based on the leak rate.
4. Packets are transmitted according to the leak rate.
5. Overflow packets are handled based on network policies.

### Use Cases
- Traffic policing
- Traffic shaping
- Buffer management
- Congestion control
- Quality of Service (QoS) assurance

### Advantages
- Traffic smoothing
- Congestion control
- QoS management
- Predictable performance
- Fairness

### Limitations
- Fixed rate constraints
- Burstiness handling
- Implementation complexity
- Buffer management needs
- Configuration challenges

## Implementation

1. **Import Libraries**:
   - Uses `random` for generating incoming packets.
   - Uses `matplotlib` for visualizing simulation results.

2. **LeakyBucket Class**:
   - Represents the leaky bucket simulation.
   - Initialized with parameters: `bucket_size`, `leak_rate_packets_per_sec`, `arrival_rate`, and `time_interval`.

3. **Simulation**:
   - Simulates the leaky bucket algorithm for a specified duration.
   - Tracks packet statuses and applies the leak rate.

4. **Visualization**:
   - Uses Matplotlib to plot simulation results showing transmitted and dropped packets.

5. **Execution**:
   - Prompts for parameters (bucket size, leak rate, arrival rate, and duration).
   - Runs the simulation and displays results.
   - Option to repeat or exit.

## Usage

1. Run the script.
2. Provide the required parameters: bucket size (B), leak rate (R), arrival rate (A), and simulation duration.
3. Review results, including transmitted and dropped packets and a plot of packet statuses.
4. Choose to run another simulation or exit.

Enter the bucket size (B): 10
Enter the leak rate (packets per second): 1
Enter the arrival rate (A): 10
Enter the simulation duration (seconds): 5

Transmitted packets: 14
Dropped packets: 14

Packet 1 - Time: 0 seconds, Status: Transmitted
Packet 2 - Time: 0 seconds, Status: Transmitted
Packet 3 - Time: 0 seconds, Status: Transmitted
Packet 4 - Time: 0 seconds, Status: Transmitted
Packet 5 - Time: 0 seconds, Status: Transmitted
Packet 6 - Time: 0 seconds, Status: Transmitted
Packet 7 - Time: 1 seconds, Status: Transmitted
Packet 8 - Time: 1 seconds, Status: Transmitted
Packet 9 - Time: 1 seconds, Status: Transmitted
Packet 10 - Time: 1 seconds, Status: Transmitted
Packet 11 - Time: 1 seconds, Status: Transmitted
Packet 12 - Time: 1 seconds, Status: Dropped
Packet 13 - Time: 1 seconds, Status: Dropped
Packet 14 - Time: 1 seconds, Status: Dropped
Packet 15 - Time: 1 seconds, Status: Dropped
Packet 16 - Time: 1 seconds, Status: Dropped
Packet 17 - Time: 3 seconds, Status: Transmitted
Packet 18 - Time: 3 seconds, Status: Transmitted
Packet 19 - Time: 3 seconds, Status: Dropped
Packet 20 - Time: 3 seconds, Status: Dropped
Packet 21 - Time: 3 seconds, Status: Dropped
Packet 22 - Time: 3 seconds, Status: Dropped
Packet 23 - Time: 3 seconds, Status: Dropped
Packet 24 - Time: 3 seconds, Status: Dropped
Packet 25 - Time: 3 seconds, Status: Dropped
Packet 26 - Time: 4 seconds, Status: Transmitted
Packet 27 - Time: 4 seconds, Status: Dropped
Packet 28 - Time: 4 seconds, Status: Dropped

### Sample plots
![plot_Figure_1](https://github.com/user-attachments/assets/82203cbc-1ce2-4382-b9ac-9819d71c21bd)
![plot_Figure_2](https://github.com/user-attachments/assets/bc37482b-cf22-4b5e-877c-5055c44bf0a2)
![plot_Figure_3](https://github.com/user-attachments/assets/555f3a43-2488-42a4-9292-7a6e05f2c248)

