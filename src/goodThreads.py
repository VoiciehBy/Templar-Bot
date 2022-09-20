import utils as u
import constants as c
import listOfThreads as lOT


def goodThreads(SEARCH_PATTERNS):
    threads = u.theThreads()
    goodThreads = list()

    for thread in threads:
        tN = thread.name
        isMatchesSearchPattern = tN.__contains__(
            SEARCH_PATTERNS[0].upper()) or tN.__contains__(
                SEARCH_PATTERNS[1].upper())
        if (isMatchesSearchPattern and (thread not in lOT.theListOfThreads)):
            goodThreads.append(thread)

    u.delete(threads)

    if (goodThreads):
        for goodThread in goodThreads:
            print(str(goodThread.link))
            if (goodThread not in lOT.theListOfThreads):
                lOT.theListOfThreads.append(goodThread)
    return goodThreads