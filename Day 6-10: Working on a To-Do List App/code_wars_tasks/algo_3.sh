#!/bin/bash

sum_of_multiples() {
    local number=$1
    local sum=0

    if [ $number -le 0 ]; then
        echo "0"
        return
    fi

    for ((i = 3; i < number; i++)); do
        if [ $((i % 3)) -eq 0 ] || [ $((i % 5)) -eq 0 ]; then
            sum=$((sum + i))
        fi
    done

    echo $sum
}

read -p "Enter a number: " num

result=$(sum_of_multiples $num)
echo "The sum of multiples of 3 or 5 below $num is: $result"
