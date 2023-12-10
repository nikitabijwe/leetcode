/**
 * @param {string} s
 * @return {string}
 */
var reverseOnlyLetters = function(s) {
    const chars = s.split('');
    let start = 0;
    let end = chars.length - 1;

    while (start < end) {
        if (/[a-zA-Z]/.test(chars[start]) && /[a-zA-Z]/.test(chars[end])) {
            [chars[start], chars[end]] = [chars[end], chars[start]];
            start++;
            end--;
        } else {
            if (!/[a-zA-Z]/.test(chars[start])) start++;
            if (!/[a-zA-Z]/.test(chars[end])) end--;
        }
    }
     return chars.join('');
};