// 1. Find a pair of numbers that sum up to a given target
// Problem Statement:
// Given a sorted array of integers and a target sum, find a pair of numbers that add up to the target.

// Example:
// Input:
// arr = [1, 2, 3, 4, 5, 6, 7, 8]
// target = 10
// Output:
// Pair found: (2, 8)

function targetSum1(arr, target) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] + arr[j] == target) {
        return [i, j];
      }
    }
  }
  return [-1, -1];
}

function targetSum2(arr, target) {
  arr.sort();
  let i = 0;
  let j = arr.length - 1;

  while (i < j) {
    if (arr[i] + arr[j] == target) {
      return [i, j];
    } else if (arr[i] + arr[j] < target) {
      i++;
    } else {
      j--;
    }
  }
  return [-1, -1];
}

arr = [1, 2, 3, 4, 5, 8, 6, 7];
// [
//   1, 2, 3, 4,
//   5, 6, 7, 8
// ]
target = 5;
ans = targetSum2(arr, target);
console.log(ans);



//2. check palindrome 

//tc=O(n)
//sc = O(1)
function pal(s){
    i = 0;
    j = s.length - 1;
    while (i < j) {
      if (s[i] != s[j]) {
        return false
      }
      i++
      j--
    }
    return true
}
s='racecar';
ans=pal(s)
console.log(ans)
