Title: Karabiner (Elements) and macOS Sierra
Date: 2017-06-14 13:00
Category: Blog

I like hacks. I like tweaks. I like setting things up just to my
specifications. I mean, I use an [Ergodox
Infinity](https://input.club/devices/infinity-ergodox/), a [CST
Trackball](http://clearlysuperiortech.com/cst2545-5wproductpage.html) and I'm
an [avid Vim user](https://github.com/basepi/dotfiles/blob/master/vim/vimrc).

But these hacks and tweaks are not without their disadvantages. When macOS
Sierra came out, it severely broke support for a key app in my setup:
[Karabiner](https://pqrs.org/osx/karabiner/). I was using Karabiner for three
very specific, very important hacks, all inspired by [Steve Losh's "A Modern
Space Cadet" blog post from
2012](http://stevelosh.com/blog/2012/10/a-modern-space-cadet/):

1. The `ctrl` key would act as `escape` if short-pressed with no other key.
   Because I rebind `caps lock` to `control` anyway, that puts both `control`
   and `escape` in perfect reach of my left pinky.  No more reaching up or down
   for either key.  It's amazing!

2. `F19` was mapped to `cmd-ctrl-shift-option`. Why `F19`? Because it is on no
   modern keyboard, and has no default usage in modern operating systems. So I
   bound it to a key on my ergodox, and use it as a
   [`hyper`](http://stevelosh.com/blog/2012/10/a-modern-space-cadet/#hyper)
   modifier key.  However, I went a step further, and made short presses on
   this key input `cmd-space` (the spotlight shortcut). Surprisingly convenient.

3. The left and right `shift` keys would act as left and right parenthesis when
   short-pressed with no other keys.

These hacks have become second nature, part of my muscle memory. Losing them
would be terrible for my productivity. So I waited for Karabiner to be updated
to Sierra.....cut to today, 9 months after Sierra was released, and Karabiner
still has not been updated.

However, I found out today that Karabiner Elements *finally* [added support for
short vs long pressed
keys](http://cmsj.net/2017/06/13/karabiner-elements-sierra-hyper.html) in their
latest beta version.

If you want to check out my implementation, I [host my dotfiles on
github](https://github.com/basepi/dotfiles/blob/master/misc/config/karabiner/karabiner.json).
The section is under `complex_modifications`. Remember that you need to be
running Karabiner Elements 0.91.3, which is in beta!

What hacks/tweaks can you not live without? Leave a comment or [tweet at
me](https://twitter.com/basepi)!
