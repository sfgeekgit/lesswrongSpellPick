from itertools import combinations

def generate_all_possible_lines():
    # Fixed values for Fire, Water, Earth, Air, Light
    base_values = [24, 39, 26, 26, 18]
    
    # Mage B abilities: Set specific abilities to 1, rest are 0
    mage_b_abilities = [0] * 12  # 13 abilities for Mage B
    # Indices for Flambeau's Flying Fireball, Merinita's Mud Missiles, Solomon's Solar Shield
    mage_b_specific_indices = [3, 6, 10]  # Assuming 0-based indexing matches the order you provided
    for index in mage_b_specific_indices:
        mage_b_abilities[index] = 1

    # Generate all combinations for Mage A abilities
    for mage_a_indices in combinations(range(12), 3):  # 13 abilities, choose 3
        mage_a_abilities = [0] * 12  # Reset Mage A abilities
        for index in mage_a_indices:
            mage_a_abilities[index] = 1
        
        # Combine all parts of the data line
        data_line = base_values + mage_a_abilities + mage_b_abilities
        
        # Yield the generated data line as a comma-separated string
        yield ','.join(map(str, data_line))

# Example: Print all possible unique lines
all_lines = generate_all_possible_lines()
for line in all_lines:
    print(line)
