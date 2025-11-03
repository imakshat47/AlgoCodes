def is_valid_segment(segment):
    if not (1 <= len(segment) <= 4):
        return False

    for char in segment:
        if not (char.isdigit() or 'a' <= char.lower() <= 'f'):
            return False

    return True


def isValid(ip):
    if not ip:
        return False

    segments = ip.split(":")
    if len(segments) != 8:
        return False

    return all(is_valid_segment(segment) for segment in segments)


if __name__ == "__main__":
    s = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    print(f"{'true' if isValid(s) else 'false'}")
