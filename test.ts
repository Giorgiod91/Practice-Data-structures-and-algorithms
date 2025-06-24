const text = "was geht ab was ja";
let word = "0";

function countWords(text: string): { [word: string]: number } {
  // TODO: Implementieren
  var wordcount = 0;

  for (const char of text) {
    if (char == word) {
      wordcount++;
    }
  }

  return { [word]: wordcount };
}

var checkifRight = countWords(text);
