Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ("yum install postfix dovecot dovecot-pigeonhole mailx")
yum install postfix dovecot dovecot-pigeonhole mailx
>>> print ("postmaster_address = เตชสิทธ์@คน.ไทย.tld")
postmaster_address = เตชสิทธ์@คน.ไทย.tld
>>> print ("lda_mailbox_autocreate = yes")
lda_mailbox_autocreate = yes
>>> print ("lda_mailbox_autosubscribe = yes")
lda_mailbox_autosubscribe = yes
>>> print ("etc/dovecot/conf.d/10-mail.conf: mail_location = maildir:~/Maildir")
etc/dovecot/conf.d/10-mail.conf: mail_location = maildir:~/Maildir
>>> print ("mailbox_command = /usr/libexec/dovecot/deliver")
mailbox_command = /usr/libexec/dovecot/deliver
>>> print ("systemctl restart postfix")
systemctl restart postfix
>>> print ("systemctl restart dovecot")
systemctl restart dovecot
>>> print ("useradd -m youruser = เตชสิทธ์@คน.ไทย")
useradd -m youruser = เตชสิทธ์@คน.ไทย
>>> print (" passwd youruser = @Techasit1198837")
 passwd youruser = @Techasit1198837
>>> 