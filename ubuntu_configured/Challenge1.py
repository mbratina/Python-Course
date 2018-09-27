#!/usr/bin/env python


def devices():
	routers = ['router1', 'router2', 'router3']
	print routers

def security():
	credentials = {'router2': 'passw0rd1', 'router3': 'passw0rd1', 'router1': 'passw0rd1'}
	print credentials

def combined():
	devices()
	security()

	
if __name__ == "__main__":

	print 'The routers are:'
        devices()
	print 'The credentials are:'
        security()
	print 'All data is:'
        combined()

