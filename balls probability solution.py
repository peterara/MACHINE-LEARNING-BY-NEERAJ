from fractions import Fraction

def calculate_probability(w_a, b_a, w_b, b_b):
    # Total balls in bag A
    total_a = w_a + b_a
    
    # Probability of drawing a white ball from bag A
    p_white_a = w_a / total_a
    
    # Probability of drawing a black ball from bag A
    p_black_a = b_a / total_a
    
    # Total balls in bag B after one transfer
    total_b_after_transfer = w_b + b_b + 1
    
    # Scenario 1: Transfer a white ball to bag B
    # New white and black ball counts in bag B
    new_w_b_1 = w_b + 1
    new_b_b_1 = b_b
    p_black_b_1 = new_b_b_1 / total_b_after_transfer
    
    # Scenario 2: Transfer a black ball to bag B
    # New white and black ball counts in bag B
    new_w_b_2 = w_b
    new_b_b_2 = b_b + 1
    p_black_b_2 = new_b_b_2 / total_b_after_transfer
    
    # Total probability of drawing a black ball from bag B
    p_black_final = (p_white_a * p_black_b_1) + (p_black_a * p_black_b_2)
    
    # Convert the probability to an irreducible fraction
    p_black_fraction = Fraction(p_black_final).limit_denominator()
    
    return p_black_fraction

# Input format
input_data = input().strip().split()
w_a = int(input_data[0])
b_a = int(input_data[1])
w_b = int(input_data[2])
b_b = int(input_data[3])

result = calculate_probability(w_a, b_a, w_b, b_b)
print(result)
