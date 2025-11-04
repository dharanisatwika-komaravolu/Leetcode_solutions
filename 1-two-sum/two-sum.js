/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const hashM = {};
    for (let i = 0; i<nums.length; i++){
        const num = nums[i]
        if(target - num in hashM){
            return [i, hashM[target - num]];
        }
        hashM[num] = i;
    }
};