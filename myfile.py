#!/usr/bin/env python2.7
import random
import time

x = ' ';
print("Hey")
time.sleep(2)
name = raw_input("What is your name? ")
print(x)
print('Hey, %s' %name)
time.sleep(2)
 

time.sleep(1)
ans_list = ['It is Certain' , 'It is decidely so' , 'Without a doubt' , 'Reply hazy, try again' , 'Ask again later' , 'Cannot predict right now' , 'My reply is no' , 'My sources say no' , 'Outlook not so good']

ans_item = random.choice(ans_list)

question = raw_input("What is your question? ")
print(x)
print("Thinking")
print(x)

time.sleep(3)
print("Thinking")
print(x)
time.sleep(4)
print(ans_item)



