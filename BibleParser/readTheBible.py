#Parsing the bible
import requests
import re

#downloading the bible
print("Downloading text...")
r = requests.get('http://www.gutenberg.org/cache/epub/10/pg10.txt')
theBible = r.text
print("Done!")


#Remove licensing info
theBible = re.search(r"(?<=START OF THIS PROJECT GUTENBERG EBOOK THE KING JAMES BIBLE )(.|\s)*", theBible).group()
theBible = str("***") + re.search(r"(?=\s{5}The)(.|\s)*", theBible).group()
theBible = re.search(r"(.|\s)*?(?=End of the Project Gutenberg EBook of The King James Bible)", theBible).group()

def phase1(theBible):
    #convert the bible all into one line where newline are replaced with ~'s
    theBible = theBible.split('\n')
    theBible = "~".join(theBible)
    return theBible

def phase2(onelinebible):
    muchbetterBible = ""

    #Get new/old
    editionName = 0
    e = re.compile(r"(?:\*\*\*).*?(?=\*\*\*|$)")
    for edition in e.findall(onelinebible):
        editionName += 1
        #book
        bookNum = 0
        e = re.compile(r"(?:~1:1[ |~]).*?(?=~1:1[ |~]|$)")
        for book in e.findall(edition):
            bookNum += 1
            #chapter
            chapterNum = 0
            e = re.compile(r"(?:[0-9][0-9]*:1[ |~]).*?(?=[0-9][0-9]*:1[ |~]|$)")
            for chapter in e.findall(book):
                chapterNum += 1
                #line
                #for char in chapter:
                lineNum = 0
                e = re.compile(r"(?:[0-9][0-9]*:[0-9][0-9]*[ |~])(.*?)(?=[0-9][0-9]*:[0-9][0-9]*[ |~]|$)")
                for line in e.findall(chapter):
                    lineNum += 1
                    muchbetterBible += str(editionName) + ':' + str(bookNum) + ':' + str(chapterNum) + ':' + str(lineNum) + ' ' + line[:-1] + "\n"

    return muchbetterBible

def phase3(thebible):
        #This will be written to a file
        messyLines = thebible.split('\n')

        cleanLines = []

        for line in messyLines:
            toCleanLine = line

            #Clean up the lines
            e = re.compile(r"(?:\~{5}).*?(?=~)")
            listOfMatches = e.findall(line)
            if (len(listOfMatches) > 0):
                e = re.compile(r".*?(?=~{5})")
                toCleanLine = e.findall(line)[0]

            myCleanLine = ""
            for char in toCleanLine:
                if char ==  '~':
                    char = ' '

                myCleanLine += char
            cleanLines.append(myCleanLine)

        return cleanLines

theBible = phase1(theBible)
print("Phase One Done")
theBible = phase2(theBible)
print("Phase Two Done")
theBible = phase3(theBible)
print("Phase Three Done")

for linenum in range(len(theBible)):
    tline = ''
    for c in range(len(theBible[linenum])):
        if theBible[linenum][c] != '\r':
            tline += theBible[linenum][c]
    theBible[linenum] = tline + '\n'

f = open("muchbetterbible.txt", 'w')
for line in theBible:
    f.write(line)
f.close()
