#!/usr/bin/python ../scripts/shcov

# BUG: Parenthesis marked as not executed
{
echo foo
}

{ ls ; }

if false; then
	{
		echo foo
	}
fi

if true; then
	# BUG: Parenthesis marked as not executed
	{
		echo foo
	}
fi
