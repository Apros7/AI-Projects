# THEORY SECTION: Did not implement, only some notes for how to implement

# Used for Autocomplete (and also caching at times)
# Go through each in char of work in dict then create the appropriate branches
# Use a .isWord to identity if this node is a word
# Use scoring to add scoring the more a word is used in texts.
# Constant time for lookup: Does not depend of size of tree of size of word being typed:
# Worst case is max len of an english words: (lets say 12) therefore 12 node checks has to be made. Still constant.