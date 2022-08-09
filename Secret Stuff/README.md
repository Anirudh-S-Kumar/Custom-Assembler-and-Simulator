# What's this folder about?

Well during the making of this project, we had a really limited number of test cases to work on (as they were to be given only on the evaluation day).
So I had a brilliant idea to convert previous year's test cases to modify to our assembler. The files in this directory were used for the same. 
Maybe the next batch will want to take inspiration from this and try to modify our test cases. 

Link to the repository I used for accessing last year's test cases - https://github.com/aflah02/Custom_Assembler_and_Simulator

## How to run them

1) For changing the assembly code,
	* Paste `assemblyChange.py` in `automatedTesting/tests/assembly/hardBin`, `errorBin` and `simpleBin`, and run the script
2) For changing the binaries
	* Paste `binChange.py` in `automatedTesting/tests/assembly/binBin` and `simpleBin`, and run the script

## How to use `traceGen.py`?
Changing the traces was not as easy as changing the assembly and binaries. So what we instead did was compare traces with different groups to see if we got the same answer

1) Paste `traceGen.py` in `automatedTesting/` and run it. Also optionally zip file if you want to
2) It will generate a folder called `myTraces` and optionally the zip file of the same name.
3) Send this zip file over to your friend
4) Ask them to extract it, rename the folder to `traces` and place it inside `automatedTestin/tests`
5) Run the automated testing. 
