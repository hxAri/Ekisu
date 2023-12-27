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


from bs4 import BeautifulSoup, Tag
from lib.parser.css import CSSParser
from lib.parser.parser import Parser
from lib.typing.element import Element
from typing import final


#[lib.parser.html.HTMLParser]
class HTMLParser( Parser ):

	#[HTMLParser.parse( BeautifulSoup|Tag node )]: Element
	@final
	@staticmethod
	def parse( node:BeautifulSoup|Tag ) -> Element:

		"""
		"""

		tree = {}
		if isinstance( node, Tag ):
			tree = {
				"type": "element",
				"name": node.name,
				"contents": None,
				"attributes": node.attrs,
				"children": []
			}
			if node.name == "style":
				tree['attributes']['styles'] = CSSParser.parse( node.getText() )
			else:
				if "style" in tree['attributes']:
					tree['attributes']['style'] = CSSParser.parse( tree['name'] + "{" + tree['attributes']['style'] + "}" )
				if node.getText():
					tree['contents'] = node.getText()
			for child in node.children:
				if isinstance( child, Tag ):
					tree['children'].append( HTMLParser.parse( child ) )

		return Element( tree )
	
	#[HTMLParser.extract( Dict<Str, Any> parsed, List<Dict<Str, Any>> schemes ): List<Element>
	@final
	@staticmethod
	def extract( parsed: Element, schemes: list[dict[str:any]] ) -> list[Element]:

		#[HTMLParser.extract$.attributeValidator( Dict<Str, Any> target, Dict<Str, Any> scheme )]: Bool
		def attributeValidator( target:dict[str:any], scheme:dict[str:any] ) -> bool:
			for key in scheme.keys():
				if key not in target:
					return False
				if scheme[key]:
					if isinstance( scheme[key], list ):
						if isinstance( target[key], list ):
							for value in scheme[key]:
								if value not in target[key]:
									return False
						elif scheme[key] != target[key]:
							return False
					elif scheme[key] != target[key]:
						return False
			return True
		
		results = []
		
		for schema in schemes:
			if schema['name'] == parsed['name']:
				if "attributes" in schema and schema['attributes']:
					if attributeValidator( scheme=schema['attributes'], target=parsed['attributes'] ) is False:
						continue
					...
				if "children" in schema and schema['children']:
					for index in range( len( parsed['children'] ) ):
						children = parsed['children'][index]
						if "index" in children and children['index'] != index:
							continue
						search = HTMLParser.extract( schemes=schema['children'], parsed=children )
						if search:
							results = [ *results, *search ]
				else:
					results.append( parsed )
		
		return results
	
