#Exam Questions <img src="../../Resources/exam.png" width=50px alt="Tick Sheet">

##Instructions
Edit this document and answer the questions in the sections surrounded by ```.

There are 30 marks available and are awarded grades as follows:

|Score|Grade|
|-----|-----|
|<6|U|
|6+|G|
|9+|F|
|12+|E|
|15+|D|
|18+|C|
|21+|B|
|24+|A|
|27+|A*|


##Data Representation

###1 - Why do we represent data using binary when using computers *(1 mark)*

```
because the computer only understands if something is on (1) or off (0)
```
###2 - How would we represent the number 147 in binary? *(1 mark)*
```
10010011
```
###3 - Can you convert the hexadecimal number **b5** to denary, there is a mark for you working. *(2 marks)*
```
181
```
###4 - Here is a function written in **pseudocode**.
```
FUNCTION validUser (users , user)
    FOR x <-1 to LEN(users)
        IF users[x] = user
			RETURN True
		ENDIF
	ENDFOR
	RETURN False
ENDFUNCTION
```

(a) What type of data is **users**? **(1 mark)**
```
perameter
```

(b) What type of data is returned by this function? **(1 mark)**
```
statement
```

##Errors
###6 - This program is supposed to find the mean of a list of numbers and print it out for the user:
```
line1:		tot <- 0
line2:		nums <- [1,6,4,2,5,3]
line3:		FOR x <- to LEN(nums)
line4:			tot <- nums[x]
line5:		ENDFOR
line6:		mean <- tot
line7:		OUTPT mean
```

(a) On which line is there a **syntax** error? **(1 mark)**
```
line 3
```

(b) What is meant by a **syntax** error? **(1 mark)**
```
python cannot understand the program and therefor it cannot run it
```

(c) Identify a logical error in the program and suggest how this might be fixed. **(2 marks)**
```
...
```

(d) Describe and give an example of the 3rd kind of programming error. **(2 marks)**
```
a runtime error is when there is an error in the code which is only found when that piece of code is trying to be ran.
```

##Algortithms
###7 - Write an **algorithm** that if given a list of numbers could find the largest. Try to use [pseudocode](http://filestore2.aqa.org.uk/subjects/AQA-GCSE-COMPSCI-W-TRB-PSEU.PDF).
```
...
```

##Networking
###8 - Research the following methods (*topologies*) for connecting devices to a network. In each case give a description and at least 1 advantage and 1 disadvantage.

**Bus Topology (6 marks)**
```
Describe: each computer or network device is connected using a single cable

Advantages: easy to set up, cheap, good for LAN

Disadvantages:difficult to detect fault on a specific device, not good for heavy traffic networks, low security
```

**Ring Topology (6 marks)**
```
Describe: devices are connected together in a circle

Advantages:quick data transfer, simple

Disadvantages: data must go through every device between the sender and the reciever, difficult to troubleshoot, all devices must be turned on for it to work.
```

**Star Topology (6 marks)**
```
Describe:each device is connected to a central device

Advantages:easy to set up and expand, any non-central failure has no impact on other users

Disadvantages:expensive, if the hub has a fault the network fails.
```
