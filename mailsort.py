import os, shlex
from email.parser import Parser
from gmailsort_settings import ORIGIN_MAILDIR, DEST_MAILDIR, IGNORED_LABELS, LABEL_ORDER, LABELS_TO_FIX

"""

This function takes a label name directly from GMail headers, and figures out the appropriate maildir path for messages tagged with that label. It also ensures that the maildir corresponding to the label exists.

"""
# Internal variable tracking labels that have been seen for efficiency.
_seen_paths = []
def maildir_path(label):
	# Checks to see if the label can be used as is.
	if label in LABELS_TO_FIX:
		maildir_path = DEST_MAILDIR(LABELS_TO_FIX[label])
	else:
		maildir_path = DEST_MAILDIR(label)
	# If this label hasn't been seen before, ensures that the maildir corresponding to it exists.
	if maildir_path not in _seen_paths:
		for directory in ['cur', 'tmp', 'new']:
			path_to_directory = os.path.join(maildir_path, directory)
			if not os.path.exists(path_to_directory):
				os.makedirs(path_to_directory)
				print 'Making directory %s' % path_to_directory
		_seen_paths.append(maildir_path)
	# Returns the path.
	return os.path.join(maildir_path, 'cur')

"""

Sorts the mail!

"""
if __name__ == '__main__':
	# Gets a list of all e-mail to be processed.
	email_files = os.listdir(ORIGIN_MAILDIR)
	counter = 0
	for file_name in email_files:
		# Opens and parses the file.
		full_path_to_file = os.path.join(ORIGIN_MAILDIR, file_name)
		with open(full_path_to_file) as fp:
			message = Parser().parse(fp, headersonly=True)
		# Checks for the header containing GMail labels and parses the header.
		if message.has_key('X-GMAIL-LABELS'):
			labels = message['X-GMAIL-LABELS']
			label_list = shlex.split(labels)
			## print label_list
			# Removes labels that are to be ignored.
			for label in IGNORED_LABELS:
				if label in label_list:
					label_list.remove(label)
			# If there's only one label, sorts the e-mail into the folder corresponding to that label.
			if len(label_list) == 1:
				os.rename(full_path_to_file, os.path.join(maildir_path(label_list[0]), file_name))
				## print 'Moving file %s to directory %s' % (full_path_to_file, os.path.join(maildir_path(label_list[0]), file_name))
			# If there are multiple labels, checks the precedence order in settings and sorts the e-mail into the appropriate folder.
			else:
				for label in LABEL_ORDER:
					if label in label_list:
						os.rename(full_path_to_file, os.path.join(maildir_path(label), file_name))
						## print 'Moving file %s to directory %s' % (full_path_to_file, os.path.join(maildir_path(label), file_name))
						break
		counter += 1
		if counter % 100 == 0:
			print 'Processed %d messages!' % (counter)