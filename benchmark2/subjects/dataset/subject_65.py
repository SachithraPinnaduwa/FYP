def process_ip(ip):
    parts = ip.split('.')
    # Check that IP has exactly four parts
    if len(parts) != 4:
        return "IP address isn't valid"
    for part in parts:
        # Check that each part of the IP is an integer
        if not part.isdigit():
            return "IP address isn't valid"
        i = int(part)
        # Check that each part is in the range 0-255
        if i < 0 or i > 255:
            return "IP address isn't valid"
        # Check that no part starts with 0 unless it is 0
        if part[0] == '0' and len(part) != 1:
            return "IP address isn't valid"
    return ''.join(parts)