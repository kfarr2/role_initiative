import os
import collections
from django.utils.six import add_metaclass
from django.core.urlresolvers import reverse


class IterableChoiceEnum(type):
	def __iter__(self):
		return iter(self._choices)

@add_metaclass(IterableChoiceEnum(type))
class FileType(object):
	UNKNOWN = 0
	PDF = 1
	TXT = 2

	_choices = (
		(UNKNOWN, "Unknown"),
		(PDF, "Video"),
		(TXT, "Text"),
	)
