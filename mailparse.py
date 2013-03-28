import mailbox, shlex, argparse, sys

parser = argparse.ArgumentParser(description='Parses a maildir and prints a list of unique GMail labels.')
parser.add_argument('path', help="The path to the maildir to be parsed.")


args = parser.parse_args()
try:
	maildir = mailbox.Maildir(args.path, factory=None, create=False)
except:
	sys.exit("%s not a maildir." % args.path)
	
all_label_combinations = []
for message in maildir:
	if message.has_key('X-GMAIL-LABELS'):
		labels = message['X-GMAIL-LABELS']
		if labels not in all_label_combinations:
			all_label_combinations.append(labels)
all_labels = []
for label_combination in all_label_combinations:
	labels = shlex.split(label_combination)
	for label in labels:
		if label not in all_labels:
			all_labels.append(label)
for label in all_labels:
	print label