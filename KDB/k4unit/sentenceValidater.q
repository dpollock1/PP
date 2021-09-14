invChar:string each enlist each til 13				     // - initialise list of invalid Alphanumeric chars/combos. 

func:{[Sentence] res:0;					             // - init res:0					            
   if[Sentence[0] in .Q.A;res:res+1];				     // - test for Capital letter start.	           
   if[0=(sum Sentence in "\"") mod 2;res:res+1];		     // - test for even quotation marks.
   if[last Sentence in ".";res:res+1];				     // - test for period at end.
   if[0=sum (-1_Sentence) in ".";res:res+1];			     // - test for periods in middle.
   if[0=sum (enlist each " " vs Sentence) in invChar;res:res+1];     // - test for numbers written in full below 13.
   $[res=5;1b;0b] 						     // - if all tests valid = true else false.

 }
