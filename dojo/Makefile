# pytest tdd watcher
tdd:
	watchmedo shell-command --patterns='*.py' --recursive \
	--command='clear && find . -wholename "*tests/test_*.py" | xargs py.test ${OPT}'

# Run all python tests
test:
	find . -wholename "*tests/test_*.py" | xargs py.test ${OPT}

# Run all acceptance tests
behave:
	behave ${OPT}

# Run all python tests and collect coverage data
coverage:
	py.test --cov dojo tests/test_* --cov-report=term-missing
