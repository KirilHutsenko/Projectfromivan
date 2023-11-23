# Practice_From_Ivan
___
Here I perform various tasks that my teacher invented for me
## file_verificatio
___
This program checks all files on the desktop 
and outputs the following data to the console:

  + File name
  + Size
  + Data has been created
  + Full path

**First**, we import two methods

```python
from pathlib import Path
import datetime
```
**Second**, a loop that checks all files
```python
for f in Path('/Users/loklotl/Desktop').iterdir():
    if f.is_file():
        m_timestamp = f.stat().st_mtime
        m_time = datetime.date.\
            fromtimestamp(m_timestamp).strftime("%d-%m-%Y")
        print(f"Name: {f.name}\n"
              f"Size: {f.stat().st_size} bytes\n"
              f"Date of creation: {m_time}\n"
              f"Full path: {f.parent.absolute()}\n")
```
This example is suitable for the specified path.
If you want to
make it more universal, 
you need to replace the path with:
   1. If the program will be in a folder located on the desktop
```python
Path('../')
```
   2. If the program will be open on the desktop 
```python
Path('.')
```
## link_for_web
____
On the desktop there is a .txt 
file in which a link to any site is written. 
Launching the program should open the page of the specified site
**The file must be created in advance!**

Importing _webbrowser_ allows you to open files.
Then we read the file and use the method _webbrowser.open_
```python
import webbrowser

with open('/Users/loklotl/Desktop/111.txt') as link_web:
    webbrowser.open(link_web.read())
```
## find_polindrom
___
A sentence is entered into the console, 
and if the sentence contains the word polynomial, 
the program displays it in the list, if there is no such word, 
the user is informed that this word was not found
```python
con = str(input("Enter a sentence: "))

while len(con) <= 0:
    con = str(input("Enter a sentence: "))
```
changing con creates a prompt, and the _while_
loop prompts for a sentence to be entered every time 
if the user has not entered anything

**Function palindrom**
```python
def palindrom(sentence):
    return f"We found polindrom: {newlist}"
```
First, the function converts everything written
the user in a list of words separated by spaces and 
writes everything in lower case
```python
 structure = sentence.lower().split()
```
Next, we take each element from our list and convert 
it to another list. Then we turn it over
```python
    for elem in structure:
        elem_list = list(elem)
        copy_el_ls_rev = elem_list[::-1]
```
This whole process looks like this:
   1. The user entered a sentence **(Hello world)**
2. Reduce the letters and divide into a list **['hello', 'world']**
3. We take each element and divide it into a second list **['h', 'e', 'l', 'l', 'o']**
4. Turn over **['o', 'l', 'l', 'e', 'h']

We compare the two lists, and if they are equal, 
we add them to the list *rezalt*
```python
        if elem_list == copy_el_ls_rev:
            str_elem = elem_list
            convert_el_ls = ''.join(map(str, str_elem))
            rezalt.append(convert_el_ls)
```
If the condition is not equal
```python
    if not rezalt:
        return "We dont't found polidrom"
```
Before the last step, the function filters 
duplicates and returns the result
```python
    for i in rezalt:
        if i not in newlist:
            newlist.append(i)
        else:
            dublicate.append(i)
    return f"We found polindrom: {newlist}"
```
