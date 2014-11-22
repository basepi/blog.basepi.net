Title: Why I switched to Octopress
Date: 2012-02-09 18:33
Category: Blog

The Problem
-----------

Last week I received an e-mail from the RSA Anti-Fraud Command Center.
It related to [my personal blog][1]:

> It appears that your website cmyers.net has been hacked by a fraudster.  It
> is now hosting a phishing attack against RBC.  Please remove the fraudulent
> folders/files as soon as possible and secure your website as it has been
> compromised.  Please note that it is possible that the fraudulent content is
> embedded in your website's legitimate files.

Great.

It turns out the claim was in fact true.  There were new files in my wp-admin
folder for my wordpress install.  When I loaded these files in a browser, it
looked like the home page for a bank.

I had been hacked.

Turns out it's actually quite a common thing.  WordPress is a common (and
apparently quite easy) target for these types of hacks.  It comes down to a
combination of it's popularity, lack of really security-centric design, and the
fact that it's written in PHP.

I considered a few options.  Do I take the time to properly harden my PHP5
install and reinstall wordpress?  Or do I change systems?

Enter Jekyll
------------

[My friend Andrew generates his blog][2] using jekyll.  [Jekyll][3] is a
"simple, blog aware, static site generator."  It's super-cool, check it out.
However, unlike WordPress, it doesn't have a bunch of built-in themes, or even
a theme directory that I could find.  You have to write your own CSS and HTML
templates, which it uses to generate the site.  But it generates an almost
completely static site -- the exception would be if you build in functionality
for [Disqus][4] comments or put your Twitter roll in the sidebar.

If I was going to switch systems, static is what I was looking for.  The
resulting site is much faster than a WordPress site, and much more secure.  But
I didn't have the time, knowledge, or creativity to create a theme from
scratch, and porting my theme from WordPress would be a many hour project.

Enter Octopress
---------------

Then I received a tweet from my friend [Julio][5] that said to check out
[Octopress][6].  It's built on top of Jekyll with built-in support for great
syntax highlighting, Disqus comments, social integration -- everything I was
looking for.  And a great default theme, which I could use as a jumping point
for my own.  I was sold.

The rest is history.  I'll spell out the details in my next post.


[1]: http://blog.cmyers.net/
[2]: http://blog.errstr.com/
[3]: https://github.com/mojombo/jekyll/wiki
[4]: http://disqus.com/
[5]: https://twitter.com/#!/julio_menendez
[6]: http://octopress.org/

