sample_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
               {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

unique_values = set()

for d in sample_data:
    values = d.values()
    for value in values:
        unique_values.add(value)
print("Unique values:", list(unique_values))
