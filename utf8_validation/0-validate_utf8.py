#!/usr/bin/python3
"""Determines whether a list of integers is a valid UTF-8 encoding."""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding, otherwise False."""
    # How many continuation bytes the current character still needs
    bytes_remaining = 0

    for number in data:
        # Only the 8 least significant bits count as the byte
        byte = number & 0xFF

        if bytes_remaining == 0:
            # Start of a new character: its first bits say how long it is
            if byte >> 7 == 0b0:
                bytes_remaining = 0
            elif byte >> 5 == 0b110:
                bytes_remaining = 1
            elif byte >> 4 == 0b1110:
                bytes_remaining = 2
            elif byte >> 3 == 0b11110:
                bytes_remaining = 3
            else:
                return False
        else:
            # Inside a character: every byte must start with 10
            if byte >> 6 != 0b10:
                return False
            bytes_remaining -= 1

    # A character cut off before its last byte is invalid
    return bytes_remaining == 0