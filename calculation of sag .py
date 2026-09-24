def calculate_sag(weight_per_meter, span_length, tension):
    """
    Calculate conductor sag.

    Parameters:
        weight_per_meter (float): Weight per meter (N/m)
        span_length (float): Span length (m)
        tension (float): Horizontal tension (N)

    Returns:
        float: Sag (m)
    """
    sag = (weight_per_meter * span_length ** 2) / (8 * tension)
    return sag


if __name__ == "__main__":
    w = float(input("Enter weight per meter (N/m): "))
    L = float(input("Enter span length (m): "))
    T = float(input("Enter tension (N): "))

    sag = calculate_sag(w, L, T)
    print(f"Sag = {sag:.3f} meters")
