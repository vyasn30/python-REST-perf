## Learning about caches and async ##

Kya sikha bhai?:

Slow IO (Network calls, diskwrites over network, userbound io):
  - Use async
  - only one processor and one native thread
  - implemented by eventloop.
  - Your vanilla async await of Node and Asyncio

Fast IO (Just network calls, cache reads and writes)
  - Use multithreading
  - Only one processor but can use multiple threads
  - implemented by the programmer. (Using compiled thread safe lang is reccomended. Need to read more about this

CPU bound Tasks:
  - Can use python but not for loops, better to delegate to another API(numpy etc)
