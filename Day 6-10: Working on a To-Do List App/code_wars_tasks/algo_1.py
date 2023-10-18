def maskify(s):
    if len(s) <= 4:
        return s
    else:
        return "#" * (len(s) - 4) + s[-4:]

# Example usage:
credit_card_number = "1234-5678-9876-5432"
masked_credit_card = maskify(credit_card_number)
print(masked_credit_card)  # Output: "############5432"
