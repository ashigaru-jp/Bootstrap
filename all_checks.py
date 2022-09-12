#!/usr/bin/env python3
import os
import sys

def check_repoot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    if check_disk_full(disk="/", min_gb=2, min_percent=10):
        print "Everythiing ok."
        sys.exit(0)

main()
