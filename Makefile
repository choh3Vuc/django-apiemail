UNIT_DIR = test
TMP = build
VERSION := $(shell python3 setup.py --version)

.PHONY: all
all:

.PHONY: clean
clean:
	rm -rf $(TMP)

.PHONY: sdist
sdist:
	mkdir -p $(TMP)
	python3 setup.py sdist --dist-dir $(TMP) --manifest $(TMP)/MANIFEST

.PHONY: test
test: unit

.PHONY: unit
unit:
	python3 -munittest discover -s $(UNIT_DIR) $(TESTOPTS)

.PHONY: upload
upload: unit
	python3 setup.py sdist --dist-dir $(TMP) --manifest $(TMP)/MANIFEST upload



# Copyright 2018 Lean Systems Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
