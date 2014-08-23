# pytest tdd watcher
tdd:
	watchmedo shell-command --patterns='*.py' --recursive \
	--command='clear && find . -wholename "*tests/test_*.py" | xargs py.test ${OPT}'

test:
	find . -wholename "*tests/test_*.py" | xargs py.test ${OPT}

behave:
	behave ${OPT}
