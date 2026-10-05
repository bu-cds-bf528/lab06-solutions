def sliding_window(seq, size, step=1):
    """Return a list of sliding windows over a sequence.

    Args:
        seq: Any sliceable sequence (list, tuple, str, ...).
        size: Window length (must be >= 1).
        step: Distance between window starts (must be >= 1).

    Returns:
        A list of slices of `seq`, each of length `size`. Trailing
        elements that don't fill a complete window are dropped.
        If `seq` is shorter than `size`, returns an empty list.

    Examples:
        >>> sliding_window([1, 2, 3, 4, 5], 3, 1)
        [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        >>> sliding_window("ACGTAC", 3, 2)
        ['ACG', 'GTA']
        >>> sliding_window([1, 2], 3, 1)
        []
    """
    if size < 1:
        raise ValueError("size must be >= 1")
    if step < 1:
        raise ValueError("step must be >= 1")

    return [seq[i:i + size] for i in range(0, len(seq) - size + 1, step)]