#!/usr/bin/node

const nums = process.argv.slice(2).map(Number).filter(num => !isNaN(num));
if (nums.length === 0 || nums.length === 1) {
  console.log(0);
} else {
  nums.sort((a, b) => b - a);
  console.log(nums[1]);
}
