Bash Coverage
=============

Based on [shcov](http://shcov.googlecode.com "A gcov and lcov coverage test tool for bourne shell / bash scripts") by Simon Kågström.
This is a purly egotistical fork. Simon has himself deprecated shcov in favour of [kcov](http://simonkagstrom.github.io/kcov/).

Noteworthy changes to underlying code
-------------------------------------
* Tries to handle here-documents.

Not yet sent upstream.

Wrapper less reports
--------------------
By using the included bash script as *BASH_ENV* the need to use shcov as a
wrapper is removed. This is also faster and makes for seamless nesting of
shell scripts.

The use case that it was developed for was to get full coverage report of
a complete system from boot to shutdown.

Example use:

	export BASH_ENV=/usr/share/shcov/bash_coverage
	./script
	./script3
	./script --arguments
	...
	shenvcov --data=/tmp/sh.coverage.bash --output=/tmp/cov.data
	shlcov /tmp/cov.data $HOME/public_html/coverage.report

If shenvcov is rerun with the same arguments it'll append any new data it
finds in the data directory to the output directory.

**WARNING:** it will not try and make sure the coverage files are completed
and will delete them after they've been parsed.

Not so noteworthy changes but documented anyway
-----------------------------------------------
* Remove dead variables and imports
* Follow the sane portions of [PEP8](http://www.python.org/dev/peps/pep-0008/)
* No redefining of built-ins

