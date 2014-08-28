import os
import collections
from django.utils.six import add_metaclass
from django.core.urlresolvers import reverse


TEXT_FILE_MIME_TYPES = set([
	'application/pdf',
])


class IterableChoiceEnum(type):
	def __iter__(self):
		return iter(self._choices)

@add_metaclass(IterableChoiceEnum)
class ChoiceEnum(object):
	_choices = ()

class FileType(ChoiceEnum):
	UNKNOWN = 0
	PDF = 1
	TXT = 2

	_choices = (
		(UNKNOWN, "Unknown"),
		(PDF, "Pdf"),
		(TXT, "Text"),
	)

class FileStatus(ChoiceEnum):
	UPLOADED = 1
	READY = 2
	FAILED = 4

	_choices = (
		(UPLOADED, "Uploaded"),
		(READY, "Ready"),
		(FAILED, "Failed"),
	)
