#!/usr/bin/python ../scripts/shcov

(
echo foo
)

( echo foo ; )

if false; then
	(
		echo foo
	)
fi

if true; then
	(
		echo foo
	)
fi
