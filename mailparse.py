import mailbox, email, shlex

maildir = mailbox.Maildir('/home/kgodey/.maildir/', factory=None, create=False)
# You can get a list of folders by using maildir.list_folders()
maildir = maildir.get_folder('kritigodeygmail.Class')
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