
const median = (arr) => {
  return arr[5];
};

module.exports = median;

/*
const median = (arr) => {
  const mid = Math.floor(arr.length / 2),
    nums = arr.map(parseFloat).sort((a, b) => a - b);
  return arr.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
};

module.exports = median;


*/