Resources
=========

Resources shared with Allen for the project.

### Notation used to keep track of the state of resources ###
* `+` - Denotes optional resources that have information that is good to know but is not critical for acheiving the goals of this project. This will be the default unless otherwise specified.
* `*` - Denotes resources that contain information that could be critical to acheiving the goals of this project.
* `@book`, `@video` .. - Denotes the type of resource.
* Allen - you can similarly have symbols to denote 2 states: i. that you are in the process of going through a resource, ii. you have completed viewing a resource.

Programming
-------------
* [Code.org course 3](http://studio.code.org/s/course3)

  > Course 3 is designed for students who have taken Course 2. Students will delve deeper into programming topics introduced in previous courses to flexible solutions to more complex problems. By the end of this course, students create interactive stories and games they can share with anyone. Recommended for grades 4-5.

* [Curriculum for Middle School Math | Code.org](http://code.org/curriculum/msm)
  > introductory curriculum which teaches algebraic and geometric concepts through computer programming. The nine units focus on concepts like order of operations, the Cartesian plane, function composition and definition, and solving word problems - all within the context of video game design. .. At the end of the nine units, students will have a completed workbook filled with word problems, notes, and math challenges, as well as a video game of their own design to share with friends and family.

Python programming
---------------
Resources for learning the language itself. Not related to game programming.

* [Invent Your Own Computer Games with Python, 2nd Edition](http://inventwithpython.com/chapters/) `*` `@book`
 - A very highly rated book made available for free by the Author that teaches programming using Python. Allen, we can use this as the main source for learning Python programming.

* [Python | Codecademy](http://www.codecademy.com/en/tracks/python) `*` `@interactive`
  - A interactive course that teaches Python. Could be done along with or after the 'Invent Your Own Computer Games with Python' book.
 
* [Introduction to Programming with Python](https://opentechschool.github.io/python-beginners/en/index.html) `+` `@tutorial` 
 - A simple tutorial that introduces Python using turtle library.

Game programming
---------------

### Game programming using Python ###
* [Making Games with Python & Pygame](http://inventwithpython.com/pygame/index.html) `*` `@book`
  - If we decide to use PyGame, we can then use this as our main text for learning PyGame.

* [Program Arcade Games With Python And Pygame](http://programarcadegames.com/index.php?lang=en) `*` `@book`
  - Anoteher highly rated book that is available for free that teaches game programming using Python and Pygame.
  
* [Game Programming L Line](http://aharrisbooks.net/pythonGame/) `+` `@book`
  - Code and course presentations from the highly rated (non-free) PyGame book [Game Programming: The L Line, The Express Line to Learning](http://www.amazon.com/Game-Programming-Line-Express-Learning/dp/0470068221/ref=sr_1_1?ie=UTF8&qid=1420444055&sr=8-1&keywords=Game+Programming+Express+Line). But there seems to be sufficient information in the presentations and code to be usable without the book.
  
* [Introduction to game programming - PyCon 2014](http://pyvideo.org/video/2620/introduction-to-game-programming) `+` `@video`
 - video from the last PyCon conference. It introduces Game programming in Python using a library called PyGame. I realize we haven't started on Python programming yet - but you should still be able to watch the video and able to learn many important information. We can revisit this again as we are learning Python.

* Sample projects
  * [PyWeek - Python Game Programming Challenge - Games](https://www.pyweek.org/all_games/)
    - Games sorted by rating along with source-code that were produced for a bi-annual programming challenge.
  * Psuedo FPS game with Pygame 
    - video - [mlambir's Pygame-FPS - YouTube](https://www.youtube.com/watch?v=yASop1CxXfE)
    - source code - 500 lines - [Pygame-FPS/src at master · mlambir/Pygame-FPS · GitHub](https://github.com/mlambir/Pygame-FPS/tree/master/src)
  * A Simple 2D game using Pygame
    - video - [A little game made with Python and Pygame - YouTube](https://www.youtube.com/watch?v=aUCyfdzP-i8)
    - source code - 1800 lines - [[Python] main.py - Pastebin.com](http://pastebin.com/VW9maqHf)  

### Gaming libraries / engines considered ###

* [Blender Game Engine](http://wiki.blender.org/index.php/Doc:2.6/Manual/Game_Engine)
 - [Tutorials](http://www.blender.org/support/tutorials/) :: [Game Engine: Simple Character - Blender Cookie](http://cgcookie.com/blender/cgc-courses/game-engine-simple-character/)
 - [Doc:2.6/Manual - BlenderWiki](http://wiki.blender.org/index.php/Doc:2.6/Manual)

* [Soya3D — The flowers of evidence](http://www.lesfleursdunormal.fr/static/informatique/soya3d/index_en.html)
  - inbuilt support for blender models
  - good doc - but still not as comprehensive (or popular) as PyGame
  - includes collision detection, physics ..
  
  > a game engine focused on rapid development and ease of use. Its goal is to enable amateur developers to create sophisticated 3D games entirely in the Python language.

  > Soya offers the features one can expect from a 3D engine, like basic scene management, cell-shading, shadows, particles systems,... as well as some unique features aiming at making 3D development easier and more rapid 


* [cocos2d](http://python.cocos2d.org/doc.html)
  - gaming wrapper over [pyglet](http://www.pyglet.org/index.html)
  - still might be a little bit complicated than Blender or PyGame
  - seems like a popular option for building games in iOs
     - might come in handy in future

* PyGame
  - wrapper over SDL
  - for 3D we need to use PyOpenGL or some other lib

* [Panda3D](http://www.panda3d.org/manual/index.php/Main_Page)
  - [Featureful](https://www.panda3d.org/manual/index.php/Features), commercial grade, open-source library 
     - but might be complex for a first timer
* Comparisons from the web

  - [Blender vs panda3d](http://blenderartists.org/forum/showthread.php?173689-Blender-vs-panda3d)

   > Panda3d is used with code only. Blender game engine can make games without coding. 

   > Panda3D doesn't have all the editing utilities for rapid development like the BGE doesn, last I've seen you need to plug in your own level editor and your own models, the engine by itself has no model, texture, sound, or level editor, you have to plug that all in with code.
Also you may have to plug in your own physics engine too using an API like Bullet or ODE, you may also have to create and define a camera using code instead of using a camera object that you can place anywhere, you may need to know some of the OpenGL API.
Panda3D is kind of like Darkbasic and other game API's, they can be very powerful, but it will take longer than a few hours to get something really playable.

   > I tried panda once; It was very confusing. As far as i know, panda doesn't have a significant community, or half-decent API docs (correct me if i'm wrong)

   >  If you are a talented coder, and have a real good understanding how to optimise your code, not only for useability, but for speed, go with Panda--as it gives you more power and flexibility overall. If you know very little about what it takes to make a game engine, stick with Blender. You'll have all the power you'll need.

  - [Differences between Python game libraries Pygame and Pyglet? - Stack Overflow](http://stackoverflow.com/questions/370680/differences-between-python-game-libraries-pygame-and-pyglet)
  
   > Pygame is geared towards game development (cursors, sprites, joystick/gamepad support)
Pyglet is more general purpose (though it has a Sprite class)

   >  Pyglet is a pure python library with fewer dependencies, I think it requires better understanding of OpenGL

   > Having looked at both pygame and pyglet I found pyglet easier to pick up and was able to write a simple breakout style game within a few days.

  - [python - PyOpenGl or pyglet? - Stack Overflow](http://stackoverflow.com/questions/279912/pyopengl-or-pyglet)

   > Start with pyglet. It contains the best high-level API, which contains all you need to get started, from opening a window to drawing sprites and OpenGL primitives using their friendly and powerful Sprite and Batch classes.

  - [Making Games with Python: Which Library To Use, pygame or pyglet? | Leap On!](http://leapon.net/en/making-games-with-python-which-library-to-use-pygame-or-pyglet)

* [ Python-Ogre](http://wiki.python-ogre.org/index.php?title=Main_Page)
 - Not updated ([since 2011](http://sourceforge.net/projects/python-ogre/files/Latest/))

### Resources ###
 
* [2d and 3d game and rendering engines for python - codeboje.de](http://codeboje.de/2d-and-3d-game-and-rendering-engines-python/)

* [Python 3D Software](http://www.vrplumber.com/py3d.py)

* [List of game engines - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/List_of_game_engines)

* [Engines and libraries](http://pyratesarecool.appspot.com/Engines_and_libraries)

* [How to make a 3D game in python?](https://uk.answers.yahoo.com/question/index?qid=20140617124940AAogp6p)	

* [PythonGames - Python Wiki](https://wiki.python.org/moin/PythonGames)

* [Python libraries resources etc - Game Prog Wiki](http://content.gpwiki.org/index.php/Python)

 
After this project
---------------------
Resources covering advanced topics that might be a good path to pursue after this project.

### Programming ###

* [Introduction to Computation and Programming Using Python, Revised and Expanded Edition | Vancouver Public Library | BiblioCommons](http://vpl.bibliocommons.com/item/show/3636111038_introduction_to_computation_and_programming_using_python,_revised_and_expanded_edition) `+` `@book`

 > This book introduces students with little or no prior programming experience to the art of computational problem solving using Python and various Python libraries, including PyLab. It provides students with skills that will enable them to make productive use of computational techniques, including some of the tools and techniques of "data science" for using computation to model and interpret data. The book is based on an MIT course (which became the most popular course offered through MIT's OpenCourseWare) and was developed for use not only in a conventional classroom but in a massive open online course (or MOOC) offered by the pioneering MIT-Harvard collaboration edX. Students are introduced to Python and the basics of programming in the context of such computational concepts and techniques as exhaustive enumeration, bisection search, and efficient approximation algorithms. The book does not require knowledge of mathematics beyond high school algebra, but does assume that readers are comfortable with rigorous thinking and not intimidated by mathematical concepts.

### Game development ###

* Participate in the bi-annual [PyWeek - Python Game Programming Challenge](https://www.pyweek.org/), where you will have to build a game from scratch in a week using Python. Could be a nice addition to the project, especially if applying to present in next year's PyCon.

* [Practical Game Development With Unity and Blender | Vancouver Public Library | BiblioCommons](http://vpl.bibliocommons.com/item/show/4059751038_practical_game_development_with_unity_and_blender) `+` `@book`

* [Creating Games With Unity and Maya | Vancouver Public Library | BiblioCommons](http://vpl.bibliocommons.com/item/show/3037113038_creating_games_with_unity_and_maya) `+` `@book`


### Linux, Opensource and Git ###

* [The Cathedral and the Bazaar](http://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/) `+` `@book`

  > The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary (abbreviated CatB) is an essay, and later a book, by Eric S. Raymond on software engineering methods, based on his observations of the Linux kernel development process and his experiences managing an open source project, fetchmail. 


* Much, much later (after you are 18) - Participate in the [Google Summer of Code](https://developers.google.com/open-source/soc/?csw=1) 

 > Google Summer of Code is a global program that offers post-secondary student developers ages 18 and older stipends to write code for various open source software projects. We have worked with open source, free software, and technology-related groups to identify and fund projects over a three month period.
