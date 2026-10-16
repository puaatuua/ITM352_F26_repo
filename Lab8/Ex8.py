import random

def assign_requirements(requirements_list):
    r1 = random.choice(requirements_list)

    remaining = [r for r in requirements_list if r != r1]
    r2 = random.choice(remaining)
    
    return r1, r2

# Example usage
reqs = ["Requirement A", "Requirement B", "Requirement C", "Requirement D", "Requirement E"]
print(assign_requirements(reqs))
    