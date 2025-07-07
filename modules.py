"""
Core module utilities for data processing operations
"""

def validate_numeric(*values: any) -> None:
    """Validate that all inputs are numeric types"""
    for val in values:
        if not isinstance(val, (int, float)):
            raise TypeError(f"Expected numeric type, got {type(val).__name__}")

def validate_positive(*values: number) -> None:
    """Ensure all numbers are positive"""
    for val in values:
        if val <= 0:
            raise ValueError(f"Value must be positive, got {val}")

def normalize_data(data: list[float]) -> list[float]:
    """Normalize data to 0-1 range"""
    validate_numeric(*data)
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def standardize_data(data: list[float]) -> list[float]:
    """Standardize data to mean=0, std=1"""
    validate_numeric(*data)
    mean = sum(data) / len(data)
    variance = sum((x - mean)**2 for x in data) / len(data)
    std = variance ** 0.5
    return [(x - mean) / std for x in data]

def calculate_statistics(data: list[float]) -> dict:
    """Calculate basic statistics for a dataset"""
    validate_numeric(*data)
    return {
        'mean': sum(data) / len(data),
        'median': sorted(data)[len(data)//2],
        'min': min(data),
        'max': max(data),
        'range': max(data) - min(data)
    }