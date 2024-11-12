def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(Name = "Pranav", Role = "SWE-I")
print("\n")
print_kwargs(Name = "Pranav")
print("\n")
print_kwargs(Name = "Pranav", Role = "SWE-I", Tech = "AI")