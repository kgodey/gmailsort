import os, glob
from email.parser import Parser
from gmailsort_settings import CHAT_DEST_MAILDIR, CHAT_ORIGIN_MAILDIR

if __name__ == '__main__':
	for directory in ['cur', 'tmp', 'new']:
		path_to_directory = os.path.join(CHAT_DEST_MAILDIR, directory)
		if not os.path.exists(path_to_directory):
			os.makedirs(path_to_directory)
			print 'Making directory %s' % path_to_directory
	for path in glob.glob(CHAT_ORIGIN_MAILDIR):
		if path != os.path.join(CHAT_DEST_MAILDIR, 'cur'):
			email_files = os.listdir(path)
			for file_name in email_files:
				full_path_to_file = os.path.join(path, file_name)
				with open(full_path_to_file) as fp:
					message = Parser().parse(fp, headersonly=True)
				if message.has_key('Message-ID') and message['Message-ID'].endswith('chat@gmail.com>'):
						os.rename(full_path_to_file, os.path.join(CHAT_DEST_MAILDIR, 'cur/%s' % file_name))
						print 'Moving e-mail "%s" to Chats!' % message['Subject']
				else:
						print 'Did not move e-mail "%s"' % message['Subject']