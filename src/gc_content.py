# Out of Scope: the only parameter is `seq`. There is no option to change
# how ambiguous bases are handled and no percentage toggle.
def gc_content(seq: str) -> float:
    """Return the fraction of G/C among unambiguous bases (A, C, G, T) in seq."""
    # Requirement: `seq` must be a str. Non-string input raises TypeError.
    if not isinstance(seq, str):
        raise TypeError(f"seq must be a str, got {type(seq).__name__}")

    gc = 0
    unambiguous = 0
    # Requirement: a single O(n) pass over the input string, with no
    # pre-scan and no intermediate list of bases.
    # Out of Scope: no chunking, buffering, or special path for large input.
    # The whole string is processed the same way, whatever its length.
    for base in seq:
        # Requirement: counting is case-insensitive (g, G, c, C all count).
        # G/C counts toward both the numerator and the denominator.
        if base in "GCgc":
            gc += 1
            unambiguous += 1
        # Requirement: the denominator is unambiguous bases only. A/T counts
        # toward the denominator only.
        elif base in "ATat":
            unambiguous += 1
        # Requirement: ambiguous IUPAC codes (N, R, Y, ...) are excluded from
        # both numerator and denominator. They match neither branch above,
        # so they are skipped.

    # Requirement: zero unambiguous bases (empty string, or entirely
    # ambiguous codes) raises ValueError instead of returning 0.0.
    if unambiguous == 0:
        raise ValueError("seq contains no unambiguous bases (A, C, G, T)")

    # Requirement: returns a fraction in [0.0, 1.0], not a percentage.
    return gc / unambiguous
