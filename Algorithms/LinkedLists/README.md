# Considerations

Benefit of array is search: Only LinearSearch is available for LinkedLists
Benefit of LinkedList: Easy to delete and shift (example of a queue) - would perform poorly with array
RingBuffer: Array, but if the tail goes to the end, you will just go to the front again i.e implementing a queue in an array
Allows for constant time both adding and deleting at head and tail.
Object pool: Instead of creating objects for each user, create the object, set the param, use it, hand back to pool to set new param.
In js ArrayList is used (un/shift is slow, push/pop/get is fast)