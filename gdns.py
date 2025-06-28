#!/home/loja01/gdns/venv/bin/python3

import argparse
import dns.resolver
import time
import os
from collections import deque
import plotext as plt

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    parser = argparse.ArgumentParser(description='Ping DNS servers and plot the query time.')
    parser.add_argument('servers', nargs='+', help='DNS servers to ping.')
    parser.add_argument('--domain', default='google.com', help='Domain to resolve for testing.')
    parser.add_argument('--count', type=int, default=20, help='Number of data points to show on the plot.')
    args = parser.parse_args()

    history = {server: deque(maxlen=args.count) for server in args.servers}
    timestamps = deque(maxlen=args.count)

    resolver = dns.resolver.Resolver()

    print(f"Pinging DNS servers: {', '.join(args.servers)}. Press Ctrl+C to stop.")
    time.sleep(2)

    try:
        # Use deques for x coordinates and labels for auto-rotating window
        x_coords = deque(maxlen=args.count)
        x_labels = deque(maxlen=args.count)
        tick_counter = 0

        while True:
            tick_counter += 1
            x_coords.append(tick_counter)
            x_labels.append(time.strftime("%H:%M:%S"))

            for server in args.servers:
                resolver.nameservers = [server]
                try:
                    start_time = time.time()
                    resolver.resolve(args.domain, 'A')
                    end_time = time.time()
                    query_time = (end_time - start_time) * 1000  # in ms
                    history[server].append(query_time)
                except dns.exception.DNSException:
                    history[server].append(0) # Indicate failure
            
            # This loop ensures all data deques have the same length, preventing errors
            for server in args.servers:
                while len(history[server]) < len(x_coords):
                    history[server].appendleft(None)

            clear_screen()
            plt.clf()
            
            plt.title("DNS Query Time")
            plt.xlabel("Time")
            plt.ylabel("Query Time (ms)")

            x_points = list(x_coords)
            for server, times in history.items():
                plt.plot(x_points, list(times), label=server)

            # Set the x-axis tick labels to match the time of the query
            plt.xticks(x_points, list(x_labels))

            plt.show()
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nExiting.")

if __name__ == "__main__":
    main()
