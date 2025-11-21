# Let's create data with different scales
height_cm = [150, 160, 170, 180, 190]  # Range: 150-190
weight_kg = [45, 55, 65, 75, 85]       # Range: 45-85
income_usd = [30000, 40000, 50000, 60000, 70000]  # Range: 30,000-70,000

print("Original data:")
print(f"Height: {height_cm}")
print(f"Weight: {weight_kg}")
print(f"Income: {income_usd}")


def manual_min_max_scaling(data):
    """Manually scale data to 0-1 range"""
    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val

    scaled_data = []
    for value in data:
        scaled_value = (value - min_val) / range_val
        scaled_data.append(round(scaled_value, 2))

    return scaled_data





# Apply manual scaling
height_scaled_manual = manual_min_max_scaling(height_cm)
weight_scaled_manual = manual_min_max_scaling(weight_kg)
income_scaled_manual = manual_min_max_scaling(income_usd)


print("\n--- MANUAL SCALING ---")
print(f"Height scaled: {height_scaled_manual}")
print(f"Weight scaled: {weight_scaled_manual}")
print(f"Income scaled: {income_scaled_manual}")






