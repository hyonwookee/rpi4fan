#!/bin/bash

# Function to max out CPU
max_cpu() {
    while :; do :; done
}

# Function to display CPU temperature
show_temp() {
    while true; do
        temp=$(vcgencmd measure_temp)
        echo "CPU Temperature: $temp"
        sleep 10
    done
}

# Number of CPU cores
num_cores=$(nproc)

# Launch the max_cpu function for each core
for i in $(seq 1 $num_cores); do
    max_cpu &
done

# Launch the temperature display function
show_temp

