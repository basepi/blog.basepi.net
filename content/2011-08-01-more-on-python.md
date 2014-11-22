Title: More on Python
Date: 2011-08-01 18:00
Category: Blog

My good friend [Chad][1] recently started learning about Python.  After getting
a fair bit into a book on the subject, he posted on [Google+][2]:

> Language seems cool, though I haven't found a compelling reason to need it. I
> think Django is the main reason I want to use it. Calling upon the powers of
> +Julio Carlos Menendez and +Colton Myers to give me some examples where using
> Python is WAY better than another language.

I decided to try to collect some of the research that I found while selecting
Python as my latest language-of-choice, and post it here.  Hopefully it will be
helpful to anyone who's trying to decide if Python is worth picking up.  Be
aware, though, this is going to be more a random collection of thoughts and
links rather than a linear blog post on the awesomeness of Python.

-------------------------------------------------------------------------------

Community
---------

I suppose one of the first things I should point out, before we get into any
language specifics, is the community.  I love the Python community.  Whether
it's the mailing list(s), or the #python channel on Freenode, the community is
very active and very helpful.  In fact, the #python channel is one of the most
active on my IRC client.  With all that help available, solving problems
becomes much less daunting than in other languages.

-------------------------------------------------------------------------------

Indentation as Syntax
---------------------

One of the most immediately obvious things people notice about Python is the
significance of whitespace.  This is in contrast to most every other modern
programming language, and often throws people when they first discover it.  I
think of this part of Python as a very positive *feature* of the language:
having indentation as part of the actual **syntax** of the language makes for
very consistent code -- across almost every Python program, control structures
look the same, because the indentation delimits code blocks, rather than
braces.  If this feature seems weird or unnatural to you, I suggest you try
writing in Python for your next project -- the initial "weirdness" of this
feature rapidly fades away, and if you're like me, you find yourself
appreciating the innate readability that it gives Python code.

------------------------------------------------------------------------------

Intuitive Language Design
-------------------------

For this next section, I'll quote an [article][3] by Eric Raymond, where he
details his early experience with Python:

> My second \[surprise\] came a couple of hours into the project, when I
> noticed (allowing for pauses needed to look up new features in *Programming
> Python*) I was generating *working* code nearly as fast as I could type. When
> I realized this, I was quite startled. An important measure of effort in
> coding is the frequency with which you write something that doesn't actually
> match your mental representation of the problem, and have to backtrack on
> realizing that what you just typed won't actually tell the language to do
> what you're thinking. An important measure of good language design is how
> rapidly the percentage of missteps of this kind falls as you gain experience
> with the language.
>
> When you're writing working code nearly as fast as you can type and your
> misstep rate is near zero, it generally means you've achieved mastery of the
> language. But that didn't make sense, because it was still day one and I was
> regularly pausing to look up new language and library features!
>
> This was my first clue that, in Python, I was actually dealing with an
> exceptionally good design. Most languages have so much friction and
> awkwardness built into their design that you learn most of their feature set
> long before your misstep rate drops anywhere near zero. Python was the first
> general-purpose language I'd ever used that reversed this process.

I've experienced this myself -- Python's design is such that it works much more
fluidly with the solutions as they live in my head.  I can just start coding
and the solution flows easily from my brainwaves to working Python code.  Try
it, I think you'll be surprised.

While on the topic of Python's intuitiveness, I think we should talk about
IDEs.  C# is one of my favorite languages.  Using Visual Studio, you can create
very advanced and full-featured GUI applications on Windows with relative ease.
However, they key part of that last statement is "Using Visual Studio".  I find
when I'm writing in Java, C#, Objective-C, etc, I end up relying heavily on
intellisense to help me recall syntax and method names.  In contrast, Python is
designed so intuitively that I find that I am able to write full-featured
programs with only Vim and a few trips to the Python documentation to refresh
the name of a certain function within a certain module.  I think that's another
testament to the great design of Python, and just how intuitive it is.

In addition, though C# can be used to create great Windows GUIs, Visual Studio
is again used to abstract away thousands of lines of GUI code which is
generated by Visual Studio as you code the GUI.  Have you ever tried to write a
C#, Java, or Objective-C GUI in a non-IDE text editor such as Vim?  It's nigh
unto impossible, because the syntax is so verbose and not intuitive enough to
easily remember.  Contrast this with Python's Tkinter toolkit, which allows one
to create GUIs with relative ease, and with no reliance on an expensive IDE.
And the Python GUIs look native on each platform.

-------------------------------------------------------------------------------

Java vs. Python
---------------

Might as well throw in a side-by-side comparison of Java vs. Python.  Shows
some of the differences in verbosity and complexity between the two languages,
even if only in small examples.

[Java vs. Python][4]

-------------------------------------------------------------------------------

Conclusion
----------

Obviously Python is not perfect.  There are definitely downsides to having a
completely dynamically-typed language like Python -- if you're not careful, you
can have difficult-to-find bugs crop up.  And the task at hand can sometimes
require the speed of C, for example, or features from other languages -- Python
is not a cure-all, and I don't pretend that it is.  But for me, it's pretty
close.

What it comes down to is that I've come to really enjoy programming in Python,
finding it intuitive, straightforward, and full of features that make my job
easier as a programmer.  And I hope that it treats you as well.  =)


[1]: https://profiles.google.com/u/0/106066712316258581810/about
[2]: http://plus.google.com
[3]: http://www.linuxjournal.com/article/3882
[4]: http://pythonconquerstheuniverse.wordpress.com/category/java-and-python/
