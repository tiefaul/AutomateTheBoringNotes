spam = '    Hello, World     '
spam.strip() # Strip reomves whitespace characters on the begining and end
spam.lstrip # Removes whitespace characters on the left
spam.rstrip # Removes whitespace characters on the right

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS')) # Tells it to stip the occurences of a,m,p and S
