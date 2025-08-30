import math

# Ballistic Limit Equation model for Whipple Shields
def kfi_from_projectile(D, V, tb, S, model='stuffed', rho_p=2700.0, projectile="Al", bumper="Al", t_stuff=0.01):
    # Placeholder calculation, refine with your actual model logic
    if model == 'stuffed':
        return 1.0 - math.exp(-D / (tb + t_stuff))  # Simplified example
    elif model == 'whipple':
        return 1.0 - math.exp(-V / (S + tb))  # Another example formula
    return 0.0
