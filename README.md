# PYTHON-PROBLEM

Design and implement a module for dynamic square matrices containing strings. An example
of such a matrix:
"aaa" "bb"
"c" "ddd"
The module must allow to solve the following problems:
- Printing the matrix;
- Determining the dimension of the matrix;
- Adding two matrices (the strings from the two matrices of the same position are
concatenated);
- Allowing to access a string from the matrix through its position;
- Searching a string in a matrix (the first occurrence, the last occurrence, or all
occurrences can be considered);
- Multiplying two matrices. Adding two strings means their concatenation ("aaa" +
"xyz" = "aaaxyz"), while the product of two strings is defined as follows:
- "yx" * "bb" = "yxyxyxyxyxyxyxyxyxyxyx": the first string is concatenate by
itself a number of times as follows: each character ’c’ from the second string is
replaced by the number obtained by subtracting ’c’ – ’a’ (in this case, ’b’ – ’a’ =
98 – 97 = 1, and the string "bb" is transformed in the decimal number 11)
- Lexicographic comparison of two matrices (matrix elements are compared in
ascending order of the lines, and strings from the lines are compared item by item).
