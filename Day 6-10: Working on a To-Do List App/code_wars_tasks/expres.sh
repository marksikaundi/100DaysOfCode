#!/bin/bash

# Function to validate each octet of the IP address
validate_octet() {
    local octet="$1"
    # Check if the octet is a non-empty string containing only digits
    if ! [[ "$octet" =~ ^[0-9]+$ ]]; then
        return 1
    fi

    # Convert the octet to an integer
    local octet_value
    octet_value=$(echo "$octet" | sed 's/^0*//')  # Remove leading zeros
    if [[ "$octet_value" -lt 0 || "$octet_value" -gt 255 ]]; then
        return 1
    fi
}

# Main function to validate the IP address
validate_ip() {
    local ip="$1"
    local IFS="."  # Set the internal field separator to split by dot

    # Split the input string into octets
    local octets=($ip)

    # Check if there are exactly four octets
    if [[ ${#octets[@]} -ne 4 ]]; then
        return 1
    fi

    # Check each octet for validity
    for octet in "${octets[@]}"; do
        validate_octet "$octet" || return 1
    done
}

ip_to_validate="123.45.67.89"
if validate_ip "$ip_to_validate"; then
    echo "$ip_to_validate is a valid IPv4 address."
else
    echo "$ip_to_validate is not a valid IPv4 address."
fi
