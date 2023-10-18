#!/bin/bash

# Function to calculate the sum of multiples of 3 or 5 below a given number
sum_of_multiples() {
    local number=$1
    local sum=0

    if [ -z "$number" ] || [ $number -le 0 ]; then
        echo "The sum of multiples of 3 or 5 below $number is: 0"
        return
    fi

    for ((i = 3; i < number; i++)); do
        if [ $((i % 3)) -eq 0 ] || [ $((i % 5)) -eq 0 ]; then
            sum=$((sum + i))
        fi
    done

    echo "The sum of multiples of 3 or 5 below $number is: $sum"
}

# Input number
read -p "Enter a number: " num

# Call the function
sum_of_multiples "$num"
