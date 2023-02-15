Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

///////////////////////////////////////////////////////////////////////////////////////////////////////////
function solution(inputString) {
    //loop through input string
    //whencver a "(" is encountered. push index to array
    //keep looping until a ")" is encounterd
    //when  ")" is encountered reverse string in the range of array[(] and  i
    
    
    let openIndexes = []
    
    for(let i = 0; i<inputString.length; i++){
        if(inputString[i] === "("){
            openIndexes.push(i)
        }
        else if(inputString[i] === ")"){
            let start = openIndexes.pop()
            let reversed = reverseRange(inputString,start, i)
            inputString = inputString.slice(0, start).concat(reversed, inputString.slice(i+1, inputString.length) )
            if(openIndexes.length >= 0){
                i = start - 1
            }
        }
    }
    
    return inputString
  
}


function reverseRange(str,start, end){
    //start is index of open parenthesis
    //end is the index of closing parenthesis
    //start + one to not include parenthesis
    //end - 1 to not include parenthesis
    start += 1;
    end -= 1;
    
    let arr1 = [];
    for(let i = end; i >= (start); i--){
        arr1.push(str[i]);
    }

    return arr1.join('');
    
}
