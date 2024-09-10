import random
from matplotlib import patches
import matplotlib.pyplot as plt

class LeakyBucket:
    def __init__(self, bucket_size, leak_rate_packets_per_sec, arrival_rate, time_interval):
        self.bucket_size = bucket_size
        self.bucket = 1
        self.leak_rate_packets_per_sec = leak_rate_packets_per_sec
        self.arrival_rate = arrival_rate
        self.time_interval = time_interval
        self.transmitted_packets = 0
        self.dropped_packets = 0
        self.time_elapsed = 0
        self.packets_in_bucket = []
        self.packet_log = []

    def simulate(self, duration):
        while self.time_elapsed < duration:
            incoming_packets = random.randint(0, self.arrival_rate) #4

            # Track the status and timestamp of each packet
            for _ in range(incoming_packets):#4
                if self.bucket <= self.bucket_size:# 11 <= 10
                    self.transmitted_packets += 1 #tran = tran + 1 
                    self.bucket += 1 #2
                    self.packet_log.append((self.time_elapsed, "Transmitted"))
                else:
                    self.dropped_packets += 1
                    self.packet_log.append((self.time_elapsed, "Dropped"))

            # Apply the leak rate per second
            packets_to_leak = self.leak_rate_packets_per_sec
            self.bucket = max(0, self.bucket - packets_to_leak)

            self.time_elapsed += self.time_interval
            self.packets_in_bucket.append(self.bucket)

    def plot_simulation(self):
        plt.figure()

        for i, (timestamp, status) in enumerate(self.packet_log):
                if status == "Transmitted":
                    plt.plot([timestamp, timestamp], [i, i], color='green', linewidth=4, marker = 'o')
                else:
                    plt.plot([timestamp, timestamp], [i, i], color='red', linewidth=4, marker='x')

        plt.xlabel("Time (seconds)")
        plt.ylabel("Packet Status")
        plt.title("Leaky Bucket Simulation")
        
        green = patches.Patch(color='green', label='Transmitted') 
        red = patches.Patch(color='red', label='Dropped') 
        plt.legend(handles=[green, red], loc='upper left')
        plt.grid()

        # Adding custom y-axis ticks with spacing
        y_ticks = range(0, len(self.packet_log), 1)  # Adjust the spacing (e.g., 5) as needed
        plt.yticks(y_ticks)
        plt.xticks(range(0, self.time_elapsed + 1))
        plt.gca().xaxis.grid(True)
        plt.gca().yaxis.grid(True)
        plt.show()

    def print_packet_status(self):
        for i, (timestamp, status) in enumerate(self.packet_log):
            print(f"Packet {i + 1} - Time: {timestamp} seconds, Status: {status}")

def main():
    while True:
        B = int(input("Enter the bucket size (B): "))
        R = int(input("Enter the leak rate (packets per second): "))
        A = int(input("Enter the arrival rate (A): "))
        duration = int(input("Enter the simulation duration (seconds): "))
        time_interval = 1  # Time interval is set to 1 second

        bucket = LeakyBucket(B, R, A, time_interval)
        bucket.simulate(duration)

        print("Transmitted packets:", bucket.transmitted_packets)
        print("Dropped packets:", bucket.dropped_packets)
        bucket.print_packet_status()
        bucket.plot_simulation()

        another_simulation = input("Do you want to run another simulation? (yes/no): ")
        if another_simulation.lower() != "yes":
            break

if __name__ == "__main__":
    main()
