Title: Fix Linode Manager Repeated Log-out (Force IPv4)
Date: 2014-11-25 13:00
Category: Blog

Recently I've been having issues with Linode Manager repeatedly logging me out
every few requests. I figured this was related to ipv4/ipv6 switching, because
sometimes the logout would also trigger a new IP whitelist request, which would
sometimes be ipv4, and sometimes be ipv6.

After a little googling, I found [this twitter conversation][twitterconv]:

[twitterconv]: https://twitter.com/endrift/status/421774360035074049

<blockquote class="twitter-tweet" lang="en"><p><a
href="https://twitter.com/linode">@linode</a> Manager keeps logging me out at
seemingly random intervals, especially when trying to do DNS management. Is
this a known problem?</p>&mdash; Jeffrey Pfau (@endrift) <a
href="https://twitter.com/endrift/status/421774360035074049">January 10,
2014</a></blockquote> <script async src="//platform.twitter.com/widgets.js"
charset="utf-8"></script>

Turns out I'm not the only one experiencing this issue. So I decided to set up
`dnsmasq` as one of the replies mentioned, and force Linode to a single ipv4
address.

Note that these instructions are for OSX (and were tested on Yosemite, 10.10).

First, I installed `dnsmasq` via [Homebrew][brew]:

[brew]: http://brew.sh

```bash
brew install dnsmasq
```

Then, I followed the homebrew instructions to install `dnsmasq` as a service to
start on startup:

```bash
sudo cp -fv /usr/local/opt/dnsmasq/*.plist /Library/LaunchDaemons
sudo chown root /Library/LaunchDaemons/homebrew.mxcl.dnsmasq.plist
```

Now, before we actually start the service, let's get our resolver in place.
OSX allows us to define resolve data for specific addresses using files in
`/etc/resolver/`. Here is my `/etc/resolver/manager.linode.com`:

```yaml
nameserver 127.0.0.1
```

Basically, we're telling the operating system to use our local DNS server
(provided by `dnsmasq`) for lookups for `manager.linode.com`.

We also need to configure `dnsmasq` to force `manager.linode.com` to a specific
address. First, we need an IPv4 address to work with:

```bash
# dscacheutil -q host -a name manager.linode.com
name: manager.linode.com
ipv6_address: 2600:3c00::14
ipv6_address: 2600:3c00::34
ipv6_address: 2600:3c00::24

name: manager.linode.com
ip_address: 69.164.200.204
ip_address: 72.14.191.204
ip_address: 72.14.180.204
```

Then, copy the example configuration into place:

```bash
cp /usr/local/opt/dnsmasq/dnsmasq.conf.example /usr/local/etc/dnsmasq.conf
```

and edit `/usr/local/etc/dnsmasq.conf`, adding this line:

```bash
address=/manager.linode.com/72.14.180.204
```

Now, start `dnsmasq`:

```bash
sudo launchctl load /Library/LaunchDaemons/homebrew.mxcl.dnsmasq.plist
```

Assuming you did everything right, you should only see one address when you
query again:

```bash
dscacheutil -q host -a name manager.linode.com
name: manager.linode.com
ip_address: 72.14.180.204
```

I haven't done much on Linode since implementing this fix, but haven't had it
log me out erroneously once yet.

If you have improvements or run into issues, please leave a comment below!
