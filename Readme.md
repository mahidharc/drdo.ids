
 "A system approach to network modeling for DDoS detection using a Naìve Bayesian classifier" by Mr. Vijayasarathy, 
  Mr. S V Raghavan and Mr. Ravindran B, published in  "Communication Systems and Networks (COMSNETS), 2011" 
  with E-ISBN: 978-1-4244-8951-0 and Print ISBN: 978-1-4244-8952-7

  This work was implemented by Mahidhar Chellamani, Nitesh A Jain, Parthasarathy M Alwar and Padmavathi K as a
  project in collaboration with BMS Institute of Technology and Centre for Artificial Intelligence (CAIR), DRDO, Bangalore.

--

#### I. Files Used in the Package

* algo1.py --------------> "Deploy" function. This module tests the input traffic and computes if a window is an attack window or not.
* algo2.py --------------> "trainPhase" function. This module initiates training.
* algo3.py --------------> "train" function. This module trains the NBC.
* algo5.py --------------> "determineOptimalBands" function. Jump clustering algorithm.
* algo6.py --------------> "updateProbabilities" function.  This algorithm computes and updates the probability based on the events.
* algo7.py --------------> "determineThresholdProbability" function. 
* algo8.py --------------> "TCPstream" class. This class holds information about a praticular stream.
* darpaattack1 ----------> Contains flags from DARPA 1999 Week 1 Tuesday and manual injection of attack flags
* darpaattack2 ----------> Contains flags from DARPA 1999 Week 3 Friday and manual injection of attack flags
* darpaattack3 ----------> Contains flags from DARPA 1998 Week 3 Thursday which contains only attack data. No manual injection.
* thesisattacks ---------> Contains flags from a manually generated attack as specified by the original authors
* darpanoattack1 --------> Contains flags from DARPA 1999 Week 1 Wednesday
* darpanoattack2---------> Contains flags from DARPA 1999 Week 3 Tuesday and Wednesday
* darpatrain ------------> Contains flags from DARPA 1999 Week 1 Monday and Thursday
* main.py ---------------> This the main program. This is to be executed first to begin testing.
* parser.py -------------> Takes tcpdump filenames and gives the output flag array
* thresholdP ------------> Stores the Threshold Probability generated 

--

#### II. Hardware Requirements : 

* Processor: Any x86 or x86_64 based processor
* Random Access Memory (RAM): 4GB or above


TO BE NOTED:  With the an Intel i5 3230M @ 2.6GHz and 8GB of RAM we have achieved an execution time for largest data file as 19m 0.011s

--

#### III. Software Requirements: 
* Operating System: Any GNU/Linux based OS. It has been tested on Debian, Manjaro and Ubuntu
* Python 2.7.6
* NumPy 1.8.1
* MatPlotLib 1.3.1


TO BE NOTED: We have tested the code found in this package on Manjaro, Ubuntu and Debian. We do not claim the same results when tested 
on a different specification not conforming to the above configuration.

--

#### IV. Details of the dataset used:

1. DARPA 1999 Week 1 All files - To generate the training, testing and the attack data.
2. DARPA 1999 Week 3 All files - To generate the training, testing and the attack data.
3. DARPA 1998 Week 3 Thursday  - To generate the attack data.

All of these datasets can be found on http://www.ll.mit.edu/ 

--

#### V. Information about the Package:

* It is to be noted that the project was conducted with strict regard to only TCP. UDP support was not defined in the scope of this package.

* To train the model "darpatrain" was used. The file "darpatrain" was generated from DARPA 1999 Week 1 Monday and Thursday.

* The attack data was manually constructed in files darpaattack1, darpaattack2 and darpaattack3 was extracted from the DARPA 1998 Week 3 Thursday.These
are the only attack files which were used.

* The algorithms written by the original authors were implemented to the best of our knowledge, keeping in mind the implementation and language 
specifications limited by Python.

* The attack files have been hard coded into the main.py file. If a different input file (attack, training or no attack) has to be inserted, the main.py file 
has to be modified with the required input file. 
