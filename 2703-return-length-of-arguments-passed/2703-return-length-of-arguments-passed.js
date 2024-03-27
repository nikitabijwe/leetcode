/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    let len = 0;
    for (let number of args) {
        len+=1
    }
    return len
};

/**
 * argumentsLength(1, 2, 3); // 3
 */