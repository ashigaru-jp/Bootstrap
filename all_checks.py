#!/usr/bin/env python3
import os
import sys

def check_repoot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")
def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def main():
    checks=[
        (chek_reboot, "Pending Reboot"),
        (check_root_full,  "Root parition full")
    ]
    for check, msg in checks:
        if check():
            print(msg)
            sys.exit(1)
    print("Everything ok")
    sys.exit(0)
main()
