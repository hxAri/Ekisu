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


from lib.typing.style import Style
from typing import final, TypeVar
from yutiriti.object import Object
from yutiriti.typing import Typing


Element = TypeVar( "Element" )


#[lib.typing.element.Element]
class Element( Typing ):

	#[Element.__items__]: List<Dict|List|Object|Str>
	@final
	@property
	def __items__( self ) -> list[dict|list|Object]:
		return [
			"name",
			"contents",
			"attributes",
			"children"
		]
	
	#[Element.__mapping__]: Dict|Object
	@final
	@property
	def __mapping__( self ) -> dict|Object:
		return {
			"attribute": {
				"style": Object
			}
		}
	
	#[Element.name]: None|Str
	@property
	def name( self ) -> None|str:
		return self['name'] if "name" in self else None

	#[Element.contents]: None|Str
	@property
	def contents( self ) -> None|str:
		return self['contents'] if "contents" in self else None

	#[Element.attributes]: Object 
	@property
	def attributes( self ) -> Object:
		return self['attributes'] if "attributes" in self else Object({})
	
	#[Element.children]: List<Element>
	@property
	def children( self ) -> list[Element]:
		return self['children'] if "children" in self else []
	
