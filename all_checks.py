#!/usr/bin/env python3
import os
import sys

def check_repoot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exist("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
        print "Everythiing ok."
        sys.exit(0)

main()