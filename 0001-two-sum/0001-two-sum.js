/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // Create a hash table to store the indices of numbers
    const numIndices={};
    
    for(let i=0; i<nums.length ; i++){
        let complement = target - nums[i];
        
        if (numIndices.hasOwnProperty(complement)){
            return [numIndices[complement], i];
        }
        numIndices[nums[i]]=i;
            
        }
        return [];
    };