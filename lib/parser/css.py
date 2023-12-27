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


from cssutils import log, parseString as ParseString
from cssutils.css.cssrule import CSSRule
from lib.constant import *
from lib.parser.parser import Parser
from lib.typing.style import Style
from logging import CRITICAL
from re import split
from typing import final
from yutiriti.common import typeof
from yutiriti.text import Text


#[lib.parser.css.CSSParser]
class CSSParser( Parser ):

	#[CSSParser.parse( Str string )]: List<Dict<Str, Any>>
	@final
	@staticmethod
	def parse( string:str ) -> list[dict]:

		"""
		"""

		if not isinstance( string, str ):
			raise TypeError( "Invalid \"string\" parameter, value must be type Str, {} passed".format( typeof( string ) ) )
		
		#[CSS.parse$.process( CSSRule rule )]: Dict<Str, Any>
		def process( rule:CSSRule ) -> dict:
			
			"""
			"""

			if not isinstance( rule, CSSRule ):
				raise TypeError( "INvalid \"rule\" parameter, value must be type CSSRule, {} passed".format( typeof( rule ) ) )

			struct = {}
			named = Text.fromSnakeToCamel( CSSRule._typestrings[rule.type] )
			
			if rule.type in [ CHARSET_RULE, COMMENT ]:
				struct = {
					"type": named,
					"style": rule.cssText
				}
			elif rule.type in [ STYLE_RULE, IMPORT_RULE ]:
				selectors = {}
				for selector in split( r"(?:,)", rule.selectorText ):
					if selector.strip():
						start = selector[0]
						match start:
							case ".":
								select = "class"
							case ":":
								select = selector[1:]
							case "[":
								select = "attribute"
							case "#":
								select = "id"
							case _:
								select = "element"
						if select not in selectors:
							selectors[select] = []
						selectors[select].append( selector )
				properties = {}
				for property in rule.style:
					properties[property.name] = property.value
				struct = {
					"type": named,
					"selectors": selectors,
					"properties": properties
				}
			elif rule.type in [ FONT_FACE_RULE, PAGE_RULE ]:
				struct = {
					"type": named,
					"style": rule.style.cssText
				}
			elif rule.type is MARGIN_RULE:
				struct = {
					"type": named
				}
			elif rule.type is MEDIA_RULE:
				rules = []
				for media in rule.cssRules:
					rules.append( process( media ) )
				struct = {
					"type": named,
					"media": rule.media.mediaText,
					"rules": rules
				}
			elif rule.type is NAMESPACE_RULE:
				struct = {
					"type": named,
					"space": rule.namespaceURI,
					"prefix": rule.prefix
				}
			elif rule.type is UNKNOWN_RULE:
				struct = {
					"type": named
				}
			elif rule.type is VARIABLES_RULE:
				struct = {
					"type": named
				}
			else:
				struct = {
					"type": named
				}

			return Style( struct )

		rules = []
		sheet = ParseString( string )
		for rule in sheet:
			rules.append( process( rule ) )
		
		return rules
	

# Disable log error from cssutils
log.setLevel( CRITICAL )
