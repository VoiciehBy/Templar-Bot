import urllib
import constants as c
import gc
import thread as t


def getWebPageAsHTML(url):
    html = urllib.request.urlopen(url)
    return html.read()


def getBody(html):
    offset = html.index(c.BODY_START) + len(c.BODY_START) - 1
    end = html.index(c.BODY_END)
    return html[offset:end]


def removeCharacters(string, characters):
    return string.replace(characters, '')


def rC(s, c):
    return (removeCharacters(s, c))


def removeSomeCharacters(s):
    s = s.strip()
    s = rC(s, "\\t")
    s = rC(s, "\\r")
    s = rC(s, "\\n")
    s = rC(s, "</div")
    s = rC(s, "><")
    return s


def rSC(s):
    return removeSomeCharacters(s)


def delete(theList):
    theList.clear()
    del theList
    gc.collect()


def getTheList(start, stop):
    html = getWebPageAsHTML(c.WebPageURL)
    html = str(html)
    html = getBody(html)

    index = html.index(start)
    offset = len(start)
    indexX = index + offset
    iEnd = html.index(stop, indexX)

    theList = list()

    i = 0
    while c.theTrue:
        if (i > 13):
            break
        html = html[iEnd:]
        index = html.index(start)
        offset = len(start)

        indexX = index + offset
        iEnd = html.index(stop, indexX)

        theList.append(rSC(html[index + offset:iEnd + 1]))
        i = i + 1

    del html
    gc.collect()
    return theList


def getThreadsLinks():
    temp = getTheList(c.FORUM_TOPIC_OVERLAY, c.FORUM_TOPIC_DETAILS)
    final = list()
    for node in temp:
        final.append(node[:-2])
    delete(temp)
    return final


def getThreadsTopicNames():
    return getTheList(c.FORUM_TOPIC_NAME, c.FORUM_TOPIC_OP)


def theThreads():
    threadsNames = getThreadsTopicNames()
    threadsLinks = getThreadsLinks()
    threads = list()

    for i in range(len(threadsNames)):
        tN = threadsNames[i].upper()
        threads.append(t.thread(tN, threadsLinks[i]))

    delete(threadsNames)
    delete(threadsLinks)
    return threads