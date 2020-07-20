def cleanUp(query, wordsToRemove):
    querywords = query.split()

    cleanedWords  = [word for word in querywords if word.lower() not in wordsToRemove]
    cleanedUp = ' '.join(cleanedWords)
    return cleanedUp