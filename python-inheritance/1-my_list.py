#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        ascend_list = sorted(self)
        print(ascend_list)
