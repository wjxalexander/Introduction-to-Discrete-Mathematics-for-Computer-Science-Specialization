// http://travisdazell.blogspot.com/2012/11/many-time-pad-attack-crib-drag.html
function stringToHex(string, format='utf-8') {
  return Buffer.from(string, format).toString('hex')
}
function hexToString(hex) {
  return Buffer.from(hex, 'hex').toString()
}

function encryptXor(text, key) {
  // text and key must have the same length.
  let result = '';
  for (var i = 0; i < text.length; i++) {
    const textInt = parseInt(text[i], 16)
    const keyInt = parseInt(key[i], 16)
    const xorRet = (textInt ^ keyInt)
    result += xorRet.toString(16)
  }
  return result;
}

// const message = "secret message"
// const key = "my secret keys"
// console.log("hex(message) = %s", stringToHex(message))
// console.log("hex(key) = %s", stringToHex(key))
// const ciphertext = encryptXor(stringToHex(message), stringToHex(key))
// console.log("ciphertext: %s", ciphertext)
// recovered_message = hexToString(encryptXor(ciphertext, stringToHex(key)))
// console.log("recovered message: %s", recovered_message) //my secret keys

const message1 = "steal the secret"
const message2 = "the boy the girl"
const key = "supersecretverys"
const ciphertext1 = encryptXor(stringToHex(message1), stringToHex(key))
const ciphertext2 = encryptXor(stringToHex(message2), stringToHex(key))
const xor_ciphertexts = encryptXor(ciphertext1, ciphertext2)
const xor_messages = encryptXor(stringToHex(message1), stringToHex(message2))
console.log(ciphertext1, ciphertext2)
console.log(xor_ciphertexts, xor_ciphertexts === xor_messages) // s1 xor key xor s2 xor key == s1 xor s2
// guess 
function tryGuessingSubstring(substring, messageLength, xorMessage){
  const goodGuess = []
  const lengthGap = messageLength - substring.length
  for (let i = 0; i < lengthGap + 1; i++){
    const conjugatedString = String.fromCharCode(0).repeat(i) + substring + String.fromCharCode(0).repeat(lengthGap - i)
    const guess = stringToHex(conjugatedString)
    const otherMessagePart = hexToString(encryptXor(guess, xorMessage)).slice(i, i + substring.length) // try to xor twice
    if (/^[a-zA-Z\s]*$/.test(otherMessagePart)){
      goodGuess.push(otherMessagePart)
    }
  }
  return goodGuess
}
console.log(tryGuessingSubstring(" the ", message1.length, xor_messages))
console.log(tryGuessingSubstring("oy the ", message1.length, xor_messages))
console.log(tryGuessingSubstring(" the ", message2.length, xor_messages))
console.log(tryGuessingSubstring("he b ", message2.length, xor_messages))