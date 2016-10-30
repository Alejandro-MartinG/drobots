#!/usr/bin/make -f
# -*- mode:makefile -*-

all:

run-client:
	python Client.py "drobots -t -e 1.1:tcp -h atclab.esi.uclm.es -p 10000 -t 60000" --Ice.Config=Player.config drobots

clean:
	$(RM) *~ 
