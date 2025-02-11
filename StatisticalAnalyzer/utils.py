import numpy as np
import pandas as pd

def calculate_statistics(data):
    """Calculate statistical measures for the input data."""
    if not data:
        return None
    
    # Convert to numpy array
    arr = np.array(data)
    
    # Calculate mean
    mean = np.mean(arr)
    
    # Calculate standard deviation
    std = np.std(arr)
    
    # Calculate standard deviation ranges
    sd_ranges = {
        "+1": mean + std,
        "-1": mean - std,
        "+2": mean + (2 * std),
        "-2": mean - (2 * std),
        "+3": mean + (3 * std),
        "-3": mean - (3 * std)
    }
    
    # Calculate coefficient of variation
    cv = (std / mean) * 100 if mean != 0 else 0
    
    return {
        "mean": mean,
        "std": std,
        "sd_ranges": sd_ranges,
        "cv": cv
    }

def validate_input(value):
    """Validate if input can be converted to float."""
    try:
        float_val = float(value)
        return True, float_val
    except ValueError:
        return False, None
