# Performance test
ROS pub/sub performance comparison across C++/Python.

## Goal
Test performance between C++ and Python between different combinations of publisher/subscriber.


## Dependencies

This application depends heavily on ROS Melodic (running on Ubuntu 18.04), a system wide install can be done following the [official instructions](http://wiki.ros.org/melodic/Installation/Ubuntu).


## Building

On catkin root, run:

```
$ catkin_make
```

## Running

### Using roslaunch

To run the application simply run:

```
$ roslaunch performance_test performance_test.launch
```
You may specificy which kind of publisher/subscriber to run as:

```
$ roslaunch performance_test performance_test.launch pub:=py sub:=cpp
```
```
$ roslaunch performance_test performance_test.launch pub:=cpp sub:=py
```
```
$ roslaunch performance_test performance_test.launch pub:=cpp sub:=both
```

Additionally to set up the nodes, the launch script initializes the param `publish_rate` (default: 10).

### Running manually

First, start roscore:
```
$ roscore
```
Make sure the param `publish_rate` is defined:
```
$ rosparam set /publish_rate 10
```
Start the node:
```
$  rosrun performance_test <node>
```
The following nodes are defined within the package> `cpp_publisher, cpp_subscriber, publisher.py, subscriber.py`.

## Project structure

The project is structured with core components organized as the following:

Folder| Purpose
------ | -------
launch | Launch file
msg | Message definition
src | C++ src files
scripts | Python scripts

## Design

The package was designed with simplicity at mind, where each publisher/subscriber in each language is defined as a different node to process the messages.

The frequency adjustment is done by means of a global param `publish_rate`, used by publishers to adjust the thread rate (i.e. in C++: `ros::Rate publish_rate(rate_param)`).

For communicating the exact time of message generation between publishers and subscribers, a timestamp in string format is used, being created just before being published and passed down in `SuperAwesome.msg`, respecting the requirement of only one string field in the message format.

To calculate the time offset between publisher/subscriber, once a message is received, a new timestamp is taken, and from their difference the elapsed millisecods between message creation and processing is calculated.

## Results

For practical results of "limits in which rates don't coincide with real life" and to avoid interference of CPU scheduling or context switch, a threshold of 10 ms was established: if the time differente between the two timestamps was greater than 10 ms and the difference remained for at least two readings the criteria was achieved. Publish rates (Hz) in the range [10, 100] (step 10), [100, 10000] (step 50) and [1000, 10000000000[ (step 10^n) were used. The lowest frequency to meet the criteria is shown below.

### Test environment

The following test environment used was: Notebook ACER HELIOS 300:
- Intel® Core™ i7-7700HQ
- 2.8 GHz - 3.8 GHz com Turbo Boost
- 6 MB Cache
- 16 GB DDR4 2.400 MHz

---------- | C++ Publisher | Python Publisher
---------- | ------------- | -------
C++ Subscriber | ? | ?
Python Subscriber | 250 Hz | 300 Hz

?: It was not possible to meet the criteria in the tests.

It was interesting to observe the cap presented on the Python subscriber vs the C++ one, whose processing speed was crucial to keep up with the buffer produced by the publisher. The C++ subscriber had no problem processing the incoming messages from neither the sources, averaging a [0,0.5] delay. The Python subscriber in the other hand, couldn't keep up with publish rates above 250 Hz in C++ and 300 Hz in Python, when messages tended to accumulate and delays increase, confirming the assumption that Python, compared to C++, is a poor choice to time critical scenarios.

## License

MIT.
