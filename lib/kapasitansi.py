#!/usr/bin/python


"""
pustaka untuk menghitung kapasitansi dari sebuah kapasitor pelat sejajar
"""


MIU = 8.85*10**-12


def c(A, s):
	return (A*MIU)/s
