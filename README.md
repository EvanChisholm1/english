# English Compiler

[English is the hottest new programming language](https://twitter.com/karpathy/status/1617979122625712128), why is there no compiler for it? Well, now there is! Simply write some english "code" in a text file, run it through this compiler and you'll hopefully get a working python program!

This compiler currently just uses GPT-3.5 to do the compilation but there is no reason I can't swap it out for something like llama, OpenHermes or any other various open source LLMs.

## Usage

first add an `OPENAI_KEY` in the .env file. Then run the following commands:

```bash
$ python compiler.py <input_file> --out <output_file>
$ python <output_file>
```

## Example

Here is an example of using english to solve a very easy problem from the Canadian Computing Competition.

```english
get the input from stdin turn it to an integer and store in a variable called n, don't prompt

create a variable called total spiciness and init as 0

create a dictionary called spicy map which maps types of pepper to spiciness initialize it as empy
Poblano is 1500, Mirasol is 6000, Serrano is 15500, Cayenne is 40000, Thai is 75000 and Habanero is 125000

loop n times and each time get stdin with no prompt this input is a kind of pepper, look it up in the spicy map and add it to the total spiciness

print the total spiciness
```
