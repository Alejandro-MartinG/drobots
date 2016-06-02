start-grid: /tmp/db/registry /tmp/db/node1 /tmp/db/node2 /tmp/db/node3
	icegridnode --Ice.Config=node1.config &
	sleep 5
	icegridnode --Ice.Config=node2.config &
	icegridnode --Ice.Config=node3.config &

stop-grid:
	for node in node1 node2 node3; do \
		icegridadmin --Ice.Config=locator.config -uuser -ppass -e "node shutdown $$node"; \
		done
	killall icegridnode

/tmp/db/%:
	mkdir -p $@

clean: stop-grid
	rm *~
	rm -r /tmp/db
