#!/usr/bin/make -f
# -*- mode:makefile -*-

start-grid: /tmp/db/registry /tmp/db/node1

	icegridnode --Ice.Config=node1.config &
	while ! netstat -lptn 2> /dev/null | grep ":4061"; do sleep 1; done

	icegridadmin --Ice.Config=locator.config -uuser -ppass -e "node list" &
	icegridadmin --Ice.Config=locator.config -uuser -ppass -e "application add 'application.xml'" &
	icegridadmin --Ice.Config=locator.config -uuser -ppass -e "application update 'application.xml'"

stop-grid:
	for node in node1; do \
		icegridadmin --Ice.Config=locator.config -uuser -ppass -e "node shutdown $$node"; \
		done
	killall icegridnode

/tmp/db/%:
	mkdir -p $@

clean: stop-grid
	rm *~
	rm -r /tmp/db
