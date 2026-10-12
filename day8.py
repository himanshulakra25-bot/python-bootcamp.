# def calculate_total(price, quantity):
#     total = price * quantity
#     print(f"Line total: total")


# calculate_total(10, 3)  
# calculate_total(25, 4)     

def calculate_library_fine(days, book_type="standard", is_premium=False):
    fine = 0
    
    # Tiered Logic based on book type
    if book_type.lower() == "reference":
        fine = days * 20
    elif book_type.lower() == "standard":
        if days <= 5:
            fine = days * 5
        else:
            fine = (5 * 5) + ((days - 5) * 10)
            
    # Apply 20% discount for premium members
    if is_premium:
        fine = fine * 0.8  # or fine = fine - (fine * 0.20)
        
    return fine

# Test Cases
print(calculate_library_fine(3, "standard", False))   # Output: 15  (3 days * 5)
print(calculate_library_fine(7, "standard", False))   # Output: 45  (5*5 + 2*10)
print(calculate_library_fine(4, "reference", False))  # Output: 80  (4 days * 20)
print(calculate_library_fine(7, "standard", True))    # Output: 36.0 (45 with 20% discount)