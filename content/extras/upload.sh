#!/bin/sh
/usr/bin/rsync -e "ssh" -P -rvc --delete /Users/steve/Dropbox/blogs/blog.coderdojo.lu/output/ aggli:/usr/local/www/vhosts/coderdojo.lu/blog --cvs-exclude
