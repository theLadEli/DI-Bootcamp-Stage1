const calculator = (num1,num2,operator) => {

    return operator == '/' ? (num1 / num2)
        : operator == '*' ? (num1 * num2)
        : operator == '-' ? (num1 - num2)
        : operator == '+' ? (num1 - num2)
        : `No valid operator provided.`

}


console.log(calculator(5,2,'/'))
console.log(calculator(10,15,'+'))

// switch(operator) {
//     case '/':
//         return(num1 / num2)
//     case '*':
//         return(num1 * num2)
//     case '-':
//         return(num1 - num2)
//     case '+':
//         return(num1 + num2)
// }