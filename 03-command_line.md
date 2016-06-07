# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

####CHEAT SHEET
```console
ls - list directory
env - look at environment
export - export/set new environment variable
grep - find things inside files
cat - print the whole file
sudo - become super user root
pushd - push directory (to a place where it can be retrieved)
popd - pop directory (from place, like a stack)
man - read a manual page
exit - exit the shell
```

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`     
`ls -a`  
`ls -l`  
`ls -lh` 
`ls -lah`
`ls -t`  
`ls -Glp`

```console
`ls`     - lists contents of a directory
`ls -a`  - includes directory entries that begin with a dot
`ls -l`  - lists in long format
`ls -lh` - lists long, human-readable format
`ls -lah`- lists long, human-readable format, including entries beginning with a dot 
`ls -t`  - lists by modification time, from most recent to oldest
`ls -Glp`- lists in long format without group names using a slash as the indicator  
```

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`ls -1`  - displays each entry on a line
`ls -r`  - displays files in reverse order
`ls -u`  - displays files by file access time
`ls -m`  - displays files in a comma-separated list
`ls -C`  - displays files in column format

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

```console
Xargs executes a command based on items read from the standard input. Often, it is used in conjunction with terms like 'find' or 'grep' to generate a list and perform some action on it. The syntax:

$ find . -name "*.txt" | xargs rm

is an example of xargs in action. The command first searches the current working directory for all .txt files, and then executes the 'remove' argument on that list, deleting the files.
```
