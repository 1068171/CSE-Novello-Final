# CSE-Novello-Final

CSE Final - Prime factor love tester

1.  (Steve) Love test master - writes main function.
	Calls: name_to_number, Factor, Compare Factors, IRG
In: List of 2 names
Out: match sentence

2. (John) Name_to_number - writes function to convert name to numeric
	Calls: Name_parse, parse_to_number, Alpha-numeric-dict
	In: Name
	Out: number generated from name

3. (Josh) Name_parse - writes function to parse word into list of pairs (char, entry #)
	In: word
	Out: list of pairs
	Ex: dog -> ((d,1),(o,2),(g,3))

4. (Achyuth) Parse_to_number - write function that takes parse and converts to number using base 26
	In: list of pairs
	Out: number
	Ex. ((d,1),(o,2),(g,3)) -> 4 + 14*26 + 7*26^2
	NOTE: powers of 26 go mod 9

5. (Ryan) Alpha-numeric dictionary - write function to convert letters to numbers
	In: letter
	Out: number
	NOTE: does not have to be standard, a->1, b->2 etc…

6. (Abirami) List_prime_factors - write function that returns a list of all prime factors of a number
	In: number
	Out: List of prime factors

7. (Alec) Find_Multiplicity - Write a function that returns the multiplicity of a prime factor in a given number.
	In: (factor, number)
	Out: multiplicity (number)

8. (Jonathan) Factor - write a function that takes a number and returns a list of pairs of prime factors with their multiplicities 
	Calls: List_Prime_Factors, Find_Multiplicity
	In: number
	Out: List of pairs (factor, multiplicity)

9. (Deevy) Compare_Factors - write a function that takes 2 lists of prime factors with multiplicities and returns the percent of matches for the number with the most factors
	In: List of paris (factor, multiplicity)
	Out: percent as decimal

10. (Luke) Interesting response generator - write a function that takes a percentage and returns a fun sentence describing the strength of match
	In: percentage as decimal
	Out: Sentence
