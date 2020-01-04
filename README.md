# Empathy


This repository contains a program which generates a small novel, in a .html file, that can be converted into a pdf. The main characters in it are 'I' and a 'He' or 'She' (there is a 50/50 chance of either occurring) and, if the I and He/She pass all levels of empathy, a 'We'. The text is based on randomness and at every run it gives a different version. It uses sentences from the books taken from Project Gutenberg. It contains four chapters: Solitude, Multitude, Empathy, Death. The main idea of the novel is to display the path how a "We" is formed.

The Books
---
* The Invisible Man
* Alice in the Wonderland
* Through The Looking Glass
* Adventures of Sherlock Holmes
* Memoirs of Sherlock Holmes
* Time Machine
* Dracula
* Frankenstein


Overall Explanation
---

Using regular expressions certain types of sentences are selected, then in specific cases the subject is converted. Mostly are selected sentences containing specific words. For example, first part of the first chapter contains sentences that have the words "alone" or "invisible", the second part contains sentences with "I" (You can see all words used for selecting if you generate the novel). Each chapter has specific kind of words selected from specific books from the library in order to express an idea, which I will explain in the following:

The chapter Solitude has, as was mentioned earlier, sentences that have in them the words "alone" and "invisible" in order to express the stage where no "We" exists, the state of complete loneliness. The text is collected from the book The Invisible Man. The next part of this chapter contains sentences which contain I, and only I, that is no You, no He, no They, nothing else, only I, in order to express the solitude. And, in some cases, because of The Invisible Man, beautiful sentences are formed.

The next chapter, called Multitude, takes all its content from the Sherlock Holmes collection, because in it are a lot of characters and dialogues. The words used to generate the text are "speak" and "ask", to express the need to interact and communicate, and "both" and "together", in order to express a unity, togetherness.  

In the chapter Empathy (the texts used here are Alice saga and Time Machine (because of a lot of I or He/She sentences)) all the important magic happens. Here is decided if a "We" is formed. It's done through multiple levels, in total 3. If the first one is passed then the next one begins, otherwise the whole chapter Empathy ends. In every level there are two types of sentences that 'compete'. In the first level compete sentences that contain an "I" and a "He" or a "She" (I forgot to mention that the other 'companion' is decided at the begining of the chapter). In the next compete sentences that contain either an I or an He/She versus sentences that contain both an I and a He/She. Then in the last level compete sentences that contain an "You" and sentences that contain either an I or a He/She. Either 'competitors' have a 50/50 chance of occurrence. The criteria by which a level is passed successfully is based on the gap ("randomly" chosen) between the occurrences of each 'competitor'. For example if the gap between number of I sentences and He sentences is too big then the next level is not created and the novel proceeds to Death. The gap is based on the number of battles (which also is choosed "randomly"(if you do no understand what "randomly" check the documentation)). If, in the end, the novel passes all these levels, a subchapter is created, in which all sentences have a 'We'. And also ...

In the chapter Death, if the "We" was formed, the sentences will contain a We instead of an I (in the case the "We " wasn't formed). Notably, the last sentence in this chapter is not randomly chosen and is always the same- "I died." (in the case "We" wasn't formed) or "We died." (in the other case). That is because, my dear friends, death is inevitable. Here all text was collected from the horror books: Frankenstein and Dracula.

More
---
If you want to see a more detailed  and technical explanation please read the documentation- .pdf file found in the folder /doc.

Or, if you want to test the program, download the code and visit the instruction in the user's manual- .txt file found in the folder /doc.

Feedback
---
All contributions or suggestions are warmly welcomed :)

Please, send feedback at alexe.spataru99@e-uvt.ro
