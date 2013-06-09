#!/usr/bin/python ../scripts/shcov

cat <<-EOF
	Line 1
	Line 2
EOF
cat <<'FOO' a
Line 1
Line 2
FOO
if false; then
	cat <<-EOF
		Line1
		Line2
	EOF
fi
