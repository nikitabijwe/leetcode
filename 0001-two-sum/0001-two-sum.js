/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // Create a hash table to store the indices of numbers
    const numIndices = {};

    // Iterate through the array
    for (let i = 0; i < nums.length; i++) {
        // Calculate the complement (the number needed to reach the target)
        const complement = target - nums[i];

        // Check if the complement exists in the hash table
        if (numIndices.hasOwnProperty(complement)) {
            // If found, return the indices of the two numbers
            return [numIndices[complement], i];
        }

        // If not found, store the current number and its index in the hash table
        numIndices[nums[i]] = i;
    }

    // If no solution is found, return an empty array or handle it as needed
    return [];
};
