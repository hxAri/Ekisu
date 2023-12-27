#!/usr/bin/env python

#
# @author Ari Setiawan
# @create -
# @github https://github.com/hxAri
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

CHARSET_RULE:int = 2
COMMENT:int = 1001
FONT_FACE_RULE:int = 5
IMPORT_RULE:int = 3
MARGIN_RULE:int = 1006
MEDIA_RULE:int = 4
NAMESPACE_RULE:int = 10
PAGE_RULE:int = 6
STYLE_RULE:int = 1
UNKNOWN_RULE:int = 0
VARIABLES_RULE:int = 1008
TYPE:list[int] = [
	CHARSET_RULE,
	COMMENT,
	FONT_FACE_RULE,
	IMPORT_RULE,
	MARGIN_RULE,
	MEDIA_RULE,
	NAMESPACE_RULE,
	PAGE_RULE,
	STYLE_RULE,
	UNKNOWN_RULE,
	VARIABLES_RULE
]
