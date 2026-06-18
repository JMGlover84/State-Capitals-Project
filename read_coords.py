import json

# Read the file that contains latitude and longitude
with open('state_capitals_with_geocode.json') as f:
    data = json.load(f)

print(f'Total states loaded: {len(data)}')
print()

# Print header
print(f"{'#':<5} {'State':<15} {'Capital':<15} {'Address':<25} {'City':<15} {'ST':<5} {'Zip':<10} {'Latitude':<12} {'Longitude'}")
print("-" * 110)

# Loop through and print each state with all fields
for i, entry in enumerate(data, start=1):
    print(f"{i:<5} {entry['state']:<15} {entry['capital']:<15} {entry['address']:<25} {entry['city']:<15} {entry['state_abbr']:<5} {entry['zip']:<10} {str(entry['latitude']):<12} {entry['longitude']}")

print()
print("-" * 110)
print(f"Total: {len(data)} states")
