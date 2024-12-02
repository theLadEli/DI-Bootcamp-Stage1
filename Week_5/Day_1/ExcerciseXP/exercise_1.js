// // #1
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     console.log(`inside the funcOne function ${a}`);
// }

// // #1.1 - run in the console:
// funcOne()
// // #1.2 What will happen if the variable is declared 
// // ANSWER: It will log 3
// // with const instead of let ?
// // ANSWER: It will give an error as you can not assign to a const in a lower scope


// //#2
// const a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     console.log(`inside the funcThree function ${a}`);
// }

// // #2.1 - run in the console:
// funcThree()
// funcTwo()
// console.log(a)
// funcThree()
// // #2.2 What will happen if the variable is declared 
// // with const instead of let ?
// // Can't assign to a const

// //#3
// function funcFour() {
//     window.a = "hello";
// }
// // Error: Window is not defined

// function funcFive() {
//     console.log(`inside the funcFive function ${a}`);
// }

// // #3.1 - run in the console:
// funcFour()
// funcFive()

// //#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     console.log(`inside the funcSix function ${a}`);
// }


// // #4.1 - run in the console:
// funcSix()
// // #4.2 What will happen if the variable is declared 
// // with const instead of let ?

// //#5
// let a = 2;
// if (true) {
//     let a = 5;
//     console.log(`in the if block ${a}`);
// }
// console.log(`outside of the if block ${a}`);

// #5.1 - run the code in the console
// #5.2 What will happen if the variable is declared 
// with const instead of let ?
// nothing, as inside the function we're declaring  a new function instead of updating an existing