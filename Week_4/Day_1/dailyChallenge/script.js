let sentence = prompt("Input a sentence")
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");
let sentenceBeforeNot = sentence.slice(0, wordNot)
let sentenceAfterBad = sentence.slice(wordBad + 3, sentence.length)

if (sentence.includes("not")) {
    if (wordBad > wordNot) {
        console.log(sentenceBeforeNot + "good" + sentenceAfterBad)
        alert(sentenceBeforeNot + "good" + sentenceAfterBad)
    }
} else {
    alert(sentence)
}