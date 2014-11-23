Title: Blog Auto-Publish with Dropbox
Date: 2014-11-23 03:00
Category: Blog
Tags: pelican, automation, tutorial, dropbox, blog

This weekend I moved my blog over to [Pelican][pelican] from
[Octopress][octopress]. I've been very happy with this decision.

[pelican]: http://getpelican.com
[octopress]: http://octopress.org

But I decided I wanted to go a step further, and set up autopublish. I knew it
could be easily done with a git hook, but I wanted to be able to easily blog
from my iOS devices as well, so I decided to go with [Dropbox][dropbox]
instead.

[dropbox]: https://db.tt/PNs6kv5z

# Getting Dropbox

First, I needed to install Dropbox on my machine. Dropbox provides [an easy
one-liner][dropbox-install]:

```bash
cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -
```

[dropbox-install]: https://www.dropbox.com/install?os=lnx

Now, when I first tried to start up dropbox, it gave me a cryptic error, which
I traced back to not having X11 libraries installed. Turns out I just needed
to unset my DISPLAY variable:

```bash
unset DISPLAY
```

Now Dropbox will start properly:

```bash
~/.dropbox-dist/dropboxd
```

Follow the instructions to get Dropbox authorized on your server, then once
you see the success message, exit using ctrl-c.

## Configure Dropbox as System Service

Next we need to create an init script for Dropbox. I found an example
[here][dropboxinit]. Here's the Ubuntu/Debian script:

[dropboxinit]: http://www.dropboxwiki.com/tips-and-tricks/install-dropbox-in-an-entirely-text-based-linux-environment#Running_on_system_startup

```bash
#!/bin/sh
#dropbox service
DROPBOX_USERS="user1 user2"

DAEMON=.dropbox-dist/dropboxd

start() {
   echo "Starting dropbox..."
   for dbuser in $DROPBOX_USERS; do
       HOMEDIR=`getent passwd $dbuser | cut -d: -f6`
       if [ -x $HOMEDIR/$DAEMON ]; then
           HOME="$HOMEDIR" start-stop-daemon -b -o -c $dbuser -S -u $dbuser -x $HOMEDIR/$DAEMON
       fi
   done
}

stop() {
   echo "Stopping dropbox..."
   for dbuser in $DROPBOX_USERS; do
       HOMEDIR=`getent passwd $dbuser | cut -d: -f6`
       if [ -x $HOMEDIR/$DAEMON ]; then
           start-stop-daemon -o -c $dbuser -K -u $dbuser -x $HOMEDIR/$DAEMON
       fi
   done
}

status() {
   for dbuser in $DROPBOX_USERS; do
       dbpid=`pgrep -u $dbuser dropbox`
       if [ -z $dbpid ] ; then
           echo "dropboxd for USER $dbuser: not running."
       else
           echo "dropboxd for USER $dbuser: running (pid $dbpid)"
       fi
   done
}

case "$1" in

   start)
       start
       ;;
   stop)
       stop
       ;;
   restart|reload|force-reload)
       stop
       start
       ;;
   status)
       status
       ;;
   *)
       echo "Usage: /etc/init.d/dropbox {start|stop|reload|force-reload|restart|status}"
       exit 1

esac

exit 0
```

Note that when I pulled down that script originally, it had a typo. The DAEMON
line near the top of the file should be `.dropbox-dist/dropboxd` -- they left
off the trailing `d` in the version I downloaded.

Place this script in `/etc/init.d/dropbox`. Replace the `DROPBOX_USERS` setting
with a space-separate list of users for which you want Dropbox running. Then,
make the file executable and set it to execute on startup:

```bash
sudo chmod +x /etc/init.d/dropbox
sudo update-rc.d dropbox defaults
```

Now, start Dropbox again, as a service:

```bash
sudo service dropbox start
```

## Selective Sync (Optional)

I have a very large Dropbox folder, and so only want to sync the Blogs folder
from my Dropbox account.

I downloaded the CLI script mentioned on that installation page:

```bash
wget https://linux.dropbox.com/packages/dropbox.py
```

Then, with Dropbox running, I excluded all the directories within the Dropbox
folder, then removed the Blogs folder from the resulting exclusion list:

```bash
./dropbox.py exclude add ~/Dropbox/*
./dropbox.py exclude remove ~/Dropbox/blogs
```

Perfect, now I have only my blogs syncing to my server's dropbox folder.

# Autopublish: The Watcher Script

The automagic regeneration of my blog I modified from [this post][zoia].

[zoia]: http://code.zoia.org/2014/02/25/pelican-dropbox-automatic-blog-regeneration/

I'm going to assume you have a working Pelican setup. Assuming you used the
Pelican quickstart, you should have both a `pelicanconf.py` and a
`publishconf.py`. The `publishconf.py` is going to be what we use.

First, you must modify your `publishconf.py` file such that it can operate from
any directory, rather than relying on relative paths. Thus, you should add your
blog's absolute directory to the Python path inside of that script. Here is my
`publishconf.py`:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

#sys.path.append(os.curdir)
# This is the directory where your pelican's
# configuration files reside
pelicanpath = '/home/basepi/Dropbox/Blogs/blog.basepi.net'
sys.path.append(pelicanpath)

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://blog.basepi.net'
RELATIVE_URLS = False

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

DELETE_OUTPUT_DIRECTORY = True
```

These are the key lines:

```python
pelicanpath = '/home/basepi/Dropbox/Blogs/blog.basepi.net'
sys.path.append(pelicanpath)
```

Now no matter what my current working directory is, the `publishconf.py` will
be able to find the files it needs to operate.

Next, I created a publish script, `publish.sh`:

```bash
#!/bin/bash

PELICAN=/usr/bin/pelican
CONTENT=/home/basepi/Dropbox/Blogs/blog.basepi.net/content
OUTPUT=/home/basepi/Dropbox/Blogs/blog.basepi.net/output
SETTINGS=/home/basepi/Dropbox/Blogs/blog.basepi.net/publishconf.py

rm -rf /home/basepi/Dropbox/Blogs/blog.basepi.net/output/*
$PELICAN $CONTENT -o $OUTPUT -s $SETTINGS || exit $?
rsync -r --delete /home/basepi/Dropbox/Blogs/blog.basepi.net/output/ /var/www/blog.basepi.net
```

Note the use of `|| exit $?`. This will cause the script to exit if the retcode
of the pelican command is non-zero. I don't want to publish my blog if there
are problems.

Make this script executable, and then run it to test that things are working.

The final step is to set up the watcher script which will run our publish
script on changes. For this purpose we will be using [this watcher
script][watcher].

[watcher]: https://github.com/splitbrain/Watcher

This script, conveniently, is ready to be used as an init script. Take [the
script][watcherraw] and put it at `/etc/init.d/watcher`. Make it executable:

[watcherraw]: https://raw.githubusercontent.com/splitbrain/Watcher/master/watcher.py

```bash
sudo chmod +x /etc/init.d/watcher
```

Now, we need to create the configuration file for the watcher. This file is at
`/etc/watcher.ini`:

```bash
[DEFAULT]

; where to store output
logfile=/var/log/watcher.log

; where to save the PID file
pidfile=/var/run/watcher.pid

[job1]
watch=/home/basepi/Dropbox/Blogs/blog.basepi.net/content
events=modify,create,delete,move
excluded=
recursive=true
autoadd=true
command=/home/basepi/Dropbox/Blogs/blog.basepi.net/publish.sh
```

Now we just need to start the watcher:

```bash
sudo service watcher start
```

You can tail the log to see if it's working (change a file to trigger it):

```bash
tail -f /var/log/watcher.log
```

If everything is in order, just have the watcher start on boot:

```bash
sudo update-rc.d watcher defaults
```

And you're done! Now, any time you change the content of your blog, it will be
automatically re-built and published for you!

Let me know what you think in the comments. Or hit me up [on Twitter][twitter]!

[twitter]: http://twitter.com/basepi
